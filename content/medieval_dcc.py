# Recompute Dickinson core % for medieval-cards.json from data/dcc-latin-core.csv
import json,csv,unicodedata,re
def n(s):
    s=unicodedata.normalize("NFD",s); s="".join(c for c in s if unicodedata.category(c)!="Mn")
    return s.lower().replace("j","i").replace("v","u")
core={}
for r in csv.DictReader(open("../data/dcc-latin-core.csv")):
    for part in r["Headword"].split(";"):
        t=part.split()
        if t: core.setdefault(n(t[0].strip(",")),1)
        if r["Part of Speech"] in ("Preposition","Conjunction","Adverb","Pronoun"):
            for x in t: core.setdefault(n(x.strip(",")),1)
core["cito"]=1  # DCC lists citō under citus
F="medieval-cards.json"; cards=json.load(open(F))
for c in cards:
    ws=c["vocab_lemmas"]; miss=sorted({w for w in ws if n(w) not in core})
    c["teaching_value"]["dickinson_core_pct"]=round(100*sum(n(w) in core for w in ws)/len(ws))
    c["teaching_value"]["non_core_lemmas"]=miss
cards.sort(key=lambda c:(-c["teaching_value"]["score"],-c["teaching_value"]["dickinson_core_pct"]))
json.dump(cards,open(F,"w"),ensure_ascii=False,indent=1)
for c in cards: print(c["teaching_value"]["score"],c["teaching_value"]["dickinson_core_pct"],c["id"],c["teaching_value"]["non_core_lemmas"])
