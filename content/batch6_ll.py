import sys,re,html,urllib.request,os
def text(u):
    fn=re.sub(r'\W','_',u)[-90:]+'.txt'
    if os.path.exists(fn): return open(fn).read()
    raw=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read()
    if raw[:2] in (b'\xff\xfe',b'\xfe\xff'): t=raw.decode('utf-16')
    else:
     try: t=raw.decode('utf-8')
     except: t=raw.decode('latin-1')
    t=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<script.*?</script>','',t,flags=re.S))))
    open(fn,'w').write(t); return t
if __name__=='__main__':
    u=sys.argv[1]
    t=text(u)
    for pat in sys.argv[2:]:
        m=[x.start() for x in re.finditer(pat,t,re.I)]
        print(f'-- {pat}: {len(m)} hits')
        for i in m[:2]: print('   ',t[max(0,i-150):i+250])
