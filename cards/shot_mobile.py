import sys
from playwright.sync_api import sync_playwright
W,H=int(sys.argv[1]),int(sys.argv[2]); O="/workspace/latin-app/shots/"
U="http://localhost:8765/cards/index.html"
CHK="""[...document.querySelectorAll('.card')].map(c=>{const b=c.querySelector('.back'),f=c.querySelector('.front');return [c.dataset.id,b.scrollHeight-b.clientHeight,f.scrollHeight-f.clientHeight]}).filter(x=>x[1]>1||x[2]>1)"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_context(viewport={"width":W,"height":H},device_scale_factor=2,is_mobile=True,has_touch=True).new_page()
    pg.goto(U); pg.evaluate("for(let u=1;u<=10;u++)localStorage.setItem('lingua.open.'+u,'1')"); pg.goto(U+"?draft=1"); pg.wait_for_timeout(1500)
    bad=[];tot=0;clamped=[]
    for u in range(1,11):
        pg.evaluate(f"setSec({u})"); pg.wait_for_timeout(300)
        tot+=pg.evaluate("document.querySelectorAll('.card').length"); bad+=pg.evaluate(CHK)
        clamped+=pg.evaluate("[...document.querySelectorAll('.ctx.clamp')].map(x=>x.closest('.card').dataset.id)")
    print(W,H,"cards",tot,"overflow",bad,"clamped",len(clamped),clamped[:8],"pageScroll",pg.evaluate("document.documentElement.scrollHeight"),H)
    def shot(cid):
        sec=pg.evaluate(f"unitOf(CARDS.find(c=>c.id==='{cid}'))"); pg.evaluate(f"setSec({sec})"); pg.wait_for_timeout(300)
        i=pg.evaluate(f"VIS().findIndex(c=>c.id==='{cid}')")
        pg.evaluate(f"document.getElementById('card-{i}').scrollIntoView({{inline:'center'}})"); pg.wait_for_timeout(500)
        pg.screenshot(path=O+f"{W}-front-{cid}.png"); pg.evaluate(f"document.getElementById('card-{i}').click()"); pg.wait_for_timeout(900)
        pg.screenshot(path=O+f"{W}-back-{cid}.png")
    for cid in ["q-virgil-forsan","q-bede-sparrow","r-vulg-genesis-1-5","i-rib-regina"]: shot(cid)
    pg.goto(U); pg.wait_for_timeout(1500); pg.evaluate("localStorage.clear();localStorage.setItem('lingua.known',JSON.stringify(CARDS.filter(c=>unitOf(c)===1).map(c=>c.id).concat(CARDS.filter(c=>unitOf(c)===2).slice(0,3).map(c=>c.id))))"); pg.goto(U); pg.wait_for_timeout(1200)
    pg.screenshot(path=O+f"{W}-home.png"); pg.click("#logo"); pg.wait_for_timeout(300); pg.screenshot(path=O+f"{W}-sections.png")
    b.close()
