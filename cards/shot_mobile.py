import sys
from playwright.sync_api import sync_playwright
W,H=int(sys.argv[1]),int(sys.argv[2]); O="/workspace/latin-app/shots/"
U="http://localhost:8765/cards/index.html"
HCHK="""[...document.querySelectorAll('.card')].filter(c=>{for(const f of c.querySelectorAll('.face')){const r=f.getBoundingClientRect();for(const e of f.querySelectorAll('*')){if(!e.offsetWidth)continue;const b=e.getBoundingClientRect();if(e.scrollWidth>e.clientWidth+1&&getComputedStyle(e).overflowX!=='hidden'&&!e.matches('img,.art,.art *,.tornwrap,.frame,.cut,.fine,.fine *'))return true;if(!e.closest('.art')&&(b.left<r.left-1||b.right>r.right+1))return true}}return false}).map(c=>c.dataset.id)"""
CHK="""[...document.querySelectorAll('.card')].map(c=>{const b=c.querySelector('.back'),f=c.querySelector('.front');return [c.dataset.id,b.style.overflowY==='auto'?0:b.scrollHeight-b.clientHeight,f.scrollHeight-f.clientHeight]}).filter(x=>x[1]>1||x[2]>1)"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_context(viewport={"width":W,"height":H},device_scale_factor=2,is_mobile=True,has_touch=True).new_page()
    import os
    if os.environ.get("WIDEFONT"): pg.add_init_script("document.addEventListener('DOMContentLoaded',()=>{const s=document.createElement('style');s.textContent='.back .ctx{font-family:Verdana,\\'DejaVu Sans\\',sans-serif!important;letter-spacing:.04em;word-spacing:.1em}';document.head.appendChild(s)})")
    TAG=os.environ.get("TAG","")
    pg.goto(U); pg.evaluate("for(let u=1;u<=14;u++)localStorage.setItem('lingua.open.'+u,'1')"); pg.goto(U+"?draft=1"); pg.wait_for_timeout(1500)
    bad=[];tot=0;clamped=[];hbad=[]
    for u in range(1,pg.evaluate("UNITS.length")+1):
        pg.evaluate(f"setSec({u})"); pg.wait_for_timeout(300)
        tot+=pg.evaluate("document.querySelectorAll('.card').length"); bad+=pg.evaluate(CHK); hb=pg.evaluate(HCHK); hbad.extend(hb)
        clamped+=pg.evaluate("[...document.querySelectorAll('.ctx.clamp')].map(x=>x.closest('.card').dataset.id)")
    print(W,H,"cards",tot,"overflow",bad,"HORIZ",len(hbad),hbad[:12],"clamped",len(clamped),clamped[:8],"clamped_without_button",pg.evaluate("[...document.querySelectorAll('.ctx.clamp')].filter(c=>c.parentElement.querySelector('.more').hidden).length"),"pageScroll",pg.evaluate("document.documentElement.scrollHeight"),H)
    def shot(cid):
        sec=pg.evaluate(f"unitOf(CARDS.find(c=>c.id==='{cid}'))"); pg.evaluate(f"setSec({sec})"); pg.wait_for_timeout(300)
        i=pg.evaluate(f"VIS().findIndex(c=>c.id==='{cid}')")
        pg.evaluate(f"document.getElementById('card-{i}').scrollIntoView({{inline:'center'}})"); pg.wait_for_timeout(500)
        pg.screenshot(path=O+f"{W}-front-{cid}.png"); pg.evaluate(f"document.getElementById('card-{i}').click()"); pg.wait_for_timeout(900)
        pg.screenshot(path=O+f"{W}-back-{cid}.png")
    for cid in ["q-ha-hadrian-murum","i-pantheon-agrippa","x-map-roma","q-ovid-urbis","q-virgil-forsan","q-bede-sparrow","r-vulg-genesis-1-5","i-rib-regina"]: shot(cid)
    sec=pg.evaluate("unitOf(CARDS.find(c=>c.id==='q-ha-hadrian-murum'))");pg.evaluate(f"setSec({sec})");pg.wait_for_timeout(300)
    i=pg.evaluate("VIS().findIndex(c=>c.id==='q-ha-hadrian-murum')");pg.evaluate(f"document.getElementById('card-{i}').scrollIntoView({{inline:'center'}})");pg.wait_for_timeout(500)
    pg.evaluate(f"document.getElementById('card-{i}').click()");pg.wait_for_timeout(900)
    vis=pg.evaluate(f"!document.querySelector('#card-{i} .more').hidden");print("hadrian more visible:",vis)
    pg.screenshot(path=O+f"{W}x{H}{TAG}-hadrian-collapsed.png")
    if vis:
        pg.evaluate(f"document.querySelector('#card-{i} .more').click()");pg.wait_for_timeout(500);pg.screenshot(path=O+f"{W}x{H}{TAG}-hadrian-expanded.png")
        pg.evaluate("document.getElementById('xov').scrollTop=9999");pg.wait_for_timeout(300);pg.screenshot(path=O+f"{W}x{H}{TAG}-hadrian-expanded-bottom.png")
        print("flipped still:",pg.evaluate(f"document.getElementById('card-{i}').classList.contains('flipped')"))
        pg.evaluate("document.querySelector('#xov .more').click()");pg.wait_for_timeout(300);print("collapsed:",pg.evaluate("!document.getElementById('xov')"))
    pg.goto(U); pg.wait_for_timeout(1500); pg.evaluate("localStorage.clear();localStorage.setItem('lingua.known',JSON.stringify(CARDS.filter(c=>unitOf(c)===1).map(c=>c.id).concat(CARDS.filter(c=>unitOf(c)===2).slice(0,3).map(c=>c.id))))"); pg.goto(U); pg.wait_for_timeout(1200)
    pg.screenshot(path=O+f"{W}-home.png"); pg.click("#nsec"); pg.wait_for_timeout(400); pg.screenshot(path=O+f"{W}-home-next.png"); pg.click("#logo"); pg.wait_for_timeout(300); pg.screenshot(path=O+f"{W}-sections.png")
    b.close()
