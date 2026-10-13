import json,urllib.request,urllib.parse,time,re
UA={"User-Agent":"LatinApp/0.1 (research; garrett)"}
get=lambda u: json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
Q={"v-urbs":"Plastico di Roma antica","g-1decl-nom":"Capitoline Wolf Musei Capitolini","i-spqr":"SPQR Arch of Titus inscription","v-pater":"Roman funerary relief couple Metropolitan","v-filius":"Roman funerary stele family portrait","g-acc":"Roman funerary relief father child","g-2decl":"Roman mosaic servants banquet","d-familia":"House of the Vettii atrium","l-bulla":"gold bulla Etruscan Walters","v-miles":"Roman legionary tombstone relief","v-castra":"Housesteads Roman fort","g-1conj":"Trajan's Column legionaries marching","g-2conj":"Caelius cenotaph Bonn centurion","i-vindolanda":"Vindolanda tablet 291 Claudia Severa","l-pila":"Roman pilum reconstruction","x-parse-signum":"Legio XX Valeria Victrix stone","v-res-publica":"Roman Forum from Capitoline","g-adj":"Patrician Torlonia bust","g-3decl":"Ara Pacis relief Tellus","g-possum":"aureus Augustus Metropolitan","i-coin-divi-f":"denarius Octavian CAESAR DIVI F","x-timeline-emp":"Bust of Trajan Glyptothek","g-imperative":"Horace manuscript Odes","g-future":"Quintus Horatius Flaccus medal","g-pronoun":"Ovid statue Constanta","v-tempus":"Roman sundial","x-meter":"Vergilius Romanus","g-ind-stat":"Romulus Remus Capitoline Wolf","d-video":"Pompeii fresco woman stylus Sappho","i-chirho":"Constantine coin Chi-Rho labarum","l-annona":"Pompeii carbonized bread","d-crux":"Early Christian cross Byzantine Metropolitan","g-relative":"Pater noster manuscript Carolingian","x-colophon":"medieval manuscript colophon scribe","x-map-medieval":"Carolingian empire map Shepherd","x-map-roma":"Seven hills of Rome map Shepherd","v-via":"Via Appia Antica tombs"}
OK=re.compile(r"^(public domain|pd|cc0|cc by(-sa)? (2\.0|2\.5|3\.0|4\.0))",re.I)
res={}
for k,q in Q.items():
    try:
        r=get("https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrlimit=8&gsrsearch="+urllib.parse.quote(q+" filetype:bitmap")+"&prop=imageinfo&iiprop=url|extmetadata|size&iiurlwidth=900")
        pages=sorted(r.get("query",{}).get("pages",{}).values(),key=lambda p:p["index"])
        for p in pages:
            ii=p["imageinfo"][0];md=ii["extmetadata"];g=lambda x:re.sub("<[^>]+>","",md.get(x,{}).get("value","")).strip()
            if OK.match(g("LicenseShortName")) and ii["width"]>=500:
                res[k]=dict(file=p["title"][5:],thumb=ii["thumburl"],page=ii["descriptionurl"],w=ii["width"],h=ii["height"],lic=g("LicenseShortName"),artist=g("Artist")[:120],desc=g("ImageDescription")[:150]);break
        else: res[k]={"err":"no ok result"}
    except Exception as e: res[k]={"err":str(e)}
    print(k,res[k].get("file") or res[k]["err"],res[k].get("lic"));time.sleep(0.3)
json.dump(res,open("lc_images_search.json","w"),indent=1,ensure_ascii=False)
