"""Apply review-medieval-3.md."""
import json
F="medieval-cards.json"; cs={c["id"]:c for c in json.load(open(F))}
c=cs["r-vulg-john-1-5"]; c["translation"]=c["translation"].replace("did not overcome it","did not comprehend it")
for g in c["gloss"]:
    if g["word"]=="conprehendērunt": g["meaning"]="grasped, comprehended"
c=cs["q-gesta-latro"]
for g in c["gloss"]:
    if g["word"]=="galeā": g["meaning"]="galley (medieval sense; classical galea = helmet)"
c["text_check"]="verified vs Latin Library ch. 146 ('latro vocor … diceris imperator')"
c=cs["q-colophon-tres-digiti"]
c["text_check"]="verified verbatim vs IRHT Bibale 18684 (BnF lat. 12234): 'Tres digiti scribunt, sed totum corpus laborat. Sicut nauiganti dulcis est portus, ita scriptori nouissimus uersus.'"
c["attribution_note"]="This is a widespread scribal formula, and its wording varies. Other manuscripts read 'tōtum corpusque labōrat' and 'nāvigantibus'. This card quotes the BnF lat. 12234 witness exactly. The image shows a different scribe (Eadwine, 12th c.)."
c=cs["q-archpoet-taberna"]; c["translation"]="It is my plan to die in the tavern, so that wine may be near the mouth of the dying man."
for g in c["gloss"]:
    if g["word"]=="morientis": g["meaning"]="of the dying man"; g["parse"]="pres. part. gen. sg. m. (substantive)"
c=cs["q-paris-statute-1215"]; c["image"]["caption_la"]="Bonōniae, nōn Parīsiīs (Bologna, not Paris)"
json.dump(list(cs.values()),open(F,"w"),ensure_ascii=False,indent=1)
