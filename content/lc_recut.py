import sys,glob,os
from rembg import remove,new_session
S=new_session(sys.argv[1]);os.chdir("/workspace/latin-app/assets/learning")
for i in sys.argv[2:]:
    raw=glob.glob(f"raw/{i}.*")[0];open(f"{i}.png","wb").write(remove(open(raw,"rb").read(),session=S,post_process_mask=True));print(i,os.path.getsize(f"{i}.png"))
