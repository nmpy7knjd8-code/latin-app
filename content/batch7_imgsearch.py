import json,urllib.request,urllib.parse,re,sys,time
UA={"User-Agent":"LatinApp/0.1 (research; garrett)"}
def get(u): return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40))
def search(q,n=7):
    r=get("https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrlimit=%d&gsrsearch="%n+urllib.parse.quote(q)+"&prop=imageinfo&iiprop=url|extmetadata|size|mime")
    out=[]
    for p in sorted(r.get("query",{}).get("pages",{}).values(),key=lambda p:p.get('index',0)):
        ii=p["imageinfo"][0];md=ii["extmetadata"];g=lambda x:re.sub("<[^>]+>","",md.get(x,{}).get("value",""))
        out.append((p["title"][5:],g("LicenseShortName"),g("Artist")[:40],ii['width'],ii['height'],ii['mime']))
    return out
if __name__=='__main__':
    qs=json.load(open(sys.argv[1]))
    for k,q in qs.items():
        print('##',k,'|',q)
        try:
            for t in search(q): 
                if 'image' in t[5] and 'svg' not in t[5]: print('  ',t[0][:90],'|',t[1],'|',t[2],'|',t[3],'x',t[4])
        except Exception as e: print('  ERR',e)
        time.sleep(0.5)
