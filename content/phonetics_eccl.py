#!/usr/bin/env python3
"""Ecclesiastical (Italianate / Roman Church) respelling for ecclesiastical-register cards.
Conventions follow the Liber Usualis-style 'Italian' pronunciation: c/cc before e,i,ae,oe,y = ch/tch;
g before front vowel = j; gn = ny; sc before front vowel = sh; ti + vowel (not after s,t,x) = tsee;
ae/oe = eh; h silent (mihi, nihil = MEE-kee, NEE-keel); v = v; consonantal i = y; ph = f; th = t; ch = k;
vowel length not distinguished (a ah, e eh, i ee, o oh, u oo). Stress as classical (penult rule), from phonetics.py.
Simplifications: x is always ks (no 'egz'); no regional (German/French) variants.
Usage: python3 phonetics_eccl.py --build  -> content/phonetics-eccl.json"""
import json,os,re,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import phonetics as P
FRONT={'ɛ','eː','ɪ','iː','ʏ','yː','ae̯','oe̯'}
V={'a':'ah','aː':'ah','ɛ':'eh','eː':'eh','ɪ':'ee','iː':'ee','ɔ':'oh','oː':'oh','ʊ':'oo','uː':'oo','ʏ':'ee','yː':'ee',
   'ae̯':'eh','oe̯':'eh','au̯':'ow','ei̯':'ay','eu̯':'eh-oo','ui̯':'wee'}
C={'k':'k','g':'g','w':'v','j':'y','pʰ':'f','tʰ':'t','kʰ':'k','kʷ':'kw','gʷ':'gw','ŋ':'n','dz':'dz'}
def word(w):
    seg=P.segment(w)
    if not seg: return None
    syl=P.syllabify(seg)
    if not syl: return None
    st=P.stress_index(syl,w)
    flat=[(p,t,k) for k,s in enumerate(syl) for p,t in s]
    out=['' for _ in syl]; lw=w.lower()
    for i,(p,t,k) in enumerate(flat):
        nxt=flat[i+1][0] if i+1<len(flat) else ''; nn=flat[i+2][0] if i+2<len(flat) else ''
        prv=flat[i-1][0] if i>0 else ''
        if t=='V': r=V.get(p,p)
        elif p=='k' and nxt in FRONT: r='sh' if prv=='s' else 'ch'
        elif p=='k' and nxt=='k' and nn in FRONT: r='t'
        elif p=='s' and nxt=='k' and nn in FRONT: r=''
        elif p=='g' and nxt in FRONT: r='j'
        elif p=='ŋ' and nxt=='n': r=''
        elif p=='n' and prv=='ŋ': r='ny'
        elif p=='t' and nxt in('ɪ','iː') and flat[i+2][1]=='V' if i+2<len(flat) else False:
            r='t' if prv in('s','t','k') else 'ts'
        elif p=='h': r='k' if lw in('mihi','nihil','michi') else ''
        else: r=C.get(p,p)
        out[k]+=r
    return '-'.join(s.upper() if k==st else s for k,s in enumerate(out))
def transcribe(text):
    ws=[word(w) for w in P.TOKEN.findall(text or '') if not (len(w)==1 and w.lower() not in 'aeiouāēīōūō')]
    ws=[w for w in ws if w]; return ' '.join(ws) or None
def build():
    base=os.path.dirname(os.path.abspath(__file__)); out={"_note":"Ecclesiastical (Italianate church) pronunciation respelling; see phonetics_eccl.py docstring. Classical IPA/respelling remain in phonetics.json."}
    for f in ('medieval-cards.json','rome-cards.json'):
        for c in json.load(open(os.path.join(base,f))):
            if c.get('register')=='ecclesiastical':
                out[c['id']]={'respelling_eccl':transcribe(c['latin']),'latin':c['latin'],'system':'italianate-ecclesiastical','src':f}
    json.dump(out,open(os.path.join(base,'phonetics-eccl.json'),'w'),ensure_ascii=False,indent=1); print(len(out)-1,'entries')
TESTS={'caelīs':'CHEH-lees','gēns':'jehns','agnus':'AH-nyoos','Deī':'DEH-ee','mihi':'MEE-kee','glōria':'GLOH-ree-ah','grātia':'GRAH-tsee-ah','scientia':'shee-EHN-tsee-ah','ecce':'EHT-cheh','excelsīs':'ehk-SHEHL-sees'}
if __name__=='__main__':
    if sys.argv[1:]==['--test']:
        for w,e in TESTS.items(): g=word(w); print('PASS' if g.lower()==e.lower() else 'FAIL',w,g,e)
    elif sys.argv[1:]==['--build']: build()
    else: print(transcribe(' '.join(sys.argv[1:])))
