import os,sys,json
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from batch4_images import IMGS
from rembg import remove, new_session
S=new_session('isnet-general-use')
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'img','batch4')
def crop(im,asp):
    a,b=map(int,asp.split(':')); r=a/b; w,h=im.size
    if w/h>r: nw=int(h*r); x=(w-nw)//2; return im.crop((x,0,x+nw,h))
    nh=int(w/r); y=max(0,int((h-nh)*0.3)); return im.crop((0,y,w,y+nh))
force='--force' in sys.argv
for k,(f,kind,alt,asp,tr) in IMGS.items():
    src=os.path.join(D,k+'.src'); dst=os.path.join(D,k+'.webp')
    if os.path.exists(dst) and not force: continue
    im=Image.open(src); im.load()
    if tr:
        im=remove(im.convert('RGB'),session=S,post_process_mask=True)
        a=im.getchannel('A').point(lambda v: 0 if v<48 else (255 if v>200 else v)); im.putalpha(a)
        bb=a.point(lambda v:255 if v>48 else 0).getbbox(); im=im.crop(bb) if bb else im
        im.thumbnail((1000,1000)); im.save(dst,'WEBP',quality=88)
    else:
        im=crop(im.convert('RGB'),asp); im.thumbnail((1000,1000)); im.save(dst,'WEBP',quality=85)
    print(k,im.size,flush=True)
