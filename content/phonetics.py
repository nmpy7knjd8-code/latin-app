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
# Respelling convention: SHORT vowels are bare letters (a e i o u, u as in "put"),
# LONG vowels are digraphs (ah ay ee oh oo). Stressed syllable in CAPS.
RESP_V = {'a':'a','ɛ':'e','ɪ':'i','ɔ':'o','ʊ':'u','ʏ':'ü','aː':'ah','eː':'ay','iː':'ee','oː':'oh','uː':'oo','yː':'üü',
          'ae̯':'eye','au̯':'ow','oe̯':'oy','ei̯':'ay','eu̯':'ew','ui̯':'oo-ee'}
# short vowel + coda j (before a jj geminate): maior MEYE-yor, Pompeius pom-PAY-yus, Troia TROY-ya, cuius KOOY-yus
RESP_VJ = {'a':'eye','ɛ':'ay','ɪ':'ee','ɔ':'oy','ʊ':'ooy','ae̯':'eye','oe̯':'oy','ei̯':'ay','eu̯':'ew'}
LEGEND = ('Short vowels: a e i o u (u as in "put"). Long vowels: ah ay ee oh oo (pure, held longer; "ay" with no glide). ew = Latin eu as one syllable (e+oo). CAPS = stressed syllable. '
          'w = Latin v; k = c (always hard); g always hard; gn sounds like ngn (magnus = MANG-nus; at the start of a word it is g+n); p/t/k after an aspirated ph/th/ch are breathy p/t/k, NOT f/th. z = dz (Allen; some sources give a long z between vowels).')
RESP_C = {'k':'k','kʰ':'k','kʷ':'kw','gʷ':'gw','g':'g','w':'w','j':'y','pʰ':'p','tʰ':'t','ŋ':'ng','h':'h','dz':'dz','r̥':'r'}
STOPS = {'p','b','t','d','k','g','pʰ','tʰ','kʰ'}
EU_WORDS = {'heu','ēheu','eheu','seu','neu','ceu','euge','euhoe','euoe','neuter','neutrum','neutra','neutrī','neutrō','neutram'}
SU_GLIDE = ('suāv','suād','suās','suēsc','suēt','suēv','suēf')   # u after s consonantal: suāvis SWAH-wis
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
        if c2=='eu' and (w in EU_WORDS or (i==0 and len(w)>2 and w[2] not in 'naeiouāēīōū')): out.append(('eu̯','V')); i+=2; continue
        if c2=='ei' and w in ('dein','deinde','hei','ei'): out.append(('ei̯','V')); i+=2; continue
        if c2=='ui' and w in UI_WORDS: out.append(('ui̯','V')); i+=2; continue
        if ch=='u' and i>0 and w[i-1]=='s' and w[i-1:].startswith(SU_GLIDE): out.append(('w','C')); i+=1; continue
        if c2=='qu' : out.append(('kʷ','C')); i+=2; continue
        if c2=='gu' and i>0 and w[i-1]=='n' and _vowel_char(nxt(i+2)): out.append(('gʷ','C')); i+=2; continue
        if c2 in ('ch','ph','th','rh'):
            out.append(({'ch':'kʰ','ph':'pʰ','th':'tʰ','rh':'r̥'}[c2],'C')); i+=2; continue
        if c2=='gn': out.extend([('g' if i==0 else 'ŋ','C'),('n','C')]); i+=2; continue
        if ch in LONG: out.append((LONG[ch],'V')); i+=1; continue
        if ch in 'ij':
            prevV = out and out[-1][1]=='V'
            nextV = _vowel_char(nxt(i+1))
            if ch=='j' or (nextV and (i==0 or prevV)) :
                if prevV and i>0:
                    # Allen VL 38-39: vowel before intervocalic i (=jj) is short; heavy by position
                    pv=out[-1][0]
                    if pv.endswith('ː'): out[-1]=({'aː':'a','eː':'ɛ','iː':'ɪ','oː':'ɔ','uː':'ʊ','yː':'ʏ'}[pv],'V')
                    out.extend([('j','C'),('j','C')])
                else: out.append(('j','C'))
                i+=1; continue
            out.append(('ɪ','V')); i+=1; continue
        if ch in SHORT: out.append((SHORT[ch],'V')); i+=1; continue
        m={'c':'k','k':'k','v':'w','x':None,'z':'dz','y':'ʏ'}
        if ch=='x':
            out.extend([('k','C'),('s','C')]); i+=1
            if nxt(i)=='s': i+=1          # exs- = /ks/ (exspectō ɛkˈspɛk.toː)
            continue
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
            if last2==('s','w'): cut=cl[-2]                      # cōn.suē.tū.dō
            if L>=3 and seg[cl[0]][0]=='k' and seg[cl[1]][0]=='s': cut=cl[1]  # ex.spec.tō
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

def word_parse(word):
    seg=segment(word)
    if not seg: return None
    syl=syllabify(seg)
    if not syl: return None
    return [list(x) for x in syl], stress_index(syl,word)

def render(syl, st):
    ipa=[]; rsp=[]
    for k,s in enumerate(syl):
        if not s: continue
        ipa.append(('ˈ' if k==st else '')+''.join(p for p,_ in s))
        r=''
        for q,(p,t) in enumerate(s):
            if t=='V' and q+1<len(s) and s[q+1][0]=='j' and p in RESP_VJ and q+2==len(s):
                r+=RESP_VJ[p]; continue
            if p=='j' and q>0 and s[q-1][1]=='V' and s[q-1][0] in RESP_VJ and q+1==len(s): continue
            if t=='N': r+=NASAL_R.get(p[0],'')+'n'; continue
            r+= RESP_V[p] if t=='V' else RESP_C.get(p,p)
        rsp.append(r.upper() if k==st else r)
    return '.'.join(ipa).replace('.ˈ','ˈ') if False else '.'.join(ipa), '-'.join(rsp)

def word_tx(word):
    p=word_parse(word)
    return render(*p) if p else None

NASAL={'a':'ã','ɛ':'ẽ','ɪ':'ĩ','ɔ':'õ','ʊ':'ũ','aː':'ã','eː':'ẽ','iː':'ĩ','oː':'õ','uː':'ũ'}
NASAL_R={'ã':'ah','ẽ':'ay','ĩ':'ee','õ':'oh','ũ':'oo'}
TOKEN=re.compile(r"[A-Za-zĀĒĪŌŪȲāēīōūȳëÿ]+")
def caps_v(w):
    """Roman capitals use V for both u and v: V is a vowel unless it precedes a vowel (QV = qu)."""
    if not (w.isupper() and 'V' in w): return w
    o=''
    for k,ch in enumerate(w):
        if ch=='V':
            nx=w[k+1] if k+1<len(w) else ''
            pv=o[-1] if o else ''
            o+= 'u' if ((pv and pv in 'Qq') or nx not in 'AEIOU' or (pv and pv not in 'AEIOUaeiou' and nx in 'AEIOU' and False)) else 'v'
        else: o+=ch
    return o.lower()

def words_of(text):
    text=text.split('→')[0]                    # derivative cards: English after the arrow is not Latin
    text=re.sub(r'(\w)\((\w+)\)',r'\1\2',text)   # F(ILIO) -> FILIO
    out=[]
    for raw in re.split(r"\s+", text):
        if raw.startswith('-') : continue
        parts=TOKEN.findall(raw)
        if len(parts)==1 and len(parts[0])==1 and parts[0].lower() not in 'aeiouāēīōū': continue
        if '·' in raw and all(len(p)==1 for p in parts): continue
        if ('…' in raw or '...' in raw) and out: out[-1]=out[-1]+'|'   # lacuna: blocks elision
        if re.search(r'[a-zāēīōū]',text): parts=[p for p in parts if not (p.isupper() and len(p)>1)]
        out+=[caps_v(p) for p in parts]
        if ('…' in raw.rstrip('…') or raw.endswith('…') or raw.endswith('...')) and out: out[-1]=out[-1].rstrip('|')+'|'
    return out

MACRONS='āēīōūȳ'
_PLAIN=str.maketrans('āēīōūȳĀĒĪŌŪȲ','aeiouyAEIOUY')
def plain(w): return w.translate(_PLAIN).lower()
LEX={}          # plain form -> unique macronized form (None if ambiguous)
FALLBACK_LOG=[] # (word, replacement) applied during the current transcribe call

def load_lexicon(texts, dcc_path=None):
    """Build plain->macronized lookup from all macronized card Latin/gloss words and the DCC core headwords.
    A key is kept only if every macronized attestation agrees; conflicting keys map to None (no guess)."""
    forms={}
    def add(w):
        w=w.strip(".,;:!?“”\"'()[]·—…").lower()
        if not w or w.startswith('-') or not any(c in MACRONS for c in w): return
        forms.setdefault(plain(w),set()).add(w)
    for t in texts:   # dictionary forms only (gloss lemmas); inflected card text is NOT used (homographs: legis/lēgis)
        for w in TOKEN.findall(t or ''): add(w)
    if dcc_path and os.path.exists(dcc_path):
        for row in json.load(open(dcc_path)):
            for w in re.split(r"[\s,]+",row[0]): add(w)
    LEX.clear()
    for k,v in forms.items(): LEX[k]=next(iter(v)) if len(v)==1 else None
    return LEX

CARD_LEX={}     # per-card plain->macronized from that card's own gloss words (context-correct)
LEX_ACTIVE=[True]
def lex_fix(w):
    if not LEX_ACTIVE[0] or any(c in MACRONS for c in w.lower()): return w
    k=plain(w); m=CARD_LEX.get(k) or LEX.get(k)
    if not m: return w
    fixed=''.join(mc.upper() if oc.isupper() else mc for oc,mc in zip(w,m)) if len(m)==len(w) else m
    FALLBACK_LOG.append((w,fixed)); return fixed

def transcribe(text, verse=False):
    """verse=True: synaloepha/elision of final V or Vm before an initial vowel or h+vowel
    (prodelision with es/est: facta'st), and nasalised final -m elsewhere (Allen VL 30-31, 78-82).
    Elided material is dropped; the remnant is joined to the next word with ‿ (IPA) / ' (respelling)."""
    if not text: return None
    raw=words_of(text)
    if re.search(r'[a-zāēīōū]',text):   # epigraphic CAPS transcription with a lower-case reading: speak only the reading
        pass
    # Policy: a card that already uses macrons is trusted (unmarked vowel = short); lexicon fallback only for unmacronized text
    LEX_ACTIVE[0]=not any(ch in MACRONS for ch in text.lower())
    brk={k for k,w in enumerate(raw) if w.endswith('|')}
    raw=[('|' if w.endswith('|') else '') and lex_fix(w.rstrip('|'))+'|' or lex_fix(w) for w in raw]
    ws=[(w.rstrip('|'),word_parse(w.rstrip('|')),k in brk) for k,w in enumerate(raw)]
    brk2=[b for w,p,b in ws if p]
    ws=[(w,p) for w,p,b in ws if p]
    if not ws: return None
    items=[[w,p[0],p[1],False] for w,p in ws]   # word, syl, stress, joined-to-next
    if verse:
        for k in range(len(items)):
            w,syl,st,_=items[k]
            last=syl[-1]
            vow=[q for q,(p,t) in enumerate(last) if t=='V']
            endsV = last[-1][1]=='V' or (len(last)>=2 and last[-1][0]=='m' and last[-2][1]=='V')
            if k+1<len(items) and not brk2[k]:
                nsyl=items[k+1][1]; first=nsyl[0]
                nV = first[0][1]=='V' or (first[0][0]=='h' and len(first)>1 and first[1][1]=='V')
                if endsV and nV and w.lower() not in ('ō','ō'):
                    nw=items[k+1][0].lower()
                    if nw in ('est','es') and len(syl)>0:
                        # prodelision: drop the e of est/es
                        items[k+1][1]=[[x for x in nsyl[0] if x[1]!='V']]; items[k+1][2]=None
                        items[k+1][3]='pro'
                    else:
                        cut=vow[0]
                        syl[-1]=last[:cut]
                        items[k][3]=True
                    continue
            if last[-1][0]=='m' and len(last)>=2 and last[-2][1]=='V':
                v=last[-2][0]; last[-2]=(NASAL.get(v,v)+'ː','N'); last.pop()
    ipas=[];rs=[];pend_i='';pend_r=''
    for w,syl,st,j in items:
        if st is not None and st>=len(syl): st=None
        i,r=render(syl,st)
        if j=='pro':
            ipas[-1]+='‿'+i; rs[-1]+="'"+r; continue
        if j:
            pend_i+=i+'‿'; pend_r+=(r if r else '')+"'"; continue
        ipas.append(pend_i+i); rs.append(pend_r+r); pend_i=pend_r=''
    return '/'+' '.join(ipas)+'/', ' '.join(rs)

# Wiktionary classical IPA (normalised: ɫ→l, final nasalised Ṽː→Vm, phonetic [ ]→phonemic, syllable dots kept)
TESTS = {
 'vēnī':'ˈweː.niː','vīdī':'ˈwiː.diː','vīcī':'ˈwiː.kiː','Caesar':'ˈkae̯.sar','Cicerō':'ˈkɪ.kɛ.roː',
 'aqua':'ˈa.kʷa','magnus':'ˈmaŋ.nʊs','lingua':'ˈlɪŋ.gʷa','iam':'jam','Iūlius':'ˈjuː.lɪ.ʊs',
 'māior':'ˈmaj.jɔr','cuius':'ˈkʊj.jʊs','rēx':'reːks','urbs':'ʊrps','poena':'ˈpoe̯.na',
 'aurum':'ˈau̯.rʊm','philosophia':'pʰɪ.lɔˈsɔ.pʰɪ.a','virumque':'wɪˈrʊm.kʷɛ','amīcus':'aˈmiː.kʊs',
 'dominus':'ˈdɔ.mɪ.nʊs','tenebrae':'ˈtɛ.nɛ.brae̯','terra':'ˈtɛr.ra','pater':'ˈpa.tɛr','māter':'ˈmaː.tɛr',
 'fēcistī':'feːˈkɪs.tiː','senātus':'sɛˈnaː.tʊs','populus':'ˈpɔ.pʊ.lʊs','hominēs':'ˈhɔ.mɪ.neːs',
 'Rōma':'ˈroː.ma','discunt':'ˈdɪs.kʊnt','ignis':'ˈɪŋ.nɪs','cōnsul':'ˈkoːn.sʊl','iuvenis':'ˈjʊ.wɛ.nɪs',
 'Graecia':'ˈgrae̯.kɪ.a','silva':'ˈsɪl.wa','vincō':'ˈwɪŋ.koː', # review-phonetics.md fixes
 'exspectō':'ɛkˈspɛk.toː','exsilium':'ɛkˈsɪ.lɪ.ʊm','exstinguō':'ɛkˈstɪŋ.gʷoː','Gnaeus':'ˈgnae̯.ʊs',
 'suāvis':'ˈswaː.wɪs','suādeō':'ˈswaː.dɛ.oː','suēscō':'ˈsweːs.koː','cōnsuētūdō':'koːn.sweːˈtuː.doː',
 'euge':'ˈeu̯.gɛ','heu':'heu̯','seu':'seu̯','neuter':'ˈneu̯.tɛr','eunt':'ˈɛ.ʊnt','Eurōpa':'eu̯ˈroː.pa',
 'Pompēius':'pɔmˈpɛj.jʊs','Trōia':'ˈtrɔj.ja','huic':'hui̯k','rhētor':'ˈr̥eː.tɔr','regnum':'ˈrɛŋ.nʊm',
}
RESP_TESTS = {'huic':'hoo-eek','cuius':'KOOY-yus','Pompēius':'pom-PAY-yus','māior':'MEYE-yor','Trōia':'TROY-ya',
 'suāvis':'SWAH-wis','vēnī':'WAY-nee','Rōma':'ROH-ma','pater':'PA-ter','māter':'MAH-ter','lūna':'LOO-na','hominēs':'HO-mi-nays'}
RESP_TESTS.update({'euge':'EW-ge','rēgīna':'ray-GEE-na'})
FALLBACK_TESTS = {  # unmacronized input -> lexicon/caps handling (needs init_lexicon)
 'regina':'/reː.ˈgiː.na/', 'SENATVS POPVLVSQVE':'/sɛ.ˈnaː.tʊs pɔ.pʊ.ˈlʊs.kʷɛ/', 'VESPASIANO':'/wɛs.pa.ˈsɪ.a.nɔ/',  # not in lexicon -> stays unmarked & is flagged in macron-report (true: Vespasiānō)

 'CAVE CANEM — Cavē canem!':'/ˈka.weː ˈka.nɛm/', 'familia → family':'/fa.ˈmɪ.lɪ.a/',
 'regina rēgīna legis':'/ˈrɛ.gɪ.na reː.ˈgiː.na ˈlɛ.gɪs/',   # policy: macronized text is trusted (no fallback; avoids legis->lēgis)
}
VERSE_TESTS = {  # Allen VL on elision/final -m; Aen. 1.3, Hor. Od. 3.2.13, Cat. 85
 'multum ille et terrīs':'/ˈmʊl.t‿ˈɪl.l‿ɛt ˈtɛr.riːs/',
 'Dulce et decōrum est':'/ˈdʊl.k‿ɛt dɛ.ˈkoː.rʊm‿st/',
 'Quāre id faciam':'/ˈkʷaː.r‿ɪd ˈfa.kɪ.ãː/',
}
def run_tests():
    ok=0
    for w,exp in TESTS.items():
        got=word_tx(w)[0]
        g=got.replace('.ˈ','ˈ'); e=exp.replace('.ˈ','ˈ')
        good = g==e
        ok+=good
        print(('PASS' if good else 'FAIL'), w, '/'+got+'/', '' if good else 'expected /'+exp+'/')
    n=len(TESTS)
    for w,exp in RESP_TESTS.items():
        got=word_tx(w)[1]; n+=1; ok+=got==exp
        if got!=exp: print('FAIL resp',w,got,'expected',exp)
    for t,exp in VERSE_TESTS.items():
        got=transcribe(t,verse=True)[0].replace('.ˈ','ˈ'); n+=1; ok+=got==exp.replace('.ˈ','ˈ')
        if got!=exp.replace('.ˈ','ˈ'): print('FAIL verse',t,got,'expected',exp)
    init_lexicon()
    for t,exp in FALLBACK_TESTS.items():
        got=transcribe(t)[0]; n+=1; ok+=got==exp
        if got!=exp: print('FAIL fallback',t,got,'expected',exp)
    import subprocess
    cli=subprocess.run([sys.executable,os.path.abspath(__file__),'--verse','multum ille'],capture_output=True,text=True); n+=1
    ok+= cli.returncode==0 and 'mʊl.t‿' in cli.stdout
    if cli.returncode: print('FAIL cli --verse',cli.stderr[-200:])
    print(f'{ok}/{n} passed (IPA words, respellings, verse, lexicon fallback, CLI)'); return ok==n

VERSE_WORKS=re.compile(r"Aeneid|Georgic|Eclogue|Odes|Satires|Epistles|Epigram|Carmina$|^Carmina|Fasti|Metamorphoses|Ars Amatoria|Epistulae ex Ponto|De Rerum Natura|Epitaphium|Amores|Tristia",re.I)
def is_verse(c):
    src=c.get('source') or {}
    w=src.get('work','') if isinstance(src,dict) else str(src)
    if 'Burana' in w or 'Dies irae' in w or 'Symphonia' in w or 'Confessio' in w: return False  # rhythmic medieval verse: no classical elision
    return bool(VERSE_WORKS.search(w))

def entry(c,f):
    CARD_LEX.clear()
    for g in c.get('gloss') or []:
        w=(g.get('word') or '').strip(".,;:!?").lower()
        if any(ch in MACRONS for ch in w): CARD_LEX[plain(w)]=w
    r=transcribe(c.get('latin',''))
    if not r: return None
    e={'ipa':r[0],'respelling':r[1]}
    if is_verse(c):
        v=transcribe(c['latin'],verse=True)
        if v and v!=r: e['ipa_verse'],e['respelling_verse']=v
    return e

def all_cards():
    base=os.path.dirname(os.path.abspath(__file__)); root=os.path.dirname(base)
    cards=[]
    for f in ('rome-cards.json','medieval-cards.json','learning-cards.json')+tuple(x for x in ('batch4-cards.json','batch5-cards.json','batch6-cards.json') if os.path.exists(os.path.join(base,x))):
        cards+=[(c,f) for c in json.load(open(os.path.join(base,f)))]
    js=open(os.path.join(root,'cards','cards.js')).read()
    cards+=[(c,'cards.js') for c in json.loads(js[js.index('['):js.rindex(']')+1])]
    return cards

def init_lexicon():
    base=os.path.dirname(os.path.abspath(__file__))
    texts=[]
    for c,_ in all_cards():
        texts+=[g.get('lemma','') for g in c.get('gloss') or []]
    return load_lexicon(texts, os.path.join(base,'data','dcc-core.json'))

def macron_check(c):
    """Words in card Latin with no macron: 'fixed' = lexicon supplied length; 'unverified' = polysyllable
    with no macron and no lexicon entry (may be genuinely all-short, e.g. pater; needs a human/dictionary check);
    'ambiguous' = lexicon has conflicting macronizations."""
    fixed=[];unver=[];amb=[]
    t=c.get('latin','')
    if any(ch in MACRONS for ch in t.lower()): return fixed,unver,amb   # macronized card: trusted
    entry(c,'')  # load card gloss lexicon
    for w in words_of(t):
        w=w.rstrip('|')
        if re.search(r'[a-z]',t) and w.isupper() and len(w)>1: continue
        if any(ch in MACRONS for ch in w.lower()): continue
        k=plain(w)
        if CARD_LEX.get(k): fixed.append([w,CARD_LEX[k]])
        elif k in LEX:
            (fixed.append([w,LEX[k]]) if LEX[k] else amb.append(w))
        else:
            seg=segment(w)
            if seg and sum(t=='V' for _,t in seg)>=2: unver.append(w)
    return fixed,unver,amb

def build():
    base=os.path.dirname(os.path.abspath(__file__)); root=os.path.dirname(base)
    init_lexicon()
    out={}; rep=[]
    for c,f in all_cards():
        e=entry(c,f)
        if e: out[c['id']]=dict(e,latin=c['latin'],src=f)
        fx,un,am=macron_check(c)
        nomac=not any(ch in MACRONS for ch in c.get('latin','').lower())
        if fx or un or am:
            rep.append({'id':c['id'],'file':f,'latin':c.get('latin',''),'no_macrons_at_all':nomac,
                        'lexicon_fixed':fx,'unverified':un,'ambiguous':am})
            if e and fx: out[c['id']]['macron_fallback']=fx
    json.dump({'_legend':LEGEND,**out},open(os.path.join(base,'phonetics.json'),'w'),ensure_ascii=False,indent=1)
    slim={k:{x:y for x,y in v.items() if x not in('latin','src','macron_fallback')} for k,v in out.items()}
    open(os.path.join(root,'cards','phonetics.js'),'w').write('// Generated by content/phonetics.py --build. Do not edit.\nwindow.PHONETICS_LEGEND = '+json.dumps(LEGEND,ensure_ascii=False)+';\nwindow.PHONETICS = '+json.dumps(slim,ensure_ascii=False,indent=1)+';\n')
    json.dump(rep,open(os.path.join(base,'macron-report.json'),'w'),ensure_ascii=False,indent=1)
    L=['# Macron report (generated by phonetics.py --build)','',
       f'Lexicon: {sum(1 for v in LEX.values() if v)} unambiguous macronized forms (card Latin + glosses + DCC core headwords).','',
       '- **fixed**: the word had no macron in the card; the engine used the lexicon form for IPA/respelling. The card text itself should be corrected.',
       '- Only cards whose Latin has NO macrons are checked; macronized cards are trusted (unmarked = short).\n- **unverified**: polysyllable with no macron and no lexicon entry; may be all-short (pater) or missing macrons. Check against L&S.',
       '- **ambiguous**: lexicon has conflicting forms (e.g. -a vs -ā); left as written.','']
    for r in rep:
        L.append(f"## {r['id']} ({r['file']}){' — NO MACRONS AT ALL' if r['no_macrons_at_all'] else ''}")
        L.append(f"> {r['latin']}")
        if r['lexicon_fixed']: L.append('- fixed: '+', '.join(f'{a}→{b}' for a,b in r['lexicon_fixed']))
        if r['unverified']: L.append('- unverified: '+', '.join(r['unverified']))
        if r['ambiguous']: L.append('- ambiguous: '+', '.join(r['ambiguous']))
        L.append('')
    open(os.path.join(base,'macron-report.md'),'w').write('\n'.join(L))
    print(len(out),'entries;',sum('ipa_verse' in v for v in out.values()),'verse variants;',
          len(rep),'cards flagged;',sum(len(r['lexicon_fixed']) for r in rep),'words fixed by lexicon;',
          sum(r['no_macrons_at_all'] for r in rep),'cards with no macrons at all')

if __name__=='__main__':
    a=sys.argv[1:]
    if a and a[0] not in('--test','--build'):
        try: init_lexicon()
        except Exception: pass
    if a and a[0]=='--verse':
        r=transcribe(' '.join(a[1:]),verse=True)
        print(r[0] if r else '(no Latin)'); print(r[1] if r else ''); sys.exit(0)
    if a==['--test']: sys.exit(0 if run_tests() else 1)
    elif a==['--build']: build()
    else:
        r=transcribe(' '.join(a))
        print(r[0] if r else '(no Latin)'); print(r[1] if r else '')
