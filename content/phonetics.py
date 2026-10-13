#!/usr/bin/env python3
"""Deterministic restored-classical (Allen, Vox Latina) transcriber for macronized Latin.
Outputs IPA and an English-reader respelling (stressed syllable in CAPS).
Usage: python3 phonetics.py "Vēnī, vīdī, vīcī."   |  python3 phonetics.py --build  |  --test
Conventions: short vowels a ɛ ɪ ɔ ʊ ʏ; long aː eː iː oː uː yː; diphthongs ae̯ au̯ oe̯ ei̯ eu̯ ui̯;
v=w, c=k, g=g, qu=kʷ, ngu+V=gʷ, gn=ŋn, n before velar=ŋ, x=ks, z=dz, bs/bt=ps/pt,
ch/ph/th=kʰ/pʰ/tʰ, intervocalic consonantal i = jj. Final -m written m (nasalisation/elision ignored).
Stress: penult if heavy, else antepenult; enclitic -que/-ve/-ne pulls stress to the syllable before it.
Stop+liquid counts as onset (prose usage), so it does not make position."""
import json, re, sys, unicodedata, os

SHORT = {'a':'a','e':'ɛ','i':'ɪ','o':'ɔ','u':'ʊ','y':'ʏ'}
LONG = {'ā':'aː','ē':'eː','ī':'iː','ō':'oː','ū':'uː','ȳ':'yː'}
RESP_V = {'a':'ah','ɛ':'eh','ɪ':'ih','ɔ':'o','ʊ':'u','ʏ':'ü','aː':'ah','eː':'ay','iː':'ee','oː':'oh','uː':'oo','yː':'ü',
          'ae̯':'eye','au̯':'ow','oe̯':'oy','ei̯':'ay','eu̯':'eh-oo','ui̯':'wee'}
RESP_C = {'k':'k','kʰ':'k','kʷ':'kw','gʷ':'gw','g':'g','w':'w','j':'y','pʰ':'p','tʰ':'t','ŋ':'ng','h':'h','dz':'dz'}
STOPS = {'p','b','t','d','k','g','pʰ','tʰ','kʰ'}
EU_WORDS = {'heu','ēheu','eheu','seu','neu','ceu','neuter','neutrum','neutra'}
UI_WORDS = {'cui','huic','cuique'}
QUE_EXC = {'atque','neque','itaque','quoque','usque','undique','ubique','utique','dēnique','plērumque','quisque',
           'quaeque','quodque','quidque','quemque','quōque','quāque','utrumque','uterque','quīcumque','quācumque',
           'quōcumque','quandōque','namque','absque','cūjusque','cuiusque','unusquisque','ūnusquisque','quamque','quīque'}
VE_EXC = {'nēve','sīve','neve','sive','ave','cave','salve','vīve','breve','leve','grave','suāve'}
NE_EXC = {'bene','sine','nōmine','homine','ōrdine','fīne','pāne','nōmine','carmine','sanguine','margine','virgine',
          'imāgine','orīgine','nēmine','fulmine','līmine','numine','nūmine','tegmine','agmine','flūmine','lūmine','gine','dōmine','domine'}

def _vowel_char(ch): return ch in SHORT or ch in LONG

def segment(w):
    """lower-case macronized word -> list of (phone, kind) kind V or C"""
    w = unicodedata.normalize('NFC', w.lower()).replace('ë','e\u0308')
    out=[]; i=0; n=len(w)
    def nxt(k): return w[k] if k<n else ''
    while i<n:
        ch=w[i]; c2=w[i:i+2]
        if ch=='\u0308': i+=1; continue
        # diphthongs (no macron, no diaeresis on second)
        if c2 in ('ae','au','oe') and nxt(i+2)!='\u0308':
            out.append((c2[0]+c2[1]+'\u032f','V')); i+=2; continue
        if c2=='eu' and w in EU_WORDS: out.append(('eu̯','V')); i+=2; continue
        if c2=='ei' and w in ('dein','deinde','hei','ei'): out.append(('ei̯','V')); i+=2; continue
        if c2=='ui' and w in UI_WORDS: out.append(('ui̯','V')); i+=2; continue
        if c2=='qu' : out.append(('kʷ','C')); i+=2; continue
        if c2=='gu' and i>0 and w[i-1]=='n' and _vowel_char(nxt(i+2)): out.append(('gʷ','C')); i+=2; continue
        if c2 in ('ch','ph','th','rh'):
            out.append(({'ch':'kʰ','ph':'pʰ','th':'tʰ','rh':'r'}[c2],'C')); i+=2; continue
        if c2=='gn': out.extend([('ŋ','C'),('n','C')]); i+=2; continue
        if ch in LONG: out.append((LONG[ch],'V')); i+=1; continue
        if ch in 'ij':
            prevV = out and out[-1][1]=='V'
            nextV = _vowel_char(nxt(i+1))
            if ch=='j' or (nextV and (i==0 or prevV)) :
                if prevV and i>0: out.extend([('j','C'),('j','C')])
                else: out.append(('j','C'))
                i+=1; continue
            out.append(('ɪ','V')); i+=1; continue
        if ch in SHORT: out.append((SHORT[ch],'V')); i+=1; continue
        m={'c':'k','k':'k','v':'w','x':None,'z':'dz','y':'ʏ'}
        if ch=='x': out.extend([('k','C'),('s','C')]); i+=1; continue
        if ch in m: out.append((m[ch],'C')); i+=1; continue
        if ch.isalpha(): out.append((ch,'C'))
        i+=1
    # assimilations
    for k,(p,t) in enumerate(out):
        nx = out[k+1][0] if k+1<len(out) else ''
        if p=='n' and nx in ('k','g','kʷ','gʷ','kʰ'): out[k]=('ŋ','C')
        if p=='b' and nx in ('s','t'): out[k]=('p','C')
    return out

def syllabify(seg):
    vi=[k for k,(p,t) in enumerate(seg) if t=='V']
    if not vi: return []
    bounds=[0]
    for a,b in zip(vi,vi[1:]):
        cl=list(range(a+1,b)); L=len(cl)
        if L==0: cut=b
        elif L==1: cut=cl[0]
        else:
            last2=(seg[cl[-2]][0],seg[cl[-1]][0])
            cut = cl[-2] if (last2[0] in STOPS and last2[1] in ('l','r')) else cl[-1]
        bounds.append(cut)
    bounds.append(len(seg))
    syl=[seg[bounds[k]:bounds[k+1]] for k in range(len(vi))]
    return syl

def heavy(s):
    v=[p for p,t in s if t=='V'][0]
    closed = s[-1][1]=='C'
    return ('ː' in v) or ('\u032f' in v) or closed

def enclitic(w):
    lw=w.lower()
    for e,exc in (('que',QUE_EXC),('ve',VE_EXC),('ne',NE_EXC)):
        if lw.endswith(e) and lw not in exc and len(lw)>len(e)+1:
            if e=='ne' and not lw.endswith(('ne','ne')): continue
            if e in('ne','ve'): # only accept if host ends in a vowel/consonant pattern typical & host≥2 letters; conservative: require macron-less host ending not 'i'
                if e=='ne' and lw in NE_EXC: return None
                if e=='ve' : return None  # too ambiguous; skip
                if e=='ne' : return None  # ambiguous without lexicon (-ne vs nouns in -ne); skip
            return e
    return None

def stress_index(syl, word):
    n=len(syl)
    if n<=1: return None
    enc=enclitic(word)
    if enc: return n-2  # syllable right before the enclitic
    if n==2: return 0
    return n-2 if heavy(syl[-2]) else n-3

def word_tx(word):
    seg=segment(word)
    if not seg: return None
    syl=syllabify(seg)
    if not syl: return None
    st=stress_index(syl,word)
    ipa=[]; rsp=[]
    for k,s in enumerate(syl):
        ipa.append(('ˈ' if k==st else '')+''.join(p for p,_ in s))
        r=''
        for p,t in s:
            r+= RESP_V[p] if t=='V' else RESP_C.get(p,p)
        rsp.append(r.upper() if k==st else r)
    # ensure respelling 's' word-finally single
    return '.'.join(ipa), '-'.join(rsp)

TOKEN=re.compile(r"[A-Za-zĀĒĪŌŪȲāēīōūȳëÿ]+")
def transcribe(text):
    if not text: return None
    ipas=[]; rs=[]
    for raw in re.split(r"\s+", text):
        if raw.startswith('-') : continue
        parts=TOKEN.findall(raw)
        # skip lone abbreviations like "f." "m." and SPQR initials
        if len(parts)==1 and len(parts[0])==1 and parts[0].lower() not in 'aeiouāēīōūō': continue
        if '·' in raw and all(len(p)==1 for p in parts): continue
        for w in parts:
            r=word_tx(w)
            if r: ipas.append(r[0]); rs.append(r[1])
    if not ipas: return None
    return '/'+' '.join(ipas)+'/', ' '.join(rs)

# Wiktionary classical IPA (normalised: ɫ→l, final nasalised Ṽː→Vm, phonetic [ ]→phonemic, syllable dots kept)
TESTS = {
 'vēnī':'ˈweː.niː','vīdī':'ˈwiː.diː','vīcī':'ˈwiː.kiː','Caesar':'ˈkae̯.sar','Cicerō':'ˈkɪ.kɛ.roː',
 'aqua':'ˈa.kʷa','magnus':'ˈmaŋ.nʊs','lingua':'ˈlɪŋ.gʷa','iam':'jam','Iūlius':'ˈjuː.lɪ.ʊs',
 'māior':'ˈmaːj.jɔr','cuius':'ˈkʊj.jʊs','rēx':'reːks','urbs':'ʊrps','poena':'ˈpoe̯.na',
 'aurum':'ˈau̯.rʊm','philosophia':'pʰɪ.lɔˈsɔ.pʰɪ.a','virumque':'wɪˈrʊm.kʷɛ','amīcus':'aˈmiː.kʊs',
 'dominus':'ˈdɔ.mɪ.nʊs','tenebrae':'ˈtɛ.nɛ.brae̯','terra':'ˈtɛr.ra','pater':'ˈpa.tɛr','māter':'ˈmaː.tɛr',
 'fēcistī':'feːˈkɪs.tiː','senātus':'sɛˈnaː.tʊs','populus':'ˈpɔ.pʊ.lʊs','hominēs':'ˈhɔ.mɪ.neːs',
 'Rōma':'ˈroː.ma','discunt':'ˈdɪs.kʊnt','ignis':'ˈɪŋ.nɪs','cōnsul':'ˈkoːn.sʊl','iuvenis':'ˈjʊ.wɛ.nɪs',
 'Graecia':'ˈgrae̯.kɪ.a','silva':'ˈsɪl.wa','vincō':'ˈwɪŋ.koː',
}
def run_tests():
    ok=0
    for w,exp in TESTS.items():
        got=word_tx(w)[0]
        g=got.replace('.ˈ','ˈ'); e=exp.replace('.ˈ','ˈ')
        good = g==e
        ok+=good
        print(('PASS' if good else 'FAIL'), w, '/'+got+'/', '' if good else 'expected /'+exp+'/')
    print(f'{ok}/{len(TESTS)} passed'); return ok==len(TESTS)

def build():
    base=os.path.dirname(os.path.abspath(__file__)); root=os.path.dirname(base)
    out={}
    for f in ('rome-cards.json','medieval-cards.json','learning-cards.json'):
        for c in json.load(open(os.path.join(base,f))):
            r=transcribe(c.get('latin',''))
            if r: out[c['id']]={'ipa':r[0],'respelling':r[1],'latin':c['latin'],'src':f}
    js=open(os.path.join(root,'cards','cards.js')).read()
    cards=json.loads(js[js.index('['):js.rindex(']')+1])
    for c in cards:
        r=transcribe(c.get('latin',''))
        if r: out[c['id']]={'ipa':r[0],'respelling':r[1],'latin':c['latin'],'src':'cards.js'}
    json.dump(out,open(os.path.join(base,'phonetics.json'),'w'),ensure_ascii=False,indent=1)
    slim={k:{'ipa':v['ipa'],'respelling':v['respelling']} for k,v in out.items()}
    open(os.path.join(root,'cards','phonetics.js'),'w').write('// Generated by content/phonetics.py --build. Do not edit.\nwindow.PHONETICS = '+json.dumps(slim,ensure_ascii=False,indent=1)+';\n')
    print(len(out),'entries')

if __name__=='__main__':
    a=sys.argv[1:]
    if a==['--test']: sys.exit(0 if run_tests() else 1)
    elif a==['--build']: build()
    else:
        r=transcribe(' '.join(a)); print(r[0]); print(r[1])
