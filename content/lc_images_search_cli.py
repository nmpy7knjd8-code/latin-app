import json,urllib.request,urllib.parse,time,re
UA={"User-Agent":"LatinApp/0.1 (research; garrett)"}
get=lambda u: json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
import sys
Q=json.load(open(sys.argv[1]));OUT=sys.argv[2]
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
json.dump(res,open(OUT,"w"),indent=1,ensure_ascii=False)
