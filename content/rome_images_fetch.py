import json,urllib.request,urllib.parse,os,sys,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from rome_meta import IMGS
H={'User-Agent':'LatinAppResearch/1.0 (garrett)'}
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'img','rome'); os.makedirs(D,exist_ok=True)
out={}
for k,(f,kind,alt,lic,cr,asp,tr) in IMGS.items():
    dst=os.path.join(D,k+'.jpg')
    if not os.path.exists(dst):
        q=urllib.parse.urlencode({'action':'query','format':'json','titles':'File:'+f,'prop':'imageinfo','iiprop':'url|extmetadata','iiurlwidth':1400})
        r=json.load(urllib.request.urlopen(urllib.request.Request('https://commons.wikimedia.org/w/api.php?'+q,headers=H),timeout=30))
        p=list(r['query']['pages'].values())[0]; ii=p['imageinfo'][0]
        out[k]=ii['extmetadata'].get('LicenseShortName',{}).get('value')
        data=urllib.request.urlopen(urllib.request.Request(ii['thumburl'],headers=H),timeout=60).read()
        open(dst,'wb').write(data)
        print(k,out[k],len(data),flush=True)
json.dump(out,open(os.path.join(D,'licences.json'),'w'),indent=1)
