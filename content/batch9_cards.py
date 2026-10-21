# Batch 9 card texts: spread over all 14 units, weighted to XI-XIV. Gloss format: "word|lemma|meaning|parse; ..."
# K(id,type,era,unit,latin,translation,context,more,person,work,cit,date,source_url,conf,note,gloss,target,preview,img,lm_label,lm_url, **extra)
LL='https://www.thelatinlibrary.com/'
WP='https://en.wikipedia.org/wiki/'
WS='https://la.wikisource.org/wiki/'
CON='Constructed teaching sentence (not a quotation).'
CARDS=[]
def K(*a,**kw): CARDS.append((a,kw))

# ---------------- UNITS 1-10: constructed vocabulary sentences ----------------
K('v-via-appia','vocab','republic',1,'Via Appia longa et antīqua est.','The Appian Way is long and old.',
 "The Via Appia was begun in 312 BC by the censor Appius Claudius, who gave it his name. It ran south from Rome to Capua and was later extended to Brundisium on the Adriatic coast. Via, longa and antīqua are all nominative, and est links them.",
 "Romans called it the queen of roads, rēgīna viārum. Stretches of the original basalt paving can still be walked just outside Rome.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Via|via|road, way|nom. sg. f.; Appia|Appius|Appian|nom. sg. f.; longa|longus|long|nom. sg. f.; et|et|and|conj.; antīqua|antīquus|old, ancient|nom. sg. f.; est|sum|is|3rd sg. pres.',
 ['nominative','sum'],[],'viaappia','Appian Way',WP+'Appian_Way',subtype='vocab')
K('v-strigilis','vocab','empire',1,'Strigilis parva et curva est.','The strigil is small and curved.',
 "Romans at the baths did not use soap. They rubbed oil on their skin and then scraped off the oil, sweat and dirt with a curved metal tool called a strigilis. Strigilis is a nominative singular, and parva and curva describe it.",
 "Athletes used strigils too, and Greek statues sometimes show a young man scraping himself. A slave often did the scraping for wealthier bathers.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Strigilis|strigilis|strigil, skin-scraper|nom. sg. f.; parva|parvus|small|nom. sg. f.; et|et|and|conj.; curva|curvus|curved|nom. sg. f.; est|sum|is|3rd sg. pres.',
 ['nominative','sum'],[],'strigil','Strigil',WP+'Strigil',subtype='vocab')
K('v-toga-vestis','vocab','republic',1,'Toga vestis Rōmāna est.','The toga is a Roman garment.',
 "The toga was a large woollen cloth wrapped around the body, and only Roman citizens were allowed to wear it. It was heavy and awkward, so most men wore it only for formal occasions such as the law courts or the Senate. Toga and vestis are both nominative, linked by est.",
 "Boys wore a toga with a purple border, the toga praetexta, until they came of age at about sixteen. Candidates for office whitened their togas with chalk, which is why they were called candidātī.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Toga|toga|toga|nom. sg. f.; vestis|vestis|garment, clothing|nom. sg. f.; Rōmāna|Rōmānus|Roman|nom. sg. f.; est|sum|is|3rd sg. pres.',
 ['nominative','sum'],[],'toga','Toga',WP+'Toga',subtype='vocab')
K('v-nauta-navem','vocab','empire',2,'Nauta nāvem et pharum videt.','The sailor sees the ship and the lighthouse.',
 "The great lighthouse, the Pharos, stood at the entrance to the harbour of Alexandria in Egypt, and its name became the Latin word for any lighthouse. Grain ships sailed from Alexandria to feed the city of Rome. Nāvem and pharum are accusative objects of videt.",
 "The Pharos was counted among the Seven Wonders of the World. French still calls a lighthouse a phare and Italian a faro.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Nauta|nauta|sailor|nom. sg. m.; nāvem|nāvis|ship|acc. sg. f.; et|et|and|conj.; pharum|pharus|lighthouse|acc. sg. f.; videt|videō|sees|3rd sg. pres.',
 ['accusative','nominative'],['present_tense'],'nauta','Lighthouse of Alexandria',WP+'Lighthouse_of_Alexandria',subtype='vocab')
K('v-miles-galeam','vocab','empire',2,'Mīles galeam et scūtum portat.','The soldier carries a helmet and a shield.',
 "A Roman legionary carried his own equipment on the march: helmet, shield, weapons, tools and food. Soldiers were nicknamed Marius' mules after the general who made them carry their own packs. Galeam and scūtum are accusative objects; scūtum is a neuter noun, so its accusative looks like its nominative.",
 "The helmet shown was found at Xanten on the Rhine, where a large legionary fortress stood. The long curved legionary shield was the scūtum, and a round one was a clipeus.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Mīles|mīles|soldier|nom. sg. m.; galeam|galea|helmet|acc. sg. f.; et|et|and|conj.; scūtum|scūtum|shield|acc. sg. n.; portat|portō|carries|3rd sg. pres.',
 ['accusative','nominative'],['present_tense'],'helmet','Roman military personal equipment',WP+'Roman_military_personal_equipment',subtype='vocab')
K('v-fibula','vocab','late_antiquity',2,'Fībula pallium tenet.','The brooch holds the cloak.',
 "Romans had no buttons, so a fībula, a metal pin like a safety pin, fastened a cloak at the shoulder. The heavy crossbow-shaped brooch shown here was a mark of rank for soldiers and officials of the late empire. Pallium is the accusative object of tenet; it is neuter, so the form is the same as the nominative.",
 "Doctors still use the word fibula for the thin bone of the lower leg, perhaps because it looks like the pin of a brooch.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Fībula|fībula|brooch, pin|nom. sg. f.; pallium|pallium|cloak|acc. sg. n.; tenet|teneō|holds|3rd sg. pres.',
 ['accusative','nominative'],['present_tense'],'fibula','Fibula (brooch)',WP+'Fibula_(brooch)',subtype='vocab')
K('v-tabulae-stili','vocab','empire',3,'Mercātōrēs tabulās et stilōs habent et litterās scrībunt.','Merchants have tablets and styluses and write letters.',
 "Romans wrote everyday notes, letters and accounts on wooden tablets coated with wax, scratching the letters with a pointed stylus. The flat end of the stylus smoothed the wax so the tablet could be used again. Habent and scrībunt are present-tense verbs with plural endings, because the subject mercātōrēs is plural.",
 "Tablets found in London date from the first years of the Roman town. One of them, from AD 57, records a debt and is the oldest dated document from London.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Mercātōrēs|mercātor|merchants|nom. pl. m.; tabulās|tabula|tablets|acc. pl. f.; et|et|and|conj.; stilōs|stilus|styluses|acc. pl. m.; habent|habeō|they have|3rd pl. pres.; et|et|and|conj.; litterās|littera|letters|acc. pl. f.; scrībunt|scrībō|they write|3rd pl. pres.',
 ['present_tense','third_person_plural'],[],'tabula','Bloomberg tablets',WP+'Bloomberg_tablets',subtype='vocab')
K('v-lararium','vocab','empire',4,'Fīlia familiae Laribus cibum dat.','The daughter of the family gives food to the household gods.',
 "Every Roman house had a shrine called a larārium where the family honoured its household gods, the Larēs. They offered small gifts of food, wine and incense, especially on family occasions. Familiae is genitive, 'of the family', and Laribus is dative, 'to the household gods'.",
 "Many larāria survive at Pompeii, some painted on walls and others built like tiny temples. Next to the Larēs stood the Penātēs, gods of the store-cupboard.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Fīlia|fīlia|daughter|nom. sg. f.; familiae|familia|of the family|gen. sg. f.; Laribus|Larēs|to the household gods|dat. pl. m.; cibum|cibus|food|acc. sg. m.; dat|dō|gives|3rd sg. pres.',
 ['genitive','dative'],['third_declension'],'lararium','Lararium',WP+'Lararium',subtype='vocab')
K('v-aquaeductus','vocab','empire',5,'Aqua ā montibus per canālem ad urbem fluit.','The water flows from the mountains through a channel to the city.',
 "Roman aqueducts carried water for many miles, sloping very gently downhill so that gravity alone kept it moving. Arched bridges such as the Pont du Gard carried the channel across valleys. Ā montibus is a preposition with the ablative, and montibus, canālem and urbem are third-declension nouns.",
 "The Pont du Gard brought water to the Roman town of Nemausus, modern Nîmes. The channel on the bridge drops only about 2.5 cm from one end to the other.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Aqua|aqua|water|nom. sg. f.; ā|ā, ab|from|prep. + abl.; montibus|mōns|mountains|abl. pl. m.; per|per|through|prep. + acc.; canālem|canālis|channel|acc. sg. m.; ad|ad|to|prep. + acc.; urbem|urbs|city|acc. sg. f.; fluit|fluō|flows|3rd sg. pres.',
 ['prep_ablative','third_declension'],[],'pontdugard','Pont du Gard',WP+'Pont_du_Gard',subtype='vocab')
K('v-pantheum','vocab','empire',6,'Agrippa Pantheum aedificāvit; posteā Hadriānus templum novum faciēbat.','Agrippa built the Pantheon; later Hadrian was making a new temple.',
 "Marcus Agrippa, the friend of Augustus, built the first Pantheon. After it burned down, the emperor Hadrian rebuilt it in the 120s AD with the vast concrete dome that still stands. Aedificāvit is perfect tense, a single completed act, and faciēbat is imperfect, work going on over time.",
 "Hadrian kept Agrippa's name on the front: the inscription still reads M AGRIPPA L F COS TERTIVM FECIT. The dome is 43 metres across and lit only by the round opening at the top.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Agrippa|Agrippa|Agrippa|nom. sg. m.; Pantheum|Pantheum|the Pantheon|acc. sg. n.; aedificāvit|aedificō|built|3rd sg. perf.; posteā|posteā|later|adv.; Hadriānus|Hadriānus|Hadrian|nom. sg. m.; templum|templum|temple|acc. sg. n.; novum|novus|new|acc. sg. n.; faciēbat|faciō|was making|3rd sg. impf.',
 ['perfect_tense','imperfect'],[],'pantheon','Pantheon, Rome',WP+'Pantheon,_Rome',subtype='vocab')
K('v-viator-lege','vocab','empire',7,'Viātor, lapidem lege! Mox ad oppidum veniēs.','Traveller, read the stone! Soon you will come to the town.',
 "Milestones stood beside Roman roads and gave the distance in Roman miles, mīlia passuum, abbreviated M P. The milestone at Middleton in Cumbria is marked M P LIII, 53 miles, probably the distance to Carlisle. Lege is an imperative, 'read!', and veniēs is future, 'you will come'.",
 "A Roman mile was a thousand double paces, about 1,480 metres. The Middleton stone was found in 1836 and set up again by the landowner, who added the Latin note shown here.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Viātor|viātor|traveller|voc. sg. m.; lapidem|lapis|stone|acc. sg. m.; lege|legō|read!|imperative sg.; Mox|mox|soon|adv.; ad|ad|to|prep. + acc.; oppidum|oppidum|town|acc. sg. n.; veniēs|veniō|you will come|2nd sg. fut.',
 ['imperative','future_tense'],[],'milestone','Milestone',WP+'Milestone',subtype='vocab')
K('v-endymion','vocab','empire',8,'Poētae dīcunt Endymiōnem semper dormīre.','The poets say that Endymion is always asleep.',
 "In Greek myth Selene, the Moon, fell in love with the shepherd Endymion, and he was granted endless sleep so that he would never grow old. Romans liked the story on coffins because death could be shown as a peaceful sleep. Dīcunt introduces an indirect statement: Endymiōnem is the accusative subject and dormīre the infinitive.",
 "The Latin name of the Moon goddess was Lūna. The marble sarcophagus shown, now in the Metropolitan Museum, dates from the early 3rd century AD.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Poētae|poēta|poets|nom. pl. m.; dīcunt|dīcō|say|3rd pl. pres.; Endymiōnem|Endymiōn|Endymion|acc. sg. m.; semper|semper|always|adv.; dormīre|dormiō|to sleep|pres. inf.',
 ['indirect_statement','infinitive'],[],'endymion','Endymion (mythology)',WP+'Endymion_(mythology)',subtype='vocab')
K('v-basilica','vocab','empire',9,'Basilica ā Maxentiō incohāta, ā Cōnstantīnō perfecta est.','The basilica was begun by Maxentius and finished by Constantine.',
 "The emperor Maxentius began this huge hall beside the Roman Forum around AD 308. After Constantine defeated him at the Milvian Bridge in 312, Constantine completed it under his own name. Perfecta est is a perfect passive, and ā with the ablative names who did the action.",
 "A basilica was a public hall for law courts and business; only later did the word come to mean a large church. Only the three great vaults of the north aisle still stand.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Basilica|basilica|basilica, public hall|nom. sg. f.; ā|ā, ab|by|prep. + abl. (agent); Maxentiō|Maxentius|Maxentius|abl. sg. m.; incohāta|incohō|begun|perf. pass. part. nom. sg. f.; ā|ā, ab|by|prep. + abl. (agent); Cōnstantīnō|Cōnstantīnus|Constantine|abl. sg. m.; perfecta est|perficiō|was finished|3rd sg. perf. pass.',
 ['passive_voice','participle'],[],'basilica','Basilica of Maxentius',WP+'Basilica_of_Maxentius',subtype='vocab')
K('v-cloaca-maxima','vocab','regal',10,'Cloāca Maxima, quam rēgēs Rōmānī fēcērunt, aquam in Tiberim dūcit.','The Cloaca Maxima, which the Roman kings built, carries water into the Tiber.',
 "The Cloaca Maxima, the 'Greatest Drain', was first dug to drain the marshy valley where the Forum later stood. Livy says the kings Tarquinius Priscus and Tarquinius Superbus built it. Quam rēgēs Rōmānī fēcērunt is a relative clause, and quam is feminine because it refers back to Cloāca.",
 "Its outlet can still be seen in the Tiber embankment. The drain was later roofed over and extended, and parts of it still carry water today.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Cloāca|cloāca|drain, sewer|nom. sg. f.; Maxima|maximus|greatest|nom. sg. f.; quam|quī|which|acc. sg. f.; rēgēs|rēx|kings|nom. pl. m.; Rōmānī|Rōmānus|Roman|nom. pl. m.; fēcērunt|faciō|made, built|3rd pl. perf.; aquam|aqua|water|acc. sg. f.; in|in|into|prep. + acc.; Tiberim|Tiberis|the Tiber|acc. sg. m.; dūcit|dūcō|leads, carries|3rd sg. pres.',
 ['relative_clause','third_declension'],[],'cloaca','Cloaca Maxima',WP+'Cloaca_Maxima',subtype='vocab')

# ---------------- UNIT 11: Scholae ----------------
K('q-quem-pastores','quote','late_medieval',11,'Quem pāstōrēs laudāvēre, quibus angelī dīxēre: absit vōbīs iam timēre, nātus est rēx glōriae.','He whom the shepherds praised, to whom the angels said: “Away with fear now, the king of glory is born.”',
 "This Christmas carol from 14th-century Germany retells Luke's story of the angels appearing to the shepherds. Absit, 'let it be away', is a jussive subjunctive of absum, and its subject is the infinitive timēre. Laudāvēre and dīxēre are shortened forms of laudāvērunt and dīxērunt.",
 "The song was often sung in turns by groups of boys placed around a church. In English it is known as Shepherds left their flocks a-straying.",
 'Anonymous','Quem pastores laudavere (carol)','stanza 1','14th century',LL+'hymni.html','verified',None,
 'Quem|quī|whom|acc. sg. m.; pāstōrēs|pāstor|shepherds|nom. pl. m.; laudāvēre|laudō|praised|3rd pl. perf. (= laudāvērunt); quibus|quī|to whom|dat. pl. m.; angelī|angelus|angels|nom. pl. m.; dīxēre|dīcō|said|3rd pl. perf. (= dīxērunt); absit|absum|let it be away|3rd sg. pres. subj.; vōbīs|vōs|from you|dat. pl.; iam|iam|now|adv.; timēre|timeō|to fear|pres. inf.; nātus est|nāscor|is born, has been born|3rd sg. perf. (deponent); rēx|rēx|king|nom. sg. m.; glōriae|glōria|of glory|gen. sg. f.',
 ['jussive_subjunctive','relative_clause','perfect_tense'],['deponent'],'shepherds','Quem pastores laudavere',WP+'Quem_pastores_laudavere',register='ecclesiastical',related=['q-puer-nobis'])
K('q-puer-nobis','quote','late_medieval',11,'Cum cantibus in chorō, cum canticīs et organō, benedīcāmus Dominō.','With songs in the choir, with hymns and the organ, let us bless the Lord.',
 "This is the last verse of Puer nōbīs nāscitur, a Christmas song in a 15th-century manuscript from Trier. Benedīcāmus is a hortatory subjunctive, 'let us bless', and the words Benedīcāmus Dominō also closed the services of the medieval church. Benedīcō takes the dative, so Dominō is dative.",
 "The song begins Puer nōbīs nāscitur, rēctor angelōrum, 'a boy is born for us, the ruler of the angels'. It was printed again in the Finnish song book Piae Cantiones of 1582.",
 'Anonymous','Puer nobis nascitur (carol)','stanza 5','15th century',LL+'hymni.html','verified','The verse opens O et A et A et O, “Omega and Alpha”, which is left out here.',
 'Cum|cum|with|prep. + abl.; cantibus|cantus|songs|abl. pl. m.; in|in|in|prep. + abl.; chorō|chorus|choir|abl. sg. m.; cum|cum|with|prep. + abl.; canticīs|canticum|hymns|abl. pl. n.; et|et|and|conj.; organō|organum|organ|abl. sg. n.; benedīcāmus|benedīcō|let us bless|1st pl. pres. subj.; Dominō|dominus|the Lord|dat. sg. m.',
 ['hortatory_subjunctive','prep_ablative','dative'],[],'nativity','Puer natus in Bethlehem',WP+'Puer_natus_in_Bethlehem',register='ecclesiastical',related=['q-quem-pastores'])
K('q-dies-irae-quid-sum','quote','high_medieval',11,'Quid sum miser tunc dictūrus, quem patrōnum rogātūrus, cum vix iūstus sit sēcūrus?','What shall I, wretched one, say then, what protector shall I ask for, when even the just man is scarcely safe?',
 "The Dies īrae, a 13th-century poem on the Last Judgement, imagines the sinner standing before the throne of Christ. Sum dictūrus and rogātūrus are future participles with sum, 'I am about to say'. Cum … sit is a cum clause with the subjunctive, here meaning 'when, since'.",
 "The poem was sung in the Latin requiem mass, so composers such as Mozart and Verdi set these lines to music. Its strong rhyme and beat are typical of medieval Latin verse.",
 'attrib. Thomas of Celano','Dies irae','stanza 7','13th century',LL+'hymni.html','verified','Authorship is uncertain; the poem is traditionally credited to the Franciscan Thomas of Celano.',
 'Quid|quis|what|acc. sg. n.; sum|sum|am|1st sg. pres.; miser|miser|wretched|nom. sg. m.; tunc|tunc|then|adv.; dictūrus|dīcō|about to say|fut. act. part. nom. sg. m.; quem|quī|which|acc. sg. m.; patrōnum|patrōnus|protector, advocate|acc. sg. m.; rogātūrus|rogō|about to ask for|fut. act. part. nom. sg. m.; cum|cum|when, since|conj.; vix|vix|scarcely|adv.; iūstus|iūstus|the just man|nom. sg. m.; sit|sum|is|3rd sg. pres. subj.; sēcūrus|sēcūrus|safe|nom. sg. m.',
 ['subjunctive','participle'],[],'judgement','Dies irae',WP+'Dies_irae',register='ecclesiastical',related=['q-dies-irae'])
K('q-stabat-quis-homo','quote','high_medieval',11,'Quis est homō quī nōn flēret, Chrīstī mātrem sī vidēret in tantō suppliciō?','Who is the man who would not weep if he saw the mother of Christ in such great torment?',
 "The Stabat Mater is a 13th-century poem about Mary standing at the cross, often credited to the Franciscan Jacopone da Todi. Flēret and vidēret are imperfect subjunctives in a condition that is imagined, 'would weep … if he saw'. The question expects the answer 'no one'.",
 "Composers including Pergolesi, Haydn, Rossini and Dvořák set the whole poem to music. Paintings of the Pietà, Mary holding her dead son, show the same grief.",
 'attrib. Jacopone da Todi','Stabat Mater','stanza 5','13th century',LL+'hymni.html','verified','The authorship is traditional and uncertain.',
 'Quis|quis|who|nom. sg. m.; est|sum|is|3rd sg. pres.; homō|homō|man|nom. sg. m.; quī|quī|who|nom. sg. m.; nōn|nōn|not|adv.; flēret|fleō|would weep|3rd sg. impf. subj.; Chrīstī|Chrīstus|of Christ|gen. sg. m.; mātrem|māter|mother|acc. sg. f.; sī|sī|if|conj.; vidēret|videō|saw|3rd sg. impf. subj.; in|in|in|prep. + abl.; tantō|tantus|such great|abl. sg. n.; suppliciō|supplicium|torment, punishment|abl. sg. n.',
 ['subjunctive','relative_clause'],[],'pieta','Stabat Mater',WP+'Stabat_Mater',register='ecclesiastical',related=['q-stabat-mater'])
K('q-personent-clericuli','quote','late_medieval',11,'Omnēs clēriculī, pariter puerī, cantent ut angelī.','Let all the little clerks, the boys as well, sing like angels.',
 "Personent hodiē is a Christmas song for choirboys, the young clerks who sang in cathedral and school choirs. Cantent, 'let them sing', is a jussive subjunctive giving an order to a third person. Clēriculī is a diminutive of clēricus, 'cleric', so it means 'little clerks'.",
 "The melody is older, but the words are best known from Piae Cantiones, a song book printed in 1582 for Finnish and Swedish schools. School songs like this let pupils practise both singing and Latin.",
 'Anonymous','Personent hodie (carol)','stanza 4','14th century (printed 1582)',LL+'hymni.html','verified',None,
 'Omnēs|omnis|all|nom. pl. m.; clēriculī|clēriculus|little clerks, choirboys|nom. pl. m.; pariter|pariter|equally, as well|adv.; puerī|puer|boys|nom. pl. m.; cantent|cantō|let them sing|3rd pl. pres. subj.; ut|ut|like, as|conj.; angelī|angelus|angels|nom. pl. m.',
 ['jussive_subjunctive','third_person_plural'],[],'clerics','Personent hodie',WP+'Personent_hodie',register='ecclesiastical')
K('q-aquinas-utrum','quote','high_medieval',11,'Prīmō, utrum Deum esse sit per sē nōtum.','First, whether it is self-evident that God exists.',
 "Thomas Aquinas set out each question of his Summa theologiae as a list of things to be asked, the way a Paris master organised a disputation. Utrum … sit is an indirect question with the subjunctive, 'whether it is'. Inside it, Deum esse is an indirect statement, 'that God exists'.",
 "Aquinas answers no: God's existence must be shown by argument, which leads to his famous five ways. A disputation set out objections, an authority, the master's answer, and replies to each objection.",
 'Thomas Aquinas','Aquinas, Summa theologiae','I, q. 2, prologue','about 1265-1274','https://www.corpusthomisticum.org/sth1002.html','verified',None,
 'Prīmō|prīmō|first|adv.; utrum|utrum|whether|conj.; Deum|deus|God|acc. sg. m.; esse|sum|to be, to exist|pres. inf.; sit|sum|is|3rd sg. pres. subj.; per|per|through|prep. + acc.; sē|suī|itself|acc.; nōtum|nōscō|known|perf. pass. part. nom. sg. n.',
 ['indirect_question','indirect_statement'],[],'aquinas','Summa Theologica',WP+'Summa_Theologica',register='medieval',related=['q-aquinas-quinque'])
K('q-cb-ecce-gratum','quote','high_medieval',11,'Iamiam cēdant trīstia! Aestās redit, nunc recēdit hiemis saevitia.','Now, now let sad things give way! Summer returns, now the savagery of winter withdraws.',
 "In Ecce grātum, a spring song from the Carmina Burana, the poet welcomes the warm season and the end of winter. Cēdant, 'let them give way', is a jussive subjunctive. Trīstia is a neuter plural adjective used as a noun, 'sad things'.",
 "Carl Orff set this song in his Carmina Burana of 1937. The manuscript spells aestās and hiemis without the classical diphthongs, as estas and hyemis.",
 'Carmina Burana (anonymous)','Carmina Burana','143','13th century',WS+'Carmina_Burana_(Orff)/Ecce_gratum','verified','Spelling normalised to classical forms: the source has Estas and Hyemis sevitia.',
 'Iamiam|iamiam|now, right now|adv.; cēdant|cēdō|let them give way|3rd pl. pres. subj.; trīstia|trīstis|sad things|nom. pl. n.; Aestās|aestās|summer|nom. sg. f.; redit|redeō|returns|3rd sg. pres.; nunc|nunc|now|adv.; recēdit|recēdō|withdraws|3rd sg. pres.; hiemis|hiems|of winter|gen. sg. f.; saevitia|saevitia|savagery, harshness|nom. sg. f.',
 ['jussive_subjunctive','neuter_plural'],[],'april','Carmina Burana',WP+'Carmina_Burana',related=['q-cb-omittamus'])
K('q-gaudeamus','quote','early_modern',11,'Gaudeāmus igitur, iuvenēs dum sumus!','Let us rejoice, therefore, while we are young!',
 "Gaudeāmus igitur is the best-known student song in Latin, still sung at university graduations. Its themes, short life, wine and the university, go back to the songs of medieval students, but the text we sing was printed by Christian Wilhelm Kindleben in 1781. Gaudeāmus is a hortatory subjunctive, 'let us rejoice'.",
 "Later verses cry Vīvat acadēmia! Vīvant professōrēs!, 'long live the university, long live the professors'. Brahms quoted the tune in his Academic Festival Overture.",
 'Christian Wilhelm Kindleben (editor)','Gaudeamus igitur','stanza 1','1781',WS+'Gaudeamus_Igitur','verified','The song has older roots; Kindleben published this version in his Studentenlieder.',
 'Gaudeāmus|gaudeō|let us rejoice|1st pl. pres. subj.; igitur|igitur|therefore|conj.; iuvenēs|iuvenis|young people|nom. pl. m.; dum|dum|while|conj.; sumus|sum|we are|1st pl. pres.',
 ['hortatory_subjunctive'],['dum_clause'],'gaudeamus','Gaudeamus igitur',WP+'Gaudeamus_igitur')
K('q-bernard-plus-potuit','quote','high_medieval',11,'… aut plūs potuit Adam in malō quam Chrīstus in bonō?','… or did Adam have more power for evil than Christ for good?',
 "Bernard of Clairvaux, the great Cistercian abbot, asks this question when he argues that Christ's goodness reaches all people just as Adam's sin did. Plūs … quam is a comparison, 'more than'. The question expects the answer no.",
 "The passage comes from Bernard's In Praise of the New Knighthood, written around 1130 for the Knights Templar. Bernard was also a famous preacher, and he called for the Second Crusade.",
 'Bernard of Clairvaux','Bernard, De laude novae militiae','11.23','about 1130',LL+'bernardclairvaux.shtml','verified','The question follows itane Dei iustitia magis ad condemnandum, quam ad restaurandum valuit?',
 'aut|aut|or|conj.; plūs|multum|more|comp. adv.; potuit|possum|was able, had power|3rd sg. perf.; Adam|Adam|Adam|nom. sg. m.; in|in|in, for|prep. + abl.; malō|malum|evil|abl. sg. n.; quam|quam|than|conj.; Chrīstus|Chrīstus|Christ|nom. sg. m.; in|in|in, for|prep. + abl.; bonō|bonum|good|abl. sg. n.',
 ['comparative','possum'],[],'bernard','Bernard of Clairvaux',WP+'Bernard_of_Clairvaux',register='ecclesiastical')

# ---------------- UNIT 12: Regna ----------------
K('q-kempis-utinam','quote','late_medieval',12,'Utinam per ūnam diem bene essēmus conversātī in hōc mundō.','If only we had lived well for a single day in this world.',
 "In the chapter of the Imitation of Christ on thinking about death, Thomas à Kempis complains that a long life often adds faults instead of mending them. Utinam with the pluperfect subjunctive, essēmus conversātī, expresses a wish about the past that did not come true. Conversor is a deponent verb, 'to live, conduct oneself'.",
 "The text has the feminine ūnam diem, a medieval use; classical Latin usually treats diēs as masculine. Kempis spent most of his life in the monastery of Mount St Agnes near Zwolle.",
 'Thomas à Kempis','Thomas à Kempis, De imitatione Christi','1.23.2','about 1420',LL+'kempis/kempis1.shtml','verified','Verbatim: per unam diem, with diēs treated as feminine (as often when it means a set day or a period of time).',
 'Utinam|utinam|if only|particle; per|per|for, throughout|prep. + acc.; ūnam|ūnus|one, a single|acc. sg. f.; diem|diēs|day|acc. sg. f. (diēs here feminine); bene|bene|well|adv.; essēmus conversātī|conversor|we had lived|1st pl. pluperf. subj. (deponent); in|in|in|prep. + abl.; hōc|hic|this|abl. sg. m.; mundō|mundus|world|abl. sg. m.',
 ['pluperfect','deponent','subjunctive'],[],'kempis','The Imitation of Christ',WP+'The_Imitation_of_Christ',register='ecclesiastical',related=['q-kempis-operari'])
K('q-einhard-caenandum','quote','early_medieval',12,'Inter caenandum aut aliquod acroāma aut lēctōrem audiēbat. Legēbantur eī historiae et antīquōrum rēs gestae.','During dinner he listened either to some entertainment or to a reader. Histories and the deeds of the ancients were read to him.',
 "Einhard, who lived at Charlemagne's court, describes the king's simple dinners of four courses. Inter caenandum, 'during dining', uses the gerund, a verbal noun, after a preposition. Legēbantur is an imperfect passive, 'were read'.",
 "Einhard adds that Charlemagne loved Augustine's City of God. Charlemagne could read, but he tried to learn to write only late in life and never mastered it.",
 'Einhard','Einhard, Vita Karoli Magni','24','about 825',LL+'ein.html','verified',None,
 'Inter|inter|during, among|prep. + acc.; caenandum|caenō|dining|gerund acc.; aut|aut|either|conj.; aliquod|aliquī|some|acc. sg. n.; acroāma|acroāma|entertainment, performer|acc. sg. n.; aut|aut|or|conj.; lēctōrem|lēctor|reader|acc. sg. m.; audiēbat|audiō|he listened to|3rd sg. impf.; Legēbantur|legō|were read|3rd pl. impf. pass.; eī|is|to him|dat. sg. m.; historiae|historia|histories|nom. pl. f.; et|et|and|conj.; antīquōrum|antīquus|of the ancients|gen. pl. m.; rēs|rēs|things|nom. pl. f.; gestae|gerō|done|perf. pass. part. nom. pl. f.',
 ['gerund','passive_voice','imperfect'],[],'charlemagne','Vita Karoli Magni',WP+'Vita_Karoli_Magni',register='medieval',related=['q-einhard-temptabat'])
K('q-asser-candelas','quote','early_medieval',12,'… cumque tanta cēra mēnsūrāta fuisset, quae septuāgintā duōs dēnāriōs pēnsāret, sex candēlās … capellānōs facere iussit.','… and when as much wax had been measured out as would weigh seventy-two pennies, he ordered his chaplains to make six candles.',
 "Asser explains how King Alfred measured time before clocks: six candles, each marked in inches, burned through a day and night. Mēnsūrāta fuisset is a pluperfect subjunctive in a cum clause, 'when it had been measured'. Iussit takes an accusative and infinitive, capellānōs facere.",
 "When draughts made the candles burn unevenly, Alfred had lanterns built of wood and thin horn to shield them. He used the candles to give half of his time to God.",
 'Asser','Asser, Vita Alfredi','104','893',LL+'asserius.html','verified','The text adds unamquamque aequa lance, inde, “each of equal weight, from it”, between candelas and capellanos.',
 'cumque|cum + -que|and when|conj.; tanta|tantus|so much|nom. sg. f.; cēra|cēra|wax|nom. sg. f.; mēnsūrāta fuisset|mēnsūrō|had been measured|3rd sg. pluperf. pass. subj.; quae|quī|which|nom. sg. f.; septuāgintā|septuāgintā|seventy|indecl.; duōs|duo|two|acc. pl. m.; dēnāriōs|dēnārius|pennies|acc. pl. m.; pēnsāret|pēnsō|would weigh|3rd sg. impf. subj.; sex|sex|six|indecl.; candēlās|candēla|candles|acc. pl. f.; capellānōs|capellānus|chaplains|acc. pl. m.; facere|faciō|to make|pres. inf.; iussit|iubeō|he ordered|3rd sg. perf.',
 ['pluperfect','subjunctive','numerals'],[],'lantern','Candle clock',WP+'Candle_clock',register='medieval',related=['q-asser-libris'])
K('q-arbroath-centum','quote','late_medieval',12,'Quia quamdiū centum ex nōbīs vīvī remānserint, numquam Anglōrum dominiō aliquātenus volumus subiugārī.','For as long as a hundred of us remain alive, we will never on any terms be brought under English rule.',
 "In 1320 the barons of Scotland sent this letter to Pope John XXII, asking him to recognise Robert the Bruce as king and to persuade England to leave Scotland in peace. Remānserint is a future perfect, 'shall have remained'. Subiugārī is a present passive infinitive after volumus.",
 "The next sentence says they fight not for glory, riches or honours but for freedom alone, which no good man gives up except with his life. The letter was probably drafted at Arbroath Abbey by its abbot, Bernard, chancellor of Scotland.",
 'Barons of Scotland','Declaration of Arbroath','—','1320',LL+'arbroath.html','verified','Manuscript spellings viui and nuncquam are normalised to vīvī and numquam.',
 'Quia|quia|for, because|conj.; quamdiū|quamdiū|as long as|conj.; centum|centum|a hundred|indecl.; ex|ex|of, from|prep. + abl.; nōbīs|nōs|us|abl. pl.; vīvī|vīvus|alive|nom. pl. m.; remānserint|remaneō|shall have remained|3rd pl. fut. perf.; numquam|numquam|never|adv.; Anglōrum|Anglus|of the English|gen. pl. m.; dominiō|dominium|rule|dat. sg. n.; aliquātenus|aliquātenus|to any extent|adv.; volumus|volō|we are willing|1st pl. pres.; subiugārī|subiugō|to be subjugated|pres. pass. inf.',
 ['passive_voice','numerals'],[],'arbroath','Declaration of Arbroath',WP+'Declaration_of_Arbroath',register='medieval-legal')
K('q-debury-libris','quote','late_medieval',12,'In librīs mortuōs quasi vīvōs inveniō; in librīs futūra praevideō.','In books I find the dead as if alive; in books I foresee things to come.',
 "Richard de Bury, bishop of Durham and tutor to King Edward III, collected so many books that they covered the floor of his room. His Philobiblon, 'Love of Books', praises reading and gives rules for treating books well. Futūra, 'things to come', is the future participle of sum used as a neuter plural noun.",
 "He asks readers not to eat over open books or mark them with dirty fingernails. He meant to leave his library to Durham College, Oxford, but much of it was sold to pay his debts.",
 'Richard de Bury','Richard de Bury, Philobiblon','1','1345',LL+'debury.html','verified',None,
 'In|in|in|prep. + abl.; librīs|liber|books|abl. pl. m.; mortuōs|mortuus|the dead|acc. pl. m.; quasi|quasi|as if|adv.; vīvōs|vīvus|alive|acc. pl. m.; inveniō|inveniō|I find|1st sg. pres.; in|in|in|prep. + abl.; librīs|liber|books|abl. pl. m.; futūra|sum|things to come|fut. part. acc. pl. n.; praevideō|praevideō|I foresee|1st sg. pres.',
 ['participle','neuter_plural','prep_ablative'],[],'library','Philobiblon',WP+'Philobiblon',register='medieval')
K('q-magna-carta-nulli','quote','high_medieval',12,'Nūllī vendēmus, nūllī negābimus aut differēmus rēctum aut iūstitiam.','To no one will we sell, to no one will we deny or delay right or justice.',
 "In clause 40 of Magna Carta, King John promises that justice will not be bought, refused or put off. The king speaks in the royal 'we', and every verb is future. Nūllī is dative, 'to no one', and the sentence repeats it for force.",
 "This clause and clause 39 are among the few parts of Magna Carta still law in England. King John set his seal to the charter at Runnymede in June 1215 and within months the pope had annulled it.",
 'King John and the barons','Magna Carta','40','1215',LL+'magnacarta.html','verified','The manuscript spelling justiciam is normalised to iūstitiam.',
 'Nūllī|nūllus|to no one|dat. sg. m.; vendēmus|vendō|we will sell|1st pl. fut.; nūllī|nūllus|to no one|dat. sg. m.; negābimus|negō|we will deny|1st pl. fut.; aut|aut|or|conj.; differēmus|differō|we will delay|1st pl. fut.; rēctum|rēctum|right|acc. sg. n.; aut|aut|or|conj.; iūstitiam|iūstitia|justice|acc. sg. f.',
 ['future_tense','dative'],[],'johnseal','Magna Carta',WP+'Magna_Carta',register='medieval-legal',related=['q-magna-carta-39'])
K('q-oresme-quamvis','quote','late_medieval',12,'Quamvīs prō ūtilitāte commūnī prīnceps habeat signāre numisma, nōn tamen ipse dominus seu proprietārius est monētae currentis in suō prīncipātū.','Although for the common good the prince has to stamp the coinage, he is not, however, the lord or owner of the money that circulates in his realm.',
 "Nicole Oresme wrote his treatise on money when French kings were profiting by debasing their coins. Here he states his main claim: the king only stamps the coin for everyone's benefit, and the money belongs to the people who use it. Quamvīs with the subjunctive habeat means 'although'.",
 "Oresme was tutor and adviser to the future Charles V of France. His argument that bad money drives out good was later credited to the Englishman Thomas Gresham.",
 'Nicole Oresme','Oresme, De moneta','6','about 1356',LL+'oresmius.html','verified',None,
 'Quamvīs|quamvīs|although|conj.; prō|prō|for|prep. + abl.; ūtilitāte|ūtilitās|benefit, good|abl. sg. f.; commūnī|commūnis|common|abl. sg. f.; prīnceps|prīnceps|prince, ruler|nom. sg. m.; habeat|habeō|has (to)|3rd sg. pres. subj.; signāre|signō|to stamp|pres. inf.; numisma|numisma|coin, coinage|acc. sg. n.; nōn|nōn|not|adv.; tamen|tamen|however|adv.; ipse|ipse|he himself|nom. sg. m.; dominus|dominus|lord|nom. sg. m.; seu|seu|or|conj.; proprietārius|proprietārius|owner|nom. sg. m.; est|sum|is|3rd sg. pres.; monētae|monēta|of the money|gen. sg. f.; currentis|currō|circulating|pres. part. gen. sg. f.; in|in|in|prep. + abl.; suō|suus|his|abl. sg. m.; prīncipātū|prīncipātus|realm, rule|abl. sg. m.',
 ['subjunctive','present_participle'],[],'royaldor','Nicole Oresme',WP+'Nicole_Oresme',register='medieval',related=['q-oresme-moneta'])
K('q-petrarch-vixisti','quote','late_medieval',12,'Tū quidem, Cicerō, quod pāce tuā dīxerim, ut homō vīxistī, ut ōrātor dīxistī, ut philosophus scrīpsistī.','You, Cicero, if I may say so with your leave, lived as a man, spoke as an orator, wrote as a philosopher.',
 "In his second letter to the long-dead Cicero, Petrarch separates the man from the writer: he blames Cicero's life but admires his genius and his eloquence. Quod pāce tuā dīxerim is a polite perfect subjunctive, 'if I may say so by your leave'. The three ut clauses mean 'as'.",
 "Petrarch rediscovered Cicero's letters to Atticus in Verona in 1345. Cicero's style became the model for Renaissance Latin.",
 'Petrarch','Petrarch, Epistolae familiares','24.4','1345',LL+'petrarch.ep1.html','verified',None,
 'Tū|tū|you|nom. sg.; quidem|quidem|indeed|adv.; Cicerō|Cicerō|Cicero|voc. sg. m.; quod|quī|which, if|acc. sg. n.; pāce|pāx|peace, leave|abl. sg. f.; tuā|tuus|your|abl. sg. f.; dīxerim|dīcō|I may say|1st sg. perf. subj.; ut|ut|as|conj.; homō|homō|man|nom. sg. m.; vīxistī|vīvō|you lived|2nd sg. perf.; ut|ut|as|conj.; ōrātor|ōrātor|orator|nom. sg. m.; dīxistī|dīcō|you spoke|2nd sg. perf.; ut|ut|as|conj.; philosophus|philosophus|philosopher|nom. sg. m.; scrīpsistī|scrībō|you wrote|2nd sg. perf.',
 ['subjunctive','perfect_tense','vocative'],[],'petrarch','Petrarch',WP+'Petrarch',register='medieval',related=['q-petrarch-irascimur'])
K('q-dante-monarchia','quote','late_medieval',12,'… et Imperātōre, quī secundum philosophica documenta genus hūmānum ad temporālem fēlīcitātem dīrigeret.','… and of an emperor, to guide the human race to happiness in this life according to the teachings of philosophy.',
 "At the end of his Monarchia, Dante argues that humans have two goals and so need two guides: the pope leads them to eternal life, the emperor to happiness on earth. Quī … dīrigeret is a relative clause of purpose with the subjunctive, 'who would guide, to guide'. Dante wanted the emperor to be free of the pope's control.",
 "A papal legate had the book burned in 1329, and it was later placed on the Index of Forbidden Books. Dante wrote it in Latin around 1312 to 1318.",
 'Dante Alighieri','Dante, Monarchia','3.16.10','about 1312-1318',LL+'dante/mon3.shtml','verified','The text spells phylosophica; here classical philosophica.',
 'et|et|and|conj.; Imperātōre|imperātor|emperor|abl. sg. m.; quī|quī|who|nom. sg. m.; secundum|secundum|according to|prep. + acc.; philosophica|philosophicus|philosophical|acc. pl. n.; documenta|documentum|teachings|acc. pl. n.; genus|genus|race, kind|acc. sg. n.; hūmānum|hūmānus|human|acc. sg. n.; ad|ad|to|prep. + acc.; temporālem|temporālis|of this life, temporal|acc. sg. f.; fēlīcitātem|fēlīcitās|happiness|acc. sg. f.; dīrigeret|dīrigō|would guide|3rd sg. impf. subj.',
 ['subjunctive','relative_clause'],[],'monarchia','De Monarchia',WP+'De_Monarchia',register='medieval')

# ---------------- UNIT 13: Ius ----------------
K('q-xii-sepelito','quote','republic',13,'Hominem mortuum in urbe nē sepelītō nēve ūritō.','Do not bury or burn a dead person within the city.',
 "This law of the Twelve Tables, from about 450 BC, banned burials inside Rome. That is why tombs lined the roads outside city gates at Rome and Pompeii. Sepelītō and ūritō are future imperatives, the 'you shall' of Roman law, and nē … nēve makes them negative.",
 "Cicero, who quotes the law, explains it as a guard against fire. Burial inside the walls stayed forbidden in Roman law for centuries.",
 'Twelve Tables','Lex XII Tabularum','10.1','about 450 BC',LL+'12tables.html','verified','The text survives only in quotations by later writers (here Cicero, De legibus 2.58).',
 'Hominem|homō|person|acc. sg. m.; mortuum|mortuus|dead|acc. sg. m.; in|in|in, within|prep. + abl.; urbe|urbs|city|abl. sg. f.; nē|nē|not|neg. particle; sepelītō|sepeliō|shall bury|fut. imperative 2nd/3rd sg.; nēve|nēve|nor|conj.; ūritō|ūrō|shall burn|fut. imperative 2nd/3rd sg.',
 ['future_imperative','prep_ablative'],[],'nocera','Twelve Tables',WP+'Twelve_Tables',register='classical',related=['q-xii-venum'])
K('q-xii-venum','quote','republic',13,'Sī pater fīlium ter vēnum duit, fīlius ā patre līber estō.','If a father sells his son three times, the son shall be free from the father.',
 "Under early Roman law a father could sell his son into the power of another man. This law of the Twelve Tables set a limit: after three sales the son was free of his father's power. Estō is the future imperative of sum, 'he shall be', and duit is an old form of the subjunctive of dō.",
 "Lawyers later used the rule as a trick: a father who wanted to free a son made three pretend sales. Freedmen and freedwomen, like the family shown on this tomb, also passed out of a master's power.",
 'Twelve Tables','Lex XII Tabularum','4.2','about 450 BC',LL+'12tables.html','verified','Preserved by Gaius (Institutes 1.132) and Ulpian.',
 'Sī|sī|if|conj.; pater|pater|father|nom. sg. m.; fīlium|fīlius|son|acc. sg. m.; ter|ter|three times|adv.; vēnum|vēnum|for sale|acc. sg. n.; duit|dō|gives, puts|3rd sg. pres. subj. (archaic); fīlius|fīlius|son|nom. sg. m.; ā|ā, ab|from|prep. + abl.; patre|pater|father|abl. sg. m.; līber|līber|free|nom. sg. m.; estō|sum|shall be|fut. imperative 3rd sg.',
 ['future_imperative','subjunctive'],[],'rabirius','Patria potestas',WP+'Patria_potestas',related=['q-xii-sepelito'])
K('q-cicero-sunto','quote','republic',13,'Rēgiō imperiō duo suntō … mīlitiae summum iūs habentō, nēminī parentō.','There shall be two with royal power … in war they shall have supreme authority and obey no one.',
 "In On the Laws, Cicero writes his own ideal constitution in the old style of the Twelve Tables. This clause describes the two consuls, who shared the power once held by the kings. Suntō, habentō and parentō are third-person plural future imperatives, 'they shall be, have, obey'.",
 "The same clause ends with the famous rule salus populī suprēma lēx estō, 'the safety of the people shall be the highest law'. Having two consuls meant each could block the other.",
 'Cicero','Cicero, De legibus','3.8','about 52 BC',LL+'cicero/leg3.shtml','verified',None,
 'Rēgiō|rēgius|royal|abl. sg. n.; imperiō|imperium|power, command|abl. sg. n.; duo|duo|two|nom. pl. m.; suntō|sum|there shall be|fut. imperative 3rd pl.; mīlitiae|mīlitia|in war|loc. sg. f.; summum|summus|highest|acc. sg. n.; iūs|iūs|right, authority|acc. sg. n.; habentō|habeō|they shall have|fut. imperative 3rd pl.; nēminī|nēmō|no one|dat. sg.; parentō|pāreō|they shall obey|fut. imperative 3rd pl.',
 ['future_imperative','superlative','numerals'],[],'brutus','Roman consul',WP+'Roman_consul',related=['q-cicero-salus'])
K('q-dig-placuit','quote','empire',13,'Quod prīncipī placuit, lēgis habet vigōrem.','What has pleased the emperor has the force of law.',
 "The jurist Ulpian wrote this in a textbook for beginners in the early 3rd century AD, and Justinian placed it in the Digest. Ulpian explains why: by the lēx rēgia the people had handed all their power to the emperor. Placuit is an impersonal verb, 'it pleased', with the dative prīncipī.",
 "Medieval lawyers argued over this sentence for centuries, some using it to support kings and others to limit them. Ulpian's next words say that whatever the emperor decides by letter or decree is law as well.",
 'Ulpian (Digest)','Digesta Iustiniani','1.4.1 pr.','early 3rd century AD (Digest 533)',LL+'justinian/digest1.shtml','verified',None,
 'Quod|quī|what, that which|nom. sg. n.; prīncipī|prīnceps|the emperor|dat. sg. m.; placuit|placet|has pleased|3rd sg. perf. (impersonal + dat.); lēgis|lēx|of law|gen. sg. f.; habet|habeō|has|3rd sg. pres.; vigōrem|vigor|force|acc. sg. m.',
 ['impersonal_verb','relative_clause','dative'],[],'vatlaw','Digest (Roman law)',WP+'Digest_(Roman_law)',register='classical',related=['q-dig-operam'])
K('q-gaius-omnes-populi','quote','empire',13,'Omnēs populī quī lēgibus et mōribus reguntur partim suō propriō, partim commūnī omnium hominum iūre ūtuntur.','All peoples who are governed by laws and customs use partly their own law and partly the law common to all humankind.',
 "The 2nd-century jurist Gaius opened his Institutes with this distinction, and Justinian's lawyers placed it in the Digest. A people's own law is its iūs cīvīle; the law that natural reason sets up among all humans is the iūs gentium. Ūtuntur is a deponent verb that takes the ablative, here iūre.",
 "The idea of a law shared by all nations later fed into international law. Gaius' own textbook was rediscovered in 1816 under later writing in a manuscript at Verona.",
 'Gaius (Digest)','Digesta Iustiniani','1.1.9','2nd century AD (Digest 533)',LL+'justinian/digest1.shtml','verified',None,
 'Omnēs|omnis|all|nom. pl. m.; populī|populus|peoples|nom. pl. m.; quī|quī|who|nom. pl. m.; lēgibus|lēx|by laws|abl. pl. f.; et|et|and|conj.; mōribus|mōs|customs|abl. pl. m.; reguntur|regō|are governed|3rd pl. pres. pass.; partim|partim|partly|adv.; suō|suus|their own|abl. sg. n.; propriō|proprius|own, particular|abl. sg. n.; partim|partim|partly|adv.; commūnī|commūnis|common|abl. sg. n.; omnium|omnis|of all|gen. pl. m.; hominum|homō|people|gen. pl. m.; iūre|iūs|law|abl. sg. n.; ūtuntur|ūtor|use|3rd pl. pres. (deponent + abl.)',
 ['ablative_with_deponent','relative_clause','passive_voice'],[],'justinian2','Jus gentium',WP+'Jus_gentium',related=['q-inst-iustitia'])
K('q-trajan-conquirendi','quote','empire',13,'Conquīrendī nōn sunt; sī dēferantur et arguantur, pūniendī sunt.','They are not to be hunted out; if they are reported and proved guilty, they are to be punished.',
 "Around AD 112 Pliny, governor of Bithynia, asked the emperor Trajan what to do about people accused of being Christians. Trajan answered that they should not be sought out, and anonymous accusations should be ignored. Conquīrendī and pūniendī are gerundives with sunt, expressing what must or must not be done.",
 "Trajan added that anyone who denied it and prayed to the Roman gods should be pardoned. This exchange is one of the earliest Roman documents about how to treat Christians.",
 'Trajan','Pliny, Epistulae','10.97.2','about AD 112',LL+'pliny.ep10.html','verified','The subject is qui Christiani ad te delati fuerant, people reported to Pliny as Christians.',
 'Conquīrendī|conquīrō|to be hunted out|gerundive nom. pl. m.; nōn|nōn|not|adv.; sunt|sum|are|3rd pl. pres.; sī|sī|if|conj.; dēferantur|dēferō|they are reported|3rd pl. pres. pass. subj.; et|et|and|conj.; arguantur|arguō|they are proved guilty|3rd pl. pres. pass. subj.; pūniendī|pūniō|to be punished|gerundive nom. pl. m.; sunt|sum|are|3rd pl. pres.',
 ['gerundive','passive_voice','subjunctive'],[],'trajan','Pliny the Younger on Christians',WP+'Pliny_the_Younger_on_Christians')
K('q-tacitus-licet-concilium','quote','empire',13,'Licet apud concilium accūsāre quoque et discrīmen capitis intendere.','It is permitted to bring accusations before the assembly too, and to press a charge that could cost a man his life.',
 "In his Germania of AD 98, Tacitus describes how the Germanic peoples judged crimes in their tribal assemblies. Licet, 'it is permitted', is an impersonal verb followed by infinitives. Discrīmen capitis, 'danger to the head', means a charge punishable by death.",
 "Tacitus says traitors were hanged from trees, while cowards were drowned in bogs under a hurdle of branches. The only full medieval manuscript of the Germania, the Codex Aesinas, was brought from Germany to Rome in the 1450s.",
 'Tacitus','Tacitus, Germania','12','AD 98',LL+'tacitus/tac.ger.shtml','verified',None,
 'Licet|licet|it is permitted|3rd sg. pres. (impersonal); apud|apud|before, at|prep. + acc.; concilium|concilium|assembly|acc. sg. n.; accūsāre|accūsō|to accuse|pres. inf.; quoque|quoque|also|adv.; et|et|and|conj.; discrīmen|discrīmen|danger, risk|acc. sg. n.; capitis|caput|of the head, of life|gen. sg. n.; intendere|intendō|to press, bring|pres. inf.',
 ['impersonal_verb','infinitive'],[],'aesinas','Germania (book)',WP+'Germania_(book)',register='classical')
K('q-dig-nemo-plus','quote','empire',13,'Nēmō plūs iūris ad alium trānsferre potest, quam ipse habēret.','No one can transfer more right to another than he himself would have.',
 "This rule of Ulpian is one of the general maxims collected at the end of Justinian's Digest. You cannot hand on a better title than you hold: someone who buys from a thief does not become the owner. Plūs iūris, 'more of right', is a comparative with a genitive, and quam means 'than'.",
 "Lawyers still quote it in a shorter form, nēmō dat quod nōn habet, 'no one gives what he does not have'. Modern law keeps the rule, with some exceptions to protect honest buyers.",
 'Ulpian (Digest)','Digesta Iustiniani','50.17.54','early 3rd century AD (Digest 533)',LL+'justinian/digest50.shtml','verified',None,
 'Nēmō|nēmō|no one|nom. sg.; plūs|plūs|more|comp. acc. sg. n.; iūris|iūs|of right|gen. sg. n.; ad|ad|to|prep. + acc.; alium|alius|another|acc. sg. m.; trānsferre|trānsferō|to transfer|pres. inf.; potest|possum|can|3rd sg. pres.; quam|quam|than|conj.; ipse|ipse|he himself|nom. sg. m.; habēret|habeō|would have|3rd sg. impf. subj.',
 ['comparative','possum_infinitive','genitive'],[],'bronzelaw','Nemo dat quod non habet',WP+'Nemo_dat_quod_non_habet',related=['q-dig-licet'])
K('q-livy-fons-iuris','quote','republic',13,'… quī nunc quoque, in hōc immēnsō aliārum super aliās acervātārum lēgum cumulō, fōns omnis pūblicī prīvātīque est iūris.','… which even now, in this vast heap of laws piled one upon another, is the source of all public and private law.',
 "Livy describes how the ten commissioners, the decemvirs, wrote the Twelve Tables in 451 to 450 BC. Even in his own day, four centuries later, he calls them the source of all Roman law. Acervātārum is a perfect passive participle, 'piled up', agreeing with lēgum.",
 "Cicero says that boys in his youth learned the Twelve Tables by heart as a set song. Livy wrote his history of Rome under Augustus.",
 'Livy','Livy, Ab urbe condita','3.34.6','about 25 BC',LL+'livy/liv.3.shtml','verified','The relative quī looks back to the code of the Ten Tables in the previous clause.',
 'quī|quī|which|nom. sg. m.; nunc|nunc|now|adv.; quoque|quoque|also, even|adv.; in|in|in|prep. + abl.; hōc|hic|this|abl. sg. m.; immēnsō|immēnsus|vast|abl. sg. m.; aliārum|alius|some|gen. pl. f.; super|super|upon|prep. + acc.; aliās|alius|others|acc. pl. f.; acervātārum|acervō|piled up|perf. pass. part. gen. pl. f.; lēgum|lēx|of laws|gen. pl. f.; cumulō|cumulus|heap|abl. sg. m.; fōns|fōns|source|nom. sg. m.; omnis|omnis|all|gen. sg. n.; pūblicī|pūblicus|public|gen. sg. n.; prīvātīque|prīvātus + -que|and private|gen. sg. n.; est|sum|is|3rd sg. pres.; iūris|iūs|of law|gen. sg. n.',
 ['participle','relative_clause','genitive'],[],'livy','Twelve Tables',WP+'Twelve_Tables',register='classical',related=['q-xii-sepelito'])

# ---------------- UNIT 14: Scientia ----------------
K('q-bacon-parendo','quote','early_modern',14,'Scientia et potentia hūmāna in idem coincidunt … Nātūra enim nōn nisi pārendō vincitur.','Human knowledge and human power come to the same thing … For nature is conquered only by obeying her.',
 "Francis Bacon's New Organon of 1620 argued that science should study nature by careful experiment instead of relying on ancient authorities. To control nature we must first learn and follow its laws. Pārendō, 'by obeying', is a gerund in the ablative, and vincitur is a present passive.",
 "Bacon left out the words between: because ignorance of the cause prevents the effect. The title page shows a ship sailing past the Pillars of Hercules, the old limits of the known world.",
 'Francis Bacon','Bacon, Novum Organum','1.3','1620',LL+'bacon/bacon.liber1.shtml','verified','Omitted: quia ignoratio causae destituit effectum.',
 'Scientia|scientia|knowledge|nom. sg. f.; et|et|and|conj.; potentia|potentia|power|nom. sg. f.; hūmāna|hūmānus|human|nom. sg. f.; in|in|into|prep. + acc.; idem|īdem|the same thing|acc. sg. n.; coincidunt|coincidō|coincide|3rd pl. pres.; Nātūra|nātūra|nature|nom. sg. f.; enim|enim|for|conj.; nōn|nōn|not|adv.; nisi|nisi|except|conj.; pārendō|pāreō|by obeying|gerund abl.; vincitur|vincō|is conquered|3rd sg. pres. pass.',
 ['gerund','passive_voice'],[],'organum','Novum Organum',WP+'Novum_Organum',register='classical')
K('q-spinoza-praeclara','quote','early_modern',14,'Sed omnia praeclāra tam difficilia quam rāra sunt.','But all excellent things are as difficult as they are rare.',
 "These are the very last words of Spinoza's Ethics, published in 1677 after his death. He admits that the path to freedom of mind he has described is hard, but argues that this is why so few find it. Tam … quam compares two qualities, 'as … as'.",
 "Spinoza set out the Ethics like a geometry book, with definitions, axioms and proofs. He earned his living partly by grinding lenses in the Netherlands.",
 'Baruch Spinoza','Spinoza, Ethica','5.42 scholium','1677',LL+'spinoza.ethica5.html','verified',None,
 'Sed|sed|but|conj.; omnia|omnis|all|nom. pl. n.; praeclāra|praeclārus|excellent things|nom. pl. n.; tam|tam|as, so|adv.; difficilia|difficilis|difficult|nom. pl. n.; quam|quam|as|conj.; rāra|rārus|rare|nom. pl. n.; sunt|sum|are|3rd pl. pres.',
 ['neuter_plural','adjectives'],[],'spinoza','Ethics (Spinoza)',WP+'Ethics_(Spinoza_book)',register='classical')
K('q-more-oves','quote','early_modern',14,'Ovēs vestrae … tam edācēs atque indomitae esse coepērunt, ut hominēs dēvorent ipsōs.','Your sheep … have begun to be so greedy and wild that they devour men themselves.',
 "In Thomas More's Utopia of 1516, a traveller tells an English cardinal that landlords are turning fields into sheep pasture for profitable wool. Farmers lose their homes and are driven to theft. Tam … ut with the subjunctive dēvorent is a result clause, 'so greedy that they devour'.",
 "The sheep that eat men became a famous image of the enclosure of common land. More's book gave English the word utopia, 'no place'.",
 'Thomas More','More, Utopia','book 1','1516',LL+'more.html','verified','The text reads inquam uestrae, quae tam mites esse … solent, nunc—uti fertur—tam edaces…; the words are shortened here.',
 'Ovēs|ovis|sheep|nom. pl. f.; vestrae|vester|your|nom. pl. f.; tam|tam|so|adv.; edācēs|edāx|greedy|nom. pl. f.; atque|atque|and|conj.; indomitae|indomitus|wild|nom. pl. f.; esse|sum|to be|pres. inf.; coepērunt|coepī|have begun|3rd pl. perf.; ut|ut|that|conj.; hominēs|homō|men|acc. pl. m.; dēvorent|dēvorō|they devour|3rd pl. pres. subj.; ipsōs|ipse|themselves|acc. pl. m.',
 ['subjunctive','infinitive'],[],'utopia','Utopia (book)',WP+'Utopia_(book)',register='classical')
K('q-luther-thesis1','quote','early_modern',14,'Dominus et magister noster Iēsus Chrīstus, dīcendō “Paenitentiam agite”, omnem vītam fidēlium paenitentiam esse voluit.','Our Lord and Master Jesus Christ, in saying “Repent”, willed the whole life of believers to be one of repentance.',
 "This is the first of the 95 theses that Martin Luther published at Wittenberg in 1517 against the sale of indulgences. He argued that repentance is a change of the whole life, not a payment or a single act. Dīcendō, 'by saying', is a gerund, and paenitentiam esse is an indirect statement after voluit.",
 "The theses were written in Latin, for debate among scholars, but they were soon translated and printed in German. Luther's protest began the Protestant Reformation.",
 'Martin Luther','Luther, 95 theses','1','1517',WS+'Disputatio_pro_declaratione_virtutis_indulgentiarum','verified','The source spells poenitentiam and adds etc. after agite.',
 'Dominus|dominus|Lord|nom. sg. m.; et|et|and|conj.; magister|magister|master|nom. sg. m.; noster|noster|our|nom. sg. m.; Iēsus|Iēsus|Jesus|nom. sg. m.; Chrīstus|Chrīstus|Christ|nom. sg. m.; dīcendō|dīcō|by saying|gerund abl.; Paenitentiam|paenitentia|repentance|acc. sg. f.; agite|agō|do!|imperative pl.; omnem|omnis|whole|acc. sg. f.; vītam|vīta|life|acc. sg. f.; fidēlium|fidēlis|of believers|gen. pl. m.; paenitentiam|paenitentia|repentance|acc. sg. f.; esse|sum|to be|pres. inf.; voluit|volō|willed, wanted|3rd sg. perf.',
 ['gerund','indirect_statement','imperative'],[],'luther','Ninety-five Theses',WP+'Ninety-five_Theses',register='ecclesiastical')
K('q-pico-adam','quote','early_modern',14,'Nec certam sēdem, nec propriam faciem, nec mūnus ūllum pecūliāre tibi dedimus, ō Adam.','We have given you, Adam, no fixed place, no form of your own, and no special task.',
 "In his Oration on the Dignity of Man of 1486, the young scholar Pico della Mirandola imagines God speaking to the first man. Every other creature has a fixed nature, but humans may choose what to become, sinking to the beasts or rising toward the divine. Ō Adam is a vocative, and dedimus is perfect, 'we have given'.",
 "The speech was written to open a public debate in Rome on 900 theses, which the pope forbade. It is often seen as a manifesto of Renaissance humanism.",
 'Giovanni Pico della Mirandola','Pico, Oratio de hominis dignitate','18','1486',WS+'Oratio_de_hominis_dignitate','verified',None,
 'Nec|nec|neither, not|conj.; certam|certus|fixed|acc. sg. f.; sēdem|sēdēs|seat, place|acc. sg. f.; nec|nec|nor|conj.; propriam|proprius|your own|acc. sg. f.; faciem|faciēs|form, face|acc. sg. f.; nec|nec|nor|conj.; mūnus|mūnus|task, gift|acc. sg. n.; ūllum|ūllus|any|acc. sg. n.; pecūliāre|pecūliāris|special|acc. sg. n.; tibi|tū|to you|dat. sg.; dedimus|dō|we have given|1st pl. perf.; ō|ō|O|interj.; Adam|Adam|Adam|voc. sg. m.',
 ['vocative','perfect_tense','fifth_declension'],[],'pico','Oration on the Dignity of Man',WP+'Oration_on_the_Dignity_of_Man',register='classical')
K('q-vespucci-novum-mundum','quote','early_modern',14,'Quāsque Novum Mundum appellāre licet, quandō apud māiōrēs nostrōs nūlla dē ipsīs fuerit habita cognitiō.','And these lands it is right to call a New World, since among our ancestors there was no knowledge of them.',
 "In the letter printed as Mundus Novus around 1503, Amerigo Vespucci reports his voyage along the coast of South America for the king of Portugal. He argues that these lands are not part of Asia but a world unknown to the ancients. Licet is an impersonal verb, 'it is permitted', with the infinitive appellāre.",
 "In 1507 Martin Waldseemüller printed a world map that named the new continent America after Vespucci. Some historians doubt that Vespucci wrote the letter in this form himself.",
 'Amerigo Vespucci (attrib.)','Vespucci, Mundus Novus','1','about 1503',WS+'Mundus_Novus','verified','Authorship of the printed letter is debated.',
 'Quāsque|quī + -que|and which|acc. pl. f.; Novum|novus|new|acc. sg. m.; Mundum|mundus|world|acc. sg. m.; appellāre|appellō|to call|pres. inf.; licet|licet|it is permitted|3rd sg. pres. (impersonal); quandō|quandō|since|conj.; apud|apud|among|prep. + acc.; māiōrēs|māiōrēs|ancestors|acc. pl. m.; nostrōs|noster|our|acc. pl. m.; nūlla|nūllus|no|nom. sg. f.; dē|dē|about|prep. + abl.; ipsīs|ipse|them|abl. pl. f.; fuerit habita|habeō|there was held|3rd sg. perf. pass. subj.; cognitiō|cognitiō|knowledge|nom. sg. f.',
 ['impersonal_verb','subjunctive','relative_clause'],[],'waldsee','Mundus Novus',WP+'Mundus_Novus')
K('q-kepler-sexangula','quote','early_modern',14,'Nam sī cāsū fit, cūr nōn aequē quīnquangula cadunt, aut septangula, cūr semper sexangula?','For if it happens by chance, why do five-cornered or seven-cornered snowflakes not fall just as often, why always six-cornered ones?',
 "In 1611 the astronomer Johannes Kepler wrote a short New Year's gift for a friend, On the Six-Cornered Snowflake. He asked why snow crystals always have six points, and began the study of how crystals form. Cāsū, 'by chance', is an ablative of manner, and the neuter plurals quīnquangula, septangula and sexangula are adjectives used as nouns, 'five-cornered (shapes)' and so on.",
 "Kepler also guessed that the densest way to stack cannonballs is a pyramid. That guess, the Kepler conjecture, was proved by Thomas Hales only in 1998.",
 'Johannes Kepler','Kepler, Strena seu de nive sexangula','—','1611',LL+'kepler/strena.html','verified',None,
 'Nam|nam|for|conj.; sī|sī|if|conj.; cāsū|cāsus|by chance|abl. sg. m.; fit|fīō|it happens|3rd sg. pres.; cūr|cūr|why|adv.; nōn|nōn|not|adv.; aequē|aequē|equally|adv.; quīnquangula|quīnquangulus|five-cornered ones|nom. pl. n.; cadunt|cadō|fall|3rd pl. pres.; aut|aut|or|conj.; septangula|septangulus|seven-cornered ones|nom. pl. n.; cūr|cūr|why|adv.; semper|semper|always|adv.; sexangula|sexangulus|six-cornered ones|nom. pl. n.',
 ['neuter_plural','present_tense'],[],'kepler','Johannes Kepler',WP+'Johannes_Kepler',register='classical')
K('q-copernicus-mathemata','quote','early_modern',14,'Mathēmata mathēmaticīs scrībuntur.','Mathematics is written for mathematicians.',
 "In the preface to On the Revolutions of 1543, addressed to Pope Paul III, Copernicus defends his idea that the Earth moves around the Sun. He expects ridicule from people who know little of mathematics but quote scripture against him. Scrībuntur is a present passive, and mathēmaticīs is dative, 'for mathematicians'.",
 "Copernicus is said to have received a printed copy of the book on the day he died. Mathēmata is a Greek neuter plural borrowed into Latin.",
 'Nicolaus Copernicus','Copernicus, De revolutionibus, praefatio','preface','1543',WS+'De_revolutionibus_orbium_coelestium/02','verified',None,
 'Mathēmata|mathēma|mathematics, mathematical works|nom. pl. n.; mathēmaticīs|mathēmaticus|for mathematicians|dat. pl. m.; scrībuntur|scrībō|are written|3rd pl. pres. pass.',
 ['passive_voice','dative','neuter_plural'],[],'helio','De revolutionibus orbium coelestium',WP+'De_revolutionibus_orbium_coelestium',register='classical')
K('q-harvey-ex-ovo','quote','early_modern',14,'Ex ōvō omnia.','Everything comes from an egg.',
 "William Harvey, who had already shown that the heart pumps blood around the body, studied how animals develop. The frontispiece of his book On the Generation of Animals of 1651 shows Jupiter opening an egg from which creatures emerge, inscribed EX OVO OMNIA. Harvey argued that all animals, even mammals, begin from an egg, against the old belief that some life arises from mud or decay.",
 "No verb is needed: Latin mottoes often leave out est or sunt. The egg cell of mammals was first seen under a microscope only in 1827.",
 'William Harvey','Harvey, Exercitationes de generatione animalium','frontispiece','1651',WP+'William_Harvey','verified','The words appear on the engraved frontispiece, not as a sentence in Harvey\'s text.',
 'Ex|ex|from, out of|prep. + abl.; ōvō|ōvum|egg|abl. sg. n.; omnia|omnis|all things|nom. pl. n.',
 ['prep_ablative','neuter_plural'],[],'harvey','William Harvey',WP+'William_Harvey',register='classical')
