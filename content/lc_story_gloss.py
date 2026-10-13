import json,re,unicodedata
D={}
for l in open("story_glosses.txt"):
    k,lem,m,p=l.rstrip("\n").split("|");D[k]=(lem,m,p)
def n(s): return "".join(c for c in unicodedata.normalize("NFD",s) if unicodedata.category(c)!="Mn").lower()
S=json.load(open("learning-stories.json"));miss=set()
for s in S:
    s["gloss"]=[]
    for i,l in enumerate(s["lines"]):
        for w in re.findall(r"[A-Za-zāēīōūĀĒĪŌŪ]+",l):
            k=w.lower()
            if k not in D: miss.add(w);continue
            lem,m,p=D[k];s["gloss"].append(dict(line=i,word=w,lemma=lem,meaning=m,parse=p))
    s["vocab_ids"]=sorted({n(g["lemma"]) for g in s["gloss"] if g["lemma"][0].islower()})
    s["status"]="constructed micro-story (Ørberg-style); glossed; Latin to be reviewed"
json.dump(S,open("learning-stories.json","w"),ensure_ascii=False,indent=1);print("missing",miss)
