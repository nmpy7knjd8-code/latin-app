import json,csv,unicodedata,re
def n(s):
    s=unicodedata.normalize("NFD",s); s="".join(c for c in s if unicodedata.category(c)!="Mn")
    return s.lower().replace("j","i").replace("v","u")
core={}
for r in csv.DictReader(open("../data/dcc-latin-core.csv")):
    for part in r["Headword"].split(";"):
        w=part.split()[0].strip(",") if part.split() else ""
        if w: core.setdefault(n(w),int(r["Frequency Rank"]))
core["cito"]=core.get("citus")  # DCC lists citō under citus
# extra headword alternates (first form only above); add 2nd tokens for multi-form preps like ā ab abs
for r in csv.DictReader(open("../data/dcc-latin-core.csv")):
    toks=r["Headword"].split()
    if r["Part of Speech"] in ("Preposition","Conjunction","Adverb","Pronoun"):
        for t in toks: core.setdefault(n(t),int(r["Frequency Rank"]))
LL="https://www.thelatinlibrary.com/"
cards=json.load(open("medieval-cards.v1.json"))
by={c["id"]:c for c in cards}
for k in ["q-ora-labora","q-memento-mori","q-gaudeamus"]: by.pop(k)
def upd(i,**kw): by[i].update(kw)
upd("q-vulg-vanitas",latin="Vānitās vānitātum, dīxit Ecclesiastēs, vānitās vānitātum; omnia vānitās.",translation="Vanity of vanities, said the Preacher, vanity of vanities; all is vanity.",text_check="verified vs Latin Library Eccl. 1:2 (punctuation added)")
by["q-vulg-vanitas"]["teaching_value"]["notes"]="3rd-decl. nominative vs genitive plural of one noun; omnia neuter plural; dīxit perfect."
upd("q-ben-ausculta",latin="Obscultā, ō fīlī, praecepta magistrī, et inclīnā aurem cordis tuī.",text_check="verified vs Latin Library (Obsculta = ausculta)")
upd("q-ben-hospites",text_check="verified vs Latin Library RB 53.1")
upd("q-abelard-dubitando",source_url="https://la.wikisource.org/wiki/Sic_et_non",text_check="verified vs la.wikisource Sic et non prologue")
upd("q-mon-unum",latin="…hūmānum genus optimē sē habēre cum ab ūnō regitur.",translation="…the human race is in the best condition when it is ruled by one.",text_check="verified vs Latin Library Mon. 1.14.11 (indirect statement after 'sequitur')")
by["q-mon-unum"]["source"]["citation"]="1.14.11 (Latin Library numbering)"
by["q-mon-unum"]["grammar_tags"]+=["accusative_infinitive"]
upd("q-vulg-pater-noster",text_check="verified vs Latin Library Matt. 6:9")
upd("q-vulg-gloria",latin="Glōria in altissimīs Deō, et in terrā pāx in hominibus bonae voluntātis.",translation="Glory to God in the highest, and on earth peace among men of good will.",text_check="verified vs Latin Library Luke 2:14")
upd("q-vulg-per-speculum",source_url="https://www.drbo.org/lvb/chapter/53013.htm",latin="Vidēmus nunc per speculum in aenigmate, tunc autem faciē ad faciem.",translation="We see now through a mirror, in a riddle, but then face to face.",text_check="verified vs drbo.org Clementine Vulgate 1 Cor 13:12 (Latin Library page didn't load)")
upd("q-vulg-de-profundis",text_check="verified vs Latin Library Ps. 129:1")
upd("q-ag-dei",source_url="https://la.wikisource.org/wiki/Agnus_Dei",text_check="verified vs la.wikisource")
upd("q-dies-irae",text_check="verified vs Latin Library")
upd("q-carmina-o-fortuna",source_url="https://www.hs-augsburg.de/homes/harsch/Chronologia/Lspost13/CarminaBurana/bur_cmo1.html",text_check="verified vs Bibliotheca Augustana CB 17 and la.wikisource")
upd("q-boethius-rota",source_url="https://www2.hs-augsburg.de/~harsch/Chronologia/Lspost06/Boethius/boe_con2.html",text_check="verified vs Bibliotheca Augustana 2 pr. 2.9 and Bibliotheca Polyglotta")
by["q-boethius-rota"]["source"]["citation"]="2 pr. 2.9"
s=by.pop("q-sic-transit")
s.update(id="q-kempis-transit",latin="Ō quam citō trānsit glōria mundī.",translation="O how quickly the glory of the world passes away.",person="Thomas à Kempis",attribution_confidence="verified",source=dict(work="De imitatione Christi",citation="1.3.6",date="c. 1418–27"),source_url=LL+"kempis/kempis1.shtml",text_check="verified vs Latin Library",context="From The Imitation of Christ, the most-read devotional book of the late Middle Ages. The later papal formula 'Sic transit gloria mundi' echoes it.")
s["teaching_value"]["notes"]="quam + adverb exclamation; citō; trānseō; genitive mundī."
by[s["id"]]=s
base=dict(type="quote",unlock_rule=dict(min_vocab_known=0.7,review_threshold=0.9))
by["q-bede-discere"]=dict(base,id="q-bede-discere",era="early_medieval",unit=10,latin="Semper aut discere aut docēre aut scrībere dulce habuī.",translation="I always found it sweet either to learn or to teach or to write.",person="Bede",source=dict(work="Historia ecclesiastica",citation="5.24",date="731"),attribution_confidence="verified",grammar_tags=["infinitive_as_noun","aut_aut","perfect_active_1sg","predicate_adjective_neuter"],teaching_value=dict(score=9,notes="Three infinitives as neuter subjects/objects with dulce; aut … aut …; habuī perfect. The 3 core verbs of a scholar's life."),context="Bede describing his own life at the monastery of Jarrow, where he lived from age seven and wrote the first history of the English.",source_url=LL+"bede/bede5.shtml",text_check="verified vs Latin Library")
by["q-alcuin-epitaph"]=dict(base,id="q-alcuin-epitaph",era="early_medieval",unit=10,latin="Quod nunc es fueram, … et quod nunc ego sum, tūque futūrus eris.",translation="What you are now, I was … and what I am now, you too will be.",person="Alcuin of York",source=dict(work="Epitaphium (Carm. 123)",citation="lines 5–6",date="804"),attribution_confidence="verified",grammar_tags=["sum_tenses","pluperfect","future","future_participle","relative_quod"],teaching_value=dict(score=9,notes="Every tense of sum in one couplet: es / sum / fueram / futūrus eris. Relative quod as 'what'. Classic tomb formula."),context="Alcuin, Charlemagne's chief scholar, wrote his own epitaph speaking to passers-by: a common Roman tomb idea reused for a medieval abbot at Tours.",source_url=LL+"alcuin/epitaphium.shtml",text_check="verified vs Latin Library (omits 'famosus in orbe, viator')")
L={ # hand-lemmatized content words (proper nouns excluded)
"q-vulg-fiat-lux":"dico deus fio lux et fio sum lux",
"q-vulg-in-principio":"in principium sum uerbum et uerbum sum apud deus et deus sum uerbum",
"q-aug-inquietum":"facio nos ad tu et inquietus sum cor noster donec requiesco in tu",
"q-aug-tolle-lege":"tollo lego tollo lego",
"q-aug-sero":"sero tu amo pulchritudo tam antiquus et tam nouus sero tu amo",
"q-aug-da-mihi":"do ego castitas et continentia sed nolo modo",
"q-vulg-vanitas":"uanitas uanitas dico uanitas uanitas omnis uanitas",
"q-ben-otiositas":"otiositas inimicus sum anima",
"q-ben-ausculta":"ausculto o filius praeceptum magister et inclino auris cor tuus",
"q-ben-hospites":"omnis superuenio hospes tamquam suscipio",
"q-bede-angli":"bene inquam nam et angelicus habeo facies",
"q-bede-sparrow":"aduenio unus passer domus cito peruolo",
"q-heloise-meretrix":"carus ego et dignus uideo tuus dico meretrix quam ille imperatrix",
"q-abelard-dubitando":"dubito quippe ad inquisitio uenio inquiro ueritas percipio",
"q-dies-irae":"dies ira dies ille soluo saeculum in fauilla",
"q-magna-carta-39":"nullus liber homo capio uel imprisono nisi per legalis iudicium par suus uel per lex terra",
"q-aquinas-tardiloquum":"tardiloquus tu sum iubeo",
"q-mon-unum":"humanus genus bene sui habeo cum ab unus rego",
"q-einhard-aachen":"basilica sanctus deus genitrix opus mirabilis construo",
"q-vulg-pater-noster":"pater noster qui sum in caelum sanctifico nomen tuus",
"q-vulg-gloria":"gloria in altus deus et in terra pax in homo bonus uoluntas",
"q-vulg-per-speculum":"uideo nunc per speculum in aenigma tunc autem facies ad facies",
"q-vulg-de-profundis":"de profundus clamo ad tu dominus",
"q-ag-dei":"agnus deus qui tollo peccatum mundus misereor nos",
"q-kempis-transit":"o quam cito transeo gloria mundus",
"q-carmina-o-fortuna":"o fortuna uelut luna status uariabilis semper cresco aut decresco",
"q-boethius-rota":"rota uolubilis orbis uerso",
"q-bede-discere":"semper aut disco aut doceo aut scribo dulcis habeo",
"q-alcuin-epitaph":"qui nunc sum sum et qui nunc ego sum tu que sum sum",
}
alias={"ego":"ego","tu":"tu","nos":"nos","sui":"sui","que":"que","o":"o","qui":"qui","cito":"cito","bene":"bene","sero":"sero"}
miss_all={}
for i,c in by.items():
    ws=L[i].split(); hit=[w for w in ws if n(w) in core]; miss=[w for w in ws if n(w) not in core]
    pct=round(100*len(hit)/len(ws)); miss_all[i]=sorted(set(miss))
    tv=c["teaching_value"]; tv.pop("dickinson_core_est",None)
    tv["dickinson_core_pct"]=pct; tv["non_core_lemmas"]=sorted(set(miss))
    c["vocab_lemmas"]=ws
IMG={
"q-vulg-in-principio":("KellsFol292rIncipJohn.jpg","Book of Kells, fol. 292r: 'In principio erat verbum'","manuscript","3:4","Public domain"),
"q-aug-inquietum":("Sandro_Botticelli_-_St_Augustine_-_WGA02709.jpg","Botticelli, St Augustine in his Study (c. 1480)","painting","2:3","Public domain"),
"q-ben-otiositas":("Angelico_-_Perugia_Altarpiece_–_Saint_Benedict_and_Peter_the_Martyr.jpg","Fra Angelico, St Benedict (Perugia Altarpiece)","painting","1:2","Public domain"),
"q-einhard-aachen":("Aachen_Palatine_Chapel_24092016_01.jpg","Interior of Charlemagne's Palatine Chapel, Aachen","building","2:3","CC0"),
"q-magna-carta-39":("Magna_Carta_(1215)_-_BL_Cotton_MS_Augustus_II_106.jpg","Magna Carta 1215, British Library Cotton MS Augustus II.106","manuscript","3:2","CC0"),
"q-bede-angli":("Beda_Petersburgiensis_f3v.jpg","St Petersburg Bede (8th c.), fol. 3v","manuscript","2:3","Public domain"),
"q-heloise-meretrix":("Haigh_-_Tomb_of_Abelard_and_Heloise_01.jpg","19th-c. print of the tomb of Abelard and Héloïse","painting","2:3","Public domain"),
"q-aquinas-tardiloquum":("Saint_Thomas_Aquinas_(Crivelli,_15th-century).jpg","Carlo Crivelli, St Thomas Aquinas","painting","2:3","Public domain"),
"q-boethius-rota":("Consolation_of_philosophy_1385_boethius_images.jpg","Boethius and Philosophy, Consolation manuscript of 1385","manuscript","3:4","Public domain"),
"q-alcuin-epitaph":("Raban-Maur_Alcuin_Otgar.jpg","Hrabanus Maurus presented by Alcuin, Fulda manuscript (c. 830)","manuscript","1:1 (crop to 3:4)","Public domain"),
"q-vulg-pater-noster":("LindisfarneFol27rIncipitMatt.jpg","Lindisfarne Gospels, incipit of Matthew","manuscript","2:3","Public domain"),
"q-vulg-de-profundis":("Utrecht_Psalter.jpg","Utrecht Psalter (Carolingian, c. 830)","manuscript","3:4","Public domain"),
"q-dies-irae":("Souls_Rising_from_the_Dead,_Cathedral_of_St._Lazare,_Autun,_France_--_Relief_sculpture_-_Vanderbilt_ACT_-_Autun16.jpg","Souls rising at the Last Judgement, Autun Cathedral tympanum","artifact","4:3","Public domain"),
}
for i,(f,alt,k,a,lic) in IMG.items():
    u="https://commons.wikimedia.org/wiki/File:"+f
    by[i]["image"]=dict(src="https://commons.wikimedia.org/wiki/Special:FilePath/"+f,alt=alt,kind=k,aspect=a,transparent=False,license=lic,credit="Wikimedia Commons ("+lic+")",source_url=u)
    by[i].pop("image_candidate",None)
for c in by.values():
    if "image_candidate" in c: c["image_candidate"]["license_status"]="no verified open-licence image found yet"
out=sorted(by.values(),key=lambda c:(-c["teaching_value"]["score"],-c["teaching_value"]["dickinson_core_pct"]))
for c in out: assert len(c["context"])<=260,c["id"]
json.dump(out,open("medieval-cards.json","w"),ensure_ascii=False,indent=1)
for c in out: print(c["teaching_value"]["score"],c["teaching_value"]["dickinson_core_pct"],c["id"],c["teaching_value"]["non_core_lemmas"],"IMG" if "image" in c else "")
print(len(out))
