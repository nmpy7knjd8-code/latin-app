import sys,re,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from batch6_ll import text
L='https://www.thelatinlibrary.com/'
def norm(s): return re.sub(r'\s+',' ',s.lower().replace('v','u').replace('j','i'))
def find(pages,phrase):
    for p in pages:
        u=p if p.startswith('http') else L+p
        try: t=text(u)
        except Exception as e: continue
        n=norm(t); i=n.find(norm(phrase))
        if i>=0: return u,t[max(0,i-120):i+len(phrase)+160]
    return None,None
