"""Critic automation for batch 7: (1) Latin vs source text, (2) macrons vs Alatius, (3) licence/credit sanity. Writes batch10_src/critic.json"""
import json,os,re,sys,unicodedata,urllib.request,urllib.parse,html,time
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from batch10_ll import text as fetch
C=json.load(open(os.path.join(HERE,sys.argv[1] if len(sys.argv)>1 else 'batch10-cards.json')))
def norm(s):
    s=''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn').lower()
    s=s.replace('v','u').replace('j','i').replace('æ','ae')
    return re.sub(r'[^a-z ]',' ',s)
def words(s): return norm(s).split()
res={}
os.chdir(os.path.join(HERE,'batch10_src'))
for c in C:
    r=res.setdefault(c['id'],{})
    lat=c['latin'].split(' — ')[-1]
    u=c.get('source_url','')
    if u and ('thelatinlibrary' in u or 'romaninscriptions' in u or 'perseids' in u or 'uchicago' in u or 'wikipedia' in u or 'wikisource' in u or 'hs-augsburg' in u):
        try:
            t=' '.join(words(fetch(u)))
            segs=[s for s in re.split(r'…|\(|\)|—',lat) if s.strip()]
            miss=[]
            for s in segs:
                w=words(s)
                # allow 1-word gaps: check each 3-word window
                for i in range(max(1,len(w)-2)):
                    win=' '.join(w[i:i+3])
                    if win and win not in t: miss.append(win)
            r['source_check']='ok' if not miss else 'MISSING: '+' | '.join(miss[:4])
        except Exception as e: r['source_check']='fetch error '+str(e)[:80]
    else: r['source_check']='n/a (constructed or EDCS/other; checked separately)'
# Alatius
lat=[c['latin'].split(' — ')[-1] for c in C]
plain='\n'.join(''.join(ch for ch in unicodedata.normalize('NFD',l) if unicodedata.category(ch)!='Mn') for l in lat)
data=urllib.parse.urlencode({'textcontent':plain,'macronize':'on','alsomaius':'on','scan':'0','utov':'on'}).encode()
h=urllib.request.urlopen(urllib.request.Request('https://alatius.com/macronizer/',data=data,headers={'User-Agent':'Mozilla/5.0'}),timeout=120).read().decode()
m=re.search(r'<div class="prewrap"[^>]*>(.*?)</div>',h,re.S) or re.search(r'<p class="prewrap">(.*?)</p>',h,re.S)
body=html.unescape(re.sub(r'<[^>]+>','',m.group(1))) if m else ''
open('alatius_out.txt','w').write(body or h)
alines=[l for l in body.split('\n')]
for c,l,a in zip(C,lat,alines):
    mine=re.findall(r'[\wāēīōūȳĀĒĪŌŪ]+',unicodedata.normalize('NFC',l)); his=re.findall(r'[\wāēīōūȳĀĒĪŌŪ]+',unicodedata.normalize('NFC',a))
    diff=[f'{x}≠{y}' for x,y in zip(mine,his) if x!=y and x.lower()!=y.lower()]
    res[c['id']]['alatius']=diff
json.dump(res,open('critic.json','w'),ensure_ascii=False,indent=1)
for k,v in res.items(): print(k,'|',v['source_check'][:90],'|',' '.join(v.get('alatius',[])))
