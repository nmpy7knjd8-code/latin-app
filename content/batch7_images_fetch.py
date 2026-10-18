"""Fetch batch-7 images from Commons, record licence metadata from the API, refuse NC/ND and British Museum-credited files."""
import json,urllib.request,urllib.parse,os,sys,re,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from batch7_images import IMGS
H={'User-Agent':'LatinAppResearch/1.0 (garrett)'}
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'img','batch7'); os.makedirs(D,exist_ok=True)
MP=os.path.join(D,'meta.json'); meta=json.load(open(MP)) if os.path.exists(MP) else {}
clean=lambda s:re.sub(r'\s+',' ',re.sub('<[^>]+>','',s or '')).strip()
for k,(f,kind,alt,asp,tr) in IMGS.items():
    if k in meta and meta[k].get('file')==f and os.path.exists(os.path.join(D,k+'.src')): continue
    q0=urllib.parse.urlencode({'action':'query','format':'json','titles':'File:'+f})
    r0=json.load(urllib.request.urlopen(urllib.request.Request('https://commons.wikimedia.org/w/api.php?'+q0,headers=H),timeout=30))
    if 'missing' in list(r0['query']['pages'].values())[0]:
        qa=urllib.parse.urlencode({'action':'query','format':'json','list':'allimages','aiprefix':f.replace(' ','_'),'ailimit':3})
        ra=json.load(urllib.request.urlopen(urllib.request.Request('https://commons.wikimedia.org/w/api.php?'+qa,headers=H),timeout=30))['query']['allimages']
        if ra: f=ra[0]['name'].replace('_',' '); print('resolved',k,'->',f)
    q=urllib.parse.urlencode({'action':'query','format':'json','titles':'File:'+f,'prop':'imageinfo','iiprop':'url|extmetadata','iiurlwidth':1600})
    r=json.load(urllib.request.urlopen(urllib.request.Request('https://commons.wikimedia.org/w/api.php?'+q,headers=H),timeout=30))
    p=list(r['query']['pages'].values())[0]
    if 'imageinfo' not in p: print('MISSING',k,f); continue
    ii=p['imageinfo'][0]; md=ii['extmetadata']; g=lambda x:clean(md.get(x,{}).get('value',''))
    m=dict(file=IMGS[k][0],resolved=f,license=g('LicenseShortName'),license_url=g('LicenseUrl'),artist=g('Artist'),credit_line=g('Credit'),usage=g('UsageTerms'),
           descurl=ii['descriptionurl'])
    bad=[]
    if re.search(r'\bNC\b|\bND\b|non-?commercial',m['license']+' '+m['usage'],re.I): bad.append('NC/ND')
    if re.search(r'British Museum',m['artist']+' '+m['credit_line'],re.I): bad.append('British Museum credit')
    if not re.search(r'public domain|cc0|cc by|cc-by|no restrictions|pdm|^attribution$',m['license'],re.I): bad.append('unrecognised licence')
    m['problems']=bad
    url=ii.get('thumburl') or ii['url']
    data=urllib.request.urlopen(urllib.request.Request(url,headers=H),timeout=90).read()
    open(os.path.join(D,k+'.src'),'wb').write(data); meta[k]=m
    print(k,'|',m['license'],'|',m['artist'][:50],'|',bad,flush=True); time.sleep(0.3)
json.dump(meta,open(MP,'w'),indent=1,ensure_ascii=False)
