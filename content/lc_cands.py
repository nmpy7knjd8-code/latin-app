import json,urllib.request,urllib.parse,re,sys,io
from PIL import Image,ImageDraw
UA={"User-Agent":"LatinApp/0.1 (research; garrett)"}
get=lambda u: urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40).read()
OK=re.compile(r"^(public domain|pd|cc0|cc by(-sa)? (2\.0|2\.5|3\.0|4\.0))",re.I)
Q=json.load(open(sys.argv[1]));out={};tiles=[]
for k,q in Q.items():
    r=json.loads(get("https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrlimit=12&gsrsearch="+urllib.parse.quote(q+" filetype:bitmap")+"&prop=imageinfo&iiprop=url|extmetadata|size&iiurlwidth=900"))
    n=0
    for p in sorted(r.get("query",{}).get("pages",{}).values(),key=lambda p:p["index"]):
        ii=p["imageinfo"][0];md=ii["extmetadata"];g=lambda x:re.sub("<[^>]+>","",md.get(x,{}).get("value","")).strip()
        cr=g("Credit")+g("Artist")
        if not OK.match(g("LicenseShortName")) or ii["width"]<500 or "British Museum" in cr: continue
        key=f"{k}#{n}";out[key]=dict(file=p["title"][5:],thumb=ii["thumburl"],page=ii["descriptionurl"],w=ii["width"],h=ii["height"],lic=g("LicenseShortName"),artist=g("Artist")[:120],desc=g("ImageDescription")[:150])
        try: im=Image.open(io.BytesIO(get(ii["thumburl"].replace("960px","330px")))).convert("RGB");im.thumbnail((240,240));tiles.append((key,im))
        except Exception as e: print(key,e)
        n+=1
        if n==4: break
json.dump(out,open(sys.argv[2],"w"),indent=1,ensure_ascii=False)
S=Image.new("RGB",(4*250,((len(tiles)+3)//4)*270),"white");d=ImageDraw.Draw(S)
for i,(k,im) in enumerate(tiles): x,y=(i%4)*250,(i//4)*270;S.paste(im,(x+5,y+5));d.text((x+5,y+252),k,fill="black")
S.save(sys.argv[3]);print(len(tiles))
