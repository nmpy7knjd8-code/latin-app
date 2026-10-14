import sys,re,html,urllib.request
def get(path):
    u='https://romaninscriptionsofbritain.org/inscriptions/'+path
    t=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read().decode()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    t=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',t)))
    i=t.find('Edition'); return u,t
for p in sys.argv[1:]:
    u,t=get(p); open(p+'.txt','w').write(t)
    a=t.find('Text field'); print('=====',p,u); print(t[max(0,t.find(' Edition ')):][:1800])
