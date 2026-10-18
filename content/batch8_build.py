"""Build content/batch8-cards.json from batch8_cards.py + batch8_images.py + img/batch8/meta.json. Lints unit order."""
import json,os,re,sys,unicodedata
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from batch8_cards import CARDS
from batch8_images import IMGS
from rome_meta import TAUGHT as _T
# Proposed grammar for the new Units 11-14 (game-design.md); units 1-10 unchanged.
TAUGHT=dict(_T)
for t in ['subjunctive','jussive_subjunctive','hortatory_subjunctive','indirect_question','comparative','superlative','ablative_of_comparison']: TAUGHT[t]=11
for t in ['deponent','ablative_with_deponent','gerundive','gerund','pluperfect','dum_clause']: TAUGHT[t]=12
for t in ['future_imperative','ablative_absolute','impersonal_verb','perfect_infinitive','dative_of_direction']: TAUGHT[t]=13
USED=set(open('/workspace/used_images.txt').read().replace('_',' ').split('\n'))
_own=os.path.join(os.path.dirname(os.path.abspath(__file__)),'img','batch8','meta.json')
if os.path.exists(_own): USED-={v.get('resolved','').replace('_',' ') for v in json.load(open(_own)).values() if isinstance(v,dict)}
META=json.load(open(os.path.join(HERE,'img','batch8','meta.json')))
def strip(s): return ''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn').lower()
dcc=set()
for r in json.load(open(os.path.join(HERE,'data','dcc-core.json'))):
    for seg in re.split(r'[;,]',r[0]):
        if seg.split(): dcc.add(strip(seg.split()[0]))
dcc|={'ab','-que','quis','qui','ego','tu','is','hic','sum','et','in','non','sui','meus','tuus','noster','nos','ipse','possum','volo'}
PROPER=lambda l:l[:1].isupper()
clean=lambda s:re.sub(r'\s+',' ',s).strip()
out=[];errs=[]
for a,kw in CARDS:
    (id,typ,era,unit,latin,tr,ctx,more,person,work,cit,date,surl,conf,note,gl,target,preview,ik,lml,lmu)=a
    g=[]
    for s in gl.split(';'):
        p=[x.strip() for x in s.split('|')]; d=dict(word=p[0],lemma=p[1],meaning=p[2])
        if len(p)>3: d['parse']=p[3]
        g.append(d)
    lem=[]
    for x in g:
        for l in re.split(r'\s*\+\s*',x['lemma']):
            l=strip(l)
            if l and l!='-que' and not PROPER(x['lemma']) and l not in lem: lem.append(l)
    known=[x for x in lem if x in dcc]; pct=round(100*len(known)/max(1,len(lem)))
    c=dict(id=id,type=typ,era=era,unit=unit,latin=latin,translation=tr,context=ctx,more=more)
    if person: c['person']=person
    c['source']=dict(work=work,citation=cit,date=date)
    if surl: c['source_url']=surl
    c['attribution_confidence']=conf
    if work=='Constructed' and conf!='constructed': errs.append(f'{id}: constructed card not marked constructed')
    if note: c['attribution_note']=note
    c['gloss']=g
    for t in target:
        if t not in TAUGHT: errs.append(f'{id}: unknown tag {t}')
        elif TAUGHT[t]>unit: errs.append(f'{id}: target {t} taught U{TAUGHT[t]} > U{unit}')
    for t in preview:
        if t not in TAUGHT: errs.append(f'{id}: unknown preview {t}')
    if unit<=3 and len(preview)>1: errs.append(f'{id}: >1 preview in U{unit}')
    c.update(grammar_target=target,grammar_preview=preview,grammar_tags=target+preview,vocab_ids=lem)
    score=5 if (pct>=80 and target and conf!='apocryphal') else 4 if pct>=60 else 3
    c['teaching_value']=dict(note=f"Targets {', '.join(target)}"+(f"; previews {', '.join(preview)}" if preview else '')+'.',dcc_core_pct=pct,non_core=[x for x in lem if x not in dcc],score=score,role='anchor' if (pct>=80 and target) else 'preview')
    c['unlock_rule']=dict(min_vocab_known=0.7,review_threshold=0.9)
    c['register']=kw.get('register','classical')
    if 'subtype' in kw: c['subtype']=kw['subtype']
    if 'formula' in kw: c['formula_glossed']=kw['formula']
    if 'related' in kw: c['related_cards']=kw['related']
    if 'raw' in kw: c['raw_text']=dict(text=kw['raw'][0],source=kw['raw'][1],label='What the original actually says')
    elif id.startswith(('i-','c-')): errs.append(f'{id}: inscription without raw_text')
    f,kind,alt,asp,trn=IMGS[ik]; m=META.get(ik)
    if not m: errs.append(f'{id}: no image meta {ik}'); continue
    if m.get('resolved',f) in USED: errs.append(f'{id}: image already used in another deck')
    if m['problems']: errs.append(f'{id}: image problems {m["problems"]}')
    src=f'img/batch8/{ik}.webp'
    if not os.path.exists(os.path.join(HERE,src)): errs.append(f'{id}: image file missing {src}')
    mod='background removed (cut-out), cropped, resized' if trn else f'cropped to {asp}, resized'
    lic={'PDM-owner':'PDM','No restrictions':'Public domain'}.get(m['license'],m['license']); art=clean(m['artist']) or 'unknown'
    title=m.get('resolved',f).rsplit('.',1)[0]
    if re.search(r'CC BY',lic,re.I):
        credit=f'“{title}” by {art}, {lic} ({m["license_url"]}), via Wikimedia Commons; modified: {mod}'
    else:
        credit=f'{art} · {lic} · via Wikimedia Commons'
    im=dict(src=src,alt=alt,kind=kind,aspect=asp,transparent=trn,license=lic,credit=credit,source_url=m['descurl'],modified=mod)
    if m['license_url']: im['license_url']=m['license_url']
    if m['license']=='No restrictions': im['license_note']='No known copyright restrictions (Flickr Commons); 15th-century manuscript, public domain'
    if lic.endswith(' fr'): im['license']=lic[:-3]; im['license_note']='Creative Commons '+lic.upper()+' (France port)'
    c['image']=im
    c['learn_more']=dict(label=lml,url=lmu)
    if len(ctx)>600: errs.append(f'{id}: context {len(ctx)}>600')
    for fld,txt in (('context',ctx),('more',more)):
        if re.search(r'\bUnit \d|preview|TODO|\bcard\b|\bgame\b|\btap\b|\bclick',txt,re.I): errs.append(f'{id}: internal/game wording in {fld}')
    ns=len(re.findall(r'[.!?]["\u201d\']?(?:\s|$)',ctx))
    if not 2<=ns<=4: errs.append(f'{id}: context has {ns} sentences')
    out.append(c)
# keep verified_http from previous build
P=os.path.join(HERE,'batch8-cards.json')
if os.path.exists(P):
    old={c['id']:c for c in json.load(open(P))}
    for c in out:
        o=old.get(c['id'],{}).get('learn_more',{})
        if o.get('url')==c['learn_more']['url'] and o.get('verified_http'): c['learn_more']['verified_http']=o['verified_http']
ids=[c['id'] for c in out]
assert len(ids)==len(set(ids))
def _decks(extra=()):
    D=[]
    for fn in ('rome-cards.json','medieval-cards.json','learning-cards.json','batch4-cards.json','batch5-cards.json','batch6-cards.json')+tuple(extra):
        if os.path.exists(os.path.join(HERE,fn)): D+=json.load(open(os.path.join(HERE,fn)))
    js=open(os.path.join(HERE,'..','cards','cards.js')).read()
    D+=json.loads(js[js.index('['):js.rindex(']')+1])  # base deck in cards.js
    return D
existing={c['id'] for c in _decks(('batch7-cards.json',))}
for i in ids:
    if i in existing: errs.append(f'{i}: id collides with existing card')
for c in out:
    for r in c.get('related_cards',[]):
        if r not in existing and r not in ids: errs.append(f'{c["id"]}: related {r} not found')
json.dump(out,open(P,'w'),ensure_ascii=False,indent=1)
print(len(out),'cards written'); print('\n'.join(errs) or 'lint OK')
# duplicate-Latin check against every existing deck
def key(s): return re.sub(r'[^a-z ]','',strip(s.split(' — ')[-1]).replace('v','u').replace('j','i'))
exl={}
for c in _decks(('batch7-cards.json',)): exl[key(c['latin'])]=c['id']
for c in out:
    k=key(c['latin']); w=k.split()
    for ek,eid in exl.items():
        if k==ek or (len(w)>=4 and ' '.join(w[:4]) in ek): print('DUP?',c['id'],'~',eid)
