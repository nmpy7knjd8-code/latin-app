"""Fetch author + licence URL from Commons for every Rome image -> data/rome-image-credits.json (used by rome_build.py)."""
import json,os,sys,re,urllib.request,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from rome_meta import IMGS
H={'User-Agent':'LatinAppResearch/1.0 (garrett)'}
out={}
for k,(f,*_) in IMGS.items():
    q=urllib.parse.urlencode({'action':'query','format':'json','titles':'File:'+f,'prop':'imageinfo','iiprop':'extmetadata'})
    p=list(json.load(urllib.request.urlopen(urllib.request.Request('https://commons.wikimedia.org/w/api.php?'+q,headers=H),timeout=30))['query']['pages'].values())[0]
    m=p['imageinfo'][0]['extmetadata']; g=lambda x: re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',m.get(x,{}).get('value',''))).strip()
    out[k]=dict(artist=g('Artist'),licence=g('LicenseShortName'),licence_url=g('LicenseUrl'),credit_line=g('Credit')[:200])
json.dump(out,open(os.path.join(HERE,'data','rome-image-credits.json'),'w'),ensure_ascii=False,indent=1)
for k,v in out.items():
    if 'BY' in v['licence']: print(k,'|',v['artist'][:80],'|',v['licence'],v['licence_url'])
