"""Apply review-medieval.md: glosses, Rome-format metadata, register, fixes. Idempotent on medieval-cards.json."""
import json,unicodedata,urllib.parse,urllib.request
F="medieval-cards.json"; cs={c["id"]:c for c in json.load(open(F))}
def strip(s): return "".join(ch for ch in unicodedata.normalize("NFD",s) if unicodedata.category(ch)!="Mn")
def vnorm(w): return strip(w).lower().replace("uu","vu")
# --- drop Einhard (noun phrase, 43% core; review §9)
cs.pop("q-einhard-aachen",None)
# --- glosses
G={};cur=None
for line in open("medieval_glosses.txt"):
    line=line.rstrip("\n")
    if not line or line.startswith("#"): continue
    if line.startswith("@"): cur=line[1:];G[cur]=[];continue
    w,l,m,p=line.split("|");G[cur].append(dict(word=w,lemma=l,meaning=m,parse=p))
for i,c in cs.items(): c["gloss"]=G[i]
# --- text/context fixes
c=cs["q-kempis-transit"]; c["context"]="From The Imitation of Christ, the most-read devotional book of the late Middle Ages. The similar 'Sic transit gloria mundi' was chanted at papal coronations from the early 1400s."
c=cs["q-aug-tolle-lege"]; c["teaching_value"]["notes"]="Two 3rd-conjugation singular imperatives (tollō, legō): the model for tolle/lege/scrībe/dīc."
c=cs["q-ag-dei"]; c["grammar_tags"]=["relative_2sg","deponent_imperative","misereri_dative_eccl"]; c["attribution_note"]="Ecclesiastical usage: miserērī + dative. Classical Latin takes the genitive (cf. Ps 50 miserēre meī)."
c=cs["q-heloise-meretrix"]; c["latin"]=c["latin"].replace("Kārius","Cārius"); c["attribution_note"]="MS spelling karius normalised to cārius."
c["context"]="Héloïse to Abelard: even if Augustus, ruler of the world, offered to marry her, she would rather be called Abelard's mistress than his empress."
c["translation"]="It would seem dearer and more honourable to me to be called your mistress than his [Augustus's] empress."
c=cs["q-magna-carta-39"]; c["latin"]=c["latin"].replace("homo ","homō ")
c["attribution_note"]="The ellipsis omits 'aut disseisiātur, aut utlagētur, aut exulētur, aut aliquō modō dēstruātur, nec super eum ībimus, nec super eum mittēmus'. MS 'terre' normalised to 'terrae'. imprisonētur, disseisiātur and utlagētur are Anglo-Norman legal coinages, not vocabulary to learn."
c=cs["q-bede-sparrow"]; c["latin"]="…cum … adveniēns ūnus passerum domum citissimē pervolāverit."
c["translation"]="…as when … a single sparrow, arriving, has flown very swiftly through the hall."
c["grammar_tags"]=["partitive_genitive","superlative_adverb","present_participle"]; c["grammar_preview"]=["cum_subjunctive","perfect_subjunctive"]
c["attribution_note"]="Bede, HE 2.13: the full clause is 'quale cum te residente ad caenam … adueniens unus passerum domum citissime peruolauerit'. The intervening ablative absolutes are omitted."
c=cs["q-bede-angli"]; c["attribution_note"]="Bede's anecdote, reported decades later (hence traditional). Bede does NOT have the popular 'Non Angli sed angeli'. The real exchange is 'Angli … angelicam habent faciem'."
c["context"]="Bede tells how Gregory the Great saw English slave boys in Rome, punned on Anglī/angelī, and later sent missionaries to England (597)."
c=cs["q-bede-discere"]; c["context"]="Bede on his life as a monk at Wearmouth (from age seven) and then Jarrow, where he wrote the first history of the English church and people."
c=cs["q-carmina-o-fortuna"]; c["context"]="From a 13th-century songbook of student poets, probably written in South Tyrol or Carinthia and found at Benediktbeuern. Carl Orff set it to music in 1937."
c=cs["q-dies-irae"]; c["person"]="attrib. Thomas of Celano"
c=cs["q-aquinas-tardiloquum"]; c["attribution_note"]="The letter De modo studendi is attributed to Aquinas, but its authenticity is doubted."
c=cs["q-abelard-dubitando"]; c["attribution_note"]="la.wikisource reads 'quippe'; some editions read 'enim'. Check against Boyer & McKeon before print."
c=cs["q-mon-unum"]; c["attribution_note"]="Latin Library numbering 1.14.11. Standard (Shaw) numbering is likely 1.14 as well, but this has not been checked against a print edition."
c=cs["q-vulg-fiat-lux"]; c["teaching_value"]["notes"]="U9 first-sighting anchor for the passive: perfect passive facta est next to jussive fīat; -que enclitic; all core words."
# --- register
EC={"q-vulg-fiat-lux","q-vulg-in-principio","q-vulg-pater-noster","q-vulg-gloria","q-vulg-de-profundis","q-vulg-per-speculum","q-ag-dei","q-vulg-vanitas","q-dies-irae","q-kempis-transit","q-ben-otiositas","q-ben-ausculta","q-ben-hospites"}
for i,c in cs.items():
    c["register"]="medieval-legal" if i=="q-magna-carta-39" else "ecclesiastical" if i in EC else "medieval" if i in {"q-carmina-o-fortuna","q-abelard-dubitando","q-heloise-meretrix","q-aquinas-tardiloquum","q-mon-unum"} else "classical"
# Augustine, Boethius, Bede and Alcuin write essentially classical Latin.
# --- grammar target vs preview
PREV={"q-aug-inquietum":["donec_subjunctive"],"q-mon-unum":["accusative_infinitive"],"q-heloise-meretrix":["imperfect_subjunctive"],"q-aquinas-tardiloquum":["accusative_infinitive"],"q-abelard-dubitando":["gerund_ablative"],"q-alcuin-epitaph":["future_participle"],"q-vulg-gloria":["genitive_of_description"],"q-boethius-rota":["ablative_of_means"]}
for i,c in cs.items():
    p=set(c.get("grammar_preview",[]))|set(PREV.get(i,[]))
    c["grammar_tags"]=[t for t in c["grammar_tags"] if t not in p] or c["grammar_tags"]
    if p: c["grammar_preview"]=sorted(p)
    else: c.pop("grammar_preview",None)
# Boethius/Abelard/Vanitas: low-core → preview/reading only
for i in ["q-boethius-rota","q-abelard-dubitando","q-vulg-vanitas","q-bede-sparrow"]: cs[i]["card_role"]="preview_reading"
# --- Rome-format teaching_value, vocab_ids (v-spelling, no macrons)
for c in cs.values():
    tv=c["teaching_value"]; old=tv.get("score10",tv["score"]) if "score10" in tv else tv["score"]
    if "notes" in tv:
        c["teaching_value"]=dict(note=tv["notes"],dcc_core_pct=tv["dickinson_core_pct"],non_core=sorted({vnorm(x) for x in tv["non_core_lemmas"]}),score=max(1,min(5,round(old/2))))
    lem=c.pop("vocab_lemmas",None)
    if lem is not None:
        c["vocab_ids"]=sorted({vnorm(w).replace("u","v") if False else vnorm(w) for w in lem})
# u->v restoration for vocab ids: use gloss lemmas (macronized, v-spelled) instead
for c in cs.values():
    c["vocab_ids"]=sorted({vnorm(g["lemma"].split()[0]) for g in c["gloss"] if g["lemma"][0].islower()})
    c["teaching_value"]["non_core"]=sorted({x.replace("uanitas","vanitas").replace("uariabilis","variabilis").replace("peruolo","pervolo").replace("uolubilis","volubilis").replace("uerso","verso").replace("ueritas","veritas").replace("superuenio","supervenio").replace("fauilla","favilla") for x in c["teaching_value"]["non_core"]})
# --- images: Tolle lege, Bede sparrow reuse, crops, tif, CC BY-SA credit, later-depiction labels
q=lambda f:urllib.parse.quote(f.replace(" ","_"))
def setimg(i,f,alt,kind,aspect,lic,credit):
    cs[i]["image"]=dict(src="https://commons.wikimedia.org/wiki/Special:FilePath/"+q(f),alt=alt,kind=kind,aspect=aspect,transparent=False,license=lic,credit=credit,source_url="https://commons.wikimedia.org/wiki/File:"+q(f))
setimg("q-aug-tolle-lege","TolleLege.jpg","Benozzo Gozzoli, St Augustine reading the Epistle of St Paul (San Gimignano, 1464–65)","painting","3:5","Public domain","Benozzo Gozzoli · Wikimedia Commons")
setimg("q-bede-sparrow","1966 Ordnance Survey - Sutton Hoo helmet.jpg","Sutton Hoo helmet, Anglo-Saxon royal burial (early 7th c.); 1966 Ordnance Survey illustration","artifact","2:3","Public domain","Ordnance Survey (1966) · Wikimedia Commons")
CROP={"q-ben-hospites":[0.5,0.45],"q-magna-carta-39":[0.35,0.4],"q-ben-ausculta":[0.5,0.4],"q-alcuin-epitaph":[0.5,0.45],"q-ben-otiositas":[0.5,0.3]}
for i,fp in CROP.items():
    im=cs[i]["image"]; im["focal_point"]=fp; im["crop_note"]="Original "+im["aspect"]+"; crop to 3:4 around focal_point"; im["aspect"]="3:4"
im=cs["q-vulg-gloria"]["image"]
if "width=" not in im["src"]: im["src"]+="?width=1200"; im["format_note"]="Original is .tif; Special:FilePath?width=1200 serves a JPEG rendition"
im["credit"]="Cleveland Museum of Art (CC0) · Wikimedia Commons"
im=cs["q-abelard-dubitando"]["image"]
api="https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=extmetadata&titles=File:"+im["source_url"].split("File:")[1]
md=json.load(urllib.request.urlopen(urllib.request.Request(api,headers={"User-Agent":"latin-app/1.0"}),timeout=20))
m=list(md["query"]["pages"].values())[0]["imageinfo"][0]["extmetadata"]
import re
artist=re.sub("<[^>]+>","",m.get("Artist",{}).get("value","")).strip()
im["credit"]="Charles Durupt (painting, public domain); image: Galerie Michel Descours, uploaded by BeatrixBelibaste, CC BY-SA 4.0 via Wikimedia Commons"
im["share_alike_note"]="Any cropped/background-processed derivative must be released under CC BY-SA 4.0 with this credit."
for i in ["q-vulg-vanitas","q-vulg-per-speculum","q-aug-sero","q-aug-da-mihi","q-aug-inquietum","q-aug-tolle-lege","q-ag-dei","q-kempis-transit","q-mon-unum","q-aquinas-tardiloquum","q-ben-otiositas","q-heloise-meretrix","q-abelard-dubitando"]:
    a=cs[i]["image"]["alt"]
    if not a.startswith("Later depiction"): cs[i]["image"]["alt"]="Later depiction: "+a
    cs[i]["image"]["later_depiction"]=True
# --- learn_more for Bede sparrow stays; rank
out=sorted(cs.values(),key=lambda c:(-c["teaching_value"]["score"],-c["teaching_value"]["dcc_core_pct"]))
for r,c in enumerate(out,1): c["teaching_value"]["rank"]=r
json.dump(out,open(F,"w"),ensure_ascii=False,indent=1)
print(len(out))
