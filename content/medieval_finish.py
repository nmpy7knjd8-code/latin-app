import json,urllib.request,urllib.parse,jsonschema
F="medieval-cards.json";cs={c["id"]:c for c in json.load(open(F))}
IMG={
"q-vulg-fiat-lux":("AdamEveMoutierGrandvalBibleBritLibAddMS10546Fol5b.jpg","Genesis frontispiece, Moutier-Grandval Bible (Tours, c. 830–40)","manuscript","3:4","Public domain"),
"q-aug-tolle-lege":("Benozzo Gozzoli - St Augustine Departing for Milan (detail) - WGA10296.jpg","Benozzo Gozzoli, Augustine departing for Milan (San Gimignano fresco cycle)","painting","4:5","Public domain"),
"q-bede-discere":("CodxAmiatinusFolio5rEzra.jpg","Scribe at work, Codex Amiatinus (Bede's monastery, c. 700)","manuscript","3:4","Public domain"),
"q-ben-ausculta":("St. Benedict delivering his rule to the monks of his order.jpg","St Benedict delivering his Rule to his monks","manuscript","1:1 (crop 3:4)","Public domain"),
"q-vulg-gloria":("France, Troyes?, 15th century - Leaf from a Book of Hours- Annunciation to the Shepherds - 2011.61 - Cleveland Museum of Art.tif","Annunciation to the Shepherds, Book of Hours leaf (Cleveland Museum of Art)","manuscript","2:3","CC0"),
"q-aug-sero":("Saint Augustine by Philippe de Champaigne.jpg","Philippe de Champaigne, St Augustine","painting","3:4","Public domain"),
"q-aug-da-mihi":("Benozzo Gozzoli - St Augustine Teaching in Rome (detail) - WGA10291.jpg","Benozzo Gozzoli, St Augustine teaching in Rome","painting","2:3","Public domain"),
"q-abelard-dubitando":("DURUPT Héloïse et Abélard (la leçon d'astronomie).jpg","Charles Durupt, Héloïse and Abelard (19th c.)","painting","4:5","CC BY-SA 4.0"),
"q-vulg-per-speculum":("Saint Paul at his Writing-Desk, by Rembrandt.jpg","Rembrandt, St Paul at his writing desk","painting","5:6","Public domain"),
"q-ben-hospites":("Monte Cassino Abbey 2019 03.jpg","Abbey of Monte Cassino, Benedict's monastery","building","16:9 (crop)","CC0"),
"q-ag-dei":("Ghent Altarpiece D - Adoration of the Lamb 2.jpg","Van Eyck, Ghent Altarpiece: Adoration of the Lamb (detail)","painting","3:4","Public domain"),
"q-carmina-o-fortuna":("Wheel-of-fortune-carmina-burana.jpg","Wheel of Fortune, Codex Buranus (13th c.)","manuscript","2:3","Public domain"),
"q-vulg-vanitas":("After Pieter Claeszoon - Vanitas-Still-Life - c. 1634.jpg","After Pieter Claesz, Vanitas still life (c. 1634)","painting","4:3","Public domain"),
"q-kempis-transit":("Portret van Thomas à Kempis, RP-P-1912-784.jpg","Portrait print of Thomas à Kempis (Rijksmuseum)","painting","2:3","CC0"),
"q-mon-unum":("Dante Alighieri's portrait by Sandro Botticelli.jpg","Botticelli, portrait of Dante","painting","2:3","Public domain"),
"q-bede-sparrow":("Benozzo Gozzoli - St Augustine Departing for Milan (detail) - WGA10297.jpg",None,None,None,None),
}
IMG["q-bede-sparrow"]=("Beda Petersburgiensis f3v.jpg","St Petersburg Bede (8th c.), fol. 3v","manuscript","2:3","Public domain")
q=lambda f:urllib.parse.quote(f.replace(" ","_"))
for i,(f,alt,k,a,lic) in IMG.items():
    cs[i]["image"]=dict(src="https://commons.wikimedia.org/wiki/Special:FilePath/"+q(f),alt=alt,kind=k,aspect=a,transparent=False,license=lic,credit="Wikimedia Commons ("+lic+")",source_url="https://commons.wikimedia.org/wiki/File:"+q(f))
for c in cs.values(): c.pop("image_candidate",None)
W="https://en.wikipedia.org/wiki/"
LM={"q-vulg-fiat-lux":"Let there be light","q-vulg-in-principio":"John 1:1","q-aug-tolle-lege":"Tolle lege","q-bede-discere":"Bede","q-alcuin-epitaph":"Alcuin","q-vulg-pater-noster":"Lord's Prayer","q-aug-inquietum":"Confessions (Augustine)","q-ben-otiositas":"Rule of Saint Benedict","q-ben-ausculta":"Rule of Saint Benedict","q-vulg-gloria":"Gloria in excelsis Deo","q-aug-sero":"Confessions (Augustine)","q-aug-da-mihi":"Augustine of Hippo","q-vulg-de-profundis":"Psalm 130","q-abelard-dubitando":"Sic et Non","q-dies-irae":"Dies irae","q-magna-carta-39":"Magna Carta","q-bede-angli":"Gregory the Great","q-vulg-per-speculum":"Through a glass, darkly","q-ben-hospites":"Monte Cassino","q-aquinas-tardiloquum":"Thomas Aquinas","q-ag-dei":"Agnus Dei","q-carmina-o-fortuna":"O Fortuna","q-vulg-vanitas":"Vanity of vanities","q-kempis-transit":"The Imitation of Christ","q-heloise-meretrix":"Heloise","q-einhard-aachen":"Palatine Chapel, Aachen","q-boethius-rota":"The Consolation of Philosophy","q-mon-unum":"De Monarchia","q-bede-sparrow":"Ecclesiastical History of the English People"}
for i,t in LM.items(): cs[i]["learn_more"]=dict(label=t.split(" (")[0]+" — Wikipedia",url=W+q(t))
bad=[]
def ok(u):
    try: return urllib.request.urlopen(urllib.request.Request(u,method="HEAD",headers={"User-Agent":"latin-app/1.0"}),timeout=20).status==200
    except Exception as e: return False
for c in cs.values():
    for u in (c["learn_more"]["url"],c["image"]["src"]):
        if not ok(u): bad.append((c["id"],u))
s=json.load(open("../card-schema.json"))
out=sorted(cs.values(),key=lambda c:(-c["teaching_value"]["score"],-c["teaching_value"]["dickinson_core_pct"]))
for c in out: jsonschema.validate(c,s)
json.dump(out,open(F,"w"),ensure_ascii=False,indent=1)
print(len(out),"valid; bad urls:",bad)
