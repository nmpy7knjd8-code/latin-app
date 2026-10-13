import json,urllib.request,urllib.parse,re
UA={"User-Agent":"LatinApp/0.1 (research; garrett)"}
get=lambda u: json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
r=get("https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrlimit=30&gsrsearch="+urllib.parse.quote("Vindolanda tablet")+"&prop=imageinfo&iiprop=url|extmetadata|size&iiurlwidth=900")
for p in r["query"]["pages"].values():
    md=p["imageinfo"][0]["extmetadata"];g=lambda x:re.sub("<[^>]+>","",md.get(x,{}).get("value",""))[:70]
    print(p["title"][5:80],"|",g("LicenseShortName"),"|",g("Artist"),"|",g("Credit"))
