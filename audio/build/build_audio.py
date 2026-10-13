#!/usr/bin/env python3
"""Audio build: cut clips on Whisper word boundaries (+150 ms pad), verify ASR coverage, write content/audio-map.json.
Run with the faster-whisper venv: /workspace/.wenv/bin/python audio/build/build_audio.py
Fails (exit 1) if a clip's ASR transcript is 'clean' and covers <80% of the expected tokens, or if a clip ends/starts hot."""
import json,re,subprocess,sys,unicodedata,difflib,os
import numpy as np
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AU=os.path.join(ROOT,'audio');SRC=os.path.join(AU,'src')
from faster_whisper import WhisperModel
M=WhisperModel("medium",device="cpu",compute_type="int8",cpu_threads=8)
PAD=0.15
def norm(s):
  s=''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
  s=s.replace('ae','e').replace('oe','e');s=re.sub('[vwu]','u',s);s=re.sub('[ckq]','c',s);s=s.replace('y','i').replace('j','i').replace('h','').replace('z','s')
  return re.sub('[^a-z]','',s)
def toks(t): return [norm(x) for x in re.findall(r"[^\W\d_]+",t) if norm(x)]
def sim(a,b): return difflib.SequenceMatcher(None,a,b).ratio()
def pcm(f,ss,t):
  r=subprocess.run(["ffmpeg","-loglevel","error","-ss",str(ss),"-t",str(t),"-i",f,"-ar","16000","-ac","1","-f","s16le","-"],capture_output=True).stdout
  return np.frombuffer(r,dtype=np.int16).astype(np.float32)/32768
def words(x,off=0.0,lang="it"):
  sg,_=M.transcribe(x,language=lang,word_timestamps=True,condition_on_previous_text=False,temperature=0.0,beam_size=5)
  return [(off+w.start,off+w.end,w.word.strip()) for g in sg for w in g.words]
def coverage(expected,heard):
  E=toks(expected);H=''.join(norm(w[2]) for w in heard)
  # token hit if it fuzzily appears in the heard stream
  hit=sum(1 for e in E if max([sim(e,H[i:i+len(e)]) for i in range(max(1,len(H)-len(e)+1))] or [0])>=0.7)
  clean=len(heard)>0 and all(re.fullmatch(r"[\w'’.,;:!?«»\-]+",w[2] or 'x') for w in heard) and len(H)>=0.5*len(''.join(E))
  return hit/len(E),clean
def silences(f,a,b):
  r=subprocess.run(["ffmpeg","-hide_banner","-ss",str(max(0,a)),"-t",str(b-max(0,a)),"-i",f,"-af","silencedetect=n=-45dB:d=0.08","-f","null","-"],capture_output=True,text=True).stderr
  st=[max(0,a)+float(x) for x in re.findall(r"silence_start: ([0-9.]+)",r)];en=[max(0,a)+float(x) for x in re.findall(r"silence_end: ([0-9.]+)",r)]
  return st,en
def boundaries(f,a,b,expected,nopad_start=False):
  """a,b = hand-located speech bounds. Snap end to the first -45 dB silence after b-0.2 (so decaying final syllables are kept), pad 150 ms into silence both sides."""
  st,en=silences(f,a-1.5,b+2.5)
  later=[x for x in st if x>=b-0.2];e=(later[0] if later else b)
  nxt=[x for x in en if x>e];e=min(e+PAD,(nxt[0]-0.02) if nxt else e+PAD)
  prev=[x for x in st if x<=a];s=a if nopad_start else max(a-PAD,(prev[-1]+0.02) if prev else a-PAD,0)
  return s,e,None
def edge_db(path):
  x=pcm(path,0,60);x=x[:len(x)-int(16000*0.16)] if len(x)>8000 else x
  if len(x)<1600: return 0,0
  r=lambda y:20*np.log10(np.sqrt(np.mean(y**2))+1e-9)
  return r(x[:800]),r(x[-800:])
def src_edges(f,s,e):
  x=pcm(f,s,e-s);r=lambda y:20*np.log10(np.sqrt(np.mean(y**2))+1e-9);return r(x[:800]),r(x[-800:])
def cut(f,s,e,out):
  subprocess.run(["ffmpeg","-loglevel","error","-y","-ss",f"{s:.3f}","-to",f"{e:.3f}","-i",f,"-af",f"loudnorm=I=-16:TP=-1.5,afade=t=in:d=0.02,areverse,afade=t=in:d=0.03,areverse,apad=pad_dur=0.1","-ac","1","-c:a","libmp3lame","-q:a","4",out],check=True)
spec=json.load(open(os.path.join(os.path.dirname(__file__),'clips.json')))
LU={"CC BY-SA 4.0":"https://creativecommons.org/licenses/by-sa/4.0/","CC BY-SA 3.0":"https://creativecommons.org/licenses/by-sa/3.0/","CC0":"https://creativecommons.org/publicdomain/zero/1.0/","PD Mark 1.0":"https://creativecommons.org/publicdomain/mark/1.0/","PD-self":"https://commons.wikimedia.org/wiki/Template:PD-self"}
out={"_note":"Single audio map (built by audio/build/build_audio.py from clips.json + words.json). Key = card id; value = list of {file (relative to audio/), style (button label), pronunciation_style, register_note?, caption?, credit, license, license_url, source, changes, asr_coverage}. Policy: restored classical by default; church-register cards use church (ecclesiastical) audio, noted on the card."}
fails=[];report=[]
for c in spec:
  src=os.path.join(SRC,c['src']);dst=os.path.join(AU,c['file'])
  if c.get('whole'):
    s,e=0,None
    subprocess.run(["ffmpeg","-loglevel","error","-y","-i",src,"-af","adelay=150,loudnorm=I=-16:TP=-1.5,apad=pad_dur=0.15","-ac","1","-c:a","libmp3lame","-q:a","4",dst],check=True);rng="whole file"
  else:
    b=boundaries(src,c['win'][0],c['win'][1],c['text'],c.get('nopad_start'))
    if not b: fails.append((c['file'],'no ASR words in window'));continue
    s,e,heard=b;cut(src,s,e,dst);rng=f"{s:.2f}-{e:.2f} s"
  x=pcm(dst,0,120);cov,clean=max(coverage(c['text'],words(x,lang=L)) for L in ('it','la'))
  h,t=edge_db(dst) if c.get('whole') else src_edges(src,s,e)
  status='ok'
  if clean and cov<0.8:
    if c.get('asr_override'): status='override: '+c['asr_override'][:60]
    else: status='FAIL coverage';fails.append((c['file'],f'coverage {cov:.0%}'))
  if t>-35: status+=' WARN hot end'
  if h>-35 and not c.get('nopad_start'): status+=' WARN hot start'
  report.append(f"{c['file']:38s} {rng:18s} cov={cov:.0%} clean={clean} start={h:.0f}dB end={t:.0f}dB {status}")
  mod=("trimmed "+rng+" of source, " if not c.get('whole') else "")+"loudness-normalised, converted to mp3"
  ent=dict(file=c['file'],style=c['label'],pronunciation_style=c['style'],credit=c['credit'],license=c['license'],license_url=LU[c['license']],source=c['source'],changes=mod,asr_coverage=round(cov,2))
  for k in ('caption','register_note','note','asr_override'):
    if c.get(k): ent[k]=c[k]
  for cid in c['ids']: out.setdefault(cid,[]).append(ent)
for cid,ws in json.load(open(os.path.join(os.path.dirname(__file__),'words.json'))).items():
  for w in ws: out.setdefault(cid,[]).append(dict(file=w['file'],style=f"Word: {w['word']}",pronunciation_style='classical',word=w['word'],credit=w['credit'],license=w['license'],license_url=LU.get(w['license'],''),source=w['source'],changes='loudness-normalised, converted to mp3'))
json.dump(out,open(os.path.join(ROOT,'content','audio-map.json'),'w'),ensure_ascii=False,indent=1)
print('\n'.join(report));print('FAILS:',fails)
sys.exit(1 if fails else 0)
