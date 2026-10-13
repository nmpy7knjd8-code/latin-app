import json,csv,unicodedata,re
F="learning-cards.json"; C={c["id"]:c for c in json.load(open(F))}
def S(id,**kw): C[id].update(kw)
S("g-infinitive",latin="Atquī vīvere, Lūcīlī, mīlitāre est.",translation="And yet to live, Lucilius, is to serve as a soldier.")
S("g-impf",latin="Rōmānī lateribus aedificābant; Augustus marmore aedificābat.",translation="The Romans used to build with bricks; Augustus was building with marble.",
  context="Imperfect -bā- = ongoing or habitual past. Suetonius (Aug. 28.3) says Augustus boasted he left Rome marble though he had received it brick (marmoream sē relinquere, quam latericiam accēpisset).")
C["g-impf"].pop("source",None);C["g-impf"].pop("attribution_confidence",None);C["g-impf"]["attribution_note"]="Constructed sentences; Suetonius Aug. 28.3 (verified, Latin Library) cited in context only."
S("g-imperative",era="empire")
for id,cit,ctx in [("i-coin-divi-f","Octavian's denarius issues, c. 32–29 BC (legend CAESAR DIVI F); catalogue number (RIC I² Augustus) to be added from the imaged coin","Real coin legend."),
                   ("i-karolus","Charlemagne portrait denier, Mainz mint, c. 812–814 (legend KAROLVS IMP AVG)","Real coin legend.")]:
    C[id]["source"]={"work":"Coin legend","citation":cit};C[id]["attribution_confidence"]="verified";C[id].pop("attribution_note",None)
C["g-adj"].pop("source",None);C["g-adj"].pop("attribution_confidence",None)
C["g-adj"]["attribution_note"]="Constructed examples; Cato's definition cited in context (Quintilian 12.1.1, verified Latin Library)."
C["g-adj"]["context"]="Adjectives copy their noun's gender, number and case. Cato defined the orator as vir bonus dīcendī perītus, 'a good man skilled in speaking' (quoted by Quintilian, Inst. 12.1.1)."
S("i-chirho",latin="Ego sum Alpha et Omega.",translation="I am the Alpha and the Omega.",teaches="Vulgate sentence with sum; reading ☧/Α/Ω symbols on late Roman coins (image)")
S("g-future",latin="Regam, regēs, reget… Nōn omnis moriar.",translation="I shall rule, you will rule, s/he will rule… I shall not wholly die.",
  teaches="3rd-conj. future (-am, -ēs, -et) with regular regō first; Horace as the authentic sighting (moriar is deponent, flagged)",
  attribution_note="regam/regēs/reget constructed; Nōn omnis moriar = Horace Odes 3.30.6 (verified Latin Library).")
C["x-parse-signum"].update(translation="Twentieth Legion, Valeria Victrix",context="Expansion: LEG(IO) XX V(ALERIA) V(ICTRIX). "+C["x-parse-signum"]["context"])
C["g-relative"]["translation"]="Our Father, who are in heaven"
C["g-acc"]["translation"]="The father loves the son. (same meaning, different emphasis)"
C["l-bulla"]["teaches"]="Daily life vocab; adjective agreement as preview only (taught Unit 4)"
C["i-vindolanda"]["source"]={"work":"Tabulae Vindolandenses","citation":"Tab. Vindol. II 291, lines 11–14 (verified against RIB Online TabVindol291)"}
C["i-vindolanda"]["image"]["license_note"]="Commons lists CC BY-SA 3.0, but if the photo derives from British Museum imagery the BM terms are CC BY-NC-SA 4.0 — confirm before commercial use."
# glosses
cur=None;G={}
for ln in open("learning_glosses.txt"):
    ln=ln.rstrip("\n")
    if not ln or ln.startswith("#"):continue
    if ln.startswith("@"): cur=ln[1:];G[cur]=[];continue
    w,l,m,p=ln.split("|");G[cur].append(dict(word=w,lemma=l,meaning=m,parse=p))
def n(s): s="".join(ch for ch in unicodedata.normalize("NFD",s) if unicodedata.category(ch)!="Mn"); return s.lower().replace("j","i").replace("v","u")
core={}
for r in csv.DictReader(open("../data/dcc-latin-core.csv")):
    for part in r["Headword"].split(";"):
        t=part.split()
        if t: core.setdefault(n(t[0].strip(",")),int(r["Frequency Rank"]))
        if r["Part of Speech"] in("Preposition","Conjunction","Adverb","Pronoun"):
            for x in t: core.setdefault(n(x.strip(",")),int(r["Frequency Rank"]))
for k in("tu","ego","meus","noster","qui","hic"): core.setdefault(k,1)
for id,c in C.items():
    c["gloss"]=G[id]
    lem=[];[lem.append(g["lemma"]) for g in G[id] if g["lemma"] not in lem]
    c["vocab_ids"]=sorted(set(c.get("vocab_ids",[]))|{n(l).replace(" ","_") for l in lem})
    ws=[g["lemma"] for g in G[id] if g["lemma"][0].islower()]
    c["dcc_core_pct"]=round(100*sum(n(w) in core for w in ws)/len(ws)) if ws else None
    c["dcc_ranks"]={w:core.get(n(w)) for w in dict.fromkeys(ws)}
json.dump(list(C.values()),open(F,"w"),ensure_ascii=False,indent=1)
print([(i,c["dcc_core_pct"]) for i,c in C.items()])
