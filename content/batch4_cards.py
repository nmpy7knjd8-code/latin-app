# Batch 4 card texts. Gloss format: "word|lemma|meaning|parse; ..."
# K(id,type,era,unit,latin,translation,context,more,person,work,cit,date,source_url,conf,note,gloss,target,preview,img,lm_label,lm_url, **extra)
LL='https://www.thelatinlibrary.com/'
RIB='https://romaninscriptionsofbritain.org/inscriptions/'
WP='https://en.wikipedia.org/wiki/'
CON='Constructed teaching sentence (not a quotation).'
CARDS=[]
def K(*a,**kw): CARDS.append((a,kw))

# ---------------- UNIT 1: Roma, the City ----------------
K('c-roma-denarius','artifact','republic',1,'ROMA — Rōma','Rome',
 "Silver denarii of the Republic often carried one word, ROMA, under the twin horsemen Castor and Pollux, with the helmeted goddess Roma on the front. The name is a plain nominative: it says who stands behind the coin. The denarius, first struck around 211 BC, was worth ten asses, hence its name (dēnī, 'ten each').",
 "The denarius was introduced around 211 BC during the war with Hannibal and stayed the main Roman silver coin for over 400 years. This anonymous type is Crawford RRC 198/1 (2nd century BC).",
 None,'Roman Republican coinage (Crawford, RRC)','198/1','2nd c. BC','https://numismatics.org/crro/id/rrc-198.1','verified',None,
 'Rōma|Rōma|Rome|nom. sg. f.',['nominative'],[],'roma','Denarius',WP+'Denarius',subtype='coin',raw=('ROMA','coin legend (exergue)'))
K('v-tiberis','vocab','regal',1,'Tiberis flūmen est; Rōma urbs est.','The Tiber is a river; Rome is a city.',
 "Rome grew up at the lowest easy crossing of the Tiber, about 25 km from the sea, where Tiber Island made a ford and later bridges possible. The river carried trade, and floods. Romans worshipped the river as the god Tiberinus, and Rome's oldest bridge, the Pons Sublicius, was built of wood without iron.",
 "Romans worshipped the river as the god Tiberinus. The Cloaca Maxima, the great drain, emptied the Forum valley into it. Note that flūmen is neuter and urbs feminine, but both sit in the nominative after est.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Tiberis|Tiberis|the Tiber|nom. sg. m.; flūmen|flūmen|river|nom. sg. n.; est|sum|is|3rd sg. pres.; Rōma|Rōma|Rome|nom. sg. f.; urbs|urbs|city|nom. sg. f.',
 ['nominative','sum'],[],'tiber','Tiber',WP+'Tiber',subtype='vocab')
K('p-forum','place','republic',1,'Hīc est Forum Rōmānum.','Here is the Roman Forum.',
 "The Forum began as a marshy valley between the Palatine and Capitoline hills, drained in the 7th–6th centuries BC. It became Rome's civic heart: Senate house, law courts, temples and the speakers' platform, the Rostra. Roads, processions and triumphs all ran along its Sacred Way, the Via Sacra.",
 "Forum first meant any open public square. Panini painted it in the 18th century, when it was half-buried pasture called the Campo Vaccino, the 'cow field'.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Hīc|hīc|here|adverb; est|sum|is|3rd sg. pres.; Forum|forum|forum, public square|nom. sg. n.; Rōmānum|Rōmānus|Roman|nom. sg. n. (fixed name)',
 ['sum','nominative'],[],'forum','Roman Forum',WP+'Roman_Forum',formula=['Forum Rōmānum'])
K('p-palatium','place','regal',1,'Palātium mōns est.','The Palatine is a hill.',
 "Tradition put Romulus's first city on the Palatine. Augustus lived there, and later emperors covered the hill with their residences, so Palātium came to mean 'the emperor's house': hence English palace, French palais, Italian palazzo. Archaeologists have found Iron Age hut foundations there, which Romans later showed off as the 'hut of Romulus'.",
 "Excavations have found Iron Age hut foundations on the Palatine from the 8th century BC, roughly the legendary date of Rome's founding (753 BC).",
 None,'Constructed','—','—',None,'constructed',CON,
 'Palātium|Palātium|the Palatine (hill)|nom. sg. n.; mōns|mōns|hill, mountain|nom. sg. m.; est|sum|is|3rd sg. pres.',
 ['nominative','sum'],[],'palatine','Palatine Hill',WP+'Palatine_Hill',subtype='derivative')
K('p-romulus-remus','person','regal',1,'Rōmulus et Remus frātrēs sunt.','Romulus and Remus are brothers.',
 "In the legend the twin sons of Mars and Rhea Silvia were set adrift on the Tiber, suckled by a she-wolf and raised by the shepherd Faustulus. They quarrelled over where to found the city; Romulus killed Remus (Livy 1.4–7). The traditional Roman date for the founding is 753 BC, and the she-wolf, lupa, became the city's emblem.",
 "Livy himself offers a rationalised version: lupa was also slang for a prostitute, so the 'wolf' might have been the shepherd's wife. Frātrēs is a nominative plural, so the verb is plural too: sunt.",
 'Romulus and Remus','Constructed (story: Livy, Ab urbe condita)','1.4–7','—',LL+'livy/liv.1.shtml','constructed',CON,
 'Rōmulus|Rōmulus|Romulus|nom. sg. m.; et|et|and|conj.; Remus|Remus|Remus|nom. sg. m.; frātrēs|frāter|brothers|nom. pl. m.; sunt|sum|are|3rd pl. pres.',
 ['nominative','sum'],[],'twins','Romulus and Remus',WP+'Romulus_and_Remus')
K('q-jerome-ciceronianus','quote','late_antiquity',1,'Cicerōniānus es, nōn Chrīstiānus.','You are a Ciceronian, not a Christian.',
 "Jerome tells the young Eustochium (Letter 22, AD 384) of a fever-dream: dragged before Christ's judgement seat, he said he was a Christian and heard this reply. He had been reading Cicero and Plautus and finding the prophets' Latin crude. He swore never again to own or read pagan books, though his later letters still quote Virgil and Cicero.",
 "He swore never again to own or read pagan books. He kept quoting them all his life, and later translated the Bible into the Latin we call the Vulgate.",
 'Jerome','Jerome, Epistulae','22.30.4','AD 384','https://fgh.perseids.org/read/latinLit/stoa0162/stoa004/perseus-lat2/22.23-22.40','verified',
 'Text verified (Perseus/Loeb): "Mentiris," ait, "Ciceronianus es, non Christianus; ubi thesaurus tuus, ibi et cor tuum." Card drops the opening Mentiris.',
 'Cicerōniānus|Cicerōniānus|a Ciceronian, follower of Cicero|nom. sg. m.; es|sum|you are|2nd sg. pres.; nōn|nōn|not|adv.; Chrīstiānus|Chrīstiānus|a Christian|nom. sg. m.',
 ['nominative','sum'],[],'jerome','Jerome',WP+'Jerome',register='ecclesiastical')
K('i-bayeux-willelm','artifact','high_medieval',1,'HIC EST WILLEL[MVS] DVX — Hīc est Willelmus dux.','Here is Duke William.',
 'At Hastings on 14 October 1066 a rumour ran through the Norman army that William had been killed. The Bayeux Tapestry shows him pushing up his helmet to show his face, while the caption names him. The tapestry is really an embroidery, about 70 metres long, probably made in England within a few decades of the battle.',
 "The tapestry is in fact an embroidery, about 70 m long, probably made in England in the 1070s. Its captions use simple medieval Latin: hīc 'here', a name in the nominative, and est.",
 'William the Conqueror','Bayeux Tapestry','scene 55','c. 1070s (event 1066)',WP+'Bayeux_Tapestry_tituli','verified','Caption as listed in the scholarly tituli (the end of WILLELMUS is lost and restored).',
 'Hīc|hīc|here|adverb; est|sum|is|3rd sg. pres.; Willelmus|Willelmus|William|nom. sg. m.; dux|dux|leader, duke|nom. sg. m.',
 ['nominative','sum'],[],'willelm','Battle of Hastings',WP+'Battle_of_Hastings',subtype='inscription',raw=('HIC EST WILLEL[MVS] DVX','embroidered caption'),register='medieval')

# ---------------- UNIT 2: Familia ----------------
K('i-claudia-lanam','artifact','republic',2,'DOMVM SERVAVIT LANAM FECIT — Domum servāvit, lānam fēcit.','She kept the house; she worked the wool.',
 'The verse epitaph of a woman named Claudia, Rome, 2nd century BC (CIL VI 15346). It asks the passer-by to stop and read, praises her love for her husband and her two sons, and ends with the Roman ideal of a matron. Spinning and weaving wool at home was the standard praise of a good Roman wife; the wording is famous for being so short.',
 "The final words are 'dīxī. abī' – 'I have spoken. Go on your way.' Domum and lānam are accusatives, the things she looked after; the perfect tense (servāvit, fēcit) is only previewed here.",
 'Claudia','Epitaph of Claudia (CIL VI 15346 = CIL I² 1211)','line 8','2nd c. BC','https://edcs.hist.uzh.ch/search','verified','Checked against EDCS-09600221: "…domum servavit lanam fecit dixi ab{e}i".',
 'Domum|domus|house, household|acc. sg. f.; servāvit|servō|she kept, looked after|3rd sg. perf.; lānam|lāna|wool|acc. sg. f.; fēcit|faciō|she made, worked|3rd sg. perf.',
 ['accusative'],['perfect_tense'],'distaff','Women in ancient Rome',WP+'Women_in_ancient_Rome',subtype='inscription',raw=('DOMVM SERVAVIT LANAM FECIT','EDCS-09600221 (CIL VI 15346), line 8'))
K('q-cicero-desideria','quote','republic',2,'Valēte, mea dēsīderia, valēte.','Farewell, my darlings, farewell.',
 "Exiled in 58 BC for executing Catiline's allies without trial, Cicero wrote from Thessalonica to his wife Terentia, daughter Tullia and son Marcus. Dēsīderia, 'longings', is neuter plural: his family are the things he misses. He was recalled to Rome the next year, in 57 BC.",
 "The letter (Ad familiares 14.2) is full of guilt: Terentia was selling property to support him. He was recalled in 57 BC; the marriage ended in divorce about ten years later.",
 'Marcus Tullius Cicero','Cicero, Epistulae ad familiares','14.2.4','5 Oct 58 BC',LL+'cicero/fam14.shtml','verified',None,
 'Valēte|valeō|farewell (to several people)|imperative pl. (formula); mea|meus|my|voc. pl. n.; dēsīderia|dēsīderium|longings, darlings|voc. pl. n.; valēte|valeō|farewell|imperative pl. (formula)',
 ['vocative','neuter_plural','possessive_adjectives'],[],'cicero','Terentia',WP+'Terentia',formula=['valēte'],related=['q-cicero-quousque'])
K('q-gaius-gaia','quote','republic',2,'Ubi tū Gāius, ego Gāia.','Where you are Gaius, I am Gaia.',
 "Plutarch (Roman Questions 30) says a Roman bride, brought to her new home, was told to say this. Gaius and Gaia worked like 'John and Jane', so the formula promised to share the household as equals. Plutarch also links the name to Gaia Caecilia, a Tarquin queen remembered as a model wife and spinner.",
 "Plutarch wrote in Greek; the Latin is the traditional reconstruction. He also suggests the names honour Gaia Caecilia, a model wife of the regal period whose spindle was kept in a temple.",
 'A Roman bride (custom reported by Plutarch)','Plutarch, Quaestiones Romanae','30','c. AD 100 (custom older)','https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Moralia/Roman_Questions*/B.html','traditional','Plutarch gives the formula in Greek; the Latin wording is a reconstruction.',
 'Ubi|ubi|where|conj.; tū|tū|you|nom. sg.; Gāius|Gāius|Gaius|nom. sg. m.; ego|ego|I|nom. sg.; Gāia|Gāia|Gaia|nom. sg. f.',
 ['nominative'],['personal_pronouns'],'marriage','Marriage in ancient Rome',WP+'Marriage_in_ancient_Rome')
K('i-pompeii-methe','artifact','republic',2,'Methē Cominiaes Ātellāna amat Chrēstum.','Methe, slave of Cominia, from Atella, loves Chrestus.',
 "Written on a wall at Pompeii (CIL IV 2457). Methe and Chrestus are Greek slave names; Cominiaes is an old-style genitive, 'Cominia's'. The writer adds a prayer that Venus of Pompeii keep them together always. Hundreds of love messages like this survive on Pompeii's walls, preserved by the eruption of AD 79.",
 "Ātellāna probably means 'from Atella', a town near Naples – or an actress in Atellan farces. Chrēstum is the accusative: the one who is loved.",
 'Methe','Pompeii wall inscription (CIL IV 2457)','—','1st c. BC – AD 14 (EDCS)','https://edcs.hist.uzh.ch/search','verified','Checked against EDCS-29300477: "Methe Cominiaes(!) Atellana amat Chrestum corde [si]t utr{e}isque Venus Pompeiana propitia et sem[per] concordes v{e}ivant".',
 'Methē|Methē|Methe|nom. sg. f. (Greek name); Cominiaes|Cominia|Cominia\'s (slave)|gen. sg. f. (old form); Ātellāna|Ātellānus|from Atella (or: an actress of Atellan farce)|nom. sg. f.; amat|amō|loves|3rd sg. pres.; Chrēstum|Chrēstus|Chrestus|acc. sg. m.',
 ['accusative','nominative'],[],'neo','Roman graffiti',WP+'Roman_graffiti',subtype='inscription',formula=['Cominiaes'],raw=('Methe Cominiaes Atellana amat Chrestum','EDCS-29300477 (CIL IV 2457)'))
K('i-vindolanda-salutant','artifact','empire',2,'Ceriālem tuum salūtā. Aelius meus … et fīliolus salūtant.','Greet your Cerialis. My Aelius and my little son send greetings.',
 "From Claudia Severa's birthday invitation to Sulpicia Lepidina, wife of Flavius Cerialis, commander at Vindolanda (Tab. Vindol. 291, c. AD 100). 'My Aelius' is her husband Aelius Brocchus; fīliolus, 'little son', is a diminutive. Part of the letter is in Severa's own hand, perhaps the earliest known writing in Latin by a woman.",
 "The scribe wrote the invitation and these greetings; Severa added the closing lines in her own hand, among the earliest Latin known to be written by a woman. Tuum and meus show possessive adjectives agreeing with the person they describe.",
 'Claudia Severa','Vindolanda tablet (Tab. Vindol. 291)','lines 9–10','c. AD 97–105',RIB+'TabVindol291','verified','RIB edition: "Cerial[em t]ụum salut á Aelius meus .[ et filioḷụs ṣalutant" (letters in brackets restored; one word lost after meus).',
 'Ceriālem|Ceriālis|Cerialis|acc. sg. m.; tuum|tuus|your|acc. sg. m.; salūtā|salūtō|greet!|imperative sg.; Aelius|Aelius|Aelius|nom. sg. m.; meus|meus|my|nom. sg. m.; et|et|and|conj.; fīliolus|fīliolus|little son|nom. sg. m.; salūtant|salūtō|they greet|3rd pl. pres.',
 ['accusative','possessive_adjectives'],['imperative'],'tab291','Claudia Severa',WP+'Claudia_Severa',subtype='daily_life',raw=('Cerial[em t]ụum salut á Aelius meus .[ et filioḷụs ṣalutant','RIB online, Tab. Vindol. 291'),related=['i-vindolanda'])
K('q-et-tu-brute','quote','republic',2,'Et tū, Brūte?','You too, Brutus?',
 "Caesar's famous last words come from Shakespeare's Julius Caesar (1599), not from an ancient source. Suetonius (Iul. 82) says Caesar died silently, though some reported him saying in Greek to Brutus, 'You too, child?' The Latin phrase may be older than Shakespeare: it appears in an English play of the 1590s, The True Tragedy of Richard Duke of York.",
 "Brūte is the vocative of Brūtus: -us nouns change to -e when you speak to someone. Caesar was stabbed 23 times at a Senate meeting in the Theatre of Pompey on the Ides of March, 44 BC.",
 'Gaius Julius Caesar (as written by Shakespeare)','Shakespeare, Julius Caesar','3.1.77','1599 (event 44 BC)',LL+'suetonius/suet.caesar.html','apocryphal','Not in any ancient source. Suetonius, Iul. 82.2, reports the Greek "καὶ σὺ τέκνον" only as something some people claimed.',
 'Et|et|also, too|adv.; tū|tū|you|nom. sg.; Brūte|Brūtus|Brutus|voc. sg. m.',
 ['vocative'],['personal_pronouns'],'caesardeath','Et tu, Brute?',WP+'Et_tu,_Brute%3F',related=['c-brutus-eidmar'])
K('v-frater-soror','vocab','empire',2,'Valē, frāter! Valē, soror!','Goodbye, brother! Goodbye, sister!',
 "Frāter and soror were family words that Romans also used for close friends and comrades. At Vindolanda, Claudia Severa calls her friend Lepidina 'soror', and the soldier Chrauttius calls his old messmate 'frāter'. The Prado statue group shown here is often identified as Castor and Pollux, the twin brothers whom Romans honoured in the Forum.",
 "Catullus ends his elegy for his real brother with 'avē atque valē, frāter'. These nouns have the same form for the vocative and the nominative; only -us nouns change (Brūte, Mārce).",
 None,'Constructed','—','—',None,'constructed',CON,
 'Valē|valeō|goodbye, farewell|imperative sg. (formula); frāter|frāter|brother|voc. sg. m.; Valē|valeō|goodbye|imperative sg. (formula); soror|soror|sister|voc. sg. f.',
 ['vocative'],[],'dioscuri','Castor and Pollux',WP+'Castor_and_Pollux',subtype='vocab',formula=['valē'],related=['i-vindolanda','i-vindolanda-miror','q-catullus-ave'])

# ---------------- UNIT 3: Legio ----------------
K('i-vindolanda-cervesa','artifact','empire',3,'Cervesam commīlitōnēs nōn habunt.','My fellow-soldiers have no beer.',
 "Masclus, a cavalry officer (decurion) of the Ninth Cohort of Batavians, wrote to his commander Flavius Cerialis asking for the next day's orders, then added a postscript: please order some beer sent (Tab. Vindol. 628, c. AD 97–105). Note habunt for standard habent: the tablets show the everyday Latin soldiers actually wrote.",
 "Cervesa is a Celtic word for beer, brewed from a wheat called bracis. Habunt is soldiers' Latin for standard habent. The writer also calls Cerialis rēx, 'king'.",
 'Masclus','Vindolanda tablet (Tab. Vindol. 628)','ii.4–6','c. AD 97–105',RIB+'TabVindol628','verified','RIB edition: "ceruesam commilitones non habunt quam rogó iubeas mitti". Quantity of the e in cervesa uncertain, so left unmarked (policy §3).',
 'Cervesam|cervesa|beer|acc. sg. f. (Celtic word); commīlitōnēs|commīlitō|fellow-soldiers|nom. pl. m.; nōn|nōn|not|adv.; habunt|habeō|they have|3rd pl. pres. (non-standard for habent)',
 ['present_tense','third_person_plural','accusative'],[],'tabpeel2','Vindolanda tablets',WP+'Vindolanda_tablets',subtype='daily_life',raw=('ceruesam commilitones non habunt','RIB online, Tab. Vindol. 628'))
K('q-ovid-militat','quote','empire',3,'Mīlitat omnis amāns, et habet sua castra Cupīdō.','Every lover is a soldier, and Cupid has his own camp.',
 'Ovid opens Amores 1.9 by turning army life into a metaphor for love: soldier and lover both keep night watch, besiege doors, march in cold and rain. Castra is plural in form but means one camp. Ovid was writing under Augustus, who was promoting marriage and military values, so the joke had an edge.',
 "The poem is addressed to a friend, Atticus, and ends with Ovid claiming love cured him of laziness. Sua (his own) agrees with castra, neuter plural.",
 'Publius Ovidius Naso','Ovid, Amores','1.9.1','c. 16 BC',LL+'ovid/ovid.amor1.shtml','verified',None,
 'Mīlitat|mīlitō|serves as a soldier|3rd sg. pres.; omnis|omnis|every|nom. sg. m.; amāns|amō|lover (lit. loving)|pres. participle as noun; et|et|and|conj.; habet|habeō|has|3rd sg. pres.; sua|suus|his own|acc. pl. n.; castra|castra|camp|acc. pl. n.; Cupīdō|Cupīdō|Cupid|nom. sg. m.',
 ['present_tense','possessive_adjectives','neuter_plural'],['present_participle'],'cupid','Amores (Ovid)',WP+'Amores_(Ovid)')
K('q-vespasian-deus','quote','empire',3,'Vae, putō, deus fīō.','Oh dear, I think I am becoming a god.',
 'Dead emperors were officially declared gods, so when Vespasian fell ill in AD 79 he joked about his coming divinity (Suetonius, Vesp. 23.4). Near the end he struggled to his feet: an emperor, he said, should die standing. He was the first emperor to be succeeded by his own son, Titus.',
 "Vespasian rose from a modest family to end the civil wars of AD 69 and began the Colosseum. Fīō, 'I become', is the present tense, first person.",
 'Vespasian','Suetonius, Divus Vespasianus','23.4','AD 79',LL+'suetonius/suet.vesp.html','verified','Checked against the Latin Library preface: "vae diebus nostris, quia periit studium litterarum a nobis".',
 'Vae|vae|alas, oh dear|interjection; putō|putō|I think|1st sg. pres.; deus|deus|a god|nom. sg. m.; fīō|fīō|I become|1st sg. pres.',
 ['present_tense','first_person','nominative'],[],'vespasian','Vespasian',WP+'Vespasian')
K('i-sator','artifact','empire',3,'ROTAS OPERA TENET AREPO SATOR — Sator Arepo tenet operā rotās.','The sower Arepo holds the wheels with care (the meaning is disputed).',
 'This five-word palindrome makes a square that reads the same four ways. One scratched on a column of the Large Palaestra at Pompeii (CIL IV 8623) proves it existed before AD 79; later Christians used it as a charm. Rearranged, the letters can spell PATER NOSTER twice in a cross, with A and O left over, but the Pompeii example makes a Christian origin unlikely.',
 "Nobody agrees what it means, and Arepo is otherwise unknown, perhaps a name. Grammatically it is a present-tense sentence with a subject (sator) and an object (rotās); word order is free.",
 None,'Pompeii graffito (CIL IV 8623)','—','before AD 79','https://edcs.hist.uzh.ch/search','verified','Checked against EDCS-24600449: "Rotas / opera / tenet / Arepo / sator". Arepo: quantity unknown, left unmarked (policy §3).',
 'Sator|sator|sower|nom. sg. m.; Arepo|Arepo|Arepo (name?)|nom. sg. m.; tenet|teneō|holds|3rd sg. pres.; operā|opera|with care, by work|abl. sg. f.; rotās|rota|wheels|acc. pl. f.',
 ['present_tense','word_order','accusative'],['ablative'],'sator','Sator Square',WP+'Sator_Square',subtype='inscription',raw=('ROTAS / OPERA / TENET / AREPO / SATOR','EDCS-24600449 (CIL IV 8623)'))
K('q-virgil-lacrimae','quote','empire',3,'Sunt lacrimae rērum et mentem mortālia tangunt.','There are tears for things, and mortal sufferings touch the mind.',
 "Shipwrecked at Carthage, Aeneas finds the Trojan War painted on Juno's new temple and weeps: even here people feel for human suffering (Aeneid 1.462). Few lines in Latin have been translated in more ways. Rērum here is vague on purpose: 'of things', of the world, of what happens to people.",
 "Lacrimae rērum ('tears of things') is famously ambiguous: tears shed for the world, or the sadness built into things. Mortālia is neuter plural used as a noun, subject of tangunt.",
 'Publius Vergilius Maro','Virgil, Aeneid','1.462','c. 29–19 BC',LL+'vergil/aen1.shtml','verified',None,
 'Sunt|sum|there are|3rd pl. pres.; lacrimae|lacrima|tears|nom. pl. f.; rērum|rēs|of things, for the world|gen. pl. f.; et|et|and|conj.; mentem|mēns|mind|acc. sg. f.; mortālia|mortālis|mortal things, sufferings|nom. pl. n.; tangunt|tangō|touch|3rd pl. pres.',
 ['present_tense','third_person_plural','neuter_plural','accusative'],['genitive'],'vergilms','Lacrimae rerum',WP+'Lacrimae_rerum')

# ---------------- UNIT 4: Forum & Senate (gen./dat., adjectives) ----------------
K('i-pompeii-celadus','artifact','empire',4,'Suspīrium puellārum, thr(aex) Celadus.','Celadus the Thracian, the girls\' heartthrob.',
 "Scratched on a Pompeii wall (CIL IV 4342): Celadus, a gladiator armed as a Thracian (thraex), from the troupe of Octavius, with three fights and three victories. Suspīrium means 'sigh': he makes the girls sigh. Thracian-style gladiators fought with a small shield and a short curved sword, the sica.",
 "Thracians fought with a small shield and a curved sword, wearing a griffin-crested helmet like this one. Puellārum is a genitive plural: the sigh of the girls.",
 'Celadus','Pompeii graffito (CIL IV 4342)','—','before AD 79','https://edcs.hist.uzh.ch/search','verified','Checked against EDCS-26000494: "Suspirium puellarum / t(h)r(aex) / Celadus Oct(avianus) III |(coronarum) III". Card omits the troupe and score.',
 'Suspīrium|suspīrium|sigh, heartthrob|nom. sg. n.; puellārum|puella|of the girls|gen. pl. f.; thr(aex)|thraex|Thracian (gladiator type)|nom. sg. m.; Celadus|Celadus|Celadus|nom. sg. m.',
 ['genitive','nominative','abbreviations'],[],'helmet','Thraex',WP+'Thraex',subtype='inscription',raw=('SVSPIRIVM PVELLARVM / TR / CELADVS OCT III III','EDCS-26000494 (CIL IV 4342)'))
K('q-statius-appia','quote','empire',4,'Appia longārum … rēgīna viārum','the Appian Way, queen of long roads',
 "Statius, travelling to a friend's villa near Sorrento, calls the Via Appia the 'queen of long roads' (Silvae 2.2.12). Begun by the censor Appius Claudius Caecus in 312 BC, it ran from Rome to Capua and later to Brundisium. Stretches of its original paving and the tombs that lined it can still be walked outside Rome today.",
 "Longārum agrees with viārum (both genitive plural feminine), wrapped around rēgīna. The full line is 'quā… Appia longārum teritur rēgīna viārum': 'where the Appia, queen of long roads, is worn down by traffic'.",
 'Publius Papinius Statius','Statius, Silvae','2.2.12','c. AD 90',LL+'statius/silvae2.shtml','verified','Excerpt; the verb teritur is omitted.',
 'Appia|Appius|the Appian (Way)|nom. sg. f.; longārum|longus|long|gen. pl. f.; rēgīna|rēgīna|queen|nom. sg. f.; viārum|via|of roads|gen. pl. f.',
 ['genitive','adjective_agreement'],[],'appia','Appian Way',WP+'Appian_Way')
K('i-turia','artifact','empire',4,'RARA SVNT TAM DIVTVRNA MATRIMONIA — Rāra sunt tam diūturna mātrimōnia.','Marriages so long are rare.',
 "A husband's funeral eulogy for his wife, carved in Rome late in the 1st century BC (the 'Laudatio Turiae', CIL VI 1527). He says their 41-year marriage was ended by death, not divorce. She had saved him during the proscriptions of 43 BC. The speech survives on fragments of marble slabs found in and around Rome.",
 "Childless, she even offered to divorce him so he could have heirs; he was horrified. Rāra and diūturna are neuter plural adjectives agreeing with mātrimōnia.",
 None,'"Laudatio Turiae" (CIL VI 1527 + 41062)','col. 1, line 27','late 1st c. BC','https://edcs.hist.uzh.ch/search','verified','Checked against EDCS-60700127: "rara sunt tam diuturna matrimonia finita morte non divertio in[terrupta]". The wife\'s name is lost; "Turia" is a modern identification.',
 'Rāra|rārus|rare|nom. pl. n.; sunt|sum|are|3rd pl. pres.; tam|tam|so|adv.; diūturna|diūturnus|long-lasting|nom. pl. n.; mātrimōnia|mātrimōnium|marriages|nom. pl. n.',
 ['neuter_plural','adjectives','sum'],[],'turia','Laudatio Turiae',WP+'Laudatio_Turiae',subtype='inscription',raw=('rara sunt tam diuturna matrimonia','EDCS-60700127'))
K('q-hadrian-animula','quote','empire',4,'Animula vagula blandula, hospes comesque corporis','Little soul, little wanderer, little charmer, guest and companion of the body',
 'The Historia Augusta (Hadr. 25.9) says the dying Hadrian wrote this little poem to his soul in AD 138. The pile of -ula diminutives makes it tender and playful. It goes on to ask where the soul is going now. The poem has five short lines, and translators from Byron onward have tried their hand at it.',
 "The last line is 'nec, ut solēs, dabis iocōs': 'and you will not make jokes, as you used to'. Corporis is a genitive (of the body); -que joins hospes and comes.",
 'Hadrian','Historia Augusta, Vita Hadriani','25.9','AD 138',LL+'sha/hadr.shtml','traditional','The Historia Augusta says "dicitur" (he is said to have written it), and the work is often unreliable.',
 'Animula|animula|little soul|voc. sg. f.; vagula|vagulus|little wandering|voc. sg. f.; blandula|blandulus|little charming|voc. sg. f.; hospes|hospes|guest|voc. sg.; comesque|comes + -que|and companion|voc. sg.; corporis|corpus|of the body|gen. sg. n.',
 ['genitive','vocative','adjective_agreement','enclitic_que'],[],'hadrian','Animula vagula blandula',WP+'Animula_vagula_blandula')
K('i-rib-818','artifact','empire',4,'I·O·M·C·CABAL·PRISCVS·TRIBVNVS — Iovī Optimō Maximō Gāius Caballius Prīscus tribūnus.','To Jupiter, Best and Greatest: Gaius Caballius Priscus, tribune (set this up).',
 "An altar from Maryport fort on the Cumbrian coast (RIB 818). Priscus commanded the First Cohort of Spaniards; the god goes in the dative ('to Jupiter'), the dedicator in the nominative. I·O·M was so standard it was never spelled out. Maryport has produced the largest group of altars to Jupiter found anywhere in Roman Britain.",
 "Seventeen altars to Jupiter were found buried together at Maryport in 1870, many set up by the fort's commanders. Iovī is the dative of Iuppiter; C. stands for Gāius.",
 'Gaius Caballius Priscus','Altar from Maryport (RIB 818 = CIL VII 375)','—','AD 122–138 (EDCS)',RIB+'818','verified','RIB online text: "I(ovi) O(ptimo) M(aximo) / G(aius) Cabal(lius) / Priscus / tribunus"; EDCS-07801109 agrees.',
 'Iovī|Iuppiter|to Jupiter|dat. sg. m.; Optimō|optimus|best|dat. sg. m.; Maximō|maximus|greatest|dat. sg. m.; Gāius|Gāius|Gaius|nom. sg. m.; Caballius|Caballius|Caballius|nom. sg. m.; Prīscus|Prīscus|Priscus|nom. sg. m.; tribūnus|tribūnus|tribune|nom. sg. m.',
 ['dative','abbreviations','adjective_agreement','nominative'],[],'rib818','Alauna (Maryport)',WP+'Alauna_(Maryport)',subtype='inscription',raw=('I O M / C CΛBΛL / PRISCVS / TRIBVNVS','RIB online, 818'))

# ---------------- UNIT 5: Gods & Temples (3rd decl., ablative) ----------------
K('q-ennius-moribus','quote','republic',5,'Mōribus antīquīs rēs stat Rōmāna virīsque.','The Roman state stands on its ancient ways and its men.',
 "A line from Ennius's epic Annales (early 2nd century BC). Cicero quoted it at the start of De re publica 5, saying it sounded like an oracle, and Augustine preserved the passage (City of God 2.21). Ennius, born in southern Italy, was called the father of Roman poetry, but his Annales survive only in quotations by later authors.",
 "Augustine quotes it to argue that Rome's old virtues had already gone. Mōribus and virīs are ablatives of means: the state stands by them. Rēs Rōmāna is a fifth-declension noun with its adjective.",
 'Quintus Ennius','Ennius, Annales (via Augustine, De civitate Dei 2.21)','fr. 156 Skutsch','early 2nd c. BC',LL+'augustine/civ2.shtml','verified',None,
 'Mōribus|mōs|by customs, ways|abl. pl. m.; antīquīs|antīquus|ancient|abl. pl. m.; rēs|rēs|state, affair|nom. sg. f.; stat|stō|stands|3rd sg. pres.; Rōmāna|Rōmānus|Roman|nom. sg. f.; virīsque|vir + -que|and by men|abl. pl. m.',
 ['ablative_means','third_declension','fifth_declension','enclitic_que','adjective_agreement'],[],'ennius','Annales (Ennius)',WP+'Annales_(Ennius)')
K('q-martial-amphitheatro','quote','empire',5,'Omnis Caesareō cēdit labor Amphitheātrō.','Every great work gives way to Caesar\'s Amphitheatre.',
 "Martial's Book of Spectacles celebrated the opening of the Flavian Amphitheatre, the Colosseum, under Titus in AD 80. The first poem says the pyramids, Babylon's walls and the Mausoleum must all yield to it. The opening games under Titus are said to have lasted 100 days.",
 "Notice the framing word order: Caesareō … Amphitheātrō hold the line together, adjective and noun far apart. Cēdō, 'yield', takes the dative.",
 'Marcus Valerius Martialis','Martial, Liber spectaculorum','1.7','AD 80',LL+'martial/mart.spec.shtml','verified',None,
 'Omnis|omnis|every|nom. sg. m.; Caesareō|Caesareus|of Caesar, imperial|dat. sg. n.; cēdit|cēdō|yields, gives way to|3rd sg. pres.; labor|labor|labour, work|nom. sg. m.; Amphitheātrō|amphitheātrum|amphitheatre|dat. sg. n.',
 ['dative','third_declension','third_conjugation','adjective_agreement'],[],'colosseum','Inaugural games of the Flavian Amphitheatre',WP+'Inaugural_games_of_the_Flavian_Amphitheatre')
K('q-cicero-respublica','quote','republic',5,'Est igitur, inquit Āfricānus, rēs pūblica rēs populī.','"So the commonwealth," said Africanus, "is the property of the people."',
 "In De re publica (54–51 BC) Cicero has Scipio Aemilianus define the state as rēs populī, 'the people's thing', and a people as a body joined by agreement about justice and shared interest. The work was lost for centuries until Cardinal Angelo Mai found much of it in 1819 under a copy of Augustine's commentary on the Psalms, the palimpsest shown here.",
 "Most of the work was lost until 1819, when Angelo Mai found it written under a later text in a Vatican palimpsest. Rēs is fifth declension; populī is a genitive.",
 'Marcus Tullius Cicero','Cicero, De re publica','1.39','54–51 BC',LL+'cicero/repub1.shtml','verified',None,
 'Est|sum|is|3rd sg. pres.; igitur|igitur|therefore, so|adv.; inquit|inquam|says, said|3rd sg.; Āfricānus|Āfricānus|Africanus (Scipio)|nom. sg. m.; rēs|rēs|thing, affair|nom. sg. f.; pūblica|pūblicus|public|nom. sg. f.; rēs|rēs|property, thing|nom. sg. f.; populī|populus|of the people|gen. sg. m.',
 ['fifth_declension','genitive','sum'],[],'palimpsest','De re publica',WP+'De_re_publica',formula=['inquit','rēs pūblica'],related=['v-res-publica'])
K('q-virgil-omnia-vincit','quote','republic',5,'Omnia vincit Amor: et nōs cēdāmus Amōrī.','Love conquers all: let us too yield to Love.',
 "In Virgil's last Eclogue (10.69, c. 39–38 BC) the poet-soldier Gallus, pining for Lycoris, admits no hard life or wild landscape will cure him. The line became a medieval motto: Chaucer's Prioress wears it on her brooch. Gallus was a real man, a poet and later the first prefect of Egypt.",
 "Omnia is neuter plural accusative (object); Amor is the subject. Cēdāmus is a subjunctive, 'let us yield', previewed here, and Amōrī a dative.",
 'Publius Vergilius Maro','Virgil, Eclogues','10.69','c. 39–38 BC',LL+'vergil/ec10.shtml','verified',None,
 'Omnia|omnis|all things|acc. pl. n.; vincit|vincō|conquers|3rd sg. pres.; Amor|amor|Love|nom. sg. m.; et|et|also|adv.; nōs|nōs|we|nom. pl.; cēdāmus|cēdō|let us yield|1st pl. pres. subj.; Amōrī|amor|to Love|dat. sg. m.',
 ['third_conjugation','third_declension','neuter_plural','dative'],['hortatory_subjunctive'],'amor','Eclogue 10',WP+'Eclogue_10')
K('q-livy-vestigia','quote','regal',5,'Vestīgia virī aliēnī, Collātīne, in lectō sunt tuō.','The traces of another man, Collatinus, are in your bed.',
 "Livy (1.58) tells how Lucretia, raped by the king's son Sextus Tarquinius, summoned her husband Collatinus and her father, told them this, and took her own life. Brutus swore vengeance and the monarchy fell (509 BC by tradition). For Romans, Lucretia stood for a wife's honour, and her story explained why they hated the title rēx.",
 "The story made Lucretia the model of Roman virtue and explained the Romans' hatred of kings. Grammar: in + ablative (in lectō … tuō) and a vocative (Collātīne).",
 'Lucretia (reported by Livy)','Livy, Ab urbe condita','1.58.7','c. 27–9 BC (event c. 509 BC)',LL+'livy/liv.1.shtml','traditional','Text verified in Livy; the speech is Livy\'s literary reconstruction of a legendary event.',
 'Vestīgia|vestīgium|traces|nom. pl. n.; virī|vir|of a man|gen. sg. m.; aliēnī|aliēnus|another\'s, of a stranger|gen. sg. m.; Collātīne|Collātīnus|Collatinus|voc. sg. m.; in|in|in|prep. + abl.; lectō|lectus|bed|abl. sg. m.; sunt|sum|are|3rd pl. pres.; tuō|tuus|your|abl. sg. m.',
 ['prep_ablative','genitive','vocative','neuter_plural','possessive_adjectives'],[],'lucretia','Lucretia',WP+'Lucretia')
K('q-nero-qualis','quote','empire',5,'Quālis artifex pereō!','What an artist dies in me!',
 "Declared a public enemy by the Senate in June AD 68, Nero fled to a freedman's villa outside Rome. As his grave was dug he wept and kept repeating this (Suetonius, Nero 49.1), mourning the performer, not the emperor. His death ended the line of Augustus, and a year of civil war among four emperors followed.",
 "Nero had sung and acted in public, scandalously for an emperor. Artifex, 'artist, craftsman', is a third-declension noun (artificis).",
 'Nero','Suetonius, Nero','49.1','June AD 68',LL+'suetonius/suet.nero.html','verified',None,
 'Quālis|quālis|what sort of, what a|nom. sg. m.; artifex|artifex|artist|nom. sg. m.; pereō|pereō|I die, perish|1st sg. pres.',
 ['third_declension','present_tense','first_person'],[],'nero','Nero',WP+'Nero')
K('i-vindolanda-brittunculi','artifact','empire',5,'Equitēs gladīs nōn ūtuntur, nec resīdunt Brittunculī ut iaculōs mittant.','The cavalry do not use swords, nor do the wretched Britons mount to throw javelins.',
 "A memo found at Vindolanda (Tab. Vindol. 164, c. AD 97–105) sizes up native fighters, perhaps for scouting or recruiting. Brittunculī, 'little Brits', is a sneering diminutive found nowhere else. The tablets survived because the waterlogged, oxygen-poor ground at Vindolanda kept the thin wooden leaves from rotting.",
 "Gladīs is a contracted form of gladiīs, ablative with ūtuntur ('use'). Resīdunt is from resīdō, 'settle down, sit on'; iaculōs treats iaculum as masculine: everyday army Latin.",
 None,'Vindolanda tablet (Tab. Vindol. 164)','lines 2–6','c. AD 97–105',RIB+'TabVindol164','verified','RIB edition: "equites gladis non ụtuntur equites nec residunt Brittunculi ut iaculos mittant" (the repeated equites is dropped here).',
 'Equitēs|eques|cavalry, horsemen|nom. pl. m.; gladīs|gladius|swords|abl. pl. m. (= gladiīs); nōn|nōn|not|adv.; ūtuntur|ūtor|they use (+ abl.)|3rd pl. pres. (deponent); nec|nec|nor|conj.; resīdunt|resīdō|they settle, mount|3rd pl. pres.; Brittunculī|Brittunculus|little Britons|nom. pl. m.; ut|ut|in order to|conj.; iaculōs|iaculum|javelins|acc. pl.; mittant|mittō|throw|3rd pl. pres. subj.',
 ['ablative_means','third_declension','present_tense','third_person_plural'],['deponent','subjunctive'],'vfort','Vindolanda',WP+'Vindolanda',subtype='daily_life',raw=('equites gladis non ụtuntur … nec residunt Brittunculi ut iaculos mittant','RIB online, Tab. Vindol. 164'))

# ---------------- UNIT 6: Imperium (perfect, imperfect, numerals) ----------------
K('q-titus-diem','quote','empire',6,'Amīcī, diem perdidī.','Friends, I have lost a day.',
 "Suetonius (Titus 8.1) says the emperor Titus, remembering at dinner that he had done nothing for anyone all day, made this 'memorable and rightly praised' remark. He reigned only AD 79–81. His reign saw the eruption of Vesuvius in AD 79 and a great fire at Rome in AD 80.",
 "His short reign saw the eruption of Vesuvius, a great fire at Rome and plague, and he opened the Colosseum. Diem is fifth declension; perdidī is perfect tense.",
 'Titus','Suetonius, Divus Titus','8.1','AD 79–81',LL+'suetonius/suet.titus.html','verified',None,
 'Amīcī|amīcus|friends|voc. pl. m.; diem|diēs|day|acc. sg. m.; perdidī|perdō|I have lost, wasted|1st sg. perf.',
 ['vocative','perfect_tense','fifth_declension','accusative'],[],'titus','Titus',WP+'Titus')
K('i-vindolanda-aegri','artifact','empire',6,'Ex eīs aegrī XV, volnerātī VI, lippientēs [X].','Of these: sick 15, wounded 6, with eye inflammation 10.',
 "A strength report of the First Cohort of Tungrians, 18 May c. AD 92–97 (Tab. Vindol. 154). Of 752 men only 296 were at Vindolanda, 337 being away at Coria (Corbridge); 31 of those present were unfit, leaving 265 ready. Lippientēs, 'the bleary-eyed', were men with eye inflammation, a common complaint in army camps.",
 "Roman numerals were simply written in the list. Volnerātī and lippientēs are participles used as nouns, previewed here; [X] is restored where the tablet is damaged.",
 None,'Vindolanda tablet (Tab. Vindol. 154)','lines 22–23','c. AD 92–97',RIB+'TabVindol154','verified','RIB edition: "ẹx eis aegri xv uolnerati vi ḷịp̣p̣ientes [x] summa eoṛ[um] x̣xxi".',
 'Ex|ex|of, out of|prep. + abl.; eīs|is|them|abl. pl.; aegrī|aeger|sick (men)|nom. pl. m.; XV|quīndecim|15|numeral; volnerātī|vulnerō|wounded|perf. pass. participle, nom. pl. m.; VI|sex|6|numeral; lippientēs|lippiō|with sore eyes|pres. participle, nom. pl. m.; X|decem|10|numeral',
 ['numerals','prep_ablative'],['participle_as_noun'],'surgical','Cohors I Tungrorum',WP+'Cohors_I_Tungrorum',subtype='daily_life',raw=('ex eis aegri xv uolnerati vi lippientes [x]','RIB online, Tab. Vindol. 154'))
K('i-vindolanda-socks','artifact','empire',6,'… tibi paria ūdōnum ab Sattuā, soleārum duo et subligāriōrum duo …','… (I have sent?) you … pairs of socks from Sattua, two pairs of sandals and two pairs of underpants …',
 "Part of a letter to a soldier at Vindolanda (Tab. Vindol. 346, c. AD 104–120): a parcel of socks, sandals and underpants, much needed in a British winter. The writer then greets the man's messmates by name. Ūdōnēs were felt or woollen socks, worn with sandals.",
 "Pāria (pairs) is followed by genitive plurals: ūdōnum, soleārum, subligāriōrum, 'pairs of socks, of sandals, of underpants'. Duo is the numeral 2.",
 None,'Vindolanda tablet (Tab. Vindol. 346)','i.2–4','c. AD 104–120',RIB+'TabVindol346','verified','RIB edition: "…r̥am tibi paria udoṇ[um] ṭ. ab Sattua solearuṃ [ duo ‣ et subligarioruṃ [ duo". The verb (perhaps mīsī) is lost.',
 'tibi|tū|to you|dat. sg.; paria|pār|pairs|acc. pl. n.; ūdōnum|ūdō|of socks|gen. pl. m.; ab|ab|from|prep. + abl.; Sattuā|Sattua|Sattua (a name)|abl. sg.; soleārum|solea|of sandals|gen. pl. f.; duo|duo|two|numeral; et|et|and|conj.; subligāriōrum|subligārium|of underpants|gen. pl. n.; duo|duo|two|numeral',
 ['numerals','genitive','prep_ablative'],['personal_pronouns'],'tabpeel3','Vindolanda tablets',WP+'Vindolanda_tablets',subtype='daily_life',raw=('… paria udoṇ[um] ṭ. ab Sattua solearuṃ [ duo ‣ et subligarioruṃ [ duo','RIB online, Tab. Vindol. 346'))
K('i-vindolanda-miror','artifact','empire',6,'Rogō tē, Veldei frāter, — mīror quod mihi tot tempus nihil rescrīpstī —','I ask you, brother Veldeius — I am surprised that you have written nothing back to me for so long —',
 "Chrauttius writes to Veldeius, his 'brother and old messmate', a groom of the governor in London (Tab. Vindol. 310, c. AD 97–105). He complains of silence, asks after family and wants the vet Virilis to send the shears he promised. Tot tempus for tantum tempus is another sign of everyday written Latin.",
 "Rescrīpstī is a shortened perfect (= rescrīpsistī). 'Tot tempus' is non-standard for tantum tempus. Veldei is the vocative of Veldeius.",
 'Chrauttius','Vindolanda tablet (Tab. Vindol. 310)','i.4–6','c. AD 97–105',RIB+'TabVindol310','verified','RIB edition: "et rogo te Veldei frater miror quod ṃihi tot tempus nihil rescripsti".',
 'Rogō|rogō|I ask|1st sg. pres.; tē|tū|you|acc. sg.; Veldei|Veldeius|Veldeius|voc. sg. m.; frāter|frāter|brother|voc. sg. m.; mīror|mīror|I am surprised|1st sg. pres. (deponent); quod|quod|that, because|conj.; mihi|ego|to me|dat. sg.; tot|tot|so much (non-standard)|indecl.; tempus|tempus|time|acc. sg. n.; nihil|nihil|nothing|acc. n.; rescrīpstī|rescrībō|you have written back|2nd sg. perf. (syncopated)',
 ['vocative','perfect_tense','first_person'],['personal_pronouns'],'shears','Vindolanda tablets',WP+'Vindolanda_tablets',subtype='daily_life',raw=('et rogo te Veldei frater miror quod ṃihi tot tempus nihil rescripsti','RIB online, Tab. Vindol. 310'),related=['v-frater-soror'])
K('q-gregory-vae','quote','early_medieval',6,'Vae diēbus nostrīs, quia periit studium litterārum ā nōbīs.','Woe to our times, for the study of letters has perished from among us.',
 'Gregory, bishop of Tours, opens his History of the Franks (c. 575–594) with this complaint he says people often voiced: nobody was left who could record the events of the age. So, apologising for his rustic Latin, he did it himself. His ten books are the main source for the history of Merovingian Gaul.',
 "His ten books are our main source for Merovingian Gaul and for Clovis. Grammar: dative after vae, a genitive (litterārum), ā + ablative and the perfect periit.",
 'Gregory of Tours','Gregory of Tours, Historiae (Decem libri historiarum)','praefatio','c. AD 575–594',LL+'gregorytours/gregorytours1.shtml','verified','Checked against the Latin Library preface: "vae diebus nostris, quia periit studium litterarum a nobis".',
 'Vae|vae|woe (+ dat.)|interjection; diēbus|diēs|days, times|dat. pl. m.; nostrīs|noster|our|dat. pl. m.; quia|quia|because|conj.; periit|pereō|has perished|3rd sg. perf.; studium|studium|study|nom. sg. n.; litterārum|littera|of letters, literature|gen. pl. f.; ā|ab|from|prep. + abl.; nōbīs|nōs|us|abl. pl.',
 ['perfect_tense','dative','genitive','prep_ablative','possessive_adjectives'],[],'gregory','History of the Franks',WP+'History_of_the_Franks',register='medieval')

# ---------------- UNIT 7: future, imperative, pronouns, demonstratives ----------------
K('q-juvenal-custodes','quote','empire',7,'Sed quis custōdiet ipsōs custōdēs?','But who will guard the guards themselves?',
 "Juvenal's sixth satire (early 2nd century AD) mocks the advice to lock up an unfaithful wife: the guards can be bribed too. The line is bracketed in many editions, since it belongs to a passage found in only one manuscript. The line now gets applied to any kind of power that has nobody watching it.",
 "It now stands for any problem of controlling those in power. Custōdiet is future tense; ipsōs is an intensive pronoun agreeing with custōdēs.",
 'Decimus Iunius Iuvenalis','Juvenal, Saturae','6.347–8 (= O 31–32)','early 2nd c. AD',LL+'juvenal/6.shtml','verified','Text verified; the lines belong to the "Oxford fragment" and are bracketed in the Latin Library text.',
 'Sed|sed|but|conj.; quis|quis|who?|nom. sg.; custōdiet|custōdiō|will guard|3rd sg. fut.; ipsōs|ipse|themselves|acc. pl. m.; custōdēs|custōs|guards|acc. pl. m.',
 ['future_tense','demonstratives','third_declension','accusative'],[],'juvenal','Quis custodiet ipsos custodes?',WP+'Quis_custodiet_ipsos_custodes%3F')
K('q-augustus-livia','quote','empire',7,'Līvia, nostrī coniugiī memor vīve, ac valē!','Livia, live on mindful of our marriage, and farewell!',
 "Augustus died at Nola on 19 August AD 14 in Livia's arms with these words (Suetonius, Aug. 99.1). Just before, he had asked his friends whether he had played his part in the comedy of life well. They had been married for more than 50 years.",
 "They had been married for over 50 years. Vīve and valē are imperatives; nostrī coniugiī is a genitive depending on memor, 'mindful of'.",
 'Augustus','Suetonius, Divus Augustus','99.1','19 August AD 14',LL+'suetonius/suet.aug.html','verified',None,
 'Līvia|Līvia|Livia|voc. sg. f.; nostrī|noster|our|gen. sg. n.; coniugiī|coniugium|marriage|gen. sg. n.; memor|memor|mindful (+ gen.)|nom. sg.; vīve|vīvō|live!|imperative sg.; ac|ac|and|conj.; valē|valeō|farewell|imperative sg.',
 ['imperative','vocative','genitive','possessive_adjectives'],[],'livia','Livia',WP+'Livia',related=['q-resgestae-annos'])
K('q-caesar-aquilifer','quote','republic',7,'Dēsilīte, mīlitēs, nisi vultis aquilam hostibus prōdere.','Jump down, soldiers, unless you want to betray the eagle to the enemy.',
 "When Caesar's ships reached Britain in 55 BC, his soldiers hesitated to leap into deep water under fire. The eagle-bearer of the Tenth Legion shouted this, jumped overboard and advanced with the standard; shamed, the men followed (BG 4.25). Losing the eagle was the worst disgrace a legion could suffer.",
 "Losing the eagle was the worst disgrace a legion could suffer. Dēsilīte is a plural imperative; hostibus is a dative (to the enemy).",
 'Eagle-bearer of the Tenth Legion (reported by Caesar)','Caesar, De bello Gallico','4.25.3','55 BC',LL+'caesar/gall4.shtml','verified','Caesar: "desilite, inquit, milites, nisi vultis aquilam hostibus prodere". Card omits inquit.',
 'Dēsilīte|dēsiliō|jump down!|imperative pl.; mīlitēs|mīles|soldiers|voc. pl. m.; nisi|nisi|unless|conj.; vultis|volō|you want|2nd pl. pres.; aquilam|aquila|eagle (standard)|acc. sg. f.; hostibus|hostis|to the enemy|dat. pl. m.; prōdere|prōdō|to betray|pres. inf.',
 ['imperative','vocative','dative','second_person_plural'],['infinitive'],'eagle','Caesar\'s invasions of Britain',WP+'Caesar%27s_invasions_of_Britain')
K('q-virgil-care-pater','quote','empire',7,'Ergō age, cāre pater, cervīcī impōnere nostrae.','Come then, dear father, climb onto my shoulders.',
 'As Troy burns (Aeneid 2.707), Aeneas lifts his old father Anchises onto his shoulders and takes his small son Iulus by the hand. The scene became the image of Roman pietās, duty to family and gods. His wife Creusa, following behind, was lost in the flight.',
 "Literally 'be placed on our neck': impōnere is a passive imperative, previewed here. Cervīcī … nostrae is a dative split around the verb; nostrae is the poetic 'our' for 'my'.",
 'Aeneas','Virgil, Aeneid','2.707','c. 29–19 BC',LL+'vergil/aen2.shtml','verified',None,
 'Ergō|ergō|therefore, then|adv.; age|agō|come on!|imperative sg. (formula); cāre|cārus|dear|voc. sg. m.; pater|pater|father|voc. sg. m.; cervīcī|cervīx|neck, shoulders|dat. sg. f.; impōnere|impōnō|be placed (climb)|imperative sg. passive; nostrae|noster|our (= my)|dat. sg. f.',
 ['imperative','vocative','dative','possessive_adjectives','adjective_agreement'],['passive_voice'],'bernini','Aeneas, Anchises, and Ascanius',WP+'Aeneas,_Anchises,_and_Ascanius',formula=['age'])
K('q-morituri','quote','empire',7,'Havē, imperātor, moritūrī tē salūtant!','Hail, emperor, those who are about to die salute you!',
 "Suetonius (Claud. 21.6) says it was shouted by fighters in a mock sea battle on the Fucine Lake in AD 52, not, as often thought, by gladiators every time. Claudius answered 'Aut nōn' ('or not'), which they took as a pardon. The phrase is recorded only on this one occasion.",
 "They refused to fight until he forced them. Havē is Suetonius's spelling of avē; moritūrī is a future participle used as a noun, previewed here.",
 'Naumachiarii (reported by Suetonius)','Suetonius, Divus Claudius','21.6','AD 52',LL+'suetonius/suet.claudius.html','verified','Suetonius: "Have imperator, morituri te salutant!"',
 'Havē|aveō|hail!|imperative (formula); imperātor|imperātor|emperor, general|voc. sg. m.; moritūrī|morior|those about to die|fut. participle, nom. pl. m.; tē|tū|you|acc. sg.; salūtant|salūtō|salute|3rd pl. pres.',
 ['present_tense','vocative','personal_pronouns','third_person_plural'],['participle_as_noun'],'naumachia','Ave Imperator, morituri te salutant',WP+'Ave_Imperator,_morituri_te_salutant',formula=['havē'])
K('q-constantine-hoc-signo','quote','late_antiquity',7,'In hōc signō vincēs.','In this sign you will conquer.',
 "Before the battle of the Milvian Bridge in AD 312, Constantine is said to have seen a cross of light in the sky with words promising victory. Eusebius reports them in Greek (Life of Constantine 1.28); the Latin became the familiar form. His soldiers then marked their shields with the Chi-Rho, the first two Greek letters of Christ's name.",
 "Constantine won, took Rome and went on to favour Christianity. Hōc is the ablative of the demonstrative hic; vincēs is the future of vincō.",
 'Constantine the Great','Eusebius, Vita Constantini (Greek)','1.28','AD 312',WP+'In_hoc_signo_vinces','traditional','Eusebius gives "τούτῳ νίκα" ("by this, conquer"); "in hoc signo vinces" is the later Latin form.',
 'In|in|in|prep. + abl.; hōc|hic|this|abl. sg. n.; signō|signum|sign|abl. sg. n.; vincēs|vincō|you will conquer|2nd sg. fut.',
 ['future_tense','demonstratives','prep_ablative'],[],'constantine','In hoc signo vinces',WP+'In_hoc_signo_vinces',register='ecclesiastical')

# ---------------- UNIT 8: infinitive, indirect statement ----------------
K('q-einhard-temptabat','quote','early_medieval',8,'Temptābat et scrībere, tabulāsque et cōdicellōs … in lectō sub cervīcālibus circumferre solēbat.','He also tried to write, and used to carry tablets and notebooks around … under the pillows on his bed.',
 "Einhard's Life of Charlemagne (ch. 25, c. 830) says the emperor kept writing tablets under his pillow to practise forming letters in spare moments, but the effort, begun late, had little success. Einhard had served at Charlemagne's court himself and modelled the Life on Suetonius' lives of the emperors.",
 "Yet the same king made schools and accurate copying a priority across his empire. Temptābat and solēbat are imperfects of repeated action, each completed by an infinitive.",
 'Einhard','Einhard, Vita Karoli Magni','25','c. AD 830',LL+'ein.html','verified','Text verified; "ad hoc" omitted (marked …).',
 'Temptābat|temptō|he tried|3rd sg. impf.; et|et|also|adv.; scrībere|scrībō|to write|pres. inf.; tabulāsque|tabula + -que|and tablets|acc. pl. f.; et|et|and|conj.; cōdicellōs|cōdicillus|notebooks|acc. pl. m.; in|in|in|prep. + abl.; lectō|lectus|bed|abl. sg. m.; sub|sub|under|prep. + abl.; cervīcālibus|cervīcal|pillows|abl. pl. n.; circumferre|circumferō|to carry around|pres. inf.; solēbat|soleō|he used to|3rd sg. impf.',
 ['imperfect','infinitive','enclitic_que','prep_ablative'],[],'einhard','Vita Karoli Magni',WP+'Vita_Karoli_Magni',register='medieval')
K('q-hugh-omnia-disce','quote','high_medieval',8,'Omnia disce; vidēbis posteā nihil esse superfluum.','Learn everything; you will see afterwards that nothing is superfluous.',
 'Hugh of St Victor, teaching at the abbey of St Victor in Paris in the 1120s, recalls in his Didascalicon (6.3) how as a schoolboy he learnt even trivial things, and none proved useless. The Didascalicon was written as a guide to everything a student should read, and in what order.',
 "He adds: 'Coartāta scientia iūcunda nōn est', narrow knowledge is no pleasure. Nihil esse superfluum is an indirect statement (accusative + infinitive) after vidēbis.",
 'Hugh of St Victor','Hugh of St Victor, Didascalicon','6.3','c. 1120s',LL+'hugo/hugo6.html','verified',None,
 'Omnia|omnis|everything|acc. pl. n.; disce|discō|learn!|imperative sg.; vidēbis|videō|you will see|2nd sg. fut.; posteā|posteā|afterwards|adv.; nihil|nihil|nothing|acc. n.; esse|sum|to be|pres. inf.; superfluum|superfluus|superfluous|acc. sg. n.',
 ['imperative','future_tense','indirect_statement','infinitive'],[],'hugh','Hugh of Saint Victor',WP+'Hugh_of_Saint_Victor',register='medieval')
K('i-vindolanda-viae','artifact','empire',8,'… iūmenta nōn cūrāvī vexāre dum viae male sunt.','… I did not want to injure the animals while the roads are bad.',
 "Octavius, a trader at Vindolanda (Tab. Vindol. 343, c. AD 104–120), writes to his 'brother' Candidus: he has bought 5,000 modii of grain, urgently needs cash, and hasn't fetched hides from Catterick because the roads would hurt his draught animals. Cataractonium is the Roman name of Catterick in North Yorkshire, on the main road north to the frontier.",
 "The tablet spells vexsare. Cūrāvī + infinitive means 'I took care / bothered to'. The dum clause (while) is previewed here.",
 'Octavius','Vindolanda tablet (Tab. Vindol. 343)','ii.13–15','c. AD 104–120',RIB+'TabVindol343','verified','RIB edition: "iumenṭa non curaui uexsaṛe dum uiae male sunt".',
 'iūmenta|iūmentum|draught animals|acc. pl. n.; nōn|nōn|not|adv.; cūrāvī|cūrō|I cared, bothered|1st sg. perf.; vexāre|vexō|to harm, shake about|pres. inf.; dum|dum|while|conj.; viae|via|roads|nom. pl. f.; male|male|badly, in a bad state|adv.; sunt|sum|are|3rd pl. pres.',
 ['perfect_tense','infinitive','neuter_plural'],['dum_clause'],'vfort2','Cataractonium',WP+'Cataractonium',subtype='daily_life',raw=('iumenṭa non curaui uexsaṛe dum uiae male sunt','RIB online, Tab. Vindol. 343'))

# ---------------- UNIT 9: passive, participles ----------------
K('i-bayeux-harold','artifact','high_medieval',9,'HIC HAROLD REX INTERFECTVS EST — Hīc Harold rēx interfectus est.','Here King Harold was killed.',
 "Scene 57 of the Bayeux Tapestry shows Harold's death at Hastings, 14 October 1066. Whether he is the figure pulling an arrow from his eye or the one cut down beside him is still debated: the caption spans both. Harold had been king for only nine months, and his death ended Anglo-Saxon rule in England.",
 "Interfectus est is a perfect passive (was killed). The Latin keeps the English name Harold undeclined.",
 'Harold Godwinson','Bayeux Tapestry','scene 57','c. 1070s (event 1066)',WP+'Bayeux_Tapestry_tituli','verified',None,
 'Hīc|hīc|here|adverb; Harold|Harold|Harold|nom. (undeclined); rēx|rēx|king|nom. sg. m.; interfectus est|interficiō|was killed|3rd sg. perf. pass.',
 ['perfect_passive','nominative'],[],'harold','Battle of Hastings',WP+'Battle_of_Hastings',subtype='inscription',raw=('HIC HAROLD REX INTERFECTVS EST','embroidered caption'),register='medieval',related=['i-bayeux-willelm'])
K('q-augustine-regna','quote','late_antiquity',9,'Remōtā itaque iūstitiā quid sunt rēgna nisi magna latrōcinia?','So, with justice removed, what are kingdoms but great robber bands?',
 "Writing the City of God after the sack of Rome in 410, Augustine argues (4.4) that without justice a state is a gang on a large scale, like the pirate who told Alexander: I have one ship and am called a robber; you have a fleet and are called emperor. Augustine took the pirate story from Cicero's De re publica.",
 "Remōtā iūstitiā is an ablative absolute ('justice having been removed'), previewed here. Rēgna and latrōcinia are neuter plurals.",
 'Augustine of Hippo','Augustine, De civitate Dei','4.4','c. AD 413–426',LL+'augustine/civ4.shtml','verified',None,
 'Remōtā|removeō|removed|perf. pass. participle, abl. sg. f.; itaque|itaque|and so|adv.; iūstitiā|iūstitia|justice|abl. sg. f.; quid|quis|what?|nom. sg. n.; sunt|sum|are|3rd pl. pres.; rēgna|rēgnum|kingdoms|nom. pl. n.; nisi|nisi|except, but|conj.; magna|magnus|great|nom. pl. n.; latrōcinia|latrōcinium|robber bands|nom. pl. n.',
 ['neuter_plural','adjectives','sum','participle'],['ablative_absolute'],'civdei','The City of God',WP+'The_City_of_God',register='ecclesiastical',related=['q-gesta-latro'])

# ---------------- UNIT 10: relative clauses ----------------
K('q-virgil-felix','quote','empire',10,'Fēlīx quī potuit rērum cognōscere causās.','Happy the one who has been able to learn the causes of things.',
 "In Georgics 2.490 (c. 29 BC) Virgil praises the philosopher, probably Lucretius, who understands nature and so has trampled fear of fate and death underfoot. It is the motto of the London School of Economics. The Georgics were presented as a poem about farming, finished after Octavian's victory at Actium.",
 "Quī potuit is a relative clause (the one who…); potuit + cognōscere is possum with an infinitive. Rērum is genitive plural of rēs.",
 'Publius Vergilius Maro','Virgil, Georgics','2.490','c. 29 BC',LL+'vergil/geo2.shtml','verified',None,
 'Fēlīx|fēlīx|happy, fortunate|nom. sg. m.; quī|quī|(the one) who|rel. pron. nom. sg. m.; potuit|possum|was able, has been able|3rd sg. perf.; rērum|rēs|of things|gen. pl. f.; cognōscere|cognōscō|to learn, understand|pres. inf.; causās|causa|causes|acc. pl. f.',
 ['relative_clause','possum_infinitive','perfect_tense','genitive','fifth_declension'],[],'majorana','Georgics',WP+'Georgics')
K('q-bernard-nanos','quote','high_medieval',10,'Dīcēbat Bernardus Carnotēnsis nōs esse quasi nānōs, gigantum umerīs īnsidentēs.','Bernard of Chartres used to say that we are like dwarfs sitting on the shoulders of giants.',
 "John of Salisbury (Metalogicon 3.4, 1159) reports his teacher's image: we see more and farther than the ancients, not by sharper sight, but because their size lifts us up. Newton echoed it in a letter to Hooke of February 1676 (1675 Old Style). Bernard taught at the cathedral school of Chartres, whose south transept windows show prophets carrying the evangelists on their shoulders.",
 "Nōs esse is an indirect statement after dīcēbat; īnsidentēs is a present participle agreeing with nānōs. Older printings read 'gigantium humeris incidentes'.",
 'Bernard of Chartres (reported by John of Salisbury)','John of Salisbury, Metalogicon','3.4','1159','https://www.logicmuseum.com/wiki/Authors/John_of_Salisbury/Metalogicon/Liber_3','verified','Text as in the modern edition (Hall); Migne PL 199.900 prints "gigantium humeris incidentes". Quantity of the o in Carnotensis uncertain, left unmarked.',
 'Dīcēbat|dīcō|used to say|3rd sg. impf.; Bernardus|Bernardus|Bernard|nom. sg. m.; Carnotēnsis|Carnotēnsis|of Chartres|nom. sg. m.; nōs|nōs|we|acc. pl.; esse|sum|to be|pres. inf.; quasi|quasi|like, as if|adv.; nānōs|nānus|dwarfs|acc. pl. m.; gigantum|gigās|of giants|gen. pl. m.; umerīs|umerus|on the shoulders|dat./abl. pl. m.; īnsidentēs|īnsideō|sitting on|pres. participle, acc. pl. m.',
 ['indirect_statement','imperfect','present_participle','genitive'],[],'chartres','Standing on the shoulders of giants',WP+'Standing_on_the_shoulders_of_giants',register='medieval')
K('q-vegetius-pacem','quote','late_antiquity',10,'Igitur quī dēsīderat pācem, praeparet bellum.','Therefore let whoever desires peace prepare for war.',
 "Vegetius' Epitome of Military Science (late 4th or 5th century), the most-copied Roman military manual of the Middle Ages, gives this in the preface to Book 3. The snappier 'Sī vīs pācem, parā bellum' is a later paraphrase. Vegetius was not a soldier but an official who gathered his advice from older writers.",
 "Quī dēsīderat is a relative clause serving as subject. Praeparet is a jussive subjunctive ('let him prepare'), previewed here.",
 'Publius Flavius Vegetius Renatus','Vegetius, Epitoma rei militaris','3, praefatio','late 4th–5th c. AD',LL+'vegetius3.html','verified',None,
 'Igitur|igitur|therefore|adv.; quī|quī|whoever|rel. pron. nom. sg. m.; dēsīderat|dēsīderō|desires|3rd sg. pres.; pācem|pāx|peace|acc. sg. f.; praeparet|praeparō|let him prepare|3rd sg. pres. subj.; bellum|bellum|war|acc. sg. n.',
 ['relative_clause','present_tense','third_declension','accusative'],['jussive_subjunctive'],'vegetius','Si vis pacem, para bellum',WP+'Si_vis_pacem,_para_bellum')
