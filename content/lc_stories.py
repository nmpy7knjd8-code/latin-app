import json
S={1:("Rōma",["Rōma urbs est.","Urbs magna est.","In urbe est via longa.","Via est Via Appia.","Lupa in Palātiō est.","Lupa nōn mala est; lupa bona est."]),
2:("Familia Cornēliae",["Cornēlia māter est.","Gracchī fīliī sunt.","Pater fīliōs amat; māter fīliōs amat.","Fēmina ornāmenta habet.","Cornēlia fīliōs vocat.","'Haec ornāmenta sunt mea,' Cornēlia dīcit."]),
3:("In castrīs",["Mīlitēs in castrīs sunt.","Centuriō mīlitēs videt.","Mīlitēs ambulant et labōrant.","Centuriō mīlitēs monet.","Mīlitēs pīla portant.","Legiō pugnat et superat."]),
4:("In Forō",["Forum Rōmānōrum magnum est.","Senātus in Cūriā est.","Cicerō senātōribus verba dat.","Cōnsul bonus rem pūblicam servat.","Catilīna est vir malus.","Populus Cicerōnī grātiās agit."]),
5:("Templum Vestae",["In urbe est templum Vestae.","Virginēs in templō sunt.","Ignis in templō semper ārdet.","Cum virginibus est sacerdōs.","Ex templō aqua nōn venit, sed ignis.","Sine igne Rōma nōn est tūta."]),
6:("Augustus",["Rōmānī lateribus aedificābant.","Augustus templa marmore aedificāvit.","Multa bella gessit.","Mīlitēs eum imperātōrem vocābant.","Nummī nōmen eius portābant.","Augustus dīcere poterat: 'Urbem marmoream relīquī.'"]),
7:("Poēta",["Horātius poēta erat.","'Carpe diem,' amīcae dīxit.","'Crās fortasse nōn erō.'","'Sed versūs meī manēbunt.'","'Nōn omnis moriar.'","Etiam nunc versūs eius legimus."]),
8:("Philosophus",["Seneca philosophus erat.","Lūcīliō epistulās scrībēbat.","Dīcit vītam esse mīlitiam.","Animus fortis esse dēbet.","Vīvere est discere.","Nōs quoque discere possumus."]),
9:("Rōma capta",["Annō quadringentēsimō decimō Gothī vēnērunt.","Rōma capta est.","Multī cīvēs territī sunt.","Augustīnus librum scrīpsit.","In librō Cīvitās Deī laudātur.","Urbs terrēna cadit; verba manent."]),
10:("Scrīptor",["In monastēriō erat monachus quī librōs scrībēbat.","Liber quem scrībēbat erat Ēvangelium.","Manūs eius frīgidae erant.","Abbās, quī eum vidēbat, laudāvit.","Tandem monachus scrīpsit: 'Explicit liber.'","'Ōrāte prō scrīptōre!'"])}
out=[dict(id=f"story-u{u}",unit=u,title=t,lines=l,status="constructed micro-story (Ørberg-style); needs reviewer Latin check + glosses",drills=[]) for u,(t,l) in S.items()]
C=json.load(open("learning-cards.json"))
for s in out: s["drills"]=[c["id"] for c in C if c["unit"]==s["unit"] and c.get("attribution_note","").startswith("Constructed")]
json.dump(out,open("learning-stories.json","w"),ensure_ascii=False,indent=1);print(len(out))
