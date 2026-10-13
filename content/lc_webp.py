import json,os
from PIL import Image
F="content/learning-cards.json";C=json.load(open(F));n=0
for c in C:
    s=c["image"]["src"]
    if "/raw/" not in s: continue
    im=Image.open(s);im=im.convert("RGBA" if im.mode in("RGBA","LA","P") else "RGB");im.thumbnail((1200,1200))
    out=f"assets/learning/{c['id']}.webp";im.save(out,"WEBP",quality=82,method=6)
    c["image"]["src"]=out;c["image"]["aspect"]=f"{im.width}:{im.height}" if False else c["image"]["aspect"];n+=1
json.dump(C,open(F,"w"),ensure_ascii=False,indent=1);print(n,"converted")
