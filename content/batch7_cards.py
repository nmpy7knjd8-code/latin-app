# Batch 7 card texts. Gloss format: "word|lemma|meaning|parse; ..."  (no semicolons inside meanings)
# K(id,type,era,unit,latin,translation,context,more,person,work,cit,date,source_url,conf,note,gloss,target,preview,img,lm_label,lm_url, **extra)
LL='https://www.thelatinlibrary.com/'
EDCS='https://edcs.hist.uzh.ch/search'
WP='https://en.wikipedia.org/wiki/'
WS='https://la.wikisource.org/wiki/'
CON='Constructed teaching sentence (not a quotation).'
CARDS=[]
def K(*a,**kw): CARDS.append((a,kw))

# ---------------- UNIT 1: Urbs ----------------
K('v-amphitheatrum','vocab','empire',1,'Amphitheātrum Flāvium magnum est.','The Flavian Amphitheatre is big.',
 "Romans called the Colosseum the Amphitheātrum Flāvium, after the Flavian emperors Vespasian and Titus, who began it in the AD 70s; it opened in AD 80. It held about 50,000 spectators for gladiator fights and animal hunts. The name Colosseum came later, probably from a colossal bronze statue of Nero that stood nearby. Est links the subject to magnum, which has the same neuter ending as amphitheātrum.",
 "Its outer wall had 80 numbered arches, and spectators' tokens showed which entrance to use. A huge canvas awning, the vēlārium, shaded the crowd.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Amphitheātrum|amphitheātrum|amphitheatre|nom. sg. n.; Flāvium|Flāvius|Flavian|nom. sg. n.; magnum|magnus|big, great|nom. sg. n.; est|sum|is|3rd sg. pres.',
 ['nominative','sum'],['adjective_agreement'],'colosseum','Colosseum',WP+'Colosseum',subtype='vocab')
K('v-circus-maximus','vocab','republic',1,'Circus Maximus longus et lātus est.','The Circus Maximus is long and wide.',
 "The Circus Maximus, in the valley between the Palatine and Aventine hills, was Rome's chariot-racing track. At its largest it was about 600 metres long and seated perhaps 150,000 people. Drivers raced seven laps for four teams, the Reds, Whites, Greens and Blues. Both adjectives, longus and lātus, describe the masculine noun circus.",
 "Circus means 'circle' or 'ring', and gives English circus and circuit. An Egyptian obelisk that once stood on its central barrier now stands in the Piazza del Popolo.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Circus|circus|racetrack, circus|nom. sg. m.; Maximus|maximus|greatest|nom. sg. m.; longus|longus|long|nom. sg. m.; et|et|and|conj.; lātus|lātus|wide|nom. sg. m.; est|sum|is|3rd sg. pres.',
 ['nominative','sum'],['adjective_agreement'],'circus','Circus Maximus',WP+'Circus_Maximus',subtype='vocab')
K('c-roma-aeterna','artifact','empire',1,'ROMA AETERNA — Rōma aeterna','Eternal Rome',
 "Emperors put this slogan on their coins to promise that Rome would last forever. This silver denarius of Septimius Severus, who ruled from AD 193 to 211, was found in Britain. The adjective aeterna, 'eternal', has the same feminine ending as Rōma. The poet Tibullus was already calling Rome the 'eternal city' around 20 BC.",
 "Hadrian built a huge temple to Venus and Roma Aeterna beside the Forum. Rome is still called the Eternal City.",
 None,'Coin legend (denarius of Septimius Severus)','—','AD 193–211','https://finds.org.uk/','verified','Legend read on the coin (Portable Antiquities Scheme record 2018T742). Tibullus 2.5.23: aeternae … urbis.',
 'Rōma|Rōma|Rome|nom. sg. f.; aeterna|aeternus|eternal|nom. sg. f.',
 ['nominative'],['adjective_agreement'],'romaaeterna','Roma Aeterna',WP+'Roma_Aeterna',subtype='coin',raw=('ROMA AETERNA','Coin legend (PAS 2018T742)'))

# ---------------- UNIT 2: Familia ----------------
K('q-catullus-sirmio','quote','republic',2,'Salvē, ō venusta Sirmiō','Greetings, lovely Sirmio',
 "Catullus wrote this poem when he came home to his family's villa at Sirmio, a peninsula on Lake Garda, after a year's service in Bithynia. Nothing, he says, is sweeter than resting in your own bed after a long journey. Sirmiō is in the vocative, because he speaks to the place, and venusta, 'lovely', agrees with it.",
 "The large Roman villa at the tip of the peninsula is called the Grotte di Catullo, though it was built after his time. In the same poem he calls Sirmio the 'little eye' of all peninsulas and islands.",
 'Catullus','Catullus, Carmina','31.12','about 56 BC',LL+'catullus.shtml','verified',None,
 'Salvē|salveō|greetings, hello|imperative; ō|ō|O|interj.; venusta|venustus|lovely, charming|voc. sg. f.; Sirmiō|Sirmiō|Sirmio|voc. sg. f.',
 ['vocative'],['imperative'],'sirmio','Sirmione',WP+'Sirmione')
K('v-paterfamilias','vocab','republic',2,'Paterfamiliās fīliōs fīliāsque vocat.','The father of the family calls his sons and daughters.',
 "The paterfamiliās was the oldest living male of a Roman family, with legal power over his children and grandchildren, even when they were grown up. In early law he could sell them or even put them to death, though this was rare. Fīliōs and fīliās are accusative plurals, joined by -que, 'and'.",
 "Familiās is an old genitive ending kept only in this phrase. A Roman familia also included the household's slaves.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Paterfamiliās|paterfamiliās|father of the family|nom. sg. m.; fīliōs|fīlius|sons|acc. pl. m.; fīliās|fīlia|daughters|acc. pl. f.; -que|-que|and|enclitic conj.; vocat|vocō|calls|3rd sg. pres.',
 ['accusative','enclitic_que'],['present_tense'],'family','Pater familias',WP+'Pater_familias',subtype='vocab')
K('v-avus-avia','vocab','republic',2,'Avus et avia nepōtem amant.','Grandfather and grandmother love their grandson.',
 "Avus and avia are 'grandfather' and 'grandmother', and nepōs is 'grandson'. Noble families kept wax masks of their ancestors in the atrium and carried them in funeral processions. Nepōtem is the accusative object of amant. Later nepōs also meant 'nephew', which is how English got nepotism, from popes favouring their 'nephews'.",
 "Avunculus, 'little grandfather', meant a mother's brother, and gives English avuncular. A great-grandfather was a proavus.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Avus|avus|grandfather|nom. sg. m.; et|et|and|conj.; avia|avia|grandmother|nom. sg. f.; nepōtem|nepōs|grandson|acc. sg. m.; amant|amō|love|3rd pl. pres.',
 ['accusative','nominative'],['present_tense'],'avus','Roman funerary practices',WP+'Roman_funerary_practices',subtype='vocab')
K('q-cicero-tulliola','quote','republic',2,'Tulliola, dēliciolae nostrae, tuum mūnusculum flāgitat.','Little Tullia, our darling, is demanding your little present.',
 "Cicero ends a letter to his best friend Atticus with family news. His daughter Tullia, then about eleven, was pestering Atticus for a promised gift and calling on her father as guarantor. Tulliola, dēliciolae and mūnusculum are all diminutives, with affectionate endings in -ola and -ulum. Tuum mūnusculum is the accusative object.",
 "Cicero jokes that he would rather deny the debt than pay it. Tullia died after childbirth in 45 BC, and his grief fills his letters for months.",
 'Cicero','Cicero, Epistulae ad Atticum','1.8.3','67 BC',LL+'cicero/att1.shtml','verified',None,
 'Tulliola|Tulliola|little Tullia|nom. sg. f.; dēliciolae|dēliciolae|darling, little delight|nom. pl. f.; nostrae|noster|our|nom. pl. f.; tuum|tuus|your|acc. sg. n.; mūnusculum|mūnusculum|little present|acc. sg. n.; flāgitat|flāgitō|demands|3rd sg. pres.',
 ['accusative','possessive_adjectives'],['present_tense'],'tulliola','Tullia (daughter of Cicero)',WP+'Tullia_(daughter_of_Cicero)')

# ---------------- UNIT 3: Legio ----------------
K('v-aquilifer','vocab','empire',3,'Aquilifer aquilam portat; mīlitēs aquilam dēfendunt.','The eagle-bearer carries the eagle; the soldiers defend the eagle.',
 "Every legion carried a gilded eagle, the aquila, on a pole. Its bearer, the aquilifer, marched with the first cohort, and losing the eagle in battle was the worst disgrace a legion could suffer. In both halves aquilam is the accusative object; the first verb is singular and the second plural.",
 "Augustus won back the eagles lost by Crassus at Carrhae through a treaty with Parthia in 20 BC. Aquilifer joins aquila with ferō, 'carry'.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Aquilifer|aquilifer|eagle-bearer|nom. sg. m.; aquilam|aquila|eagle|acc. sg. f.; portat|portō|carries|3rd sg. pres.; mīlitēs|mīles|soldiers|nom. pl. m.; aquilam|aquila|eagle|acc. sg. f.; dēfendunt|dēfendō|defend|3rd pl. pres.',
 ['third_person_plural','accusative'],[],'aquilifer','Aquilifer',WP+'Aquilifer',subtype='vocab')
K('v-equites-pedites','vocab','empire',3,'Equitēs equōs cūrant; peditēs ambulant.','The horsemen look after the horses; the foot soldiers walk.',
 "A Roman army had foot soldiers, peditēs, and horsemen, equitēs. In the imperial army most cavalry served in auxiliary units recruited from provincials such as Gauls, Thracians and Batavians. Both verbs end in -nt, the third person plural.",
 "Equitēs was also the name of Rome's wealthy 'knights', the class below the senators. Pedes comes from pēs, 'foot', like English pedestrian.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Equitēs|eques|horsemen|nom. pl. m.; equōs|equus|horses|acc. pl. m.; cūrant|cūrō|look after|3rd pl. pres.; peditēs|pedes|foot soldiers|nom. pl. m.; ambulant|ambulō|walk|3rd pl. pres.',
 ['third_person_plural','present_tense'],[],'equites','Roman cavalry',WP+'Roman_cavalry',subtype='vocab')

# ---------------- UNIT 4: Forum ----------------
K('i-amymone','artifact','empire',4,'HIC SITA EST AMYMONE MARCI … — Hīc sita est Amymōnē Mārcī, optima et pulcherrima, lānifica, pia, pudīca, frūgī, casta, domiseda.','Here lies Amymone, Marcus’s, the best and most beautiful, a wool-spinner, dutiful, modest, thrifty, chaste, a stay-at-home.',
 "This epitaph from Rome lists the virtues Romans praised in a woman of the household. Mārcī is a genitive, 'of Marcus', and probably means his wife, though it could mean a slave or freedwoman. Every adjective agrees with Amymōnē in the feminine nominative. Spinning wool, lānifica, was the classic sign of a good housewife, as on the earlier epitaph of Claudia.",
 "Optima and pulcherrima are superlatives, 'best' and 'most beautiful'. Domiseda, 'home-sitting', is a rare word found almost only in epitaphs.",
 None,'Epitaph from Rome (CIL VI 11602)','—','imperial period',EDCS,'verified','Text checked in EDCS (EDCS-17201284, CIL VI 11602).',
 'Hīc|hīc|here|adv.; sita est|sinō|lies (is placed)|3rd sg. perf. pass.; Amymōnē|Amymōnē|Amymone|nom. sg. f.; Mārcī|Mārcus|of Marcus|gen. sg. m.; optima|optimus|best|nom. sg. f.; et|et|and|conj.; pulcherrima|pulcher|most beautiful|nom. sg. f.; lānifica|lānificus|wool-spinning|nom. sg. f.; pia|pius|dutiful|nom. sg. f.; pudīca|pudīcus|modest|nom. sg. f.; frūgī|frūgī|thrifty|indecl. adj.; casta|castus|chaste|nom. sg. f.; domiseda|domiseda|staying at home|nom. sg. f.',
 ['genitive','adjective_agreement'],['superlative','perfect_passive'],'amymone','Women in ancient Rome',WP+'Women_in_ancient_Rome',subtype='inscription',raw=('HIC SITA EST AMYMONE MARCI OPTIMA ET PULCHERRIMA LANIFICA PIA PUDICA FRUGI CASTA DOMISEDA','EDCS-17201284 (CIL VI 11602)'),related=['i-claudia-lanam'])
K('q-juvenal-reverentia','quote','empire',4,'Maxima dēbētur puerō reverentia.','The greatest respect is owed to a child.',
 "In his fourteenth satire Juvenal argues that children copy their parents' vices, so a father must watch what he does at home. Puerō is a dative, 'to a boy', and reverentia is the subject of dēbētur, 'is owed'. Maxima, 'greatest', agrees with reverentia.",
 "Juvenal goes on: if you are planning something shameful, think of your infant son. Teachers and child-welfare campaigners still quote the line.",
 'Juvenal','Juvenal, Saturae','14.47','early 2nd century AD',LL+'juvenal/14.shtml','verified',None,
 'Maxima|maximus|greatest|nom. sg. f.; dēbētur|dēbeō|is owed|3rd sg. pres. pass.; puerō|puer|to a boy, child|dat. sg. m.; reverentia|reverentia|respect|nom. sg. f.',
 ['dative','adjective_agreement'],['passive_voice','superlative'],'reverentia','Juvenal',WP+'Juvenal')
K('q-cicero-pax','quote','republic',4,'Pāx est tranquilla lībertās.','Peace is liberty in tranquillity.',
 "In his Second Philippic, a pamphlet against Mark Antony, Cicero insists that peace bought with slavery is no peace at all. The adjective tranquilla agrees with the feminine noun lībertās. He goes on to call slavery the worst of all evils, to be resisted by war or even by death.",
 "Antony had Cicero killed in December 43 BC, and his head and hands were nailed up on the speakers' platform in the Forum. Pāx gives English peace and pacify.",
 'Cicero','Cicero, Philippicae','2.113','44 BC',LL+'cicero/phil2.shtml','verified',None,
 'Pāx|pāx|peace|nom. sg. f.; est|sum|is|3rd sg. pres.; tranquilla|tranquillus|calm, tranquil|nom. sg. f.; lībertās|lībertās|freedom, liberty|nom. sg. f.',
 ['sum','adjective_agreement'],[],'pax','Philippicae',WP+'Philippicae')

# ---------------- UNIT 5: Dei ----------------
K('q-plautus-lar','quote','republic',5,'Ego Lar sum familiāris ex hāc familiā','I am the household god of this family',
 "Plautus' comedy The Pot of Gold opens with the family's household god, the Lar familiāris, stepping out of the house to explain the plot. He says he has guarded this house, and the gold hidden in it, for generations. Ex hāc familiā uses the ablative after ex. Every Roman house had a small shrine to the Lar, the larārium.",
 "Molière based his comedy The Miser on this play. Familiāris first meant 'belonging to the household', and gives English familiar.",
 'Plautus (the Lar in the prologue)','Plautus, Aulularia','Prologue 2','early 2nd century BC',LL+'plautus/aulularia.shtml','verified','Spoken by the Lar familiaris in the prologue.',
 'Ego|ego|I|nom. sg.; Lar|Lar|household god|nom. sg. m.; sum|sum|am|1st sg. pres.; familiāris|familiāris|of the household|nom. sg. m.; ex|ex|from, of|prep. + abl.; hāc|hic|this|abl. sg. f.; familiā|familia|family, household|abl. sg. f.',
 ['sum','prep_ablative','third_declension'],['demonstratives','personal_pronouns'],'lar','Lares',WP+'Lares',related=['l-lares'])
K('q-apuleius-isis','quote','empire',5,'Ēn adsum tuīs commōta, Lūcī, precibus, rērum nātūrae parēns','Here I am, Lucius, moved by your prayers, mother of the natural world',
 "At the climax of Apuleius' novel The Golden Ass, Lucius, who has been turned into a donkey, prays to the moon, and the Egyptian goddess Isis rises from the sea to save him. Precibus, 'by prayers', is an ablative, and tuīs agrees with it from earlier in the line. Lūcī is the vocative of Lūcius, and parēns, 'parent', is a third-declension noun; rērum nātūrae, 'of the nature of things', is a genitive.",
 "Lucius regains human shape by eating roses carried in a procession of Isis, and then becomes her initiate. The Golden Ass is the only Latin novel to survive complete.",
 'Apuleius (speech of Isis)','Apuleius, Metamorphoses','11.5','2nd century AD',LL+'apuleius/apuleius11.shtml','verified','Spoken by Isis in the novel.',
 'Ēn|ēn|here, behold|interj.; adsum|adsum|I am here|1st sg. pres.; tuīs|tuus|your|abl. pl. f.; commōta|commoveō|moved|perf. pass. part. nom. sg. f.; Lūcī|Lūcius|Lucius|voc. sg. m.; precibus|prex|by prayers|abl. pl. f.; rērum|rēs|of things|gen. pl. f.; nātūrae|nātūra|of nature|gen. sg. f.; parēns|parēns|parent, mother|nom. sg. f.',
 ['ablative_means','third_declension','vocative'],['participle'],'isis','The Golden Ass',WP+'The_Golden_Ass')
K('q-cato-mars','quote','republic',5,'Mārs pater, tē precor quaesōque','Father Mars, I pray and beseech you',
 "Cato's farming manual records the prayer a landowner said while leading a pig, a sheep and a bull around his fields before sacrificing them. In early Rome, Mars protected farmland as well as armies. Mārs pater is vocative, tē is the accusative object, and -que joins the two verbs.",
 "The prayer asks Mars to keep away disease, drought and storms, and to let crops, flocks and household thrive. It is one of the oldest Latin prayers to survive.",
 'Cato the Elder (farm prayer)','Cato, De agri cultura','141.2','about 160 BC',LL+'cato/cato.agri.html','verified','A traditional prayer recorded by Cato.',
 'Mārs|Mārs|Mars|voc. sg. m.; pater|pater|father|voc. sg. m.; tē|tū|you|acc. sg.; precor|precor|I pray|1st sg. pres.; quaesō|quaesō|I beseech|1st sg. pres.; -que|-que|and|enclitic conj.',
 ['vocative','enclitic_que','first_person'],['personal_pronouns','deponent'],'mars','Mars (mythology)',WP+'Mars_(mythology)')

# ---------------- UNIT 6: Imperium ----------------
K('q-resgestae-auctoritate','quote','empire',6,'Post id tempus auctōritāte omnibus praestitī.','After that time I surpassed everyone in influence.',
 "Near the end of his Res Gestae, Augustus describes the settlement of 27 BC, when he 'handed back' the state to the Senate and people and received the name Augustus. He claims he had no more legal power than his colleagues, only more auctōritās, personal prestige. Praestitī is a perfect tense, auctōritāte an ablative, 'in influence', and omnibus a dative after the verb.",
 "The sentence continues: 'but I had no more power than the others who were my colleagues in each magistracy.' Historians still argue about how honest this claim was.",
 'Augustus','Res Gestae Divi Augusti','34.3','AD 14',LL+'resgestae.html','verified',None,
 'Post|post|after|prep. + acc.; id|is|that|acc. sg. n.; tempus|tempus|time|acc. sg. n.; auctōritāte|auctōritās|in influence, prestige|abl. sg. f.; omnibus|omnis|everyone|dat. pl. m.; praestitī|praestō|I surpassed|1st sg. perf.',
 ['perfect_tense','ablative','dative'],[],'rgankara','Res Gestae Divi Augusti',WP+'Res_Gestae_Divi_Augusti')
K('q-eutropius-dacia','quote','empire',6,'Urbēs trāns Rhēnum in Germāniā reparāvit. Dāciam Decibalō victō subēgit.','He restored cities across the Rhine in Germany. He defeated Decebalus and conquered Dacia.',
 "Eutropius' short history of Rome sums up Trajan's conquests: he restored towns beyond the Rhine, defeated the Dacian king Decebalus, and made Dacia a province in AD 106. Reparāvit and subēgit are both perfect tenses. Decibalō victō, 'with Decebalus defeated', is an ablative absolute.",
 "Trajan's Column in Rome tells the story of the Dacian Wars in a spiral relief. Romania takes its name, and its Romance language, from the Roman settlers.",
 'Eutropius','Eutropius, Breviarium','8.2','AD 369',LL+'eutropius/eutropius8.shtml','verified',None,
 'Urbēs|urbs|cities|acc. pl. f.; trāns|trāns|across|prep. + acc.; Rhēnum|Rhēnus|the Rhine|acc. sg. m.; in|in|in|prep. + abl.; Germāniā|Germānia|Germany|abl. sg. f.; reparāvit|reparō|he restored|3rd sg. perf.; Dāciam|Dācia|Dacia|acc. sg. f.; Decibalō|Decibalus|Decebalus|abl. sg. m.; victō|vincō|defeated|perf. pass. part. abl. sg. m.; subēgit|subigō|he conquered|3rd sg. perf.',
 ['perfect_tense','in_ablative','accusative'],['ablative_absolute'],'dacia',"Trajan's Dacian Wars",WP+"Trajan's_Dacian_Wars")
K('q-eutropius-felicior','quote','late_antiquity',6,'Fēlīcior Augustō, melior Trāiānō!','Luckier than Augustus, better than Trajan!',
 "Eutropius says that even in his own day, 250 years after Trajan, the Senate greeted each new emperor with this wish. Augustus stood for good fortune and Trajan for goodness, so the hope was that the new ruler would outdo them both. Fēlīcior and melior are comparatives, and Augustō and Trāiānō are ablatives meaning 'than'.",
 "The Senate gave Trajan the official title Optimus, 'the Best'. His ashes were placed in the base of his column.",
 'Roman Senate (acclamation)','Eutropius, Breviarium','8.5.3','AD 369',LL+'eutropius/eutropius8.shtml','verified','Eutropius reports the acclamation as still in use in his time.',
 'Fēlīcior|fēlīx|luckier|comp. nom. sg. m.; Augustō|Augustus|than Augustus|abl. sg. m.; melior|bonus|better|comp. nom. sg. m.; Trāiānō|Trāiānus|than Trajan|abl. sg. m.',
 ['ablative'],['comparative','ablative_of_comparison'],'trajan','Trajan',WP+'Trajan')

# ---------------- UNIT 7: Poetae ----------------
K('q-martial-fidentine','quote','empire',7,'Quem recitās meus est, ō Fīdentīne, libellus: sed male cum recitās, incipit esse tuus.','The little book you are reciting is mine, Fidentinus: but when you recite it badly, it starts to be yours.',
 "Martial accuses a certain Fidentinus of reciting Martial's poems in public as his own. The joke turns on the possessives: the book is meus, 'mine', but when Fidentinus recites it badly, it begins to be tuus, 'yours'. Ō Fīdentīne is a vocative, and recitās is second person singular.",
 "In another poem (1.52) Martial calls a poem-thief a plagiārius, 'kidnapper', the origin of English plagiarist.",
 'Martial','Martial, Epigrammata','1.38','about AD 86',LL+'martial/mart1.shtml','verified',None,
 'Quem|quī|which|acc. sg. m.; recitās|recitō|you recite|2nd sg. pres.; meus|meus|mine|nom. sg. m.; est|sum|is|3rd sg. pres.; ō|ō|O|interj.; Fīdentīne|Fīdentīnus|Fidentinus|voc. sg. m.; libellus|libellus|little book|nom. sg. m.; sed|sed|but|conj.; male|male|badly|adv.; cum|cum|when|conj.; recitās|recitō|you recite|2nd sg. pres.; incipit|incipiō|it begins|3rd sg. pres.; esse|sum|to be|pres. inf.; tuus|tuus|yours|nom. sg. m.',
 ['vocative','possessive_adjectives','personal_pronouns'],['relative_clause','infinitive'],'martialms','Martial',WP+'Martial')
K('q-catullus-obdura','quote','republic',7,'At tū, Catulle, dēstinātus obdūrā.','But you, Catullus, be resolute and hold firm.',
 "In poem 8 Catullus orders himself to stop loving a girl who no longer wants him. He lists the kisses and pleasures she will now miss, then ends with this command to himself. Obdūrā is an imperative, tū the personal pronoun, and Catulle the vocative of Catullus.",
 "The poem begins Miser Catulle, dēsinās ineptīre, 'Poor Catullus, stop being a fool'. The girl is usually taken to be Lesbia.",
 'Catullus','Catullus, Carmina','8.19','mid-1st century BC',LL+'catullus.shtml','verified',None,
 'At|at|but|conj.; tū|tū|you|nom. sg.; Catulle|Catullus|Catullus|voc. sg. m.; dēstinātus|dēstinō|resolute, determined|perf. pass. part. nom. sg. m.; obdūrā|obdūrō|hold firm|imperative sg.',
 ['imperative','personal_pronouns','vocative'],['participle'],'lesbia','Catullus 8',WP+'Catullus_8')
K('q-ovid-phaethon','quote','empire',7,'Mediō tūtissimus ībis.','You will go most safely in the middle.',
 "The Sun god advises his son Phaethon before letting him drive the chariot of the sun: not too high, not too low. Ībis is the future of eō, 'go', and mediō, 'by the middle', is an ablative. Phaethon could not control the horses, scorched the earth and was struck down by Jupiter's thunderbolt.",
 "The line became a proverb for moderation. Ovid says the Ethiopians' dark skin and the deserts of Libya came from Phaethon's wild ride.",
 'Ovid (speech of the Sun)','Ovid, Metamorphoses','2.137','AD 8',LL+'ovid/ovid.met2.shtml','verified','Spoken by the Sun god to Phaethon.',
 'Mediō|medius|by the middle way|abl. sg. n.; tūtissimus|tūtus|most safely (safest)|superl. nom. sg. m.; ībis|eō|you will go|2nd sg. fut.',
 ['future_tense','ablative'],['superlative'],'phaethon','Phaethon',WP+'Phaethon')

# ---------------- UNIT 8: Philosophi ----------------
K('q-livy-maharbal','quote','republic',8,'Vincere scīs, Hannibal; victōriā ūtī nescīs.','You know how to win, Hannibal; you do not know how to use a victory.',
 "After the Roman disaster at Cannae in 216 BC, Hannibal's cavalry commander Maharbal urged him to march on Rome at once. When Hannibal hesitated, Maharbal said these words. Vincere and ūtī are infinitives completing scīs and nescīs, and victōriā is ablative because ūtor takes the ablative. Livy adds that the delay of that one day saved the city.",
 "Hannibal stayed in Italy for thirteen more years but never took Rome. Historians still argue about whether he could have.",
 'Maharbal (in Livy)','Livy, Ab urbe condita','22.51.4','about 25 BC',LL+'livy/liv.22.shtml','verified','Livy attributes the words to Maharbal.',
 'Vincere|vincō|to win|pres. inf.; scīs|sciō|you know (how)|2nd sg. pres.; Hannibal|Hannibal|Hannibal|voc. sg. m.; victōriā|victōria|victory|abl. sg. f.; ūtī|ūtor|to use|pres. inf. (deponent); nescīs|nesciō|you do not know|2nd sg. pres.',
 ['infinitive','vocative'],['deponent','ablative_with_deponent'],'hannibalalps','Maharbal',WP+'Maharbal',related=['q-hannibal-ad-portas'])
K('q-seneca-animum','quote','empire',8,'Animum dēbēs mūtāre, nōn caelum.','You need to change your mind, not your sky.',
 "A friend complained to Seneca that long travels had not cured his gloom. Seneca answers that you take yourself with you wherever you go, so it is your mind, not your sky, that must change. Mūtāre is an infinitive completing dēbēs, 'you ought', and animum and caelum are both its objects.",
 "Seneca is echoing Horace's line caelum, nōn animum mūtant. He also quotes Socrates: why be surprised that travel does you no good, when you carry yourself around with you?",
 'Seneca the Younger','Seneca, Epistulae morales','28.1','about AD 63',LL+'sen/seneca.ep3.shtml','verified',None,
 'Animum|animus|mind|acc. sg. m.; dēbēs|dēbeō|you ought, must|2nd sg. pres.; mūtāre|mūtō|to change|pres. inf.; nōn|nōn|not|adv.; caelum|caelum|sky|acc. sg. n.',
 ['infinitive','accusative'],[],'ship','Epistulae Morales ad Lucilium',WP+'Epistulae_Morales_ad_Lucilium',related=['q-horace-caelum'])
K('q-seneca-difficilia','quote','empire',8,'Nōn quia difficilia sunt nōn audēmus, sed quia nōn audēmus difficilia sunt.','It is not because things are difficult that we do not dare; it is because we do not dare that they are difficult.',
 "Seneca argues that hardships are less heavy than we fear: our lack of nerve is what makes them hard. The sentence repeats its own words in reverse order, a pattern called chiasmus. Difficilia, 'difficult things', is a neuter plural adjective used as a noun.",
 "He offers Socrates as a model: poor, old and badly treated, yet never broken. Seneca wrote 124 letters to his friend Lucilius in his last years, about AD 62 to 65.",
 'Seneca the Younger','Seneca, Epistulae morales','104.26','about AD 64',LL+'sen/seneca.ep17-18.shtml','verified',None,
 'Nōn|nōn|not|adv.; quia|quia|because|conj.; difficilia|difficilis|difficult (things)|nom. pl. n.; sunt|sum|they are|3rd pl. pres.; nōn|nōn|not|adv.; audēmus|audeō|we dare|1st pl. pres.; sed|sed|but|conj.; quia|quia|because|conj.; nōn|nōn|not|adv.; audēmus|audeō|we dare|1st pl. pres.; difficilia|difficilis|difficult|nom. pl. n.; sunt|sum|they are|3rd pl. pres.',
 ['neuter_plural','present_tense','third_declension'],[],'seneca','Seneca the Younger',WP+'Seneca_the_Younger')
K('q-cicero-absurde','quote','republic',8,'Nihil tam absurdē dīcī potest quod nōn dīcātur ab aliquō philosophōrum.','Nothing can be said so absurd that it is not said by one of the philosophers.',
 "Cicero is mocking Pythagorean dream rules, such as avoiding beans before sleep. Nothing, he says, is so absurd that some philosopher has not said it. Dīcī is a passive infinitive after potest, and philosophōrum, 'of the philosophers', is a genitive of the whole.",
 "Descartes echoed the line in his Discourse on Method (1637). Cicero himself studied philosophy in Athens and Rhodes.",
 'Cicero','Cicero, De divinatione','2.119','44 BC',LL+'cicero/divinatione2.shtml','verified',None,
 'Nihil|nihil|nothing|nom. sg. n.; tam|tam|so|adv.; absurdē|absurdē|absurdly|adv.; dīcī|dīcō|to be said|pres. pass. inf.; potest|possum|can|3rd sg. pres.; quod|quī|that|nom. sg. n.; nōn|nōn|not|adv.; dīcātur|dīcō|is said|3rd sg. pres. pass. subj.; ab|ab|by|prep. + abl.; aliquō|aliquis|some, one|abl. sg. m.; philosophōrum|philosophus|of the philosophers|gen. pl. m.',
 ['possum_infinitive','genitive'],['passive_voice','subjunctive','relative_clause'],'academy','De Divinatione',WP+'De_Divinatione')
K('q-cicero-socrates-nihil','quote','republic',8,'… nihil sē scīre dīcat nisi id ipsum','… he says that he knows nothing except that very fact',
 "Cicero describes how Socrates argued: he affirmed nothing himself, refuted others, and said that he knew nothing except that one thing. Sē scīre, 'that he knows', is an indirect statement, an accusative with an infinitive after a verb of saying. The familiar English line 'I know that I know nothing' grew from passages like this one.",
 "In Plato's Apology Socrates says the oracle at Delphi called him the wisest man because he alone knew that he did not know. Cicero's Academica defends the sceptical school, which taught that certainty is impossible.",
 'Cicero (on Socrates)','Cicero, Academica','1.16','45 BC',LL+'cicero/acad.shtml','verified','Cicero reports Socrates\' method; not a direct quotation of Socrates.',
 'nihil|nihil|nothing|acc. sg. n.; sē|suī|that he|acc.; scīre|sciō|to know|pres. inf.; dīcat|dīcō|he says|3rd sg. pres. subj.; nisi|nisi|except|conj.; id|is|that|acc. sg. n.; ipsum|ipse|very, itself|acc. sg. n.',
 ['indirect_statement','infinitive'],['subjunctive'],'socrates','I know that I know nothing',WP+'I_know_that_I_know_nothing',related=['q-cicero-socrates-caelo'])
K('q-seneca-discendum','quote','empire',8,'Vīvere tōtā vītā discendum est.','Living has to be learned throughout one’s whole life.',
 "In On the Shortness of Life Seneca says that busy people never learn the hardest skill of all, which is how to live. It takes a whole lifetime to learn to live, he says, and, more surprisingly, to learn to die. Vīvere is an infinitive used as a noun, and tōtā vītā, 'throughout the whole of life', is an ablative of time.",
 "Seneca addressed the essay to Paulinus, the official in charge of Rome's grain supply. It opens by insisting that life is long enough, if we use it well.",
 'Seneca the Younger','Seneca, De brevitate vitae','7.3','about AD 49',LL+'sen/sen.brevita.shtml','verified',None,
 'Vīvere|vīvō|living, to live|pres. inf.; tōtā|tōtus|whole|abl. sg. f.; vītā|vīta|life|abl. sg. f.; discendum est|discō|must be learned|gerundive + est',
 ['infinitive_as_subject','ablative_of_time'],['gerundive'],'schoolrelief','De Brevitate Vitae (Seneca)',WP+'De_Brevitate_Vitae_(Seneca)')
K('q-horace-ridentem','quote','republic',8,'Rīdentem dīcere vērum quid vetat?','What stops someone from telling the truth while laughing?',
 "Horace defends the joking style of his Satires: what is to stop a person from speaking the truth with a smile? Teachers, he adds, give children cakes to coax them into learning their letters. Dīcere is an infinitive after vetat, and rīdentem, 'someone laughing', is a present participle used as a noun.",
 "Satirists and comedians ever since have claimed the same right to mix jokes with truth. Vērum, 'truth', is a neuter adjective used as a noun.",
 'Horace','Horace, Satires','1.1.24–25','about 35 BC',LL+'horace/serm1.shtml','verified',None,
 'Rīdentem|rīdeō|someone laughing|pres. part. acc. sg. m.; dīcere|dīcō|to tell|pres. inf.; vērum|vērum|the truth|acc. sg. n.; quid|quis|what|nom. sg. n.; vetat|vetō|forbids, stops|3rd sg. pres.',
 ['infinitive'],['present_participle','participle_as_noun'],'mask','Satires (Horace)',WP+'Satires_(Horace)')
K('q-cicero-errare','quote','republic',8,'Cuiusvīs hominis est errāre, nūllīus nisi īnsipientis in errōre persevērāre.','Anyone can make a mistake, but only a fool persists in error.',
 "Cicero had supported sending peace envoys to Mark Antony, then changed his mind and admitted his mistake to the Senate. Any human being may err, he says, but only a fool goes on in error. Errāre and persevērāre are infinitives used as subjects, and cuiusvīs hominis est means 'it is the mark of any person'.",
 "The proverb errāre hūmānum est, 'to err is human', grew from sayings like this one. Augustine added that to persist in error out of pride is devilish.",
 'Cicero','Cicero, Philippicae','12.5','43 BC',LL+'cicero/phil12.shtml','verified',None,
 'Cuiusvīs|quīvīs|of any|gen. sg. m.; hominis|homō|person|gen. sg. m.; est|sum|it is (the mark)|3rd sg. pres.; errāre|errō|to err|pres. inf.; nūllīus|nūllus|of no one|gen. sg. m.; nisi|nisi|except|conj.; īnsipientis|īnsipiēns|of a fool|gen. sg. m.; in|in|in|prep. + abl.; errōre|error|error|abl. sg. m.; persevērāre|persevērō|to persist|pres. inf.',
 ['infinitive_as_subject','genitive'],[],'antony','Philippicae',WP+'Philippicae')

# ---------------- UNIT 9: Crux ----------------
K('q-aug-civitates','quote','late_antiquity',9,'Fēcērunt itaque cīvitātēs duās amōrēs duo, terrēnam scīlicet amor suī usque ad contemptum Deī, caelestem vērō amor Deī usque ad contemptum suī.','Two loves, then, made two cities: the earthly city was made by love of self, even to contempt of God; the heavenly city by love of God, even to contempt of self.',
 "Augustine began the City of God after the Goths sacked Rome in 410, when pagans blamed the Christians for the disaster. His answer was that two 'cities' are always mixed together in this world, defined by what people love most. Fēcērunt is a perfect tense whose plural subject, amōrēs duo, comes at the end.",
 "The work took Augustine thirteen years, from 413 to 426, and fills 22 books. Medieval thinkers used it to reflect on Church and state.",
 'Augustine of Hippo','Augustine, De civitate Dei','14.28','about 420',LL+'augustine/civ14.shtml','verified',None,
 'Fēcērunt|faciō|made|3rd pl. perf.; itaque|itaque|therefore|adv.; cīvitātēs|cīvitās|cities|acc. pl. f.; duās|duo|two|acc. pl. f.; amōrēs|amor|loves|nom. pl. m.; duo|duo|two|nom. pl. m.; terrēnam|terrēnus|the earthly (city)|acc. sg. f.; scīlicet|scīlicet|namely|adv.; amor|amor|love|nom. sg. m.; suī|suī|of self|gen.; usque ad|usque ad|even to|prep. + acc.; contemptum|contemptus|contempt|acc. sg. m.; Deī|deus|of God|gen. sg. m.; caelestem|caelestis|the heavenly (city)|acc. sg. f.; vērō|vērō|but|adv.',
 ['perfect_tense','genitive','third_declension'],[],'cityofgod','The City of God',WP+'The_City_of_God')
K('q-vulg-petrus','quote','late_antiquity',9,'Tū es Petrus, et super hanc petram aedificābō ecclēsiam meam.','You are Peter, and on this rock I will build my church.',
 "Jesus gives Simon the name Peter, 'Rock', and promises to build his church on this rock. The pun works in Greek and in Latin, Petrus and petra. Aedificābō is a future tense, and hanc is a demonstrative agreeing with petram. The words run around the inside of the dome of Saint Peter's Basilica in letters about two metres high.",
 "Catholic tradition reads the verse as founding the papacy, while many Protestant readers take the rock to be Peter's faith. In the next verse Jesus gives Peter the keys of the kingdom of heaven, which is why Peter is shown holding keys.",
 'Jesus (Gospel of Matthew)','Vulgate, Matthew','16:18','Gospel about AD 80; Vulgate about 383',LL+'bible/matthew.shtml','verified',None,
 'Tū|tū|you|nom. sg.; es|sum|are|2nd sg. pres.; Petrus|Petrus|Peter|nom. sg. m.; et|et|and|conj.; super|super|on|prep. + acc.; hanc|hic|this|acc. sg. f.; petram|petra|rock|acc. sg. f.; aedificābō|aedificō|I will build|1st sg. fut.; ecclēsiam|ecclēsia|church|acc. sg. f.; meam|meus|my|acc. sg. f.',
 ['future_tense','demonstratives','personal_pronouns'],[],'keys','Saint Peter',WP+'Saint_Peter')
K('q-vulg-dominus-reget','quote','late_antiquity',9,'Dominus reget mē, et nihil mihi deerit.','The Lord will guide me, and I shall lack nothing.',
 "This is the opening of the psalm English readers know as 'The Lord is my shepherd': Psalm 23, numbered 22 in the Vulgate. Jerome's Latin follows the Greek translation, in which the Lord 'rules' or 'guides' me. Reget and deerit are future tenses, and mihi is a dative, 'to me'.",
 "Some Vulgate editions print regit, 'guides', in the present tense. The figure of the Good Shepherd carrying a sheep was one of the earliest Christian images.",
 'Psalm 23 (22)','Vulgate, Psalms','22:1','Vulgate about 390',LL+'bible/psalms.shtml','verified','The Latin Library (Stuttgart) text reads reget; the Clementine Vulgate reads regit.',
 'Dominus|dominus|the Lord|nom. sg. m.; reget|regō|will guide, rule|3rd sg. fut.; mē|ego|me|acc. sg.; et|et|and|conj.; nihil|nihil|nothing|nom. sg. n.; mihi|ego|to me|dat. sg.; deerit|dēsum|will be lacking|3rd sg. fut.',
 ['future_tense','personal_pronouns','dative'],[],'shepherd','Psalm 23',WP+'Psalm_23')
K('q-vulg-reddite','quote','late_antiquity',9,'Reddite ergō quae sunt Caesaris Caesarī, et quae sunt Deī Deō.','So give back to Caesar what is Caesar’s, and to God what is God’s.',
 "Opponents tried to trap Jesus by asking whether it was right to pay tax to the Roman emperor. He asked whose image was on a denarius, and when they said 'Caesar's', he gave this answer. Reddite is a plural imperative; Caesaris is genitive, 'Caesar's', and Caesarī is dative, 'to Caesar'.",
 "The coin was probably a silver denarius of the emperor Tiberius. The saying has been quoted ever since in debates about Church and state.",
 'Jesus (Gospel of Matthew)','Vulgate, Matthew','22:21','Gospel about AD 80; Vulgate about 383',LL+'bible/matthew.shtml','verified',None,
 'Reddite|reddō|give back|imperative pl.; ergō|ergō|therefore|adv.; quae|quī|the things which|nom. pl. n.; sunt|sum|are|3rd pl. pres.; Caesaris|Caesar|Caesar’s|gen. sg. m.; Caesarī|Caesar|to Caesar|dat. sg. m.; et|et|and|conj.; Deī|deus|God’s|gen. sg. m.; Deō|deus|to God|dat. sg. m.',
 ['imperative','genitive','dative'],['relative_clause'],'tribute',"Render unto Caesar",WP+'Render_unto_Caesar')
K('q-martin-miles','quote','late_antiquity',9,'Chrīstī ego mīles sum: pugnāre mihi nōn licet.','I am a soldier of Christ: it is not right for me to fight.',
 "Martin, a young officer in the Roman cavalry, said this to Julian, then Caesar and later emperor, on the eve of a battle in Gaul, as he refused his bonus. Accused of cowardice, he offered to stand unarmed in front of the battle line the next day. Pugnāre is an infinitive used as the subject of licet, 'it is allowed'.",
 "Martin later became bishop of Tours and one of the most popular saints in Europe. The story of him cutting his cloak in half for a beggar comes from the same biography.",
 'Martin of Tours (in Sulpicius Severus)','Sulpicius Severus, Vita Martini','4.3','about 396',LL+'sulpiciusseverusmartin.html','verified','Words given to Martin by his biographer Sulpicius Severus.',
 'Chrīstī|Chrīstus|of Christ|gen. sg. m.; ego|ego|I|nom. sg.; mīles|mīles|soldier|nom. sg. m.; sum|sum|am|1st sg. pres.; pugnāre|pugnō|to fight|pres. inf.; mihi|ego|for me|dat. sg.; nōn|nōn|not|adv.; licet|licet|it is allowed|impersonal 3rd sg. pres.',
 ['infinitive_as_subject','personal_pronouns','genitive'],['impersonal_verb'],'martin','Martin of Tours',WP+'Martin_of_Tours')
K('q-boethius-carmina','quote','late_antiquity',9,'Carmina quī quondam studiō flōrente perēgī, flēbilis heu maestōs cōgor inīre modōs.','I who once wrote poems with flourishing zeal am now, alas, forced in tears to take up sad measures.',
 "Boethius, a Roman senator and scholar, wrote the Consolation of Philosophy in prison while awaiting execution under the Gothic king Theodoric. The book opens with this lament: the poet who once wrote with eager joy must now sing sad songs. Cōgor, 'I am forced', is a present passive, and studiō flōrente is an ablative absolute.",
 "Lady Philosophy then appears and drives away the Muses of poetry from his bedside. The Consolation was one of the most widely read books of the Middle Ages, translated by King Alfred and by Chaucer.",
 'Boethius','Boethius, De consolatione philosophiae','1, metrum 1.1–2','about 524',WS+'De_philosophiae_consolatione/Liber_Primus','verified',None,
 'Carmina|carmen|poems|acc. pl. n.; quī|quī|who|nom. sg. m.; quondam|quondam|once|adv.; studiō|studium|zeal|abl. sg. n.; flōrente|flōreō|flourishing|pres. part. abl. sg. n.; perēgī|peragō|I completed, wrote|1st sg. perf.; flēbilis|flēbilis|in tears|nom. sg. m.; heu|heu|alas|interj.; maestōs|maestus|sad|acc. pl. m.; cōgor|cōgō|I am forced|1st sg. pres. pass.; inīre|ineō|to take up|pres. inf.; modōs|modus|measures, songs|acc. pl. m.',
 ['passive_voice','perfect_tense','present_participle'],['relative_clause','ablative_absolute'],'boethius','The Consolation of Philosophy',WP+'The_Consolation_of_Philosophy')
K('q-vulg-pulvis','quote','late_antiquity',9,'Pulvis es, et in pulverem revertēris.','You are dust, and to dust you shall return.',
 "God speaks these words to Adam as he and Eve are driven out of Eden. Pulvis is a third-declension noun, and revertēris is the future of a deponent verb, passive in form but active in meaning. On Ash Wednesday priests say a version of the line while marking foreheads with ashes.",
 "The same verse begins 'in the sweat of your face you shall eat bread', the source of the English 'by the sweat of your brow'.",
 'God to Adam (Genesis)','Vulgate, Genesis','3:19','Vulgate about 400',LL+'bible/genesis.shtml','verified',None,
 'Pulvis|pulvis|dust|nom. sg. m.; es|sum|you are|2nd sg. pres.; et|et|and|conj.; in|in|into|prep. + acc.; pulverem|pulvis|dust|acc. sg. m.; revertēris|revertor|you will return|2nd sg. fut. (deponent)',
 ['future_tense','third_declension'],['deponent'],'expulsion','Ash Wednesday',WP+'Ash_Wednesday')
K('q-patrick-ego','quote','late_antiquity',9,'Ego Patricius, peccātor rūsticissimus et minimus omnium fidēlium','I, Patrick, a sinner, very unlearned, the least of all the faithful',
 "Patrick opens his Confession, written in Ireland in the 5th century, with this humble description of himself. Kidnapped from Roman Britain by raiders at sixteen, he escaped years later, then returned to Ireland as a bishop. Rūsticissimus and minimus are superlatives, and omnium fidēlium, 'of all the faithful', is a genitive of the whole.",
 "His Latin is plain and sometimes awkward, and he was painfully aware of it. The Confession and a letter to the soldiers of Coroticus are the only writings surely by him.",
 'Saint Patrick','Patrick, Confessio','1','5th century','https://www.confessio.ie/etexts/confessio_latin','verified',None,
 'Ego|ego|I|nom. sg.; Patricius|Patricius|Patrick|nom. sg. m.; peccātor|peccātor|sinner|nom. sg. m.; rūsticissimus|rūsticus|very unlearned|superl. nom. sg. m.; et|et|and|conj.; minimus|parvus|least|superl. nom. sg. m.; omnium|omnis|of all|gen. pl. m.; fidēlium|fidēlis|of the faithful|gen. pl. m.',
 ['genitive','personal_pronouns','third_declension'],['superlative'],'patrick','Saint Patrick and his writings',WP+'Saint_Patrick')
K('q-venantius-vexilla','quote','early_medieval',9,'Vēxilla rēgis prōdeunt, fulget crucis mystērium','The banners of the King go forth; the mystery of the Cross shines out',
 "Venantius Fortunatus wrote this hymn in 569 for the arrival at Poitiers of a relic of the True Cross, sent from Constantinople to the former queen Radegund. The banners belong to Christ the King, and the Cross is pictured as a royal standard. Rēgis and crucis are third-declension genitives.",
 "The hymn is still sung in Holy Week. Dante parodies its first line at the bottom of Hell: Vēxilla rēgis prōdeunt īnfernī.",
 'Venantius Fortunatus','Venantius Fortunatus, Vexilla regis','1–2','569',LL+'venantius.html','verified',None,
 'Vēxilla|vēxillum|banners|nom. pl. n.; rēgis|rēx|of the King|gen. sg. m.; prōdeunt|prōdeō|go forth|3rd pl. pres.; fulget|fulgeō|shines|3rd sg. pres.; crucis|crux|of the Cross|gen. sg. f.; mystērium|mystērium|mystery|nom. sg. n.',
 ['genitive','third_declension','neuter_plural'],[],'vexilla','Vexilla Regis',WP+'Vexilla_Regis')

# ---------------- UNIT 10: Monachi ----------------
K('q-ora-et-labora','quote','early_medieval',10,'Ōrā et labōrā.','Pray and work.',
 "This short motto sums up the Benedictine way of life. The Rule of Benedict, written around 530, divides the monk's day between communal prayer, manual work and reading, but the motto itself is not in the Rule and became popular much later. Ōrā and labōrā are singular imperatives of first-conjugation verbs.",
 "The Rule does say that monks are truly monks when they live by the work of their own hands, like the apostles (chapter 48). Benedictine monasteries kept farming, copying books and brewing for centuries.",
 'Benedictine motto (traditional)','Traditional motto','—','later than the Rule; popularised in the 19th century',None,'traditional','Not found in the Rule of Benedict; a later summary of Benedictine life. Compare Regula 48.8: tunc vere monachi sunt si labore manuum suarum vivunt.',
 'Ōrā|ōrō|pray|imperative sg.; et|et|and|conj.; labōrā|labōrō|work|imperative sg.',
 ['imperative'],[],'monksfield','Ora et labora',WP+'Ora_et_labora',related=['q-ben-otiositas'])
K('q-bede-caedmon','quote','early_medieval',10,'Nunc laudāre dēbēmus auctōrem rēgnī caelestis','Now we must praise the Author of the heavenly kingdom',
 "Bede tells how Caedmon, a cowherd at Whitby Abbey who could not sing, dreamed that a stranger asked him to sing about the Creation. He woke able to compose religious poems in Old English, and Bede gives this Latin version of his first hymn. Laudāre is an infinitive after dēbēmus, 'we ought', and rēgnī caelestis is a genitive.",
 "The Old English original survives in the margins of early copies of Bede, making Caedmon the first English poet known by name. Bede admits that poetry cannot be translated word for word without losing its beauty.",
 'Caedmon (in Bede)','Bede, Historia ecclesiastica','4.24','731',LL+'bede/bede4.shtml','verified',"Bede's Latin paraphrase of Caedmon's Old English hymn.",
 'Nunc|nunc|now|adv.; laudāre|laudō|to praise|pres. inf.; dēbēmus|dēbeō|we ought, must|1st pl. pres.; auctōrem|auctor|author, creator|acc. sg. m.; rēgnī|rēgnum|of the kingdom|gen. sg. n.; caelestis|caelestis|heavenly|gen. sg. n.',
 ['infinitive','genitive','adjective_agreement'],[],'caedmon',"Cædmon's Hymn",WP+'C%C3%A6dmon%27s_Hymn')
K('q-arf-carolo','quote','early_medieval',12,'Carolō augustō, ā Deō corōnātō magnō et pācificō imperātōrī Rōmānōrum, vīta et victōria!','To Charles Augustus, crowned by God, great and peace-giving emperor of the Romans, life and victory!',
 "On Christmas Day 800, Pope Leo III placed a crown on Charlemagne's head in Saint Peter's in Rome, and the whole congregation shouted this acclamation. Every word describing Charlemagne is a dative agreeing with Carolō, 'to Charles'. Corōnātō, 'crowned', is a perfect passive participle, with ā Deō, 'by God'.",
 "Einhard claims Charlemagne said he would not have entered the church that day had he known the pope's plan. Rulers in the West went on claiming the title of emperor until 1806.",
 'Roman crowd (acclamation)','Annales regni Francorum','year 801','800 (event); about 830 (Annals)',LL+'annalesregnifrancorum.html','verified','The Annals enter the coronation under 801, as their year began at Christmas.',
 'Carolō|Carolus|to Charles|dat. sg. m.; augustō|augustus|Augustus|dat. sg. m.; ā|ab|by|prep. + abl.; Deō|deus|God|abl. sg. m.; corōnātō|corōnō|crowned|perf. pass. part. dat. sg. m.; magnō|magnus|great|dat. sg. m.; et|et|and|conj.; pācificō|pācificus|peace-giving|dat. sg. m.; imperātōrī|imperātor|emperor|dat. sg. m.; Rōmānōrum|Rōmānus|of the Romans|gen. pl. m.; vīta|vīta|life|nom. sg. f.; et|et|and|conj.; victōria|victōria|victory|nom. sg. f.',
 ['dative','adjective_agreement','participle'],[],'coronation','Coronation of Charlemagne',WP+'Coronation_of_Charlemagne')
K('q-ben-adiutorium','quote','early_medieval',10,'Deus, in adiūtōrium meum intende; Domine, ad adiuvandum mē festīnā.','O God, come to my aid; O Lord, make haste to help me.',
 "The Rule of Benedict orders each of the daily prayer services, the Hours, to begin with this verse from Psalm 69 (70). Monks sang it many times a day, from the night office before dawn to Compline at bedtime. Intende and festīnā are imperatives addressed to God, and Deus and Domine are vocatives.",
 "John Cassian, a century before Benedict, recommended repeating the verse constantly as a prayer against every temptation. It still opens the Hours in Catholic and Anglican services.",
 'Rule of Benedict (Psalm 69)','Regula Benedicti','18.1','about 530',LL+'benedict.html','verified','Psalm 69(70):2, prescribed by the Rule for the start of each Hour.',
 'Deus|deus|O God|voc. sg. m.; in|in|to, for|prep. + acc.; adiūtōrium|adiūtōrium|help, aid|acc. sg. n.; meum|meus|my|acc. sg. n.; intende|intendō|turn, attend|imperative sg.; Domine|dominus|O Lord|voc. sg. m.; ad|ad|for|prep. + acc.; adiuvandum|adiuvō|helping|gerund acc.; mē|ego|me|acc. sg.; festīnā|festīnō|hurry|imperative sg.',
 ['imperative','vocative','possessive_adjectives'],['gerund'],'benedict','Liturgy of the Hours',WP+'Liturgy_of_the_Hours')
K('q-histbrit-arthur','quote','early_medieval',10,'Tunc Arthur pugnābat contrā illōs in illīs diēbus cum rēgibus Brittonum, sed ipse erat dux bellōrum.','Then Arthur fought against them in those days with the kings of the Britons, but he himself was the leader of battles.',
 "The Historia Brittonum, a Welsh compilation from about 829, contains the earliest list of Arthur's battles against the Anglo-Saxons. It calls him not a king but dux bellōrum, 'leader of battles', and lists twelve victories ending at Mount Badon. Pugnābat and erat are imperfects, and illōs, illīs and ipse are demonstratives.",
 "Historians still debate whether Arthur existed at all. Camelot, Guinevere and the Round Table were added by later writers such as Geoffrey of Monmouth.",
 'Historia Brittonum (attributed to Nennius)','Historia Brittonum','56','about 829',LL+'histbrit.html','verified','The Latin Library text: sed ipse erat dux bellorum.',
 'Tunc|tunc|then|adv.; Arthur|Arthur|Arthur|nom. sg. m.; pugnābat|pugnō|fought|3rd sg. impf.; contrā|contrā|against|prep. + acc.; illōs|ille|them|acc. pl. m.; in|in|in|prep. + abl.; illīs|ille|those|abl. pl. m.; diēbus|diēs|days|abl. pl. m.; cum|cum|with|prep. + abl.; rēgibus|rēx|kings|abl. pl. m.; Brittonum|Britto|of the Britons|gen. pl. m.; sed|sed|but|conj.; ipse|ipse|he himself|nom. sg. m.; erat|sum|was|3rd sg. impf.; dux|dux|leader|nom. sg. m.; bellōrum|bellum|of battles|gen. pl. n.',
 ['imperfect','demonstratives','genitive'],[],'arthur','Historia Brittonum',WP+'Historia_Brittonum')
K('q-asser-codicem','quote','early_medieval',12,'Quisquis vestrum discere citius istum cōdicem possit, dabō illī illum.','Whichever of you can learn this book more quickly, I will give it to him.',
 "Asser, a Welsh monk at King Alfred's court, tells how Alfred's mother showed her sons a book of English poetry and promised it to whoever could learn it first. Young Alfred, drawn by a beautiful capital letter, had it read to him, recited it back, and won the book. Possit is a subjunctive in a 'whoever' clause, citius, 'faster', is a comparative adverb, and dabō is a future tense.",
 "Alfred learned Latin as an adult and translated books such as Boethius' Consolation into Old English. He is the only English-born king called 'the Great'.",
 'Osburh, mother of Alfred (in Asser)','Asser, Vita Alfredi','23','893',LL+'asserius.html','verified',"Words given to Alfred's mother by Asser.",
 'Quisquis|quisquis|whoever|nom. sg. m.; vestrum|vōs|of you|gen. pl.; discere|discō|to learn|pres. inf.; citius|citō|faster|comp. adv.; istum|iste|this|acc. sg. m.; cōdicem|cōdex|book|acc. sg. m.; possit|possum|can|3rd sg. pres. subj.; dabō|dō|I will give|1st sg. fut.; illī|ille|to him|dat. sg. m.; illum|ille|it|acc. sg. m.',
 ['subjunctive','comparative','future_tense','demonstratives'],[],'alfred','Alfred the Great',WP+'Alfred_the_Great')
K('q-te-deum','quote','late_antiquity',10,'Tē Deum laudāmus: tē Dominum cōnfitēmur.','We praise you as God: we acknowledge you to be the Lord.',
 "The Te Deum is an early Christian hymn of praise, probably from the 4th century. A medieval legend said Ambrose and Augustine improvised it together at Augustine's baptism in Milan in 387. Tē is the accusative object of both verbs; Deum and Dominum are accusatives in apposition to it, 'you as God', 'you as Lord', though the hymn is traditionally rendered 'We praise thee, O God'. Cōnfitēmur is a deponent verb, passive in form but active in meaning.",
 "Monks sang it at the end of the night office on feast days, and it is still sung at coronations and thanksgivings. Many scholars attribute it to Nicetas, bishop of Remesiana.",
 'Anonymous hymn (traditionally Ambrose and Augustine)','Te Deum','1–2','4th century',WS+'Te_Deum','traditional','The text is the standard liturgical one; the authorship of Ambrose and Augustine is legend.',
 'Tē|tū|you|acc. sg.; Deum|deus|as God|acc. sg. m. (in apposition to tē); laudāmus|laudō|we praise|1st pl. pres.; tē|tū|you|acc. sg.; Dominum|dominus|as Lord|acc. sg. m. (in apposition to tē); cōnfitēmur|cōnfiteor|we acknowledge|1st pl. pres. (deponent)',
 ['personal_pronouns','accusative','present_tense'],['deponent'],'ambrose','Te Deum',WP+'Te_Deum')
K('q-hrotsvit-clamor','quote','early_medieval',10,'Ego, Clāmor validus Gandeshemēnsis','I, the Strong Voice of Gandersheim',
 "Hrotsvit, a canoness of the abbey of Gandersheim in Saxony, wrote six Latin plays in the 10th century and is often called the first known woman dramatist. Here she translates her Saxon name, roughly 'strong voice', into Latin. She says she imitated the Roman playwright Terence, but to praise chaste women instead of shameless ones. Clāmor validus is nominative, with the adjective agreeing.",
 "Her works were rediscovered by the humanist Conrad Celtis and printed in 1501 with woodcuts by Albrecht Dürer and his circle.",
 'Hrotsvit of Gandersheim','Hrotsvit, Praefatio in comoedias','3','about 965',WS+'Praefatio_in_VI_comoedias_(Hrothsuita_Gandersheimensis)','verified','The Wikisource (Migne) text spells the place name Gandeishermensis; the usual reading is Gandeshemensis.',
 'Ego|ego|I|nom. sg.; Clāmor|clāmor|voice, shout|nom. sg. m.; validus|validus|strong|nom. sg. m.; Gandeshemēnsis|Gandeshemēnsis|of Gandersheim|nom. sg. m.',
 ['nominative','adjective_agreement','personal_pronouns'],[],'hrotsvit','Hrotsvitha',WP+'Hrotsvitha')

# ---------------- UNIT 11: Scholae ----------------
K('q-cb-in-taberna','quote','high_medieval',11,'In tabernā quandō sumus, nōn cūrāmus quid sit humus','When we are in the tavern, we do not care what the earth may be',
 "This drinking song from the Carmina Burana, a 13th-century collection of student and wandering-scholar poetry, goes on to toast everyone from the pope to the king. 'Not caring about the earth' means forgetting the grave that waits for everyone. The rhythm depends on word stress and rhyme, not long and short syllables as in classical verse. Quid sit is an indirect question with the subjunctive.",
 "Carl Orff set the poem to music in his Carmina Burana (1937). The manuscript was found at the abbey of Benediktbeuern in Bavaria in 1803.",
 'Carmina Burana (anonymous)','Carmina Burana','196.1','13th century',LL+'carm.bur.html','verified',None,
 'In|in|in|prep. + abl.; tabernā|taberna|tavern|abl. sg. f.; quandō|quandō|when|conj.; sumus|sum|we are|1st pl. pres.; nōn|nōn|not|adv.; cūrāmus|cūrō|we care|1st pl. pres.; quid|quis|what|nom. sg. n.; sit|sum|may be, is|3rd sg. pres. subj.; humus|humus|earth, ground|nom. sg. f.',
 ['indirect_question','subjunctive','in_ablative'],[],'buranus','Carmina Burana',WP+'Carmina_Burana',related=['q-archpoet-taberna'])
K('q-stabat-mater','quote','high_medieval',11,'Stābat māter dolōrōsa iūxtā crucem lacrimōsa, dum pendēbat fīlius','The grieving mother stood in tears beside the Cross, while her son was hanging there',
 "This medieval hymn pictures Mary standing at the foot of the Cross. It is often attributed to the Franciscan poet Jacopone da Todi, though the author is uncertain. Stābat and pendēbat are imperfects, and the rhyme of dolōrōsa and lacrimōsa is typical of medieval verse.",
 "Composers from Palestrina and Pergolesi to Rossini and Dvořák set it to music. Dolōrōsa gives the name of the Via Dolorosa in Jerusalem.",
 'Jacopone da Todi (attributed)','Stabat Mater','1.1–3','13th century',LL+'hymni.html','traditional','Authorship uncertain; often attributed to Jacopone da Todi.',
 'Stābat|stō|stood|3rd sg. impf.; māter|māter|mother|nom. sg. f.; dolōrōsa|dolōrōsus|grieving|nom. sg. f.; iūxtā|iūxtā|beside|prep. + acc.; crucem|crux|the Cross|acc. sg. f.; lacrimōsa|lacrimōsus|in tears|nom. sg. f.; dum|dum|while|conj.; pendēbat|pendeō|was hanging|3rd sg. impf.; fīlius|fīlius|son|nom. sg. m.',
 ['imperfect','adjective_agreement'],['dum_clause'],'pieta','Stabat Mater',WP+'Stabat_Mater')
K('q-abelard-o-quanta','quote','high_medieval',11,'Ō quanta, quālia sunt illa sabbata, quae semper celebrat superna cūria!','O how great, how wonderful are those sabbaths which the heavenly court celebrates forever!',
 "Peter Abelard wrote this hymn about the endless rest of heaven for Heloise and the nuns of the Paraclete, the convent he had founded. Quanta and quālia, 'how great, how wonderful', are exclamations, and quae begins a relative clause. Superna cūria, 'the heavenly court', pictures heaven as a royal court.",
 "Abelard wrote a whole hymn book for the Paraclete at Heloise's request. The two lovers are buried together in Père Lachaise cemetery in Paris.",
 'Peter Abelard','Abelard, O quanta qualia','1.1–2','about 1130s',LL+'hymni.html','verified',None,
 'Ō|ō|O|interj.; quanta|quantus|how great|nom. pl. n.; quālia|quālis|how wonderful|nom. pl. n.; sunt|sum|are|3rd pl. pres.; illa|ille|those|nom. pl. n.; sabbata|sabbata|sabbaths, days of rest|nom. pl. n.; quae|quī|which|acc. pl. n.; semper|semper|always|adv.; celebrat|celebrō|celebrates|3rd sg. pres.; superna|supernus|heavenly|nom. sg. f.; cūria|cūria|court|nom. sg. f.',
 ['relative_clause','neuter_plural','demonstratives'],[],'abelard','Peter Abelard',WP+'Peter_Abelard',related=['q-abelard-dubitando','q-heloise-meretrix'])
K('q-aquinas-quinque','quote','high_medieval',11,'Respondeō dīcendum quod Deum esse quīnque viīs probārī potest.','I answer that it must be said that God’s existence can be proved in five ways.',
 "In his Summa Theologiae Thomas Aquinas sets out five 'ways' to show that God exists, starting from motion, causes and the order of the world. Every article of the Summa follows the same scholastic pattern: objections, a quotation on the other side, the answer beginning respondeō dīcendum, and replies to each objection. Deum esse, 'that God exists', is an indirect statement, and probārī is a passive infinitive.",
 "Aquinas left the Summa unfinished in 1273 after an experience that, he said, made everything he had written seem like straw.",
 'Thomas Aquinas','Aquinas, Summa Theologiae','I, q. 2, a. 3','about 1268','https://www.corpusthomisticum.org/sth1002.html','verified',None,
 'Respondeō|respondeō|I answer|1st sg. pres.; dīcendum|dīcō|(it) must be said|gerundive n.; quod|quod|that|conj.; Deum|deus|God|acc. sg. m.; esse|sum|to be, exist|pres. inf.; quīnque|quīnque|five|indecl.; viīs|via|in ways|abl. pl. f.; probārī|probō|to be proved|pres. pass. inf.; potest|possum|can|3rd sg. pres.',
 ['indirect_statement','passive_voice','ablative_means'],['gerundive'],'aquinas','Five Ways (Aquinas)',WP+'Five_Ways_(Aquinas)',related=['q-aquinas-tardiloquum'])
K('q-bernard-stat-roma','quote','high_medieval',11,'Stat Rōma prīstina nōmine, nōmina nūda tenēmus.','Ancient Rome stands only in its name; we hold bare names.',
 "Bernard of Cluny's long satire On Contempt for the World, written around 1140, laments that all earthly glory fades away. Ancient Rome survives only as a name, and so do its heroes. Nōmine, 'in name', is an ablative of respect, and nōmina nūda is a neuter plural object with its adjective.",
 "Umberto Eco ended The Name of the Rose (1980) with a version reading rosa for Rōma: 'the rose of old stands only in its name'. The manuscripts differ on the word.",
 'Bernard of Cluny','Bernard of Cluny, De contemptu mundi','1.952','about 1140',LL+'bernardcluny1.html','verified','The Latin Library edition reads Roma; the version with rosa is famous from Eco.',
 'Stat|stō|stands|3rd sg. pres.; Rōma|Rōma|Rome|nom. sg. f.; prīstina|prīstinus|ancient, former|nom. sg. f.; nōmine|nōmen|in name|abl. sg. n. (respect); nōmina|nōmen|names|acc. pl. n.; nūda|nūdus|bare|acc. pl. n.; tenēmus|teneō|we hold|1st pl. pres.',
 ['ablative','neuter_plural','adjective_agreement'],[],'forum','Bernard of Cluny',WP+'Bernard_of_Cluny')

# ---------------- UNIT 12: Regna ----------------
K('q-arbroath','quote','late_medieval',12,'Nōn enim propter glōriam, dīvitiās aut honōrēs pugnāmus, sed propter lībertātem sōlummodo, quam nēmō bonus nisi simul cum vītā āmittit.','For we fight not for glory, riches or honours, but for freedom alone, which no good man gives up except with his life.',
 "In 1320 Scottish nobles sent this letter to Pope John XXII, asking him to recognise Robert the Bruce as king and Scotland as independent of England. Its most famous lines say they fight not for glory or wealth, but for freedom alone. Quam begins a relative clause referring back to lībertātem.",
 "Some historians see the Declaration as an early statement that a king rules with the consent of his people. Its date, 6 April, is celebrated as Tartan Day in the United States.",
 'Scottish barons (Declaration of Arbroath)','Declaration of Arbroath','—','1320',LL+'arbroath.html','verified','The Latin Library text has the medieval spellings set and diuicias; the card uses sed and dīvitiās.',
 'Nōn|nōn|not|adv.; enim|enim|for|conj.; propter|propter|for, on account of|prep. + acc.; glōriam|glōria|glory|acc. sg. f.; dīvitiās|dīvitiae|riches|acc. pl. f.; aut|aut|or|conj.; honōrēs|honor|honours|acc. pl. m.; pugnāmus|pugnō|we fight|1st pl. pres.; sed|sed|but|conj.; lībertātem|lībertās|freedom|acc. sg. f.; sōlummodo|sōlummodo|only|adv.; quam|quī|which|acc. sg. f.; nēmō|nēmō|no one|nom. sg. m.; bonus|bonus|good|nom. sg. m.; nisi|nisi|except|conj.; simul|simul|together|adv.; cum|cum|with|prep. + abl.; vītā|vīta|life|abl. sg. f.; āmittit|āmittō|loses, gives up|3rd sg. pres.',
 ['relative_clause','accusative','first_person'],[],'arbroath','Declaration of Arbroath',WP+'Declaration_of_Arbroath')
K('q-kempis-homo','quote','late_medieval',12,'Homō prōpōnit, sed Deus dispōnit.','Man proposes, but God disposes.',
 "The Imitation of Christ, a book of spiritual advice usually attributed to Thomas à Kempis, became one of the most widely read Christian books after the Bible. Here it reminds readers that their plans depend on God. Prōpōnit and dispōnit, 'proposes' and 'disposes', are compounds of pōnō, 'put'.",
 "The saying echoes Proverbs 16:9: the heart of a man plans his way, but the Lord directs his steps. It is still a common proverb in many languages.",
 'Thomas à Kempis','Thomas à Kempis, De imitatione Christi','1.19.2','about 1420',LL+'kempis/kempis1.shtml','verified',None,
 'Homō|homō|man, a person|nom. sg. m.; prōpōnit|prōpōnō|proposes|3rd sg. pres.; sed|sed|but|conj.; Deus|deus|God|nom. sg. m.; dispōnit|dispōnō|disposes, arranges|3rd sg. pres.',
 ['present_tense','third_conjugation','third_declension'],[],'kempis1','The Imitation of Christ',WP+'The_Imitation_of_Christ',related=['q-kempis-transit'])
K('q-kempis-nesciri','quote','late_medieval',12,'Amā nescīrī, et prō nihilō reputārī.','Love to be unknown, and to be counted as nothing.',
 "The Imitation advises anyone who wants truly useful learning to love being unknown and thought of as nothing. It warns against scholars who seek knowledge in order to be admired. Nescīrī and reputārī are passive infinitives after the imperative amā.",
 "The book came from the Devotio Moderna, a Dutch movement of religious renewal. Its first chapter says it is better to feel sorrow for sin than to know how to define it.",
 'Thomas à Kempis','Thomas à Kempis, De imitatione Christi','1.2.3','about 1420',LL+'kempis/kempis1.shtml','verified',None,
 'Amā|amō|love|imperative sg.; nescīrī|nesciō|to be unknown|pres. pass. inf.; et|et|and|conj.; prō|prō|as|prep. + abl.; nihilō|nihil|nothing|abl. sg. n.; reputārī|reputō|to be counted|pres. pass. inf.',
 ['imperative','passive_voice','infinitive'],[],'kempis2','Devotio Moderna',WP+'Devotio_Moderna')
K('q-debury-magistri','quote','late_medieval',12,'Hī sunt magistrī quī nōs īnstruunt sine virgīs et ferulā.','These are the teachers who instruct us without rods or cane.',
 "Richard de Bury, bishop of Durham and a passionate book collector, praises books as teachers who instruct us without rods or cane, without angry words, and without charging fees. Quī begins a relative clause describing magistrī. His Philobiblon, 'Love of Books', also scolds readers who eat over their books or mark them with dirty fingernails.",
 "A chronicler claimed de Bury owned more books than all the other bishops of England. He meant to leave them to Durham College, Oxford, but most were sold after his death to pay his debts.",
 'Richard de Bury','Richard de Bury, Philobiblon','1','1345',LL+'debury.html','verified',None,
 'Hī|hic|these|nom. pl. m.; sunt|sum|are|3rd pl. pres.; magistrī|magister|teachers|nom. pl. m.; quī|quī|who|nom. pl. m.; nōs|nōs|us|acc. pl.; īnstruunt|īnstruō|instruct|3rd pl. pres.; sine|sine|without|prep. + abl.; virgīs|virga|rods|abl. pl. f.; et|et|and|conj.; ferulā|ferula|cane|abl. sg. f.',
 ['relative_clause','prep_ablative','demonstratives'],[],'debury','Philobiblon',WP+'Philobiblon')
K('q-dante-nobilior','quote','late_medieval',12,'Hārum quoque duārum nōbilior est vulgāris.','Of these two, the vernacular is the nobler.',
 "In On Eloquence in the Vernacular, written in Latin around 1304, Dante compares the language children learn from their nurses with 'grammar', the learned Latin of the schools. Of the two, he argues, the everyday language is nobler, because it came first and is natural to all people. Nōbilior is a comparative, and hārum duārum, 'of these two', is a genitive.",
 "Dante then wrote the Divine Comedy in Italian, helping to make his Tuscan dialect the basis of modern Italian. The treatise breaks off unfinished in its second book.",
 'Dante Alighieri','Dante, De vulgari eloquentia','1.1.4','about 1304',LL+'dante/vulgar.shtml','verified',None,
 'Hārum|hic|of these|gen. pl. f.; quoque|quoque|also|adv.; duārum|duo|two|gen. pl. f.; nōbilior|nōbilis|nobler|comp. nom. sg. f.; est|sum|is|3rd sg. pres.; vulgāris|vulgāris|the vernacular (language)|nom. sg. f.',
 ['comparative','genitive','demonstratives'],[],'dante','De vulgari eloquentia',WP+'De_vulgari_eloquentia',related=['q-mon-unum'])

# ---------------- UNIT 13: Ius ----------------
K('q-xii-in-ius','quote','republic',13,'Sī in iūs vocat, itō.','If he summons you to court, you shall go.',
 "The Twelve Tables, Rome's first written laws, were set up in the Forum around 450 BC after the plebeians demanded laws that everyone could see. The very first rule says that if someone summons you to court, you must go. Itō is a future imperative, the commanding 'you shall' or 'he shall' of Roman law (the same form serves for both persons), and the subject of vocat is simply understood.",
 "Cicero says that as boys he and his friends learned the Tables by heart like a song. The original tablets were lost, and the laws are known only from later quotations.",
 'Twelve Tables','Lex Duodecim Tabularum','Table I.1','about 450 BC',LL+'12tables.html','verified','Text as reconstructed from later quotations.',
 'Sī|sī|if|conj.; in|in|into|prep. + acc.; iūs|iūs|court, law|acc. sg. n.; vocat|vocō|(he) summons|3rd sg. pres.; itō|eō|you shall go, he shall go|fut. imperative 2nd/3rd sg.',
 ['future_imperative','present_tense'],[],'twelvetables','Twelve Tables',WP+'Twelve_Tables')
K('q-inst-iustitia','quote','late_antiquity',13,'Iūstitia est cōnstāns et perpetua voluntās iūs suum cuique tribuēns.','Justice is the constant and lasting will that gives each person his due.',
 "Justinian's Institutes, a textbook for first-year law students published in 533, open with this definition taken from the jurist Ulpian. Justice is a steady will to give everyone what belongs to them. Tribuēns, 'giving', is a present participle, and cuique is a dative, 'to each'.",
 "Suum cuique, 'to each his own', became a legal maxim in its own right. The Institutes, Digest and Code together form the Corpus Iuris Civilis, the foundation of civil law in most of Europe and Latin America.",
 'Justinian (after Ulpian)','Justinian, Institutiones','1.1 pr.','533',LL+'justinian/institutes1.shtml','verified','The Digest (1.1.10 pr.) gives the same definition with tribuendi.',
 'Iūstitia|iūstitia|justice|nom. sg. f.; est|sum|is|3rd sg. pres.; cōnstāns|cōnstāns|constant|nom. sg. f.; et|et|and|conj.; perpetua|perpetuus|lasting|nom. sg. f.; voluntās|voluntās|will|nom. sg. f.; iūs|iūs|right, due|acc. sg. n.; suum|suus|his own|acc. sg. n.; cuique|quisque|to each|dat. sg. m.; tribuēns|tribuō|giving|pres. part. nom. sg. f.',
 ['present_participle','dative','adjective_agreement'],[],'justinian','Institutes of Justinian',WP+'Institutes_of_Justinian')
K('q-dig-praecepta','quote','empire',13,'Iūris praecepta sunt haec: honestē vīvere, alterum nōn laedere, suum cuique tribuere.','These are the precepts of the law: to live honourably, to harm no one, to give each person his due.',
 "Ulpian, a leading jurist of the early 3rd century AD, summed up the whole of law in three rules. Justinian's Digest of 533 preserved the sentence among thousands of extracts from Roman legal writers. The three infinitives explain haec, 'these', and alterum means 'another person'.",
 "Ulpian was killed by the Praetorian Guard in the 220s. Philosophers of law, including Kant, discussed his three precepts.",
 'Ulpian','Digesta Iustiniani','1.1.10.1','early 3rd century AD (Digest 533)',LL+'justinian/digest1.shtml','verified',None,
 'Iūris|iūs|of the law|gen. sg. n.; praecepta|praeceptum|precepts|nom. pl. n.; sunt|sum|are|3rd pl. pres.; haec|hic|these|nom. pl. n.; honestē|honestē|honourably|adv.; vīvere|vīvō|to live|pres. inf.; alterum|alter|another|acc. sg. m.; nōn|nōn|not|adv.; laedere|laedō|to harm|pres. inf.; suum|suus|his own|acc. sg. n.; cuique|quisque|to each|dat. sg. m.; tribuere|tribuō|to give|pres. inf.',
 ['infinitive','demonstratives','genitive'],[],'digest','Digest (Roman law)',WP+'Digest_(Roman_law)',related=['q-inst-iustitia'])
K('q-dig-cogitationis','quote','empire',13,'Cōgitātiōnis poenam nēmō patitur.','No one suffers punishment for a thought.',
 "This one-line rule from Ulpian says that thoughts alone are never punished. Roman law punished deeds and attempts, not mere intentions. Patitur is a deponent verb, passive in form but active in meaning, and cōgitātiōnis, 'of a thought', is a genitive.",
 "Modern criminal law keeps the same idea: a crime needs a guilty act, not just a guilty mind. Laws on conspiracy and preparing crimes still test where the line falls.",
 'Ulpian','Digesta Iustiniani','48.19.18','early 3rd century AD (Digest 533)',LL+'justinian/digest48.shtml','verified',None,
 'Cōgitātiōnis|cōgitātiō|of (for) a thought|gen. sg. f.; poenam|poena|punishment|acc. sg. f.; nēmō|nēmō|no one|nom. sg. m.; patitur|patior|suffers|3rd sg. pres. (deponent)',
 ['deponent','genitive','accusative'],[],'ulpian','Ulpian',WP+'Ulpian')
K('q-dig-benigniora','quote','empire',13,'Semper in dubiīs benigniōra praeferenda sunt.','In doubtful cases the kinder interpretation should always be preferred.',
 "This rule of the jurist Gaius stands among the 211 general rules collected at the very end of the Digest. In uncertain cases, it says, the more generous reading should win. Benigniōra, 'kinder things', is a comparative used as a noun, and praeferenda sunt, 'must be preferred', is a gerundive of obligation.",
 "The modern principle in dubiō prō reō, 'when in doubt, for the accused', grew from rules like this one. Gaius' own Institutes, the only classical law textbook to survive almost complete, was rediscovered in Verona in 1816.",
 'Gaius (jurist)','Digesta Iustiniani','50.17.56','2nd century AD (Digest 533)',LL+'justinian/digest50.shtml','verified',None,
 'Semper|semper|always|adv.; in|in|in|prep. + abl.; dubiīs|dubius|doubtful (cases)|abl. pl. n.; benigniōra|benignus|kinder (things)|comp. nom. pl. n.; praeferenda sunt|praeferō|must be preferred|gerundive nom. pl. n. + sunt',
 ['comparative','gerundive','neuter_plural'],[],'justitia','In dubio pro reo',WP+'In_dubio_pro_reo')
K('q-cicero-summum-ius','quote','republic',13,'Summum iūs, summa iniūria.','The highest law, the highest injustice.',
 "Cicero calls this a well-worn proverb: the strictest application of the law can become the greatest injustice. His example is a general who agreed a thirty-day truce and then raided the enemy by night, arguing that the treaty spoke of days, not nights. Summum and summa are superlatives agreeing with neuter iūs and feminine iniūria.",
 "Terence has a similar line, iūs summum saepe summa est malitia (Heauton Timorumenos 796). Judges still invoke the maxim against using the letter of the law to defeat its purpose.",
 'Proverb (quoted by Cicero)','Cicero, De officiis','1.33','44 BC',LL+'cicero/off1.shtml','verified','Cicero quotes it as an established proverb.',
 'Summum|summus|highest|nom. sg. n.; iūs|iūs|law, right|nom. sg. n.; summa|summus|highest|nom. sg. f.; iniūria|iniūria|injustice|nom. sg. f.',
 ['superlative','adjective_agreement'],[],'lictors','De Officiis',WP+'De_Officiis')
K('q-dig-dura-lex','quote','empire',13,'Quod quidem perquam dūrum est, sed ita lēx scrīpta est.','This is very harsh indeed, but that is how the law is written.',
 "Ulpian comments on a clause of Augustus' law on adultery that stopped a divorced wife from freeing or selling any of her slaves for sixty days, even slaves living far away. It is very harsh, he admits, but that is how the law was written. The later maxim dūra lēx, sed lēx, 'the law is harsh, but it is the law', grew from this sentence.",
 "The slaves were kept in the household because they could be questioned as witnesses. Roman jurists often criticised a rule while still applying it.",
 'Ulpian','Digesta Iustiniani','40.9.12.1','early 3rd century AD (Digest 533)',LL+'justinian/digest40.shtml','verified',None,
 'Quod|quī|this (which)|nom. sg. n.; quidem|quidem|indeed|adv.; perquam|perquam|extremely|adv.; dūrum|dūrus|harsh|nom. sg. n.; est|sum|is|3rd sg. pres.; sed|sed|but|conj.; ita|ita|so, thus|adv.; lēx|lēx|the law|nom. sg. f.; scrīpta est|scrībō|is written|3rd sg. perf. pass.',
 ['perfect_passive','relative_clause','third_declension'],[],'digest2','Dura lex, sed lex',WP+'Dura_lex,_sed_lex')
K('q-seneca-medea','quote','empire',13,'Quī statuit aliquid parte inaudītā alterā, aequum licet statuerit, haud aequus fuit.','Whoever has decided anything without hearing the other side has not been fair, even if what he decided was fair.',
 "In Seneca's tragedy, King Creon banishes Medea without hearing her case, and she throws this principle back at him. Parte inaudītā alterā, 'the other side unheard', is an ablative absolute, and licet with the subjunctive statuerit means 'although'. The legal principle audī alteram partem, 'hear the other side', says the same thing.",
 "Medea, the sorceress who helped Jason win the Golden Fleece, has been abandoned by him for Creon's daughter. Seneca's tragedies shaped Renaissance drama, including Shakespeare's.",
 'Medea (in Seneca)','Seneca, Medea','199–200','1st century AD',LL+'sen/sen.medea.shtml','verified','Spoken by Medea in the play.',
 'Quī|quī|whoever|nom. sg. m.; statuit|statuō|has decided|3rd sg. perf.; aliquid|aliquis|anything|acc. sg. n.; parte|pars|side|abl. sg. f.; inaudītā|inaudītus|unheard|abl. sg. f.; alterā|alter|the other|abl. sg. f.; aequum|aequus|something fair|acc. sg. n.; licet|licet|although|conj.; statuerit|statuō|he has decided|3rd sg. perf. subj.; haud|haud|not|adv.; aequus|aequus|fair|nom. sg. m.; fuit|sum|has been|3rd sg. perf.',
 ['ablative_absolute','relative_clause','subjunctive'],[],'medea','Audi alteram partem',WP+'Audi_alteram_partem')
K('q-cicero-servi-legum','quote','republic',13,'Lēgum dēnique idcircō omnēs servī sumus, ut līberī esse possīmus.','In the end we are all slaves of the laws for this reason, so that we can be free.',
 "Defending Aulus Cluentius on a murder charge, Cicero reminds the jurors that magistrates serve the laws and judges interpret them. In the end, he says, everyone is a slave of the laws, and that is exactly what keeps us free. Ut … possīmus is a purpose clause with the subjunctive, and lēgum is a genitive.",
 "Cluentius was acquitted. Quintilian says Cicero later boasted that he had thrown dust in the jurors' eyes in this case.",
 'Cicero','Cicero, Pro Cluentio','146','66 BC',LL+'cicero/cluentio.shtml','verified',None,
 'Lēgum|lēx|of the laws|gen. pl. f.; dēnique|dēnique|in the end|adv.; idcircō|idcircō|for this reason|adv.; omnēs|omnis|all|nom. pl. m.; servī|servus|slaves|nom. pl. m.; sumus|sum|we are|1st pl. pres.; ut|ut|so that|conj.; līberī|līber|free|nom. pl. m.; esse|sum|to be|pres. inf.; possīmus|possum|we can|1st pl. pres. subj.',
 ['subjunctive','genitive','possum_infinitive'],[],'fasces','Pro Cluentio',WP+'Pro_Cluentio')
K('q-bracton-lex','quote','high_medieval',13,'Ipse autem rēx nōn dēbet esse sub homine sed sub Deō et sub lēge, quia lēx facit rēgem.','The king himself ought not to be under any man, but under God and under the law, because the law makes the king.',
 "The great medieval treatise On the Laws and Customs of England, linked with the royal judge Henry de Bracton, says that even the king is bound by law. The idea that a ruler is under the law became central to English constitutional thought. Sub here takes the ablative, and esse is an infinitive after dēbet.",
 "Sir Edward Coke quoted the line to King James I around 1608, to the king's fury. The treatise was probably written by several royal judges between about 1220 and 1260.",
 'Henry de Bracton (attributed)','Bracton, De legibus et consuetudinibus Angliae','f. 5b (Thorne ed. vol. 2, p. 33)','13th century','https://amesfoundation.law.harvard.edu/Bracton/Unframed/Latin/v2/33.htm','verified','Text from the Thorne edition (Harvard Law School Library); authorship is debated.',
 'Ipse|ipse|himself|nom. sg. m.; autem|autem|however|conj.; rēx|rēx|king|nom. sg. m.; nōn|nōn|not|adv.; dēbet|dēbeō|ought|3rd sg. pres.; esse|sum|to be|pres. inf.; sub|sub|under|prep. + abl.; homine|homō|a man|abl. sg. m.; sed|sed|but|conj.; Deō|deus|God|abl. sg. m.; et|et|and|conj.; lēge|lēx|law|abl. sg. f.; quia|quia|because|conj.; lēx|lēx|the law|nom. sg. f.; facit|faciō|makes|3rd sg. pres.; rēgem|rēx|king|acc. sg. m.',
 ['infinitive','prep_ablative','demonstratives'],[],'bracton','De Legibus et Consuetudinibus Angliae',WP+'De_Legibus_et_Consuetudinibus_Angliae')
K('q-cj-omnes-tangit','quote','late_antiquity',13,'Quod omnēs similiter tangit, ab omnibus comprobētur.','What touches all alike should be approved by all.',
 "This rule in Justinian's Code first concerned guardians: a decision affecting several guardians needed all of them to agree. Medieval lawyers turned it into a principle of government, and in 1295 Edward I quoted it when summoning representatives to the so-called Model Parliament. Comprobētur, 'let it be approved', is a jussive subjunctive in the passive.",
 "The maxim is often abbreviated as quod omnēs tangit. Historians link it to later ideas such as 'no taxation without representation'.",
 'Justinian (Code)','Codex Iustinianus','5.59.5.2','531',LL+'justinian/codex5.shtml','verified','In the Code the clause depends on ut ("so that what touches all alike may be approved by all"); quoted on its own as a maxim, comprobētur reads as a jussive.',
 'Quod|quī|what|nom. sg. n.; omnēs|omnis|all|acc. pl. m.; similiter|similiter|alike|adv.; tangit|tangō|touches, concerns|3rd sg. pres.; ab|ab|by|prep. + abl.; omnibus|omnis|all|abl. pl. m.; comprobētur|comprobō|let it be approved|3rd sg. pres. pass. subj.',
 ['jussive_subjunctive','relative_clause','passive_voice'],[],'parliament','Parliament of England',WP+'Parliament_of_England')

# ---------------- UNIT 14: Scientia ----------------
K('q-copernicus-sol','quote','early_modern',14,'In mediō vērō omnium residet Sōl.','But in the middle of them all sits the Sun.',
 "In the tenth chapter of On the Revolutions of the Heavenly Spheres, published in 1543, Copernicus lists the planets outward from the centre and then places the Sun in the middle of them all. Who, he asks, would put this lamp of a most beautiful temple anywhere else? Omnium is a genitive plural, 'of all', and mediō an ablative after in.",
 "Copernicus is said to have received a printed copy on his deathbed in May 1543. A preface added without his consent by Andreas Osiander presented the theory as a mere tool for calculation.",
 'Nicolaus Copernicus','Copernicus, De revolutionibus orbium coelestium','1.10','1543',WS+'De_revolutionibus_orbium_coelestium/05','verified',None,
 'In|in|in|prep. + abl.; mediō|medium|the middle|abl. sg. n.; vērō|vērō|but, indeed|adv.; omnium|omnis|of all|gen. pl.; residet|resideō|sits, resides|3rd sg. pres.; Sōl|sōl|the Sun|nom. sg. m.',
 ['in_ablative','genitive','third_declension'],[],'copernicus','De revolutionibus orbium coelestium',WP+'De_revolutionibus_orbium_coelestium')
K('q-galileo-lunam','quote','early_modern',14,'… Lūnam superficiē lēnī et perpolītā nēquāquam esse indūtam, sed asperā et inaequālī','… that the Moon is by no means clothed with a smooth and polished surface, but with a rough and uneven one',
 "In 1609 Galileo turned his improved telescope on the sky, and in March 1610 he published his discoveries as Sidereus Nuncius, 'The Starry Messenger'. He reported that the Moon is not perfectly smooth, as followers of Aristotle held, but has mountains and valleys like the Earth. Lūnam … esse indūtam is an indirect statement with a perfect passive infinitive.",
 "The same short book announced four moons circling Jupiter, which Galileo named the Medicean Stars after his patrons. They are now called the Galilean moons.",
 'Galileo Galilei','Galileo, Sidereus Nuncius','Introduction','1610',LL+'galileo/galileo.sid.html','verified','The Latin Library text spells inêquali (= inaequali).',
 'Lūnam|lūna|the Moon|acc. sg. f.; superficiē|superficiēs|with a surface|abl. sg. f.; lēnī|lēnis|smooth|abl. sg. f.; et|et|and|conj.; perpolītā|perpolītus|polished|abl. sg. f.; nēquāquam|nēquāquam|by no means|adv.; esse indūtam|induō|to have been clothed, to be covered|perf. pass. inf.; sed|sed|but|conj.; asperā|asper|rough|abl. sg. f.; inaequālī|inaequālis|uneven|abl. sg. f.',
 ['indirect_statement','perfect_infinitive','adjective_agreement'],['fifth_declension'],'moon','Sidereus Nuncius',WP+'Sidereus_Nuncius')
K('q-descartes-existo','quote','early_modern',14,'Ego sum, ego existō.','I am, I exist.',
 "In his second Meditation, published in 1641, Descartes searches for one thing that cannot be doubted, even if an all-powerful deceiver were fooling him about everything else. Whenever he thinks or says 'I am, I exist', it must be true. His better-known formula, ego cōgitō, ergō sum, 'I think, therefore I am', appears in Latin in his Principles of Philosophy (1644).",
 "Descartes first wrote je pense, donc je suis in French in the Discourse on Method (1637). He chose Latin for the Meditations to reach scholars across Europe.",
 'René Descartes','Descartes, Meditationes de prima philosophia','2.3','1641',LL+'descartes/des.med2.shtml','verified',None,
 'Ego|ego|I|nom. sg.; sum|sum|am|1st sg. pres.; ego|ego|I|nom. sg.; existō|exsistō|exist|1st sg. pres.',
 ['sum','personal_pronouns','first_person'],[],'descartes','Cogito, ergo sum',WP+'Cogito,_ergo_sum')
K('q-newton-lex1','quote','early_modern',14,'Corpus omne persevērāre in statū suō quiēscendī vel movendī ūnifōrmiter in dīrēctum, nisi quātenus ā vīribus impressīs cōgitur statum illum mūtāre.','Every body continues in its state of rest or of moving uniformly straight ahead, except insofar as it is compelled by impressed forces to change that state.',
 "This is Newton's first law of motion, the law of inertia, as he published it in the Principia in 1687. The sentence depends on an understood 'it is a law that', so corpus is accusative and persevērāre an infinitive, an indirect statement. Quiēscendī and movendī are gerunds, 'of resting' and 'of moving', and cōgitur is passive.",
 "Newton wrote the Principia in Latin, still the international language of science. Physics students now learn the same law in their own languages.",
 'Isaac Newton','Newton, Philosophiae Naturalis Principia Mathematica','Axiomata, Lex I','1687',WS+'Philosophiae_Naturalis_Principia_Mathematica/Axiomata,_sive_Leges_Motus','verified',None,
 'Corpus|corpus|body|acc. sg. n.; omne|omnis|every|acc. sg. n.; persevērāre|persevērō|to continue|pres. inf.; in|in|in|prep. + abl.; statū|status|state|abl. sg. m.; suō|suus|its own|abl. sg. m.; quiēscendī|quiēscō|of resting|gerund gen.; vel|vel|or|conj.; movendī|moveō|of moving|gerund gen.; ūnifōrmiter|ūnifōrmiter|uniformly|adv.; in dīrēctum|dīrēctus|straight ahead|prep. phrase; nisi quātenus|nisi quātenus|except insofar as|conj.; ā|ab|by|prep. + abl.; vīribus|vīs|forces|abl. pl. f.; impressīs|imprimō|impressed|perf. pass. part. abl. pl. f.; cōgitur|cōgō|it is compelled|3rd sg. pres. pass.; statum|status|state|acc. sg. m.; illum|ille|that|acc. sg. m.; mūtāre|mūtō|to change|pres. inf.',
 ['indirect_statement','gerund','passive_voice'],[],'principia',"Newton's laws of motion",WP+"Newton's_laws_of_motion")
K('q-spinoza-deus','quote','early_modern',14,'Deus seu Nātūra','God, or Nature',
 "In his Ethics, published after his death in 1677, Spinoza argues that God is not a person outside the world but the one infinite substance of which everything is a part. The phrase Deus seu Nātūra, 'God, or Nature', shows that the two words name the same thing. Seu, 'or', here offers an equivalent rather than an alternative.",
 "The Ethics is laid out like a geometry book, with definitions, axioms and propositions. Spinoza had been expelled from Amsterdam's Jewish community in 1656.",
 'Baruch Spinoza','Spinoza, Ethica','Part 4, preface','1677',LL+'spinoza.ethica4.html','verified',None,
 'Deus|deus|God|nom. sg. m.; seu|seu|or (in other words)|conj.; Nātūra|nātūra|Nature|nom. sg. f.',
 ['nominative'],[],'spinoza','Ethics (Spinoza)',WP+'Ethics_(Spinoza)')
K('q-columbus-insulas','quote','early_modern',14,'In mare Indicum pervēnī, ubi plūrimās īnsulās innumerīs habitātās hominibus reperī.','I reached the Indian Sea, where I found very many islands inhabited by countless people.',
 "Columbus' letter announcing his first voyage was printed in Latin in 1493 and carried his news across Europe within months. He believed he had reached islands off Asia, in the 'Indian Sea', not a new continent. Habitātās, 'inhabited', is a perfect participle agreeing with īnsulās, and plūrimās is a superlative.",
 "The Latin version was translated from Columbus' Spanish by Leandro de Cosco. Columbus died in 1506 still insisting that he had reached Asia.",
 'Christopher Columbus','Columbus, Epistola de insulis nuper inventis','—','1493',LL+'columbus','verified','The printed Latin spells reperi (classical repperi).',
 'In|in|into|prep. + acc.; mare|mare|sea|acc. sg. n.; Indicum|Indicus|Indian|acc. sg. n.; pervēnī|perveniō|I reached|1st sg. perf.; ubi|ubi|where|adv.; plūrimās|plūrimus|very many|superl. acc. pl. f.; īnsulās|īnsula|islands|acc. pl. f.; innumerīs|innumerus|countless|abl. pl. m.; habitātās|habitō|inhabited|perf. pass. part. acc. pl. f.; hominibus|homō|by people|abl. pl. m.; reperī|reperiō|I found|1st sg. perf.',
 ['perfect_tense','participle','superlative'],[],'columbus',"Columbus's letter on the first voyage","https://en.wikipedia.org/wiki/Columbus%27s_letter_on_the_first_voyage")
K('q-more-utopia','quote','early_modern',14,'… dē optimō reīpūblicae statū dēque novā īnsulā Ūtopiā','… on the best state of a commonwealth, and on the new island of Utopia',
 "Thomas More's Utopia, published in Latin in 1516, describes an imaginary island where property is shared and citizens live by reason. More coined the name from Greek: 'no place', with a pun on 'good place'. Optimō is a superlative, and -que joins the two phrases beginning with dē.",
 "More became Lord Chancellor of England and was executed in 1535 for refusing to accept Henry VIII as head of the Church. The word utopia entered English and many other languages from this book.",
 'Thomas More','More, Utopia','title page','1516',LL+'more.html','verified','From the book\'s full title.',
 'dē|dē|on, about|prep. + abl.; optimō|optimus|best|superl. abl. sg. m.; reīpūblicae|rēs pūblica|of a commonwealth|gen. sg. f.; statū|status|state|abl. sg. m.; dē|dē|on, about|prep. + abl.; -que|-que|and|enclitic conj.; novā|novus|new|abl. sg. f.; īnsulā|īnsula|island|abl. sg. f.; Ūtopiā|Ūtopia|Utopia|abl. sg. f.',
 ['superlative','prep_ablative','enclitic_que','fifth_declension'],[],'utopia','Utopia (book)',WP+'Utopia_(book)')
K('q-gravissimas','quote','early_modern',14,'… decem diēs inclūsīvē ā tertiā Nōnārum usque ad prīdiē Īdūs eximantur','… let ten days, inclusive, be removed, from the third day before the Nones up to the day before the Ides',
 "With the bull Inter gravissimas, Pope Gregory XIII reformed the calendar in 1582, because the old Julian calendar had drifted ten days out of step with the seasons. Ten days were removed from October 1582, so that Thursday 4 October was followed by Friday 15 October. Eximantur, 'let them be removed', is a jussive subjunctive, and the dates use the Roman reckoning by Nones and Ides.",
 "Britain and its colonies switched only in 1752, when eleven days were dropped. Russia changed after 1917, which is why the 'October Revolution' falls in November by the new calendar.",
 'Pope Gregory XIII','Gregory XIII, Inter gravissimas','§ 4','1582',LL+'gravissimas.html','verified',None,
 'decem|decem|ten|indecl.; diēs|diēs|days|nom. pl. m.; inclūsīvē|inclūsīvē|inclusively|adv.; ā|ab|from|prep. + abl.; tertiā|tertius|the third (day)|abl. sg. f.; Nōnārum|Nōnae|before the Nones|gen. pl. f.; usque ad|usque ad|up to|prep. + acc.; prīdiē|prīdiē|the day before|adv. + acc.; Īdūs|Īdūs|the Ides|acc. pl. f.; eximantur|eximō|let them be removed|3rd pl. pres. pass. subj.',
 ['jussive_subjunctive','numerals','passive_voice','fifth_declension'],[],'gregory','Inter gravissimas',WP+'Inter_gravissimas')
K('q-comenius-veni','quote','early_modern',14,'Venī, puer! disce sapere.','Come, boy! Learn to be wise.',
 "Comenius' Orbis Pictus, 'The World in Pictures', printed in 1658, is often called the first picture book for children, with a numbered woodcut on every page. It opens with a teacher inviting a boy to learn to be wise. Venī and disce are imperatives, puer is a vocative, and sapere is an infinitive.",
 "Comenius, a Czech bishop and refugee, believed children should learn about things through their senses, not just words. Goethe remembered the Orbis Pictus as one of the books of his childhood.",
 'John Amos Comenius','Comenius, Orbis Sensualium Pictus','Invitatio','1658','https://www.gutenberg.org/cache/epub/28299/pg28299.txt','verified',None,
 'Venī|veniō|come|imperative sg.; puer|puer|boy|voc. sg. m.; disce|discō|learn|imperative sg.; sapere|sapiō|to be wise|pres. inf.',
 ['imperative','vocative','infinitive'],[],'orbis','Orbis Pictus',WP+'Orbis_Pictus')
K('q-erasmus-stultitia','quote','early_modern',14,'Stultitia loquitur.','Folly speaks.',
 "In Erasmus' Praise of Folly, published in 1511, the goddess Folly herself gives a speech boasting of her power over gods and humans. Behind her jokes Erasmus mocks quarrelsome theologians, greedy clergy and pompous scholars. Loquitur is a deponent verb, passive in form but active in meaning.",
 "Erasmus wrote the book in about a week while staying with Thomas More in London; its Greek title, Mōriae encōmium, puns on More's name. Hans Holbein drew comic sketches in the margins of a copy owned by a Basel schoolmaster.",
 'Erasmus of Rotterdam','Erasmus, Moriae encomium','heading of ch. 1','1511',LL+'erasmus/moriae.shtml','verified','The heading that introduces Folly\'s speech.',
 'Stultitia|stultitia|Folly|nom. sg. f.; loquitur|loquor|speaks|3rd sg. pres. (deponent)',
 ['deponent','nominative'],[],'erasmus','In Praise of Folly',WP+'In_Praise_of_Folly')
