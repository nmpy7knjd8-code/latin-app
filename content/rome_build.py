import json,unicodedata,re
LL='https://www.thelatinlibrary.com/'
WM='https://commons.wikimedia.org/wiki/File:'
def strip(s): return ''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn').lower()
dcc=set()
for r in json.load(open(''+__import__('os').path.dirname(__import__('os').path.abspath(__file__))+'/data/dcc-core.json')):
    for seg in re.split(r'[;,]',r[0]):
        if seg.split(): dcc.add(strip(seg.split()[0]))
dcc|={'ab','malum','-que','tu + -que','tertium','filius','quis','qui','ego','tu','is','hic','sum','et','in','non','sui','meus','tuus','noster'}
def img(file,kind,alt,lic,credit,transp=None,aspect='3:4'):
    if transp is None: transp=kind in('statue_cutout','coin','artifact')
    return dict(src='TODO:'+file,alt=alt,kind=kind,aspect=aspect,transparent=transp,license=lic,credit=credit,source_url=WM+file.replace(' ','_'))
IM={
 'pantheon':img('Fotografi. Pantheon di Agrippa. Rom, Italien - Hallwylska museet - 104733.tif','building','19th-c. photograph of the Pantheon portico with the Agrippa inscription','Public domain','Hallwyl Museum, Stockholm (photograph collection)'),
 'titus':img('Arco di Tito plaque forum romanum Rome Italy.jpg','inscription','Dedicatory inscription on the Arch of Titus, Roman Forum','CC0','Arch of Titus, Rome · Wikimedia Commons (CC0)'),
 'wolf':img('Lupa Capitolina, Rome.jpg','statue_cutout','Bronze she-wolf (Lupa Capitolina), Capitoline Museums','CC0','Lupa Capitolina, Musei Capitolini · Wikimedia Commons (CC0)','statue_cutout' and True,'4:3'),
 'romulus':img('Romulus and Remus MET DP822897.jpg','artifact','Romulus and Remus with the she-wolf, The Met','CC0','The Metropolitan Museum of Art (Open Access)'),
 'cornelia':img('Francesco Bartolozzi - Cornelia, Mother of the Gracchi - B1977.14.19782 - Yale Center for British Art.jpg','painting','Bartolozzi print: Cornelia presents her sons as her jewels','CC0','Francesco Bartolozzi · Yale Center for British Art'),
 'woman':img('Marble portrait bust of a woman MET DP345018.jpg','statue_cutout','Roman marble portrait bust of a woman, The Met','CC0','The Metropolitan Museum of Art (Open Access)'),
 'boy':img('Marble portrait bust of a boy MET DP328527.jpg','statue_cutout','Roman marble portrait bust of a boy, The Met','CC0','The Metropolitan Museum of Art (Open Access)'),
 'soldier':img('Fragmentary marble head of a helmeted soldier MET DP106984.jpg','statue_cutout','Marble head of a helmeted soldier, Flavian period, The Met','CC0','The Metropolitan Museum of Art (Open Access)'),
 'cuirass':img('Bronze torso from an equestrian statue wearing a cuirass MET DP108183.jpg','statue_cutout','Bronze torso of a Roman commander in a cuirass, The Met','CC0','The Metropolitan Museum of Art (Open Access)'),
 'augustus':img('Marble portrait of the emperor Augustus MET DP331249.jpg','statue_cutout','Marble portrait of the emperor Augustus, The Met','CC0','The Metropolitan Museum of Art (Open Access)'),
 'primaporta':img('Statue-Augustus.jpg','statue_cutout','Augustus of Prima Porta, Vatican Museums','Public domain','Augustus of Prima Porta · Wikimedia Commons (public domain)','statue_cutout' and True,'2:3'),
 'octavian':img('Silver denarius of Octavian MET sf0817088r.jpg','coin','Silver denarius of Octavian, The Met','CC0','The Metropolitan Museum of Art (Open Access)',None,'4:5'),
 'venus':img('Marble statue of Aphrodite, the so-called Venus Genetrix MET DP107609.jpg','statue_cutout','Marble Venus Genetrix, The Met','CC0','The Metropolitan Museum of Art (Open Access)'),
 'laocoon':img('Laocoön and his sons group.jpg','statue_cutout','Laocoön and his sons, Vatican Museums','CC0','Laocoön group · Wikimedia Commons (CC0)'),
 'colosseum':img('Giovanni Battista Piranesi, The Colosseum.png','painting','Piranesi etching of the Colosseum','Public domain','Giovanni Battista Piranesi · public domain',False,'4:3'),
 'virgil':img('Virgil mosaic in the Bardo National Museum (Tunis) (12241228546).jpg','painting','Virgil between two Muses, mosaic, Bardo Museum','Public domain','Virgil Mosaic, Bardo Museum, Tunis · Wikimedia Commons'),
 'muses':img('Marble sarcophagus with the contest between the Muses and the Sirens MET DP138718.jpg','artifact','Sarcophagus with Muses and Sirens, The Met','CC0','The Metropolitan Museum of Art (Open Access)',None,'2:1'),
 'lamp':img('Oil Lamp MET cop0414s1.jpg','artifact','Ancient clay oil lamp, The Met','CC0','The Metropolitan Museum of Art (Open Access)',None,'4:3'),
 'cup':img('Glass cup MET DP203343.jpg','artifact','Roman glass cup, The Met','CC0','The Metropolitan Museum of Art (Open Access)'),
 'seneca':img('Pseudo-Seneca BM GR1962.8-24.1.jpg','statue_cutout','"Pseudo-Seneca" bronze-type head, British Museum (identity uncertain)','Public domain','British Museum · Wikimedia Commons'),
 'memento':img('Roman Mosaic Reminder of Death, from the House 1, 5, 2 in Pompeii (48451661416).jpg','painting','Pompeian memento-mori mosaic: skull, level and wheel','Public domain','Naples Archaeological Museum · Wikimedia Commons',False,'1:1'),
 'hannibal':img('Hannibal Barca bust from Capua photo.jpg','statue_cutout','Marble bust from Capua traditionally identified as Hannibal','Public domain','Wikimedia Commons (public domain)'),
 'resgestae':img('Res gestae divi Augusti, GD006036.jpg','inscription','Res Gestae text on the Temple of Augustus, Ankara','Public domain','Wikimedia Commons (public domain)',False,'4:3'),
 'gnothi':img('Roman-mosaic-know-thyself.jpg','painting','Roman mosaic of a skeleton with the Greek motto "know thyself"','Public domain','Museo Nazionale Romano · Wikimedia Commons',False,'4:3'),
 'cicero':{"src":"img/cicero.webp","alt":"Marble bust of Cicero, Capitoline Museums, cut out","kind":"statue_cutout","aspect":"3:4","transparent":True,"license":"CC0","credit":"Bust of Cicero, Capitoline Museums","source_url":"https://commons.wikimedia.org/wiki/File:M._Tullius_Cicero,_Capitoline_Museum,_Rome_(cropped).png"},
 'caesar':{"src":"img/caesar.webp","alt":"Tusculum portrait of Julius Caesar, cut out","kind":"statue_cutout","aspect":"3:4","transparent":True,"license":"Public domain","credit":"Tusculum portrait, Turin · photo Jastrow","source_url":"https://commons.wikimedia.org/wiki/File:Head_of_Julius_Caesar_from_Tusculum_MAntTorino_2089_n01.jpg"},
 'horace':{"src":"img/horace.webp","alt":"Manuscript page of Horace","kind":"manuscript","aspect":"3:4","transparent":False,"license":"Public domain","credit":"see existing horace card","source_url":"https://commons.wikimedia.org/"},
}
C=[]
def card(id,unit,era,person,latin,tr,work,cit,date,url,conf,tags,ctx,teach,im,gl,note=None,core_skip=()):
    g=[]
    for s in gl.split(';'):
        w,l,m,*p=[x.strip() for x in s.split('|')]
        d=dict(word=w,lemma=l,meaning=m)
        if p: d['parse']=p[0]
        if 'proper' in p: d['proper']=True
        g.append(d)
    lem=[strip(x['lemma']) for x in g if not x.get('proper')]
    known=[x for x in lem if x in dcc]
    pct=round(100*len(known)/max(1,len(lem)))
    c=dict(id=id,type='quote',era=era,unit=unit,latin=latin,translation=tr,context=ctx,person=person,
      source=dict(work=work,citation=cit,date=date),source_url=url,attribution_confidence=conf)
    if note: c['attribution_note']=note
    c.update(gloss=g,grammar_tags=tags,vocab_ids=sorted(set(lem)),
      teaching_value=dict(note=teach,dcc_core_pct=pct,non_core=[x for x in lem if x not in dcc]),
      unlock_rule=dict(min_vocab_known=0.7,review_threshold=0.9))
    for x in g: x.pop('proper',None)
    if im: c['image']=IM[im]
    assert len(ctx)<=260,(id,len(ctx))
    C.append(c)
exec(open(''+__import__('os').path.dirname(__import__('os').path.abspath(__file__))+'/rome_cards.py').read())

import os,sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from rome_meta import META,TAUGHT,IMGS,EXISTING,WP
CRED=json.load(open(os.path.join(HERE,'data','rome-image-credits.json')))
EXIST_IMG={}
try:
    js=open(os.path.join(HERE,'..','cards','cards.js')).read()
    arr=json.loads(js[js.index('['):js.rindex(']')+1])
    for c in arr:
        if 'image' in c: EXIST_IMG[c['image']['src']]=c['image']
except Exception as e: print('warn: cards.js',e)
errs=[]
for c in C:
    s,t=c['teaching_value']['note']; c['teaching_value']['note']=t
    unit,target,preview,ik,lml,lmt=META[c['id']]
    c['unit']=unit
    c['grammar_target']=target; c['grammar_preview']=preview; c['grammar_tags']=target+preview
    for tg in target:
        if tg not in TAUGHT: errs.append(f"{c['id']}: unknown tag {tg}")
        elif TAUGHT[tg]>unit: errs.append(f"{c['id']}: target {tg} taught U{TAUGHT[tg]} > card U{unit}")
    for tg in preview:
        if tg not in TAUGHT: errs.append(f"{c['id']}: unknown preview tag {tg}")
    pct=c['teaching_value']['dcc_core_pct']
    if s==5 and pct<80: s=4
    c['teaching_value']['score']=s
    c['teaching_value']['role']='anchor' if (pct>=80 and target) else 'preview'
    c['vocab_ids']=[v for v in c['vocab_ids'] if ' ' not in v]
    if ik in EXISTING:
        im=dict(EXIST_IMG.get(EXISTING[ik]) or {}); im['src']=EXISTING[ik]
        if not im.get('source_url'): errs.append(f"{c['id']}: missing existing image meta {ik}")
    else:
        f,kind,alt,lic,cr,asp,tr=IMGS[ik]
        im=dict(src=f'img/rome/{ik}.webp',alt=alt,kind=kind,aspect=asp,transparent=tr,license=lic,credit=cr,source_url='https://commons.wikimedia.org/wiki/File:'+f.replace(' ','_'))
        if not os.path.exists(os.path.join(HERE,im['src'])): errs.append(f"{c['id']}: image file missing {im['src']}")
    if ik not in EXISTING:
        cr=CRED.get(ik,{}); art=re.split(r' You are free| \(talk\)',cr.get('artist',''))[0].strip()
        title=f.rsplit('.',1)[0]
        im['modified']='background removed (cut-out), cropped, resized' if tr else 'cropped to %s, resized'%asp
        if 'BY' in lic:
            im['license_url']=cr.get('licence_url','')
            im['credit']=f'“{title}” by {art or "unknown"}, {lic} ({cr.get("licence_url","")}), via Wikimedia Commons; modified: {im["modified"]}'
            if not art or not cr.get('licence_url'): errs.append(f"{c['id']}: CC BY credit incomplete")
        elif art: im['credit']=f'{cr_ if (cr_:=im["credit"]) else ""} · {art}'[:240]
    c['image']=im
    url=('https://ancientgraffiti.org/Graffiti/graffito/'+lmt[4:]) if lmt.startswith('AGP:') else ('https://romaninscriptionsofbritain.org/inscriptions/'+lmt[4:]) if lmt.startswith('RIB:') else WP+lmt
    c['learn_more']=dict(label=lml,url=url)
    for k in ('credit','source_url'):
        v=str(im.get(k,''))
        if 'see existing' in v or v.rstrip('/')=='https://commons.wikimedia.org': errs.append(f"{c['id']}: placeholder {k}")
    if c.get('attribution_note','').startswith('Speech') : pass
from collections import Counter
dup=[k for k,v in Counter(c['image']['src'] for c in C).items() if v>1]
C.sort(key=lambda c:(-c['teaching_value']['score'],-c['teaching_value']['dcc_core_pct'],c['unit']))
for i,c in enumerate(C,1): c['teaching_value']['rank']=i
from collections import defaultdict
byu=defaultdict(list)
for c in C: byu[c['unit']].append(c)
warn=[]
for u,L in sorted(byu.items()):
    for k,c in enumerate(L):
        if k>=10: c['bonus']=True; c['bonus_set']='Lege plūra'
        else: c.pop('bonus',None); c.pop('bonus_set',None)
    core=min(len(L),10)
    if core<4 or len(L)>10: warn.append(f'U{u}: {len(L)} cards ({len(L)-core} bonus)')
json.dump(C,open(os.path.join(HERE,'rome-cards.json'),'w'),ensure_ascii=False,indent=1)
for c in C: print(c['teaching_value']['rank'],c['teaching_value']['score'],c['teaching_value']['role'],c['teaching_value']['dcc_core_pct'],'U%d'%c['unit'],c['id'])
print('duplicate images:',dup)
print('unit balance warnings:',warn)
if errs:
    print('LINT ERRORS:'); [print(' ',e) for e in errs]; sys.exit(1)
print('lint ok')
