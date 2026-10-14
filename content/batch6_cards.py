# Batch 6 card texts. Gloss format: "word|lemma|meaning|parse; ..."  (no semicolons inside meanings)
# K(id,type,era,unit,latin,translation,context,more,person,work,cit,date,source_url,conf,note,gloss,target,preview,img,lm_label,lm_url, **extra)
LL='https://www.thelatinlibrary.com/'
RIB='https://romaninscriptionsofbritain.org/inscriptions/'
EDCS='https://edcs.hist.uzh.ch/search'
WP='https://en.wikipedia.org/wiki/'
CON='Constructed teaching sentence (not a quotation).'
CARDS=[]
def K(*a,**kw): CARDS.append((a,kw))

# ---------------- UNIT 1: Urbs ----------------
K('v-vesta-dea','vocab','regal',1,'Vesta dea est; Vestālēs sacerdōtēs sunt.','Vesta is a goddess; the Vestals are priestesses.',
 "Vesta was the goddess of the hearth, and her sacred fire in the Forum was believed to keep Rome safe. Six Vestal Virgins tended it day and night, serving for thirty years from childhood. If the fire went out, it was taken as a terrible omen. Dea is a singular noun and sacerdōtēs a plural one, so the verbs are est and sunt.",
 "Vestals had rare privileges: they could make wills and travel in carriages, and a condemned prisoner who met one by chance was pardoned. A Vestal who broke her vow of chastity was buried alive.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Vesta|Vesta|Vesta|nom. sg. f.; dea|dea|goddess|nom. sg. f.; est|sum|is|3rd sg. pres.; Vestālēs|Vestālis|the Vestals|nom. pl. f.; sacerdōtēs|sacerdōs|priestesses|nom. pl. f.; sunt|sum|are|3rd pl. pres.',
 ['nominative','sum'],[],'vestal','Vestal Virgin',WP+'Vestal_Virgin',subtype='vocab')
K('v-trias-capitolina','vocab','regal',1,'Iuppiter, Iūnō et Minerva deī sunt.','Jupiter, Juno and Minerva are gods.',
 "These three were the Capitoline Triad, worshipped together in Rome's greatest temple on the Capitoline Hill. Jupiter was king of the gods, Juno his wife and queen, and Minerva the goddess of wisdom and crafts. Roman colonies across the empire built their own capitolium temples to the same three gods. Deī is the plural of deus, and a mixed group of gods and goddesses takes the masculine plural.",
 "The Guidonia group, found near Rome in 1992, is the only surviving statue group of all three gods together, with Jupiter's eagle, Juno's peacock and Minerva's owl.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Iuppiter|Iuppiter|Jupiter|nom. sg. m.; Iūnō|Iūnō|Juno|nom. sg. f.; et|et|and|conj.; Minerva|Minerva|Minerva|nom. sg. f.; deī|deus|gods|nom. pl. m.; sunt|sum|are|3rd pl. pres.',
 ['nominative','sum'],[],'triad','Capitoline Triad',WP+'Capitoline_Triad',subtype='vocab')
K('i-pompeii-felicitas','artifact','empire',1,'HIC HABITAT FELICITAS — Hīc habitat Fēlīcitās.','Here lives Good Luck.',
 "This short sign was carved on a plaque above an oven in a Pompeian bakery, beside a lucky charm meant to ward off the evil eye. Fēlīcitās, 'good fortune', was also worshipped as a goddess. The verb habitat sits between the adverb hīc, 'here', and its subject, the nominative Fēlīcitās. Pompeian shopkeepers often painted wishes for profit and luck on their walls.",
 "The plaque is now in the Naples Archaeological Museum. English felicity and Felicity come from fēlīcitās.",
 None,'Pompeii inscription (CIL IV 1454)','—','before AD 79',EDCS,'verified','Text checked in EDCS (CIL IV 1454).',
 'Hīc|hīc|here|adv.; habitat|habitō|lives|3rd sg. pres.; Fēlīcitās|fēlīcitās|Good Luck, Happiness|nom. sg. f.',
 ['nominative','word_order'],['present_tense'],'pompeii','Pompeii',WP+'Pompeii',subtype='inscription',raw=('HIC HABITAT FELICITAS','EDCS (CIL IV 1454)'))

# ---------------- UNIT 2: Familia ----------------
K('i-pompeii-salve-lucru','artifact','empire',2,'SALVE LVCRV — Salvē, lucrum!','Welcome, profit!',
 "Visitors to the House of Siricus at Pompeii stepped over this greeting set into the entrance mosaic. Instead of welcoming the guest, it hails profit, as if money were a friend arriving at the door. Lucrum is addressed directly, in the vocative, which for neuter nouns looks the same as the nominative. Merchants' houses in Pompeii often show this frank delight in gain.",
 "The final M of lucrum is missing in the mosaic, as it often was in everyday speech. English lucrative and lucre come from lucrum.",
 None,'Pompeii mosaic inscription (CIL X 874)','—','before AD 79',EDCS,'verified','Text checked in EDCS (EDCS-11400966, CIL X 874): Salve lucru[m].',
 'Salvē|salveō|welcome, hello|imperative; lucrum|lucrum|profit|voc. sg. n.',
 ['vocative'],[],'salve','Pompeii',WP+'Pompeii',subtype='inscription',raw=('SALVE LVCRV','EDCS-11400966 (CIL X 874)'))
K('q-virgil-nate','quote','empire',2,'Nāte, meae vīrēs, mea magna potentia sōlus','My son, my strength, you alone my great power',
 "In Aeneid 1 Venus calls on her son Cupid to make Queen Dido fall in love with Aeneas, so that Carthage will shelter him. She heaps up titles in the vocative: nāte, 'son', then 'my strength', 'my great power'. The possessive adjectives meae and mea agree with the nouns they describe. Venus's plan works, and leads to Dido's tragedy in Book 4.",
 "Cupid takes the shape of Aeneas's little son Ascanius and sits on Dido's lap at the banquet. Vīrēs, 'strength', is the plural of vīs.",
 'Virgil (speech of Venus)','Virgil, Aeneid','1.664','c. 19 BC',LL+'vergil/aen1.shtml','verified','Spoken by Venus in the poem.',
 'Nāte|nātus|son|voc. sg. m.; meae|meus|my|nom. pl. f.; vīrēs|vīs|strength|nom. pl. f.; mea|meus|my|nom. sg. f.; magna|magnus|great|nom. sg. f.; potentia|potentia|power|nom. sg. f.; sōlus|sōlus|alone|nom. sg. m.',
 ['vocative','possessive_adjectives'],[],'venuscupid','Cupid',WP+'Cupid')

# ---------------- UNIT 3: Legio ----------------
K('q-hannibal-ad-portas','quote','republic',3,'Hannibal ad portās!','Hannibal is at the gates!',
 "After Hannibal crushed the Romans at Cannae in 216 BC, panic swept Rome, and in 211 BC he marched right up to the city walls. The cry became a proverb for any danger on the doorstep. Cicero uses it in this form in On Ends, and 'Hannibal ante portās' in his first Philippic. The sentence has no verb: portās is accusative after ad, 'to, at'.",
 "Roman parents were said to frighten children with the phrase. Hannibal never attacked Rome itself, as he lacked siege equipment.",
 'Proverb (quoted by Cicero)','Cicero, De finibus','4.22','45 BC',LL+'cicero/fin4.shtml','traditional','A proverb. Cicero has si Hannibal ad portas venisset (De fin. 4.22) and Hannibal ante portas (Phil. 1.11).',
 'Hannibal|Hannibal|Hannibal|nom. sg. m.; ad|ad|at, to|prep. + acc.; portās|porta|the gates|acc. pl. f.',
 ['nominative','accusative'],[],'hannibal','Hannibal ad portas',WP+'Hannibal_ad_portas')
K('v-centurio-vocat','vocab','empire',3,'Centuriō mīlitēs vocat; mīlitēs currunt.','The centurion calls the soldiers; the soldiers run.',
 "A centurion commanded a century, which in the imperial army meant about 80 men, not 100. Centurions were the army's professional backbone, promoted for long service and courage, and they carried a vine stick for discipline. In the first clause mīlitēs is the accusative object; in the second it is the nominative subject, so the verb is plural.",
 "A legion had about sixty centurions. The senior one, the prīmus pīlus, was among the most respected men in the army.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Centuriō|centuriō|centurion|nom. sg. m.; mīlitēs|mīles|soldiers|acc. pl. m.; vocat|vocō|calls|3rd sg. pres.; mīlitēs|mīles|soldiers|nom. pl. m.; currunt|currō|they run|3rd pl. pres.',
 ['third_person_plural','accusative'],[],'centurion','Centurion',WP+'Centurion',subtype='vocab')
K('v-cornicen','vocab','empire',3,'Cornicen cornū īnflat; mīlitēs signa movent.','The horn-player blows the horn; the soldiers move the standards.',
 "Roman armies passed orders by sound. The cornicen blew the cornū, a large curved bronze horn, and the soldiers followed the standards, signa, which showed where each unit should go. 'Moving the standards' meant setting off on the march or into battle. Signa is a neuter plural ending in -a.",
 "Cornicen is made from cornū, 'horn', and canō, 'sing, play'. The tubicen played the straight trumpet, the tuba.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Cornicen|cornicen|horn-player|nom. sg. m.; cornū|cornū|horn|acc. sg. n.; īnflat|īnflō|blows|3rd sg. pres.; mīlitēs|mīles|soldiers|nom. pl. m.; signa|signum|standards|acc. pl. n.; movent|moveō|they move|3rd pl. pres.',
 ['third_person_plural','neuter_plural'],[],'cornicen','Cornicen',WP+'Cornicen',subtype='vocab')
K('v-pila-iaciunt','vocab','republic',3,'Mīlitēs pīla in hostēs iaciunt.','The soldiers throw their javelins at the enemy.',
 "A legionary carried two heavy javelins, pīla. Just before the lines met, the soldiers threw them, then charged with their swords. The long soft-iron shank of a pīlum bent on impact, so the enemy could not throw it back and a shield it stuck in became useless. Hostēs, 'the enemy', is plural in Latin.",
 "Caesar describes Gauls throwing away their shields because pīla had pinned them together (Gallic War 1.25).",
 None,'Constructed','—','—',None,'constructed',CON,
 'Mīlitēs|mīles|soldiers|nom. pl. m.; pīla|pīlum|javelins|acc. pl. n.; in|in|against, at|prep. + acc.; hostēs|hostis|the enemy|acc. pl. m.; iaciunt|iaciō|they throw|3rd pl. pres.',
 ['third_person_plural','neuter_plural'],[],'pilum','Pilum',WP+'Pilum',subtype='vocab')
K('v-gladius-scutum','vocab','empire',3,'Legiōnārius gladium et scūtum portat.','The legionary carries a sword and a shield.',
 "The gladius was a short stabbing sword about 50 cm long, worn on the right side. The curved rectangular scūtum covered the body from shoulder to knee and let soldiers lock shields into a wall. Both nouns are accusative, the things being carried. English gladiator comes from gladius, a 'swordsman'.",
 "Gladiolus, the flower, means 'little sword', after its blade-shaped leaves.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Legiōnārius|legiōnārius|legionary|nom. sg. m.; gladium|gladius|sword|acc. sg. m.; et|et|and|conj.; scūtum|scūtum|shield|acc. sg. n.; portat|portō|carries|3rd sg. pres.',
 ['accusative','present_tense'],[],'gladius','Gladius',WP+'Gladius',subtype='vocab')

# ---------------- UNIT 4: Forum & Senate ----------------
K('q-cicero-o-tempora','quote','republic',4,'Ō tempora, ō mōrēs! Senātus haec intellegit. Cōnsul videt; hic tamen vīvit.','What times, what morals! The Senate understands these things. The consul sees them; and yet this man lives.',
 "Cicero, consul in 63 BC, hurled these words at Catiline in the Senate, with the conspirator sitting in front of him. The Senate knows of the plot, the consul sees it, and still the traitor is alive. The short sentences hit like blows. Ō tempora and ō mōrēs are exclamations, and senātus is a fourth-declension noun.",
 "Haec, 'these things', and hic, 'this man', are demonstratives. The phrase ō tempora, ō mōrēs is still used to complain about modern times.",
 'Cicero','Cicero, In Catilinam','1.2','63 BC',LL+'cicero/cat1.shtml','verified',None,
 'Ō|ō|O|interj.; tempora|tempus|times|acc. pl. n. (exclam.); mōrēs|mōs|morals, customs|acc. pl. m. (exclam.); Senātus|senātus|the Senate|nom. sg. m.; haec|hic|these things|acc. pl. n.; intellegit|intellegō|understands|3rd sg. pres.; Cōnsul|cōnsul|the consul|nom. sg. m.; videt|videō|sees|3rd sg. pres.; hic|hic|this man|nom. sg. m.; tamen|tamen|yet|adv.; vīvit|vīvō|lives|3rd sg. pres.',
 ['present_tense','neuter_plural'],['demonstratives'],'ciceroapsley','Catilinarian Orations',WP+'Catilinarian_orations')
K('q-cicero-civis','quote','republic',4,'Cīvis Rōmānus sum.','I am a Roman citizen.',
 "Cicero prosecuted Verres, governor of Sicily, in 70 BC for corruption and cruelty. His most shocking charge was that Verres had a man named Gavius flogged and crucified, although Gavius kept crying out this sentence. A Roman citizen had the right to appeal and could not legally be flogged or crucified. Cicero says the cry had brought help to many in faraway lands.",
 "Saint Paul claims the same right in Acts 22:25. Lord Palmerston echoed the phrase in 1850 to defend British subjects abroad.",
 'Gavius (reported by Cicero)','Cicero, In Verrem','2.5.162','70 BC',LL+'cicero/verres.2.5.shtml','verified',None,
 'Cīvis|cīvis|citizen|nom. sg. m.; Rōmānus|Rōmānus|Roman|nom. sg. m.; sum|sum|I am|1st sg. pres.',
 ['adjective_agreement','first_person'],[],'togatus','Roman citizenship',WP+'Roman_citizenship')
K('q-cicero-cui-bono','quote','republic',4,'Cui bonō?','Who benefits?',
 "Cicero (defending Sextus Roscius on a murder charge, 80 BC) recalls the judge Lucius Cassius, famous for asking 'to whom was it a benefit?' in every case. People rarely commit crimes without hoping to gain something, so find who gains and you may find the culprit. Cui and bonō are both datives: literally 'to whom (is it) for a benefit?'",
 "This 'double dative' pairs a person with a purpose. The question is still used by detectives, lawyers and journalists.",
 'Lucius Cassius Longinus Ravilla (quoted by Cicero)','Cicero, Pro Sexto Roscio Amerino','84','80 BC',LL+'cicero/sex.rosc.shtml','verified','Cicero attributes the question to the judge L. Cassius.',
 'Cui|quis|to whom|dat. sg. (interrog.); bonō|bonum|for a benefit|dat. sg. n.',
 ['dative'],[],'basilica','Cui bono',WP+'Cui_bono')
K('q-cicero-o-fortunatam','quote','republic',4,'Ō fortūnātam nātam mē cōnsule Rōmam!','O lucky Rome, born in my consulship!',
 "Cicero wrote an epic poem about his own consulship of 63 BC, and this line made him a laughing-stock for centuries. Juvenal quotes it in Satire 10 (about AD 120) and jokes that if Cicero had only written such poetry, Antony's swords would have spared him. The jingle fortūnātam nātam is part of what made it ridiculous. Every word agrees with Rōmam, an accusative of exclamation.",
 "Mē cōnsule, 'with me as consul', is an ablative absolute. Cicero was killed on Antony's orders in 43 BC.",
 'Cicero (quoted by Juvenal)','Juvenal, Saturae','10.122','c. AD 120',LL+'juvenal/10.shtml','verified','Fragment of Cicero\'s lost poem De consulatu suo, preserved by Juvenal and Quintilian.',
 'Ō|ō|O|interj.; fortūnātam|fortūnātus|lucky|acc. sg. f.; nātam|nāscor|born|acc. sg. f. perf. part.; mē|ego|me|abl. sg.; cōnsule|cōnsul|consul|abl. sg. m.; Rōmam|Rōma|Rome|acc. sg. f. (exclam.)',
 ['adjective_agreement','accusative'],['ablative_absolute'],'ciceroludovisi','Cicero',WP+'Cicero')
K('q-cato-vir-bonus','quote','republic',4,'Vir bonus dīcendī perītus','A good man skilled in speaking',
 "This was Cato the Elder's definition of an orator, quoted by Quintilian at the start of the last book of his Training of the Orator (about AD 95). For Cato and Quintilian, eloquence without good character was dangerous, so the good man came first. Dīcendī is a genitive, 'of speaking', depending on the adjective perītus, 'skilled in'.",
 "Dīcendī is a gerund, a verbal noun. Cato (234–149 BC) also gave the advice rem tenē, verba sequentur: 'hold on to the matter, the words will follow'.",
 'Cato the Elder (quoted by Quintilian)','Quintilian, Institutio oratoria','12.1.1','c. AD 95',LL+'quintilian/quintilian.institutio12.shtml','verified','Quintilian says the definition is Cato\'s.',
 'Vir|vir|man|nom. sg. m.; bonus|bonus|good|nom. sg. m.; dīcendī|dīcō|of speaking|gen. gerund; perītus|perītus|skilled|nom. sg. m.',
 ['adjectives','genitive'],[],'arringatore','Quintilian',WP+'Quintilian')
K('q-cicero-silent-leges','quote','republic',4,'Silent enim lēgēs inter arma.','For laws fall silent amid weapons.',
 "In 52 BC Milo's armed escort killed his rival Clodius in a brawl on the Appian Way, and Cicero defended Milo for murder. He argued that killing in self-defence is lawful, because when weapons are drawn the laws cannot protect you. Soldiers guarded the court, and Cicero reportedly spoke badly. Milo was convicted and went into exile at Massilia.",
 "The phrase is often quoted as inter arma silent lēgēs, especially in debates about civil liberties in wartime.",
 'Cicero','Cicero, Pro Milone','11','52 BC',LL+'cicero/milo.shtml','verified',None,
 'Silent|sileō|are silent|3rd pl. pres.; enim|enim|for|conj.; lēgēs|lēx|laws|nom. pl. f.; inter|inter|among, amid|prep. + acc.; arma|arma|weapons|acc. pl. n.',
 ['third_person_plural','neuter_plural'],[],'curia','Pro Milone',WP+'Pro_Milone')
K('v-consul-senatui','vocab','republic',4,'Cōnsul senātuī ōrātiōnem habet.','The consul gives a speech to the Senate.',
 "Two consuls were elected every year as the Republic's highest magistrates, and they called the Senate together and put business to it. Senators then spoke in order of rank before a vote. Senātuī is the dative, 'to the Senate', and ōrātiōnem habēre is the normal Latin for 'to make a speech'. The Senate usually met in the Curia in the Forum.",
 "The Senate's decrees were technically only advice, senātūs cōnsulta, but magistrates rarely ignored them.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Cōnsul|cōnsul|the consul|nom. sg. m.; senātuī|senātus|to the Senate|dat. sg. m.; ōrātiōnem|ōrātiō|speech|acc. sg. f.; habet|habeō|gives, delivers|3rd sg. pres.',
 ['dative','accusative'],[],'plutei','Roman Senate',WP+'Roman_Senate',subtype='vocab')

# ---------------- UNIT 5: Gods & Temples ----------------
K('q-catullus-dianae','quote','republic',5,'Diānae sumus in fidē puellae et puerī integrī','We are in Diana\'s care, girls and boys untouched',
 "Catullus 34 is a hymn to Diana written for a chorus of girls and boys, the kind sung at Roman festivals. Diana was goddess of the moon, hunting and childbirth, and protector of the young. In fidē means 'under the protection': fidē is a fifth-declension ablative. Diānae is a genitive, 'of Diana'.",
 "Horace's Carmen Saeculare of 17 BC was sung by just such a chorus of 27 girls and 27 boys.",
 'Catullus','Catullus, Carmina','34.1–2','c. 55 BC',LL+'catullus.shtml','verified','The first i of Diana is short in Catullus\'s metre and is left unmarked.',
 'Diānae|Diāna|of Diana|gen. sg. f.; sumus|sum|we are|1st pl. pres.; in|in|in|prep. + abl.; fidē|fidēs|protection, trust|abl. sg. f.; puellae|puella|girls|nom. pl. f.; et|et|and|conj.; puerī|puer|boys|nom. pl. m.; integrī|integer|pure, untouched|nom. pl. m.',
 ['fifth_declension','in_ablative','genitive'],[],'diana','Diana (mythology)',WP+'Diana_(mythology)')
K('q-lucretius-aeneadum','quote','republic',5,'Aeneadum genetrīx, hominum dīvomque voluptās, alma Venus','Mother of Aeneas\'s people, delight of men and gods, nurturing Venus',
 "Lucretius opens his poem On the Nature of Things with a hymn to Venus, mother of Aeneas and so of the Romans. This is surprising, since his Epicurean philosophy teaches that the gods take no interest in human life. Venus here stands for the creative force of nature. The vocatives pile up titles, each with a genitive: 'of the Aeneadae', 'of men and gods'.",
 "Dīvom is an old genitive plural of dīvus, 'god', the same as dīvōrum. Aeneadum is likewise a short genitive plural, 'of the descendants of Aeneas'.",
 'Lucretius','Lucretius, De rerum natura','1.1–2','c. 55 BC',LL+'lucretius/lucretius1.shtml','verified',None,
 'Aeneadum|Aeneadae|of the descendants of Aeneas|gen. pl. m.; genetrīx|genetrīx|mother|voc. sg. f.; hominum|homō|of men|gen. pl. m.; dīvom|dīvus|of gods|gen. pl. m.; -que|-que|and|enclitic; voluptās|voluptās|delight|voc. sg. f.; alma|almus|nurturing|voc. sg. f.; Venus|Venus|Venus|voc. sg. f.',
 ['vocative','genitive','third_declension'],[],'venus','De rerum natura',WP+'De_rerum_natura')
K('q-virgil-ab-iove','quote','republic',5,'Ab Iove prīncipium, Mūsae; Iovis omnia plēna.','From Jupiter the beginning, Muses; all things are full of Jupiter.',
 "In Eclogue 3 (about 39 BC) two shepherds hold a singing contest, and Damoetas begins with Jupiter, as Greek poets traditionally did. The line echoes the opening of Aratus's Phaenomena, a Greek poem about the stars. Ab Iove uses the ablative after a preposition, Iovis is the genitive, and Mūsae is a vocative plural.",
 "Iuppiter is irregular: Iovem, Iovis, Iovī, Iove. English jovial comes from Iovis, because the planet Jupiter was thought to make people cheerful.",
 'Virgil (speech of Damoetas)','Virgil, Eclogues','3.60','c. 39 BC',LL+'vergil/ec3.shtml','verified','Spoken by the shepherd Damoetas in the poem.',
 'Ab|ab|from|prep. + abl.; Iove|Iuppiter|Jupiter|abl. sg. m.; prīncipium|prīncipium|beginning|nom. sg. n.; Mūsae|Mūsa|Muses|voc. pl. f.; Iovis|Iuppiter|of Jupiter|gen. sg. m.; omnia|omnis|all things|nom. pl. n.; plēna|plēnus|full|nom. pl. n.',
 ['prep_ablative','genitive','third_declension'],[],'jupiter','Eclogues',WP+'Eclogues')
K('q-horace-mercuri','quote','empire',5,'Mercurī, fācunde nepōs Atlantis','Mercury, eloquent grandson of Atlas',
 "Horace's Ode 1.10 is a hymn to Mercury, messenger of the gods and patron of speakers, travellers, merchants and thieves. The god's mother Maia was a daughter of the Titan Atlas, hence 'grandson of Atlas'. Horace praises him for civilising early humans through speech and for stealing Apollo's cattle as a baby. Mercurī is a vocative, and Atlantis a third-declension genitive.",
 "Mercury, the god of trade, may take his name from merx, 'goods'. Wednesday is mercredi in French and mercoledì in Italian, 'Mercury's day'.",
 'Horace','Horace, Odes','1.10.1','c. 23 BC',LL+'horace/carm1.shtml','verified',None,
 'Mercurī|Mercurius|Mercury|voc. sg. m.; fācunde|fācundus|eloquent|voc. sg. m.; nepōs|nepōs|grandson|voc. sg. m.; Atlantis|Atlās|of Atlas|gen. sg. m.',
 ['vocative','genitive','third_declension'],[],'mercury','Mercury (mythology)',WP+'Mercury_(mythology)')
K('q-ovid-iane','quote','empire',5,'Iāne biceps, annī tacitē lābentis orīgō','Two-headed Janus, source of the silently gliding year',
 "Ovid's Fasti is a poem on the Roman calendar, and its first god is Janus, god of doors, gates and beginnings. January, the first month, takes his name. Janus had two faces, looking forward and back, and his name was spoken first in Roman prayers. Iāne is a vocative, and annī lābentis a genitive phrase, 'of the gliding year'.",
 "Lābentis is a present participle, 'slipping by'. A iānua is a door, from the same root.",
 'Ovid','Ovid, Fasti','1.65','c. AD 8',LL+'ovid/ovid.fasti1.shtml','verified',None,
 'Iāne|Iānus|Janus|voc. sg. m.; biceps|biceps|two-headed|voc. sg. m.; annī|annus|of the year|gen. sg. m.; tacitē|tacitē|silently|adv.; lābentis|lābor|gliding|gen. sg. pres. part.; orīgō|orīgō|source, origin|voc. sg. f.',
 ['vocative','genitive','third_declension'],['present_participle'],'janus','Janus',WP+'Janus')
K('q-ovid-est-deus','quote','empire',5,'Est deus in nōbīs; agitante calēscimus illō.','There is a god within us; when he stirs us, we grow warm.',
 "Ovid opens Book 6 of the Fasti by claiming that poets are inspired: a god lives in them and fires them up. Romans spoke of a poet as vātēs, a prophet, and believed the Muses or Apollo breathed songs into him. Ovid immediately admits that some readers will say he made it all up. In nōbīs is an ablative after in, 'in us'.",
 "Agitante illō, 'with him stirring', is an ablative absolute. English enthusiasm comes from Greek for 'having a god within'.",
 'Ovid','Ovid, Fasti','6.5','c. AD 8',LL+'ovid/ovid.fasti6.shtml','verified',None,
 'Est|sum|there is|3rd sg. pres.; deus|deus|a god|nom. sg. m.; in|in|in|prep. + abl.; nōbīs|nōs|us|abl. pl.; agitante|agitō|stirring|abl. sg. pres. part.; calēscimus|calēscō|we grow warm|1st pl. pres.; illō|ille|he|abl. sg. m.',
 ['in_ablative','first_person'],['ablative_absolute'],'ovidstatue','Fasti (poem)',WP+'Fasti_(poem)')
K('i-rib-1534','artifact','empire',5,'DEAE COVVENTINAE T D COSCONIANVS PR COH I BAT L M — Deae Coventinae T(itus) D(…) Cosconiānus, praefectus cohortis I Batāvōrum, libēns meritō.','To the goddess Coventina, Titus D… Cosconianus, prefect of the First Cohort of Batavians, willingly and deservedly.',
 "Coventina was a local water goddess worshipped at a sacred spring beside the fort at Carrawburgh on Hadrian's Wall. When the well was excavated in 1876 it held over 13,000 coins, altars, carved reliefs and other offerings. This slab was set up by the commander of a cohort from the Rhine delta. Deae Coventinae is dative, 'to the goddess', and cohortis is genitive.",
 "L M stands for libēns meritō, 'willingly, as she deserved'. The formula thanks a god for an answered prayer.",
 None,'Dedication slab from Coventina\'s Well, Carrawburgh (RIB 1534)','—','2nd–3rd c. AD',RIB+'1534','verified','The quantities of the vowels in Coventina are unknown and left unmarked. The text is the RIB online edition.',
 'Deae|dea|to the goddess|dat. sg. f.; Coventinae|Coventina|Coventina|dat. sg. f.; Cosconiānus|Cosconiānus|Cosconianus|nom. sg. m.; praefectus|praefectus|commander|nom. sg. m.; cohortis|cohors|of the cohort|gen. sg. f.; Batāvōrum|Batāvī|of the Batavians|gen. pl. m.; libēns|libēns|willingly|nom. sg. m.; meritō|meritō|deservedly|adv.',
 ['dative','genitive','abbreviations'],[],'coventina','Coventina',WP+'Coventina',subtype='inscription',raw=('DEAE / COVVENTINAE / T D COSCONIA / NVS PR COH / I BAT L M','RIB online, 1534'))
K('i-rib-1545','artifact','empire',5,'D IN M S AVL CLVENTIVS HABITVS PRAF COH I BATAVORVM … V S L M — Deō Invictō Mithrae sacrum. Aulus Cluentius Habitus, praefectus cohortis I Batāvōrum, … vōtum solvit libēns meritō.','Sacred to the Unconquered God Mithras. Aulus Cluentius Habitus, prefect of the First Cohort of Batavians, … fulfilled his vow willingly and deservedly.',
 "This altar stood at the end of a small Mithraic temple at Carrawburgh, found in 1949. Mithras was a god of Persian origin whose secret cult spread among Roman soldiers and officials. His worshippers met in dark, cave-like temples for initiation and sacred meals. Deō Invictō Mithrae is dative: the altar is 'for' the god.",
 "The dedicator came from Larinum in Italy. A man of the same name from Larinum was Cicero's client in the Pro Cluentio (66 BC), perhaps an ancestor.",
 None,'Altar from the Mithraeum at Carrawburgh (RIB 1545)','—','3rd c. AD',RIB+'1545','verified','Lines 6–8 (his home town, Colonia Septimia Aurelia Larinum) are omitted. The text is the RIB online edition.',
 'Deō|deus|to the god|dat. sg. m.; Invictō|invictus|unconquered|dat. sg. m.; Mithrae|Mithrās|Mithras|dat. sg. m.; sacrum|sacer|sacred|nom. sg. n.; Aulus Cluentius Habitus|Aulus Cluentius Habitus|Aulus Cluentius Habitus|nom. sg. m.; praefectus|praefectus|commander|nom. sg. m.; cohortis|cohors|of the cohort|gen. sg. f.; Batāvōrum|Batāvī|of the Batavians|gen. pl. m.; vōtum|vōtum|vow|acc. sg. n.; solvit|solvō|fulfilled|3rd sg. perf.; libēns|libēns|willingly|nom. sg. m.; meritō|meritō|deservedly|adv.',
 ['dative','genitive','abbreviations'],['perfect_tense'],'mithraeum','Brocolitia (Carrawburgh)',WP+'Brocolitia',subtype='inscription',raw=('D IN M S / AVL CLVENTIVS / HABITVS PRAF / COH I / BATAVORVM / DOMV VLTI / NA COLON SEPT AVR L / V S L M','RIB online, 1545'))
K('v-templum-iovis','vocab','republic',5,'Templum Iovis in Capitōliō est.','The temple of Jupiter is on the Capitol.',
 "The Temple of Jupiter Optimus Maximus on the Capitoline Hill was the religious heart of Rome, traditionally dedicated in 509 BC, the first year of the Republic. Generals ended their triumphs there, and consuls made vows there when taking office. It burned down several times and was always rebuilt on a grander scale. In Capitōliō is an ablative of place.",
 "English capitol and Capitol Hill in Washington come from Capitōlium. The temple was shared with Juno and Minerva.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Templum|templum|temple|nom. sg. n.; Iovis|Iuppiter|of Jupiter|gen. sg. m.; in|in|on|prep. + abl.; Capitōliō|Capitōlium|the Capitol|abl. sg. n.; est|sum|is|3rd sg. pres.',
 ['in_ablative','genitive'],[],'capitolium','Temple of Jupiter Optimus Maximus',WP+'Temple_of_Jupiter_Optimus_Maximus',subtype='vocab')
K('v-vestales-ignem','vocab','republic',5,'Vestālēs ignem sacrum in aede Vestae servant.','The Vestals keep the sacred fire in the temple of Vesta.',
 "Vesta's temple in the Forum was round, recalling the huts of early Rome, and held no statue, only the eternal flame. Besides the fire it guarded sacred objects said to have come from Troy. Each year on 1 March the fire was ritually renewed. Ignem and aede are third-declension nouns; aedēs means a temple building.",
 "Vesta's temple was rebuilt many times, most recently by Julia Domna around AD 191. The surviving ruins date from that rebuilding.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Vestālēs|Vestālis|the Vestals|nom. pl. f.; ignem|ignis|fire|acc. sg. m.; sacrum|sacer|sacred|acc. sg. m.; in|in|in|prep. + abl.; aede|aedēs|temple|abl. sg. f.; Vestae|Vesta|of Vesta|gen. sg. f.; servant|servō|they keep|3rd pl. pres.',
 ['third_declension','in_ablative'],[],'vestatemple','Temple of Vesta',WP+'Temple_of_Vesta',subtype='vocab')
K('v-sacerdos-sacrificat','vocab','republic',5,'Sacerdōs porcum, ovem et taurum Mārtī sacrificat.','The priest sacrifices a pig, a sheep and a bull to Mars.',
 "The suovetaurilia, from sūs, ovis and taurus, was the sacrifice of a pig, a sheep and a bull to Mars. It purified farmland, armies and, every five years, the whole Roman people at the census. The animals were led around the area to be purified before being killed. Mārtī is dative, 'to Mars', and the three animals are accusative.",
 "Romans sacrificed with the head covered by a fold of the toga, capite vēlātō. The animal's internal organs were then examined for signs from the gods.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Sacerdōs|sacerdōs|priest|nom. sg. m.; porcum|porcus|pig|acc. sg. m.; ovem|ovis|sheep|acc. sg. f.; et|et|and|conj.; taurum|taurus|bull|acc. sg. m.; Mārtī|Mārs|to Mars|dat. sg. m.; sacrificat|sacrificō|sacrifices|3rd sg. pres.',
 ['dative','third_declension'],[],'suovetaurilia','Suovetaurilia',WP+'Suovetaurilia',subtype='vocab')
K('q-horace-phoebe','quote','empire',5,'Phoebe silvārumque potēns Diāna','Phoebus, and Diana, ruler of the woods',
 "In 17 BC Augustus held the Secular Games to mark a new age for Rome, and Horace wrote the official hymn, the Carmen Saeculare. A choir of girls and boys sang it to Apollo (Phoebus) and his sister Diana on the Palatine and the Capitol. An inscription recording the games survives and names Horace as the author of the hymn. Phoebe is vocative, and silvārum a genitive after potēns, 'powerful over'.",
 "Apollo was Augustus's patron god: his temple stood beside Augustus's house on the Palatine.",
 'Horace','Horace, Carmen Saeculare','1','17 BC',LL+'horace/carmsaec.shtml','verified',None,
 'Phoebe|Phoebus|Phoebus (Apollo)|voc. sg. m.; silvārum|silva|of the woods|gen. pl. f.; -que|-que|and|enclitic; potēns|potēns|powerful, ruling|voc. sg. f.; Diāna|Diāna|Diana|voc. sg. f.',
 ['vocative','genitive','third_declension'],[],'apollo','Carmen Saeculare',WP+'Carmen_Saeculare')

# ---------------- UNIT 6: Imperium ----------------
K('q-caesar-veni-vidi-vici','quote','republic',6,'Vēnī, vīdī, vīcī.','I came, I saw, I conquered.',
 "In 47 BC Caesar defeated King Pharnaces of Pontus at Zela in a battle of about four hours. At his Pontic triumph in 46 BC a placard was carried with just these three words. Suetonius says it showed how quickly the war was finished. The three perfects, each two syllables starting with v, are a perfect example of Latin brevity.",
 "Plutarch says Caesar also wrote the phrase in a letter to a friend in Rome. Venī, vīdī, vīcī are the first-person perfects of veniō, videō and vincō.",
 'Julius Caesar','Suetonius, Divus Iulius','37.2','early 2nd c. AD',LL+'suetonius/suet.caesar.html','verified','Suetonius reports the words as the title carried in Caesar\'s Pontic triumph.',
 'Vēnī|veniō|I came|1st sg. perf.; vīdī|videō|I saw|1st sg. perf.; vīcī|vincō|I conquered|1st sg. perf.',
 ['perfect_tense','first_person'],[],'caesar','Veni, vidi, vici',WP+'Veni,_vidi,_vici')
K('q-resgestae-templa','quote','empire',6,'Duo et octōgintā templa deum in urbe … refēcī.','I restored eighty-two temples of the gods in the city.',
 "Augustus presented himself as the restorer of Roman religion after the civil wars. In 28 BC, by decree of the Senate, he repaired 82 temples in a single year, 'leaving out none that needed repair'. He also built new ones, such as Mars Ultor in his own forum. Duo et octōgintā is a numeral, and refēcī a perfect, 'I rebuilt'.",
 "Deum is an old genitive plural, the same as deōrum. The omitted words are cōnsul sextum ex auctōritāte senātūs, 'in my sixth consulship, by authority of the Senate'.",
 'Augustus','Res Gestae Divi Augusti','20.4','AD 14',LL+'resgestae.html','verified',None,
 'Duo et octōgintā|duo et octōgintā|eighty-two|numeral; templa|templum|temples|acc. pl. n.; deum|deus|of the gods|gen. pl. m.; in|in|in|prep. + abl.; urbe|urbs|the city|abl. sg. f.; refēcī|reficiō|I restored|1st sg. perf.',
 ['numerals','perfect_tense'],[],'marsultor','Res Gestae Divi Augusti',WP+'Res_Gestae_Divi_Augusti')
K('q-ha-hadrian-murum','quote','empire',6,'Mūrum per octōgintā mīlia passuum prīmus dūxit.','He was the first to build a wall for eighty miles.',
 "The Historia Augusta's life of Hadrian says that on his visit to Britain in AD 122 he built a wall 'to divide the barbarians from the Romans'. Hadrian's Wall ran 80 Roman miles from coast to coast, with forts, milecastles and turrets. A Roman mile, mīlle passūs, was a thousand paces, about 1,480 m. Octōgintā is a numeral and dūxit a perfect: literally 'he led a wall'.",
 "The text goes on: quī barbarōs Rōmānōsque dīvideret. About twenty years later Antoninus Pius built a turf wall further north in Scotland.",
 'Historia Augusta (anonymous)','Historia Augusta, Vita Hadriani','11.2','late 4th c. AD',LL+'sha/hadr.shtml','verified','Source reads murumque; the card drops -que.',
 'Mūrum|mūrus|wall|acc. sg. m.; per|per|for, through|prep. + acc.; octōgintā|octōgintā|eighty|numeral; mīlia|mīlle|thousands|acc. pl. n.; passuum|passus|of paces|gen. pl. m.; prīmus|prīmus|first|nom. sg. m.; dūxit|dūcō|he built, drew|3rd sg. perf.',
 ['numerals','perfect_tense'],[],'wall',"Hadrian's Wall",WP+'Hadrian%27s_Wall')
K('q-caligula-oderint','quote','empire',6,'Ōderint, dum metuant.','Let them hate, so long as they fear.',
 "Suetonius says the emperor Caligula (AD 37–41) kept repeating this line from a tragedy by Accius, a Roman poet of the 2nd century BC. In the play it was spoken by Atreus, the cruel king of Mycenae. Caligula was murdered by officers of his own guard. Ōdī, 'I hate', has only perfect forms but present meaning.",
 "Ōderint and metuant are subjunctives. Cicero and Seneca also quote the line as the motto of a tyrant.",
 'Accius (quoted by Caligula)','Suetonius, Gaius Caligula','30.1','early 2nd c. AD',LL+'suetonius/suet.cal.html','verified','The line comes from Accius\'s tragedy Atreus. Suetonius says Caligula often quoted it.',
 'Ōderint|ōdī|let them hate|3rd pl. perf. subj.; dum|dum|so long as|conj.; metuant|metuō|they fear|3rd pl. pres. subj.',
 ['perfect_form_present_meaning'],['subjunctive'],'caligula','Caligula',WP+'Caligula')
K('q-eutropius-augustus','quote','empire',6,'Ex eō rem pūblicam per quadrāgintā et quattuor annōs sōlus obtinuit.','From then on he held the state alone for forty-four years.',
 "Eutropius wrote a short history of Rome around AD 369 for the emperor Valens, and his plain Latin made him a school author for centuries. Here he describes Augustus after the defeat of Antony and Cleopatra. Counting from 30 BC to his death in AD 14 gives 44 years. Quadrāgintā et quattuor is a numeral and obtinuit a perfect.",
 "Rēs pūblica, literally 'public thing', means the state, and gives English republic.",
 'Eutropius','Eutropius, Breviarium ab urbe condita','7.8','c. AD 369',LL+'eutropius/eutropius7.shtml','verified',None,
 'Ex|ex|from|prep. + abl.; eō|is|that (time)|abl. sg. n.; rem pūblicam|rēs pūblica|the state|acc. sg. f.; per|per|for|prep. + acc.; quadrāgintā et quattuor|quadrāgintā et quattuor|forty-four|numeral; annōs|annus|years|acc. pl. m.; sōlus|sōlus|alone|nom. sg. m.; obtinuit|obtineō|held|3rd sg. perf.',
 ['numerals','perfect_tense'],[],'augustus','Eutropius',WP+'Eutropius')
K('q-eutropius-titus','quote','empire',6,'Hic Rōmae amphitheātrum aedificāvit et quīnque mīlia ferārum in dēdicātiōne eius occīdit.','He built an amphitheatre at Rome and killed five thousand wild animals at its dedication.',
 "Eutropius credits the emperor Titus with the Colosseum, begun by his father Vespasian and opened by Titus in AD 80 with a hundred days of games. Five thousand beasts in a day is the figure Suetonius also gives. Rōmae is a locative, 'at Rome', and both verbs are perfects. Quīnque mīlia, 'five thousand', takes the genitive ferārum.",
 "The building's ancient name was the Flavian Amphitheatre. The name Colosseum came later, probably from a colossal statue of Nero nearby.",
 'Eutropius','Eutropius, Breviarium ab urbe condita','7.21','c. AD 369',LL+'eutropius/eutropius7.shtml','verified',None,
 'Hic|hic|he, this man|nom. sg. m.; Rōmae|Rōma|at Rome|locative; amphitheātrum|amphitheātrum|amphitheatre|acc. sg. n.; aedificāvit|aedificō|built|3rd sg. perf.; et|et|and|conj.; quīnque|quīnque|five|numeral; mīlia|mīlle|thousands|acc. pl. n.; ferārum|fera|of wild beasts|gen. pl. f.; in|in|at|prep. + abl.; dēdicātiōne|dēdicātiō|dedication|abl. sg. f.; eius|is|its|gen. sg.; occīdit|occīdō|killed|3rd sg. perf.',
 ['numerals','perfect_tense'],['demonstratives'],'colosseum','Colosseum',WP+'Colosseum')
K('q-resgestae-ianum','quote','empire',6,'Iānum Quirīnum … ter mē prīncipe senātus claudendum esse cēnsuit.','The Senate decreed three times while I was leader that Janus Quirinus should be closed.',
 "The doors of the shrine of Janus in the Forum were closed only when Rome was at peace on land and sea. Augustus boasts that this had happened only twice in all Roman history before him, and three times in his own reign. Peace was a central theme of his propaganda. Ter, 'three times', is a numeral adverb, and cēnsuit a perfect.",
 "Mē prīncipe, 'with me as leader', is an ablative absolute and claudendum a gerundive. Nero later struck coins showing the closed doors.",
 'Augustus','Res Gestae Divi Augusti','13','AD 14',LL+'resgestae.html','verified','Ellipsis omits a long clause on how peace had been won by victories on land and sea. The Latin Library text misprints Quinnum for Quirinum.',
 'Iānum|Iānus|Janus|acc. sg. m.; Quirīnum|Quirīnus|Quirinus (title of Janus)|acc. sg. m.; ter|ter|three times|adv.; mē|ego|me|abl. sg.; prīncipe|prīnceps|leader|abl. sg. m.; senātus|senātus|the Senate|nom. sg. m.; claudendum esse|claudō|should be closed|gerundive + inf.; cēnsuit|cēnseō|decreed|3rd sg. perf.',
 ['numerals','perfect_tense'],['ablative_absolute','gerundive'],'januscoin','Temple of Janus (Roman Forum)',WP+'Temple_of_Janus_(Roman_Forum)')

# ---------------- UNIT 7: Poets ----------------
K('q-ovid-parve','quote','empire',7,'Parve (nec invideō) sine mē, liber, ībis in urbem','Little book, you will go to the city without me (I don\'t begrudge it)',
 "In AD 8 Augustus banished Ovid to Tomis on the Black Sea, modern Constanța in Romania, for 'a poem and a mistake'. The first poem of his Sorrows (Tristia) sends his book off to Rome, where its author may not go. Ībis is a future, 'you will go', and parve and liber are vocatives, as Ovid speaks to the book. He never returned and died in exile around AD 17.",
 "The 'poem' was probably his Art of Love. The 'mistake' has never been explained.",
 'Ovid','Ovid, Tristia','1.1.1','c. AD 9',LL+'ovid/ovid.tristia1.shtml','verified',None,
 'Parve|parvus|little|voc. sg. m.; nec|nec|and not|conj.; invideō|invideō|I begrudge|1st sg. pres.; sine|sine|without|prep. + abl.; mē|ego|me|abl. sg.; liber|liber|book|voc. sg. m.; ībis|eō|you will go|2nd sg. fut.; in|in|into|prep. + acc.; urbem|urbs|the city|acc. sg. f.',
 ['future_tense','vocative','personal_pronouns'],[],'delacroix','Tristia',WP+'Tristia')
K('q-catullus-lugete','quote','republic',7,'Lūgēte, ō Venerēs Cupīdinēsque','Mourn, O Venuses and Cupids',
 "Catullus 3 is a mock funeral song for the pet sparrow of his girlfriend Lesbia. He calls on all the goddesses and gods of love, and 'all charming people', to grieve. The imperative lūgēte is plural, because he addresses a crowd. The poem mixes real tenderness with the comedy of a grand lament for a small bird.",
 "Lesbia's real name was probably Clodia, from one of Rome's grandest families. Catullus's poems about the sparrow were famous enough for Martial to imitate them.",
 'Catullus','Catullus, Carmina','3.1','c. 55 BC',LL+'catullus.shtml','verified',None,
 'Lūgēte|lūgeō|mourn|2nd pl. imperative; ō|ō|O|interj.; Venerēs|Venus|Venuses|voc. pl. f.; Cupīdinēs|Cupīdō|Cupids|voc. pl. m.; -que|-que|and|enclitic',
 ['imperative','vocative','enclitic_que'],[],'sparrow','Catullus 3',WP+'Catullus_3')
K('q-catullus-basia','quote','republic',7,'Dā mī bāsia mīlle, deinde centum','Give me a thousand kisses, then a hundred',
 "In Catullus 5 the poet urges Lesbia to ignore the gossip of grumpy old men and love while life lasts, for 'one endless night must be slept'. Then he demands kisses: a thousand, a hundred, another thousand, until they lose count so that no one can cast the evil eye on them. Dā is an imperative and mīlle and centum are numerals. Mī is a short form of mihi.",
 "Ben Jonson's 'Come, my Celia' and many other love poems imitate this one.",
 'Catullus','Catullus, Carmina','5.7','c. 55 BC',LL+'catullus.shtml','verified',None,
 'Dā|dō|give|2nd sg. imperative; mī|ego|to me|dat. sg.; bāsia|bāsium|kisses|acc. pl. n.; mīlle|mīlle|a thousand|numeral; deinde|deinde|then|adv.; centum|centum|a hundred|numeral',
 ['imperative','numerals','personal_pronouns'],[],'lesbia','Catullus 5',WP+'Catullus_5')
K('q-propertius-cynthia','quote','empire',7,'Cynthia prīma suīs miserum mē cēpit ocellīs','Cynthia was the first to capture wretched me with her eyes',
 "Propertius's first book of elegies (about 29 BC) is named after Cynthia, and her name is its very first word. The Latin love-poet makes himself the helpless captive of his mistress, a pose Ovid would later parody. Mē is the object of cēpit, 'captured', and ocellīs, 'little eyes', is an ablative of means.",
 "Cynthia was a pen-name, perhaps for a woman called Hostia. It is also a title of Diana, born on Mount Cynthus.",
 'Propertius','Propertius, Elegiae','1.1.1','c. 29 BC',LL+'propertius1.html','verified',None,
 'Cynthia|Cynthia|Cynthia|nom. sg. f.; prīma|prīmus|first|nom. sg. f.; suīs|suus|her|abl. pl. m.; miserum|miser|wretched|acc. sg. m.; mē|ego|me|acc. sg.; cēpit|capiō|captured|3rd sg. perf.; ocellīs|ocellus|with little eyes|abl. pl. m.',
 ['personal_pronouns','perfect_tense'],['ablative_means'],'propertius','Propertius',WP+'Propertius')
K('q-horace-eheu','quote','empire',7,'Ēheu fugācēs, Postume, Postume, lābuntur annī','Alas, Postumus, Postumus, the fleeting years slip by',
 "Horace's Ode 2.14 is a meditation on death addressed to a friend called Postumus. No piety, he says, can delay wrinkles and old age, and an heir will drink the fine wine Postumus has hoarded. Repeating the name gives the line the sound of a sigh. Postume is a vocative, and fugācēs, 'fleeting', agrees with annī.",
 "Lābuntur comes from the deponent verb lābor, 'slip, glide'. Romans liked mosaics like the Pompeian skull to remind diners that life is short.",
 'Horace','Horace, Odes','2.14.1–2','c. 23 BC',LL+'horace/carm2.shtml','verified',None,
 'Ēheu|ēheu|alas|interj.; fugācēs|fugāx|fleeting|nom. pl. m.; Postume|Postumus|Postumus|voc. sg. m.; lābuntur|lābor|slip by|3rd pl. pres.; annī|annus|years|nom. pl. m.',
 ['vocative','adjective_agreement'],['deponent'],'skull','Odes (Horace)',WP+'Odes_(Horace)')
K('q-ovid-arbor','quote','empire',7,'Arbor eris certē mea!','You will certainly be my tree!',
 "In Ovid's Metamorphoses Apollo chases the nymph Daphne, who prays to escape and is turned into a laurel tree. Since she cannot be his wife, the god declares that she will be his tree. Laurel wreaths would crown his lyre, his quiver and Roman generals in triumph. Eris is the future of sum, 'you will be'.",
 "Daphne is Greek for 'laurel'. Bernini's marble statue in the Galleria Borghese shows the moment her fingers sprout leaves.",
 'Ovid (speech of Apollo)','Ovid, Metamorphoses','1.557–58','c. AD 8',LL+'ovid/ovid.met1.shtml','verified','Spoken by Apollo in the poem. The source has arbor eris certe, dixit, mea; the card omits dixit (he said).',
 'Arbor|arbor|tree|nom. sg. f.; eris|sum|you will be|2nd sg. fut.; certē|certē|certainly|adv.; mea|meus|my|nom. sg. f.',
 ['future_tense','possessive_adjectives'],[],'daphne','Apollo and Daphne',WP+'Apollo_and_Daphne')
K('q-virgil-tityre','quote','republic',7,'Tītyre, tū patulae recubāns sub tegmine fāgī','Tityrus, you, lying back under the cover of a spreading beech',
 "These are the first words of Virgil's Eclogues (about 39 BC). The shepherd Meliboeus, driven off his land, envies Tityrus, who can relax and sing in the shade. The poem reflects real confiscations of farmland to settle veterans after the civil wars. Tītyre is a vocative and tū a personal pronoun.",
 "Recubāns is a present participle, 'lying back'. The Vergilius Romanus, a 5th-century manuscript in the Vatican, illustrates this scene.",
 'Virgil (speech of Meliboeus)','Virgil, Eclogues','1.1','c. 39 BC',LL+'vergil/ec1.shtml','verified','Spoken by Meliboeus in the poem.',
 'Tītyre|Tītyrus|Tityrus|voc. sg. m.; tū|tū|you|nom. sg.; patulae|patulus|spreading|gen. sg. f.; recubāns|recubō|lying back|nom. sg. pres. part.; sub|sub|under|prep. + abl.; tegmine|tegmen|cover|abl. sg. n.; fāgī|fāgus|of a beech|gen. sg. f.',
 ['vocative','personal_pronouns'],['present_participle'],'tityrus','Eclogue 1',WP+'Eclogue_1')
K('q-ovid-penelope','quote','empire',7,'Haec tua Pēnelopē lentō tibi mittit, Ulixe','Your Penelope sends this to you, slow Ulysses',
 "Ovid's Heroines are imaginary letters from mythical women to absent lovers, and the first is from Penelope to Ulysses, still not home twenty years after leaving for Troy. Troy has fallen, she writes, so why has he not come back? Haec, 'these (words)', is a neuter plural demonstrative, the object of mittit, tibi a dative, and Ulixe a vocative. Lentō, 'slow', is a reproach.",
 "Ulixēs is the Latin form of Odysseus. Penelope kept her suitors waiting by weaving and secretly unweaving a shroud.",
 'Ovid (as Penelope)','Ovid, Heroides','1.1','c. 15 BC',LL+'ovid/ovid.her1.shtml','verified','Written by Ovid in the voice of Penelope. The quantity of the final e of the vocative Ulixe is uncertain and left unmarked. Some editions read Hanc (sc. epistulam), \'this letter\'.',
 'Haec|hic|this|acc. pl. n.; tua|tuus|your|nom. sg. f.; Pēnelopē|Pēnelopē|Penelope|nom. sg. f.; lentō|lentus|slow|dat. sg. m.; tibi|tū|to you|dat. sg.; mittit|mittō|sends|3rd sg. pres.; Ulixe|Ulixēs|Ulysses|voc. sg. m.',
 ['demonstratives','dative','personal_pronouns'],[],'penelope','Heroides',WP+'Heroides')
K('q-sulpicia-tandem','quote','empire',7,'Tandem vēnit amor','At last love has come',
 "Sulpicia, a young noblewoman and niece of Augustus's general Messalla, is the only Roman woman poet whose verse survives in any quantity. Her six short elegies were preserved among the poems of Tibullus. This one opens with frank joy: love has come at last, and she would rather people talk about it than hide it. Vēnit is a perfect, 'has come'.",
 "She calls her lover Cerinthus. Scholars long doubted a woman could have written the poems, but most now accept them as hers.",
 'Sulpicia','Corpus Tibullianum (Sulpicia)','3.13.1','late 1st c. BC',LL+'tibullus3.html','verified',None,
 'Tandem|tandem|at last|adv.; vēnit|veniō|has come|3rd sg. perf.; amor|amor|love|nom. sg. m.',
 ['perfect_tense','nominative'],[],'woman','Sulpicia',WP+'Sulpicia')
K('q-horace-persicos','quote','empire',7,'Persicōs ōdī, puer, apparātūs','I hate Persian fuss, boy',
 "Ode 1.38 closes Horace's first book of odes with a tiny poem to a slave boy. Horace wants no elaborate wreaths or late roses, only plain myrtle as he drinks under a vine. The 'Persian' luxury stands for showy excess, set against the poet's simple pleasures. Ōdī has a perfect form but present meaning, 'I hate', and puer is a vocative.",
 "Apparātūs is a fourth-declension accusative plural. Horace's farm in the Sabine hills, a gift from his patron Maecenas, became a symbol of the simple life.",
 'Horace','Horace, Odes','1.38.1','c. 23 BC',LL+'horace/carm1.shtml','verified',None,
 'Persicōs|Persicus|Persian|acc. pl. m.; ōdī|ōdī|I hate|1st sg. perf. (pres. meaning); puer|puer|boy|voc. sg. m.; apparātūs|apparātus|fuss, elaborate preparations|acc. pl. m.',
 ['perfect_form_present_meaning','vocative'],[],'drinkers','Odes (Horace)',WP+'Odes_(Horace)')
K('q-horace-odi-profanum','quote','empire',7,'Ōdī profānum volgus et arceō.','I hate the uninitiated crowd and keep it away.',
 "Book 3 of Horace's Odes opens like a religious ceremony: a priest orders the uninitiated to stand back before the sacred rite begins. Horace calls himself 'priest of the Muses' and offers new songs to girls and boys. Profānum literally means 'in front of the temple', outside the sacred space. Ōdī is a perfect with present meaning.",
 "Volgus is the older spelling of vulgus, 'crowd', the root of English vulgar. Profane comes from profānus.",
 'Horace','Horace, Odes','3.1.1','c. 23 BC',LL+'horace/carm3.shtml','verified',None,
 'Ōdī|ōdī|I hate|1st sg. perf. (pres. meaning); profānum|profānus|uninitiated, profane|acc. sg. n.; volgus|vulgus|crowd|acc. sg. n.; et|et|and|conj.; arceō|arceō|I keep away|1st sg. pres.',
 ['perfect_form_present_meaning','first_person'],[],'priest','Odes (Horace)',WP+'Odes_(Horace)')
K('q-catullus-cenabis','quote','republic',7,'Cēnābis bene, mī Fabulle, apud mē','You will dine well, my Fabullus, at my house',
 "Catullus 13 is a joking dinner invitation. Fabullus will dine splendidly, the poet promises, as long as he brings the food, the wine, the girl and the wit, because Catullus's purse is 'full of cobwebs'. In return Catullus will provide a perfume so lovely that Fabullus will pray to become all nose. Cēnābis is a future and mī Fabulle a vocative.",
 "Mī is the vocative of meus. Apud mē means 'at my house', like French chez moi.",
 'Catullus','Catullus, Carmina','13.1','c. 55 BC',LL+'catullus.shtml','verified',None,
 'Cēnābis|cēnō|you will dine|2nd sg. fut.; bene|bene|well|adv.; mī|meus|my|voc. sg. m.; Fabulle|Fabullus|Fabullus|voc. sg. m.; apud|apud|at the house of|prep. + acc.; mē|ego|me|acc. sg.',
 ['future_tense','vocative','personal_pronouns'],[],'banquet','Catullus 13',WP+'Catullus_13')
