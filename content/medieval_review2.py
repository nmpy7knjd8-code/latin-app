"""Apply review-medieval-2.md partials + parent fixes."""
import json
F="medieval-cards.json"; cs={c["id"]:c for c in json.load(open(F))}
c=cs["q-abelard-dubitando"]
c["attribution_note"]="'quippe' is the reading of the Boyer & McKeon critical edition (1976–77), as transcribed by Peter King with B&M page markers (/104/). 'enim' is the older Henke–Lindenkohl/Migne (PL 178) text."
c["text_check"]="verified vs la.wikisource and Peter King's transcription of Boyer & McKeon (individual.utoronto.ca/pking/resources/abelard/Sic_et_non.txt); Migne reads 'enim'"
c=cs["q-mon-unum"]; c["source"]["citation"]="1.14.11"
c["attribution_note"]="Mon. 1.14.11: the closing sentence of ch. 14, before ch. 15 'In omni genere optimum esse quod est maxime unum'. Bibliotheca Augustana's chapter-numbered text (Ricci-type divisions, as used by Shaw) and the Latin Library agree."
c["text_check"]="verified vs Latin Library and Bibliotheca Augustana (tha.de/~harsch/.../dan_mn01.html)"
im=cs["q-bede-sparrow"]["image"]
im["alt"]="Modern reconstruction drawing of the Sutton Hoo helmet (A. T. Chester, Ordnance Survey, 1966)"
im["credit"]="A. T. Chester / Ordnance Survey (1966) · Wikimedia Commons"; im["modern_reconstruction"]=True
for i in ["q-bede-discere","q-bede-angli","q-bede-sparrow","q-alcuin-epitaph"]: cs[i]["register"]="medieval"
for i in ["q-aug-inquietum","q-aug-tolle-lege","q-aug-sero","q-aug-da-mihi"]: cs[i]["register"]="ecclesiastical"
json.dump(list(cs.values()),open(F,"w"),ensure_ascii=False,indent=1)
