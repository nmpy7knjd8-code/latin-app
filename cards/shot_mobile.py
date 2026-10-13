from playwright.sync_api import sync_playwright
U="http://localhost:8765/cards/index.html?draft=1"; O="/workspace/latin-app/shots/"
import sys
W,H=int(sys.argv[1]),int(sys.argv[2])
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_context(viewport={"width":W,"height":H},device_scale_factor=2,is_mobile=True,has_touch=True).new_page()
    pg.goto(U); pg.wait_for_timeout(1500)
    n=pg.evaluate("document.querySelectorAll('.card').length")
    bad=pg.evaluate("""[...document.querySelectorAll('.card')].map(c=>{const bk=c.querySelector('.back');return [c.dataset.id,bk.scrollHeight-bk.clientHeight,c.querySelector('.front').scrollHeight-c.querySelector('.front').clientHeight, c.getBoundingClientRect().bottom]}).filter(x=>x[1]>1||x[2]>1)""")
    print(n,"overflowing:",bad, pg.evaluate("document.querySelector('.card').getBoundingClientRect().bottom"), pg.evaluate("document.documentElement.scrollHeight"))
    lens=pg.evaluate("[...document.querySelectorAll('.card')].map((c,i)=>[i,c.dataset.id,c.querySelector('.back').innerText.length]).sort((a,b)=>b[2]-a[2]).slice(0,4)")
    ids=pg.evaluate("[...document.querySelectorAll('.card')].map(c=>c.dataset.id)");lens=[(ids.index(k),k,0) for k in ['q-caesar-veni','r-vulg-genesis-1-5','q-bede-sparrow','q-magna-carta-39','i-rib-facilis']]
    for i,cid,_ in lens:
        pg.evaluate(f"document.getElementById('card-{i}').scrollIntoView({{inline:'center'}})"); pg.wait_for_timeout(400)
        pg.screenshot(path=O+f"{W}-front-{cid}.png")
        pg.evaluate(f"document.getElementById('card-{i}').click()"); pg.wait_for_timeout(800)
        pg.screenshot(path=O+f"{W}-back-{cid}.png")
    pg.evaluate("document.getElementById('card-0').scrollIntoView({inline:'center'});document.querySelector('#card-0 .fine').open=true"); pg.wait_for_timeout(300); pg.screenshot(path=O+f"{W}-credits-open.png")
    b.close()
