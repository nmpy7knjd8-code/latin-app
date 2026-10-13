import json
C=json.load(open("learning-cards.json"))
for c in C:
    if c["id"]=="l-bulla": c["grammar_preview"]=["adjective_agreement (taught Unit 4)"]
json.dump(C,open("learning-cards.json","w"),ensure_ascii=False,indent=1)
S={s["unit"]:s for s in json.load(open("learning-stories.json"))}
L=S[4]["lines"]; L.insert(L.index("Cicerō senātōribus verba dat."),"Sed Cicerō in templō Iovis Statōris dīcit.")
L=S[5]["lines"]; L[L.index("Ex templō aqua nōn venit, sed ignis.")]="Virginēs aquam ex fonte portant."
L=S[10]["lines"]; L[L.index("Abbās, quī eum vidēbat, laudāvit.")]="Abbās, quī monachum vidēbat, eum laudāvit."
S[6]["grammar_preview"]=["eius/eum pronouns (taught Unit 7)"]; S[6]["attribution_note"]="'Urbem marmoream relīquī' adapted from Suetonius, Aug. 28.3."
json.dump(list(S.values()),open("learning-stories.json","w"),ensure_ascii=False,indent=1)
