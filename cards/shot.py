from playwright.sync_api import sync_playwright
U="file:///workspace/latin-app/cards/index.html"; O="/workspace/latin-app/cards/"
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":1900,"height":680})
    pg.goto(U); pg.wait_for_timeout(800)
    pg.screenshot(path=O+"preview.png")                      # all fronts, incl. Augustine
    pg.click("#card-0"); pg.wait_for_timeout(900)
    pg.screenshot(path=O+"preview-back.png")                 # Caesar back
    pg.click("#m-learn"); pg.wait_for_timeout(300); pg.click("#card-0 .w"); pg.wait_for_timeout(200)
    pg.screenshot(path=O+"preview-learn.png")
    pg.click("#card-1 .say"); pg.wait_for_timeout(200)
    pg.screenshot(path=O+"preview-ipa.png")
    m=p.devices["iPhone 13"]; pg2=b.new_context(**m).new_page()
    pg2.goto(U); pg2.wait_for_timeout(800)
    pg2.screenshot(path=O+"preview-mobile.png")
    pg2.evaluate("document.getElementById('card-4').scrollIntoView({inline:'center'})"); pg2.wait_for_timeout(600)
    pg2.screenshot(path=O+"preview-mobile-augustine.png")
    b.close()
