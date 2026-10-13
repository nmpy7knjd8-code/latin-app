# Recompute Dickinson core % for medieval-cards.json from data/dcc-latin-core.csv
import json,csv,unicodedata,re
def strip(s): return "".join(ch for ch in unicodedata.normalize("NFD",s) if unicodedata.category(ch)!="Mn")
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
core["cito"]=1; core["suus"]=1; core["sui"]=1; core["tuus"]=1  # DCC lists citō under citus
F="medieval-cards.json"; cards=json.load(open(F))
for c in cards:
    ws=[g["lemma"].split()[0] for g in c["gloss"] if g["lemma"][0].islower()]; miss=sorted({strip(w).lower() for w in ws if n(w) not in core})
    c["teaching_value"]["dcc_core_pct"]=round(100*sum(n(w) in core for w in ws)/len(ws))
    c["teaching_value"]["non_core"]=miss
cards.sort(key=lambda c:(-c["teaching_value"]["score"],-c["teaching_value"]["dcc_core_pct"]))
for r,c in enumerate(cards,1): c["teaching_value"]["rank"]=r
json.dump(cards,open(F,"w"),ensure_ascii=False,indent=1)
for c in cards: print(c["teaching_value"]["score"],c["teaching_value"]["dcc_core_pct"],c["id"],c["teaching_value"]["non_core"])
