import json
from PIL import Image,ImageDraw
C=json.load(open("content/learning-cards.json"))
def sheet(items,name):
    W=260;H=320;cols=6;rows=(len(items)+cols-1)//cols
    S=Image.new("RGB",(cols*W,rows*H),"white");d=ImageDraw.Draw(S)
    for i,c in enumerate(items):
        im=Image.open(c["image"]["src"]).convert("RGBA");im.thumbnail((W-10,H-30))
        bg=Image.new("RGBA",im.size,(230,120,200,255));bg.alpha_composite(im)
        x,y=(i%cols)*W,(i//cols)*H;S.paste(bg.convert("RGB"),(x+5,y+5));d.text((x+5,y+H-22),c["id"],fill="black")
    S.save(name)
cut=[c for c in C if c["image"]["transparent"]];oth=[c for c in C if not c["image"]["transparent"]]
sheet(cut,"/tmp/lc_sheet_cut.png");sheet(oth[:24],"/tmp/lc_sheet_o1.png");sheet(oth[24:],"/tmp/lc_sheet_o2.png");print(len(cut),len(oth))
