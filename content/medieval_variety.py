"""Adds variety cards + graded readings to medieval-cards.json (idempotent: replaces by id)."""
import json,urllib.parse,urllib.request
F="medieval-cards.json"; cs={c["id"]:c for c in json.load(open(F))}
G={};cur=None
for line in open("medieval_glosses.txt"):
    line=line.rstrip("\n")
    if not line or line.startswith("#"): continue
    if line.startswith("@"): cur=line[1:];G[cur]=[];continue
    w,l,m,p=line.split("|");G[cur].append(dict(word=w,lemma=l,meaning=m,parse=p))
q=lambda f:urllib.parse.quote(f.replace(" ","_"))
def img(f,alt,kind,aspect,lic,credit,**kw):
    d=dict(src="https://commons.wikimedia.org/wiki/Special:FilePath/"+q(f),alt=alt,kind=kind,aspect=aspect,transparent=False,license=lic,credit=credit,source_url="https://commons.wikimedia.org/wiki/File:"+q(f));d.update(kw);return d
W=lambda t:dict(label=t.split(" (")[0]+" — Wikipedia",url="https://en.wikipedia.org/wiki/"+q(t))
UR=dict(min_vocab_known=0.7,review_threshold=0.9)
new=[
dict(id="q-archpoet-taberna",type="quote",era="high_medieval",unit=11,register="medieval",
 latin="Meum est prōpositum in tabernā morī, ut sint vīna proxima morientis ōrī.",
 translation="It is my plan to die in the tavern, so that wine may be close to my mouth as I die.",
 context="The 'Archpoet', an anonymous wandering scholar at Frederick Barbarossa's court, mock-confesses his vices (c. 1163). The stanza became a student drinking song.",
 person="The Archpoet (Archipoeta)",source=dict(work="Confessio (Estuans intrinsecus), st. 12",citation="Archipoeta 10.12",date="c. 1163"),
 source_url="https://www.thelatinlibrary.com/archpoet.html",attribution_confidence="verified",text_check="verified vs Latin Library",
 grammar_tags=["ut_purpose_subjunctive","deponent_infinitive","dative_with_proximus"],grammar_preview=["present_participle_substantive"],
 teaching_value=dict(note="Clean ut + present subjunctive purpose clause; deponent infinitive morī; proximus + dative. Rhymed, memorable, funny.",score=4),
 image=img("Codex Buranus, landscape with plants and animals (folio 64v).jpg","Codex Buranus, fol. 64v (13th c.), the songbook where many goliard poems survive","manuscript","2:3","Public domain","Bayerische Staatsbibliothek · Wikimedia Commons"),
 learn_more=W("Archpoet"),attribution_note="Also preserved in the Carmina Burana (CB 191)."),
dict(id="q-gesta-latro",type="quote",era="late_medieval",unit=12,register="medieval",
 latin="Sed quia ego hoc agō ūnā galeā, latrō vocor; tū vērō, mundum opprimēns nāvium multitūdine magnā, dīceris imperātor.",
 translation="But because I do this with one ship, I am called a pirate; you, crushing the world with a great fleet, are called emperor.",
 context="A captured pirate answers Alexander the Great. The Gesta Romanorum, a 14th-century preachers' story collection, retells it from Augustine's City of God (4.4).",
 person="Gesta Romanorum (anon.)",source=dict(work="Gesta Romanorum",citation="146",date="c. 1300–1350"),
 source_url="https://www.thelatinlibrary.com/gestarom.shtml",attribution_confidence="verified",text_check="verified vs Latin Library (ch. 146)",
 grammar_tags=["present_passive","quia_causal","ablative_of_means"],grammar_preview=["present_participle"],
 teaching_value=dict(note="Perfect pair of present passives vocor / dīceris with predicate nominatives; ablative of means; a reusable 'X is called Y' frame. A story learners can retell.",score=5),
 image=img("Gesta Romanorum - Donaueschingen 9r.jpg","Gesta Romanorum manuscript, Donaueschingen copy, fol. 9r","manuscript","2:3","Public domain","Wikimedia Commons"),
 learn_more=W("Gesta Romanorum"),attribution_note="The anecdote originates in Cicero (De re publica 3) via Augustine, De civitate Dei 4.4."),
dict(id="q-paris-statute-1215",type="quote",era="high_medieval",unit=12,register="medieval-legal",
 latin="Nōn legantur librī Aristotelis dē metaphysicā et dē nātūrālī philosophiā.",
 translation="Let the books of Aristotle on metaphysics and on natural philosophy not be lectured on.",
 context="In 1215 the papal legate Robert de Courçon laid down the arts curriculum at Paris: Aristotle's logic yes, his physics and metaphysics no. Within forty years they were required reading.",
 person="Robert de Courçon (papal legate)",source=dict(work="Statutes for the University of Paris",citation="Chartularium Universitatis Parisiensis I, no. 20, p. 78",date="1215"),
 source_url="https://papiro.unizar.es/ojs/index.php/analisis/article/download/2075/2626/7772",attribution_confidence="verified",
 text_check="Matches two independent quotations of the Denifle–Chatelain edition (Brepols chapter; Análisis, Univ. Zaragoza). MS spelling methafisica normalised.",
 grammar_tags=["jussive_subjunctive_passive","de_ablative"],
 teaching_value=dict(note="Negative jussive passive subjunctive (nōn legantur), the voice of every medieval rule-book; legere = 'to lecture on'; dē + abl.",score=4),
 image=img("Henry of Germany delivering a lecture to university students in Bologna by Laurentius de Voltolina (21114437820).jpg","Laurentius de Voltolina, a lecture at the University of Bologna (14th c.)","manuscript","4:3 (crop to 3:4, focal on lecturer)","Public domain","Kupferstichkabinett Berlin · Wikimedia Commons",focal_point=[0.3,0.4]),
 learn_more=W("Condemnations of 1210–1277"),attribution_note="Image shows Bologna, not Paris."),
dict(id="q-colophon-tres-digiti",type="quote",era="early_medieval",unit=10,register="medieval",
 latin="Trēs digitī scrībunt, sed tōtum corpus labōrat. Sīcut nāvigantī dulcis est portus, ita scrīptōrī novissimus versus.",
 translation="Three fingers write, but the whole body toils. As the harbour is sweet to the sailor, so is the last line to the scribe.",
 context="A 9th-century scribe, Guarembertus, signed off a manuscript with this complaint (Paris, BnF lat. 12234). Scribes all over Europe copied these lines into their colophons.",
 person="Guarembertus (scribe)",source=dict(work="Colophon, Paris BnF lat. 12234",citation="IRHT Bibale no. 18684",date="9th c."),
 source_url="https://bibale.irht.cnrs.fr/18684",attribution_confidence="verified",text_check="verified vs IRHT Bibale transcription; formula also attested in BL Royal 6 A.vi, Harley 3013 (Porck 2017)",
 grammar_tags=["third_conjugation_present","sicut_ita","dative_of_reference"],grammar_preview=["present_participle_substantive"],
 teaching_value=dict(note="Present 3pl/3sg, sīcut … ita comparison, dative 'to the sailor/scribe', superlative novissimus. All about writing: perfect for the Monks & Manuscripts unit.",score=5),
 image=img("Unknown-artist-eadwine-the-scribe-at-work-eadwine-psalter-christ-church-canterbury-england-uk-circa-1160-70.jpg","Eadwine the scribe at work, Eadwine Psalter (Canterbury, c. 1160–70)","manuscript","5:7","Public domain","Trinity College Cambridge · Wikimedia Commons"),
 learn_more=W("Colophon (publishing)"),attribution_note="Image is a different scribe (Eadwine, 12th c.)."),
dict(id="q-hildegard-aurora",type="quote",era="high_medieval",unit=11,register="ecclesiastical",
 latin="Tū rubēs ut aurōra, et ārdēs ut sōlis flamma.",
 translation="You glow red like the dawn, and you burn like the flame of the sun.",
 context="From Hildegard of Bingen's chant 'O nobilissima viriditas' for virgins. Hildegard was a 12th-century abbess, visionary, composer and scientist, and is now a Doctor of the Church.",
 person="Hildegard of Bingen",source=dict(work="O nobilissima viriditas (Symphonia), verse",citation="Dendermonde MS 165r–v; Riesencodex 471rb–va",date="c. 1150s"),
 source_url="http://www.hildegard-society.org/2017/04/o-nobilissima-viriditas-responsory.html",attribution_confidence="verified",text_check="verified vs Int. Society of Hildegard Studies (collated from Newman's edition)",
 grammar_tags=["second_conjugation_2sg","ut_comparison"],
 teaching_value=dict(note="Two 2nd-conj. 2nd-sg presents (rubēs, ārdēs); ut = 'like' with no verb (contrast ut + subjunctive); genitive sōlis.",score=5),
 image=img("Hildegard von Bingen.jpg","Hildegard receiving a vision, Rupertsberg Scivias (12th c., facsimile)","manuscript","2:3","Public domain","Wikimedia Commons"),
 learn_more=W("Hildegard of Bingen")),
dict(id="r-vulg-john-1-5",type="quote",era="late_antiquity",unit=9,register="ecclesiastical",card_role="graded_reading",
 latin="In prīncipiō erat Verbum, et Verbum erat apud Deum, et Deus erat Verbum. Hoc erat in prīncipiō apud Deum. Omnia per ipsum facta sunt, et sine ipsō factum est nihil quod factum est. In ipsō vīta erat, et vīta erat lūx hominum. Et lūx in tenebrīs lūcet, et tenebrae eam nōn conprehendērunt.",
 translation="In the beginning was the Word, and the Word was with God, and the Word was God. He was in the beginning with God. All things were made through him, and without him nothing was made that was made. In him was life, and the life was the light of men. And the light shines in the darkness, and the darkness did not overcome it.",
 context="The opening of John's Gospel in Jerome's Vulgate: five short verses that recycle a handful of words. Ideal first continuous reading.",
 person="Jerome (Vulgate)",source=dict(work="Vulgate, John",citation="1:1–5",date="c. 390–405"),
 source_url="https://www.thelatinlibrary.com/bible/john.shtml",attribution_confidence="verified",text_check="verified vs Latin Library",
 grammar_tags=["imperfect_esse","perfect_passive","prepositions_abl_acc","genitive"],
 teaching_value=dict(note="Graded reading: ~50 tokens, ~20 lemmas; erat ×6, facta sunt / factum est, per/apud + acc., in/sine + abl. Builds on the John 1:1 card.",score=5),
 image=img("The St Cuthbert Gospel of St John. (formerly known as the Stonyhurst Gospel) is the oldest intact European book. - Upper cover (Add Ms 89000).jpg","St Cuthbert Gospel of John, original leather binding (early 8th c.), British Library","artifact","9:10 (crop 3:4)","CC0","British Library · Wikimedia Commons",focal_point=[0.5,0.5]),
 learn_more=W("John 1:1"),unlock_rule=UR),
dict(id="r-vulg-genesis-1-5",type="quote",era="late_antiquity",unit=9,register="ecclesiastical",card_role="graded_reading",
 latin="In prīncipiō creāvit Deus caelum et terram. Terra autem erat inānis et vacua, et tenebrae erant super faciem abyssī, et spīritus Deī ferēbātur super aquās. Dīxitque Deus: “Fīat lūx.” Et facta est lūx. Et vīdit Deus lūcem quod esset bona, et dīvīsit lūcem ā tenebrīs. Appellāvitque lūcem Diem, et tenebrās Noctem; factumque est vespere et māne, diēs ūnus.",
 translation="In the beginning God created heaven and earth. The earth was empty and void, and darkness was over the face of the deep, and the spirit of God moved over the waters. And God said, “Let there be light.” And light came to be. And God saw the light, that it was good, and he divided the light from the darkness. And he called the light Day, and the darkness Night; and there was evening and morning, one day.",
 context="The first verses of the Bible in Jerome's Latin, read aloud in every medieval monastery. Short clauses, repeated nouns and a clear story make it a model beginner text.",
 person="Jerome (Vulgate)",source=dict(work="Vulgate, Genesis",citation="1:1–5",date="c. 390–405"),
 source_url="https://www.thelatinlibrary.com/bible/genesis.shtml",attribution_confidence="verified",text_check="verified vs Latin Library (punctuation lightly modernised)",
 grammar_tags=["perfect_active","imperfect","jussive_subjunctive","perfect_passive","ablative_of_separation"],grammar_preview=["quod_clause_eccl","imperfect_passive"],
 teaching_value=dict(note="Graded reading: perfects creāvit/vīdit/dīvīsit/appellāvit vs imperfects erat/erant; double accusative with appellō; ecclesiastical quod-clause instead of acc. + inf. (flag).",score=5),
 image=img("BibleMoralisee.jpg","God as architect of creation, Bible moralisée (c. 1220–30)","manuscript","3:4","Public domain","Österreichische Nationalbibliothek · Wikimedia Commons"),
 learn_more=W("Genesis creation narrative"),unlock_rule=UR),
]
for c in new:
    c["gloss"]=G[c["id"]]; c.setdefault("unlock_rule",UR)
    c["teaching_value"].update(dcc_core_pct=0,non_core=[],rank=0)
    c["vocab_ids"]=sorted({__import__("medieval_dcc").strip(g["lemma"].split()[0]).lower() for g in c["gloss"] if g["lemma"][0].islower()}) if False else None
    cs[c["id"]]=c
import unicodedata
def strip(s): return "".join(ch for ch in unicodedata.normalize("NFD",s) if unicodedata.category(ch)!="Mn")
for c in new: c["vocab_ids"]=sorted({strip(g["lemma"].split()[0]).lower() for g in c["gloss"] if g["lemma"][0].islower()})
json.dump(list(cs.values()),open(F,"w"),ensure_ascii=False,indent=1); print(len(cs))
