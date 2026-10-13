from rembg import remove as _rm, new_session
S=new_session("isnet-general-use")
remove=lambda b:_rm(b,session=S)
import json,urllib.request,os,subprocess
UA={"User-Agent":"LatinApp/0.1 (research; garrett)"}
pi=json.load(open("lc_images_meta.json"))
keep="g-sum-est x-whosays-cornelia v-senatus g-gen g-dat l-toga d-dico v-deus v-templum g-abl-prep i-pantheon-parse l-lares v-imperator g-perf-rg g-impf l-denarius v-amo v-animus g-infinitive x-greek-flag l-schola g-passive v-rex x-vulgate v-liber l-monasterium i-karolus d-scribo".split()
M={k:pi[k] for k in keep}
for f in ["lc_images_search.json","lc_images_search3.json","lc_images_search4.json","lc_images_search5.json"]:
    for k,v in json.load(open(f)).items():
        if "file" in v and k not in keep: M[k]=v
KIND={"statue_cutout":"g-sum-est g-1decl-nom g-ind-stat l-toga d-dico v-imperator x-timeline-emp v-animus g-adj v-amo".split(),
 "coin":"i-coin-divi-f g-possum l-denarius v-rex i-chirho i-karolus".split(),
 "artifact_cut":"l-bulla l-lares l-pila l-annona d-crux".split(),
 "painting":"x-whosays-cornelia v-senatus g-dat g-passive x-map-roma x-map-medieval d-video g-2decl v-urbs".split(),
 "manuscript":"g-infinitive x-greek-flag x-vulgate v-liber l-monasterium d-scribo g-imperative g-future x-meter x-colophon g-relative".split(),
 "inscription":"i-spqr g-perf-rg i-vindolanda x-parse-signum v-miles g-2conj".split(),
 "artifact":"v-pater v-filius g-acc g-3decl l-schola g-1conj v-tempus v-deus".split()}
kind_of={c:k for k,l in KIND.items() for c in l}
LIC={"public domain":"Public domain","cc0":"CC0","cc by 4.0":"CC BY 4.0","cc by-sa 4.0":"CC BY-SA 4.0"}
C=json.load(open("learning-cards.json"))
os.makedirs("../assets/learning/raw",exist_ok=True)
for c in C:
    m=M.get(c["id"])
    if not m: print("MISSING",c["id"]);continue
    k=kind_of.get(c["id"],"building"); cut=k in("statue_cutout","coin","artifact_cut")
    ext=os.path.splitext(m["thumb"].split("?")[0])[1].lower() or ".jpg"
    raw=f"../assets/learning/raw/{c['id']}{ext}"
    if not os.path.exists(raw):
        open(raw,"wb").write(urllib.request.urlopen(urllib.request.Request(m["thumb"],headers=UA),timeout=60).read())
    src=raw
    if cut:
        src=f"../assets/learning/{c['id']}.png"
        if not os.path.exists(src): open(src,"wb").write(remove(open(raw,"rb").read()))
    w,h=m["w"],m["h"]
    c["image"]=dict(src="assets/learning/"+os.path.relpath(src,"../assets/learning"),alt=(m.get("desc") or m["file"])[:140],
      kind="artifact" if k=="artifact_cut" else k,aspect=f"{w}:{h}",transparent=cut,
      credit=(m.get("artist") or "Wikimedia Commons")+" / Wikimedia Commons",
      license=LIC.get(m["lic"].lower(),m["lic"]),source_url=m["page"])
    c["image_idea"]["license_status"]=f"verified on file page via Commons API: {m['lic']}"
json.dump(C,open("learning-cards.json","w"),ensure_ascii=False,indent=1)
print("done")
