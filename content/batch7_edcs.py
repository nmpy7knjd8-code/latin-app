"""EDCS (edcs.hist.uzh.ch) check: full-text search -> monument JSON. Usage: batch7_edcs.py 'phrase' ..."""
import sys,json,urllib.request,urllib.parse,time
UA={'User-Agent':'Mozilla/5.0 (latin-app research)'}
def get(u): return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40))
def search(q): return get('https://edcs.hist.uzh.ch/api/search?'+urllib.parse.urlencode({'q':q}))
def mon(i):
    s=str(int(i)).zfill(8); return get(f'https://edcs.hist.uzh.ch/data/monument/{s[:3]}/{s}.json')
if __name__=='__main__':
    out={}
    for q in sys.argv[1:]:
        ids=search(q); print('==',q,ids[:5])
        for i in ids[:3]:
            m=mon(i); out.setdefault(q,[]).append(m); print(json.dumps(m,ensure_ascii=False)[:700]); time.sleep(1)
    json.dump(out,open('batch7_src/edcs_'+str(int(time.time()))+'.json','w'),ensure_ascii=False)
