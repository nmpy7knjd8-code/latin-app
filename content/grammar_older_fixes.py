"""Idempotent grammar/text fixes from review-grammar-older.md for rome-, medieval- and learning-cards.json.
(Do NOT run rome_build.py: its inputs are stale. This script edits the built JSON in place.)"""
import json,os
HERE=os.path.dirname(os.path.abspath(__file__))
def S(cid,field,old,new):  # string replace in a top-level field, idempotent
    return ('S',cid,field,old,new)
def G(cid,idx_word,newg):   # replace gloss entries: idx_word = list of words to drop (first match), newg inserted at first dropped position
    return ('G',cid,idx_word,newg)
FIX={
'rome-cards.json':[
 G('q-virgil-arma',['Ītaliam','normally Ĭtalia)'],{'word':'Ītaliam','lemma':'Italia','meaning':'to Italy','parse':'acc. of motion (Ī lengthened for metre; normally Ĭtalia)'}),
 S('q-cicero-quousque','latin','Quō ūsque','Quō usque'),
 ('W','q-cicero-quousque','ūsque',{'word':'usque','lemma':'usque'}),
 S('q-ovid-expedit','translation','and, since it is useful,','and, as it is useful,'),
 S('q-cicero-cedant','context','Cedant is a subjunctive of wish','Cēdant is a subjunctive of wish'),
],
'medieval-cards.json':[
 S('q-vulg-gloria','context',"In excelsīs means 'in the highest (places)'.","In altissimīs means 'in the highest (places)'; the Gloria of the Mass says in excelsīs."),
 S('q-aug-da-mihi','context',"nōndum means 'not yet'.","nōlī modo, literally 'do not (do it) just now', means 'not yet'."),
 S('q-ben-ausculta','context',"Auscultā is an imperative, 'listen',","Obscultā (the manuscript spelling of auscultā) is an imperative, 'listen',"),
],
'learning-cards.json':[
 ('P','l-bulla','grammar_preview',['adjective_agreement']),
 S('x-whosays-cornelia','latin','Haec ornāmenta','Haec ōrnāmenta'),
 ('W','x-whosays-cornelia','ornāmenta',{'word':'ōrnāmenta','lemma':'ōrnāmentum'}),
 S('x-greek-flag','latin','Marcus Aurēlius','Mārcus Aurēlius'),
 ('W','x-greek-flag','Marcus Aurēlius',{'word':'Mārcus Aurēlius'}),
 S('i-karolus','context','like a Roman emperor., deliberately','like a Roman emperor, deliberately'),
 ('T','x-colophon','relative_clause'),
 S('l-monasterium','latin','monasterium, abbās','monastērium, abbās'),
 ('W','l-monasterium','monasterium',{'word':'monastērium'}),
 S('i-pantheon-parse','context','L·F is Lūciī fīlius','L·F is Lūcī fīlius'),
],
}
for fn,fixes in FIX.items():
    P=os.path.join(HERE,fn); C=json.load(open(P)); by={c['id']:c for c in C}; n=0
    for f in fixes:
        c=by[f[1]]
        if f[0]=='S':
            _,_,fld,old,new=f
            if new in c[fld]: continue
            assert old in c[fld],(f[1],fld,old); c[fld]=c[fld].replace(old,new); n+=1
        elif f[0]=='G':
            _,_,drop,newg=f; gl=c['gloss']
            if any(g==newg for g in gl): continue
            pos=[i for i,g in enumerate(gl) if g.get('word') in drop]; assert pos,f[1]
            c['gloss']=[g for i,g in enumerate(gl) if i not in pos]; c['gloss'].insert(pos[0],newg); n+=1
        elif f[0]=='W':
            _,_,word,upd=f
            for g in c['gloss']:
                if g.get('word')==word: g.update(upd); n+=1; break
        elif f[0]=='P':
            _,_,fld,val=f
            if c.get(fld)!=val: c[fld]=val; n+=1
        elif f[0]=='T':
            _,_,tag=f
            if tag in c.get('grammar_tags',[]): c['grammar_tags'].remove(tag); n+=1
    json.dump(C,open(P,'w'),ensure_ascii=False,indent=1); print(fn,n,'changes')
