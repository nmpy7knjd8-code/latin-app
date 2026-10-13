import json,urllib.request,os,shutil
from rembg import remove,new_session
S=new_session("isnet-general-use");UA={"User-Agent":"LatinApp/0.1 (research; garrett)"}
A=json.load(open("lc_cands6.json"));A.update(json.load(open("lc_cands7.json")))
LIC={"public domain":"Public domain","cc0":"CC0"}
M={"g-sum-est":("g-sum-est#2","building",False),"v-animus":("v-animus#1","statue_cutout",True),"i-coin-divi-f":("i-coin-divi-f#3","coin",True),
 "x-parse-signum":("x-parse-signum#0","artifact",True),"v-tempus":("v-tempus#2","artifact",True),"g-pronoun":("g-pronoun#2","building",False),"i-vindolanda":("i-vindolanda#0","artifact",False)}
C=json.load(open("learning-cards.json"));B={c["id"]:c for c in C}
os.chdir("../assets/learning")
for id,(k,kind,cut) in M.items():
    m=A[k];ext=os.path.splitext(m["thumb"].split("?")[0])[1].lower()
    for f in os.listdir("raw"):
        if f.startswith(id+"."): os.remove("raw/"+f)
    raw=f"raw/{id}{ext}";open(raw,"wb").write(urllib.request.urlopen(urllib.request.Request(m["thumb"],headers=UA)).read())
    src=raw
    if cut:
        src=f"{id}.png"
        if ext==".png" and id=="x-parse-signum": shutil.copy(raw,src)
        else: open(src,"wb").write(remove(open(raw,"rb").read(),session=S,post_process_mask=True))
    elif os.path.exists(f"{id}.png"): os.remove(f"{id}.png")
    B[id]["image"]=dict(src="assets/learning/"+src,alt=m["desc"][:140] or m["file"],kind=kind,aspect=f'{m["w"]}:{m["h"]}',transparent=cut,
        credit=(m["artist"] or "Wikimedia Commons")+" / Wikimedia Commons",license=LIC.get(m["lic"].lower(),m["lic"]),source_url=m["page"])
    B[id]["image_idea"]["license_status"]=f"verified on file page via Commons API: {m['lic']} (visual pass Oct 13)"
# g-future reuses Horace Odes MS from g-imperative
B["g-future"]["image"]=dict(B["g-imperative"]["image"]);B["g-future"]["image_idea"]["license_status"]="reuses g-imperative Horace Odes MS (Public domain)"
# coin legend upgrade
c=B["i-coin-divi-f"];c["latin"]="IMP·CAESAR·DIVI·F"; c["translation"]="Imperator Caesar, son of the deified (Julius)"
c["source"]={"work":"Coin legend","citation":"Denarius of Octavian, Crawford RRC 538/1 (c. 37 BC), obverse IMP·CAESAR·DIVI·F·III·VIR·ITER·R·P·C"}
c["gloss"].insert(0,dict(word="IMP",lemma="imperātor",meaning="commander (title)",parse="abbr. nom."))
if "imperator" not in c["vocab_ids"]: c["vocab_ids"]=sorted(c["vocab_ids"]+["imperator"])
json.dump(C,open("/workspace/latin-app/content/learning-cards.json","w"),ensure_ascii=False,indent=1);print("ok")
