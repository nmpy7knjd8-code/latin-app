import os,sys
from PIL import Image
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from rome_meta import IMGS
from rembg import remove, new_session
S=new_session('isnet-general-use')
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'img','rome')
def crop(im,asp):
    a,b=map(int,asp.split(':')); r=a/b; w,h=im.size
    if w/h>r: nw=int(h*r); x=(w-nw)//2; return im.crop((x,0,x+nw,h))
    nh=int(w/r); y=max(0,int((h-nh)*0.3)); return im.crop((0,y,w,y+nh))
for k,(f,kind,alt,lic,cr,asp,tr) in IMGS.items():
    src=os.path.join(D,k+'.jpg'); dst=os.path.join(D,k+'.webp')
    if os.path.exists(dst): continue
    im=Image.open(src); im.load()
    if tr:
        im=remove(im.convert('RGB'),session=S)
        bb=im.getbbox(); im=im.crop(bb) if bb else im
        im.thumbnail((1000,1000)); im.save(dst,'WEBP',quality=88)
    else:
        im=crop(im.convert('RGB'),asp); im.thumbnail((1000,1000)); im.save(dst,'WEBP',quality=85)
    print(k,im.size,flush=True)
