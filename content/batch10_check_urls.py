"""HTTP-check learn_more and source_url for batch-7 cards; stamp learn_more.verified_http."""
import json,urllib.request,os,time
HERE=os.path.dirname(os.path.abspath(__file__)); P=os.path.join(HERE,'batch10-cards.json')
C=json.load(open(P)); H={'User-Agent':'Mozilla/5.0 (LatinApp research)'}
def code(u):
    for i in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30).status
        except urllib.error.HTTPError as e: 
            if e.code in(429,503): time.sleep(3); continue
            return e.code
        except Exception as e: time.sleep(2); last=str(e)[:60]
    return last
seen={}
for c in C:
    for k,u in (('learn_more',c['learn_more']['url']),('source_url',c.get('source_url'))):
        if not u: continue
        if u not in seen: seen[u]=code(u); time.sleep(0.2)
        if k=='learn_more': c['learn_more']['verified_http']=str(seen[u])
        if seen[u]!=200: print('BAD',c['id'],k,u,seen[u])
json.dump(C,open(P,'w'),ensure_ascii=False,indent=1); print('checked',len(seen),'urls')
