import json,urllib.request,urllib.parse,time,os,re
UA={"User-Agent":"LatinApp/0.1 (research; garrett)"}
def get(u):
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
C=json.load(open("learning-cards.json"))
os.makedirs("../assets/learning",exist_ok=True)
out={}
for c in C:
    t=urllib.parse.unquote(c["learn_more"]["url"].rsplit("/",1)[1])
    try:
        p=get("https://en.wikipedia.org/w/api.php?action=query&format=json&prop=pageimages&piprop=name&redirects=1&titles="+urllib.parse.quote(t))
        name=list(p["query"]["pages"].values())[0].get("pageimage")
        if not name: out[c["id"]]={"err":"no pageimage"};continue
        m=get("https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url|extmetadata|size&iiurlwidth=900&titles="+urllib.parse.quote("File:"+name))
        pg=list(m["query"]["pages"].values())[0]
        if "imageinfo" not in pg: out[c["id"]]={"err":"not on commons (likely enwiki fair use)","file":name};continue
        ii=pg["imageinfo"][0];md=ii["extmetadata"]
        g=lambda k:re.sub("<[^>]+>","",md.get(k,{}).get("value","")).strip()
        out[c["id"]]=dict(file=name,thumb=ii["thumburl"],page=ii["descriptionurl"],w=ii["width"],h=ii["height"],lic=g("LicenseShortName"),artist=g("Artist")[:120],desc=g("ImageDescription")[:150])
    except Exception as e: out[c["id"]]={"err":str(e)}
    time.sleep(0.3)
json.dump(out,open("lc_images_meta.json","w"),indent=1,ensure_ascii=False)
for k,v in out.items(): print(k,v.get("lic") or v.get("err"),v.get("file"),v.get("w"),v.get("h"))
