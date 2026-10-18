"""Patch medieval-cards.json (idempotent): give unit 11/12 cards explicit grammar_target / grammar_preview
using the shared tag names, so Units XI-XII show the grammar they actually carry (see game-design.md section 3)."""
import json,os
HERE=os.path.dirname(os.path.abspath(__file__)); P=os.path.join(HERE,'medieval-cards.json')
T={ # id: (target, preview)
 'q-archpoet-taberna':(['subjunctive','dative'],['deponent']),          # ut sint (purpose subj.); morī deponent inf.
 'q-heloise-meretrix':(['comparative','subjunctive','passive_voice'],[]), # cārius/dignius … quam; vidērētur; dīcī
 'q-abelard-dubitando':(['ablative_means'],['gerund']),                   # dubitandō, inquīrendō
 'q-magna-carta-39':(['jussive_subjunctive','passive_voice'],[]),       # capiātur, imprisonētur
 'q-paris-statute-1215':(['jussive_subjunctive','passive_voice'],[]),   # nōn legantur
 'q-mon-unum':(['superlative','indirect_statement','passive_voice'],[]),# optimē; sē habēre; regitur
 'q-gesta-latro':(['passive_voice','present_participle','ablative_means'],[]),
 'q-aquinas-tardiloquum':(['infinitive','accusative'],[]),             # iubeō + acc. + inf. is a command, not indirect statement
}
DROP={'q-aquinas-tardiloquum':['indirect_statement']}  # stale tags from earlier retag
CTX={ # id: (old substring, new substring) - idempotent context corrections
 'q-archpoet-taberna':("Mihi est prōpositum, 'it is my plan', uses the dative of possession.","Meum est prōpositum, 'my plan is', uses the possessive adjective meum; ōrī is a dative after proxima, 'nearest to'."),
 'q-aquinas-tardiloquum':("its authorship is not certain.","its authorship is not certain. Iubeō, 'I order', takes an accusative and infinitive, tē esse, 'you to be': a command, not an indirect statement."),
}
C=json.load(open(P)); n=0
for c in C:
    if c['id'] in T:
        t,p=T[c['id']]; c['grammar_target']=t; c['grammar_preview']=p
        tags=c.get('grammar_tags',[])
        tags=[x for x in tags if x not in DROP.get(c['id'],[])]
        for x in t+p:
            if x not in tags: tags.append(x)
        c['grammar_tags']=tags; n+=1
    if c['id'] in CTX:
        a,b=CTX[c['id']]
        if b not in c['context']:
            assert a in c['context'],c['id']; c['context']=c['context'].replace(a,b)
json.dump(C,open(P,'w'),ensure_ascii=False,indent=1); print(n,'medieval cards retagged')
