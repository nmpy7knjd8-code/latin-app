import json,re,sys
sys.argv=[""];exec(open("lc_images_search.py").read().split("Q={")[0])
Q={"v-miles":"Roman legionary reenactor lorica segmentata","l-pila":"pilum Roman javelin","i-chirho":"Constantius II coin labarum Chi-Rho","l-annona":"carbonized bread Pompeii loaf","g-relative":"Lord's Prayer Latin manuscript","g-acc":"Roman grave relief father son","x-colophon":"Latin manuscript scribe colophon explicit","d-crux":"Cross of Justin II","x-map-roma":"Ancient Rome map seven hills Kiepert","g-future":"Horace Odes manuscript Latin Carmina"}
exec("Q=Q\n"+open("lc_images_search.py").read().split("res={}",1)[1].join(["res={}",""]).replace("lc_images_search.json","lc_images_search2.json"))
