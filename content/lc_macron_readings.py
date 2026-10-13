"""Idempotent patch: add lower-case macronized expanded readings after capitals on inscription/coin
learning cards (MACRON-POLICY.md). Run after any other lc_*/gen_learning step."""
import json,os
P=os.path.join(os.path.dirname(os.path.abspath(__file__)),'learning-cards.json')
C=json.load(open(P))
R={'i-pantheon-parse':('M·AGRIPPA·L·F·COS·TERTIVM·FECIT','Mārcus Agrippa Lūcī fīlius cōnsul tertium fēcit'),
   'i-coin-divi-f':('IMP·CAESAR·DIVI·F','Imperātor Caesar Dīvī fīlius'),
   'i-karolus':('KAROLVS IMP AVG','Karolus Imperātor Augustus')}
n=0
for c in C:
    if c['id'] in R:
        cap,rd=R[c['id']]
        if c['latin'].split(' — ')[0]==cap and ' — ' not in c['latin']:
            c['latin']=f'{cap} — {rd}'; n+=1
    if c['id']=='i-chirho' and 'Omega' in c['latin']:
        c['latin']=c['latin'].replace('Omega','Ōmega'); n+=1
        for g in c.get('gloss',[]):
            if g.get('word')=='Omega': g['word']='Ōmega'; g['lemma']='Ōmega'
json.dump(C,open(P,'w'),ensure_ascii=False,indent=1)
print('patched',n)
