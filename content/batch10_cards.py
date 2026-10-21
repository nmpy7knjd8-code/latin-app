# Batch 10 card texts, weighted to the thinnest units (XIV, XI, XIII, I, XII, II). Gloss format: "word|lemma|meaning|parse; ..."
# K(id,type,era,unit,latin,translation,context,more,person,work,cit,date,source_url,conf,note,gloss,target,preview,img,lm_label,lm_url, **extra)
LL='https://www.thelatinlibrary.com/'
WP='https://en.wikipedia.org/wiki/'
WS='https://la.wikisource.org/wiki/'
CON='Constructed teaching sentence (not a quotation).'
CARDS=[]
def K(*a,**kw): CARDS.append((a,kw))
def V(id,era,unit,lat,tr,ctx,more,gl,tg,pv,img,lml,lmu):
    K(id,'vocab',era,unit,lat,tr,ctx,more,None,'Constructed','—','—',None,'constructed',CON,gl,tg,pv,img,lml,lmu,subtype='vocab')

# ---------------- UNIT 1 ----------------
V('v-amphora','empire',1,'Amphora magna et plēna est.','The amphora is big and full.',
 "An amphora was a tall clay jar with two handles, used to ship wine, olive oil and fish sauce around the Mediterranean. Its pointed base could be pushed into sand or stacked in a ship's hold. Amphora, magna and plēna are all nominative singular, linked by est.",
 "Monte Testaccio in Rome is a hill made almost entirely of broken oil amphorae. Amphora also served as a unit of volume, about 26 litres.",
 'Amphora|amphora|amphora, two-handled jar|nom. sg. f.; magna|magnus|big|nom. sg. f.; et|et|and|conj.; plēna|plēnus|full|nom. sg. f.; est|sum|is|3rd sg. pres.',
 ['nominative','sum'],[],'amphora','Amphora',WP+'Amphora')
V('v-columna-traiana','empire',1,'Columna Trāiāna alta est.',"Trajan's Column is tall.",
 "The emperor Trajan set up this marble column in his new forum in AD 113. A carved band spirals up it showing his wars against the Dacians, in what is now Romania. Columna and alta are nominative, and est links them.",
 "The column is about 30 metres high without its base, and a staircase winds up inside it. A statue of Saint Peter has stood on top since 1588.",
 'Columna|columna|column|nom. sg. f.; Trāiāna|Trāiānus|of Trajan|nom. sg. f.; alta|altus|tall, high|nom. sg. f.; est|sum|is|3rd sg. pres.',
 ['nominative','sum'],[],'columna',"Trajan's Column",WP+"Trajan's_Column")
V('v-ara-pacis','empire',1,'Āra Pācis pulchra est.','The Altar of Peace is beautiful.',
 "The Senate voted this altar in 13 BC to honour the peace Augustus brought after years of civil war. Its marble walls show the family of Augustus walking in procession. Āra and pulchra are nominative; Pācis, 'of Peace', is a genitive that is simply part of the name.",
 "The altar was dug up in pieces and reassembled in the 1930s. It now stands in a glass museum building beside the Tiber.",
 'Āra|āra|altar|nom. sg. f.; Pācis|pāx|of Peace|gen. sg. f.; pulchra|pulcher|beautiful|nom. sg. f.; est|sum|is|3rd sg. pres.',
 ['nominative','sum'],['genitive'],'arapacis','Ara Pacis',WP+'Ara_Pacis')
V('v-thermae','empire',1,'Thermae magnae et antīquae sunt.','The baths are big and old.',
 "Thermae were huge public bath buildings with hot, warm and cold rooms, exercise yards, gardens and even libraries. The Baths of Caracalla, opened in Rome in the AD 210s, could hold well over a thousand bathers. Thermae is a plural noun, so the adjectives are plural and the verb is sunt.",
 "Entry cost very little, so bathing was a daily habit for many Romans. In summer the ruins are used as a stage for opera.",
 'Thermae|thermae|public baths|nom. pl. f.; magnae|magnus|big|nom. pl. f.; et|et|and|conj.; antīquae|antīquus|old|nom. pl. f.; sunt|sum|are|3rd pl. pres.',
 ['nominative','sum'],[],'thermae','Baths of Caracalla',WP+'Baths_of_Caracalla')
V('v-insula-alta','empire',1,'Īnsula alta sed angusta est.','The apartment block is tall but narrow.',
 "Most people in Rome and Ostia lived in rented flats in blocks called īnsulae, the same word as 'island'. Shops opened onto the street at ground level, and the higher floors were cheaper and more dangerous in a fire. Īnsula, alta and angusta are nominative, linked by est.",
 "Augustus limited the height of such buildings to about 20 metres. Brick blocks at Ostia still stand three storeys high.",
 'Īnsula|īnsula|apartment block|nom. sg. f.; alta|altus|tall|nom. sg. f.; sed|sed|but|conj.; angusta|angustus|narrow|nom. sg. f.; est|sum|is|3rd sg. pres.',
 ['nominative','sum'],[],'insula','Insula (building)',WP+'Insula_(building)')
V('v-speculum','empire',1,'Speculum rotundum et lūcidum est.','The mirror is round and bright.',
 "Roman mirrors were not glass but polished bronze or silver, so they had to be cleaned often to keep their shine. Rich women had slaves to hold the mirror while their hair was done. Speculum is a neuter noun, so its adjectives end in -um too.",
 "English speculate comes from the same root, specere, 'to look'. Glass mirrors backed with metal were rare until the Middle Ages.",
 'Speculum|speculum|mirror|nom. sg. n.; rotundum|rotundus|round|nom. sg. n.; et|et|and|conj.; lūcidum|lūcidus|bright, shining|nom. sg. n.; est|sum|is|3rd sg. pres.',
 ['nominative','sum'],[],'speculum','Mirror',WP+'Mirror')

# ---------------- UNIT 2 ----------------
V('v-puella-pupam','empire',2,'Puella pūpam amat.','The girl loves her doll.',
 "Roman girls played with dolls of rag, clay, bone or ivory, some with jointed arms and legs. Before her wedding a girl dedicated her dolls to the gods as a sign that childhood was over. Pūpam is the accusative object of amat.",
 "A jointed ivory doll was buried with a young woman named Crepereia Tryphaena in Rome. Pūpa, 'doll' or 'little girl', gives English pupil and puppet.",
 'Puella|puella|girl|nom. sg. f.; pūpam|pūpa|doll|acc. sg. f.; amat|amō|loves|3rd sg. pres.',
 ['accusative','nominative'],['present_tense'],'pupa','Doll',WP+'Doll')
V('v-coquus-cibum','empire',2,'Coquus cēnam parat.','The cook prepares dinner.',
 "In a wealthy Roman house the cook was usually a slave, and a skilled one could cost a fortune. Dinner, cēna, was the main meal of the day, eaten in the late afternoon. Cēnam is the accusative object of parat.",
 "A bronze pot like this caccabus sat on a tripod over a charcoal fire. The only Roman cookbook that survives goes under the name of Apicius.",
 'Coquus|coquus|cook|nom. sg. m.; cēnam|cēna|dinner|acc. sg. f.; parat|parō|prepares|3rd sg. pres.',
 ['accusative','nominative'],['present_tense'],'caccabus','Apicius',WP+'Apicius')
V('v-mercator-nummos','empire',2,'Mercātor dēnāriōs numerat.','The merchant counts the denarii.',
 "The dēnārius was Rome's main silver coin for over four hundred years. People without banks often buried their savings in a pot, and hoards like this one are still being dug up. Dēnāriōs is the accusative plural object of numerat.",
 "A legionary of the early empire earned about 225 denarii a year. The letter d in the old British abbreviation £sd stood for denarius.",
 'Mercātor|mercātor|merchant|nom. sg. m.; dēnāriōs|dēnārius|denarii (silver coins)|acc. pl. m.; numerat|numerō|counts|3rd sg. pres.',
 ['accusative','nominative'],['present_tense'],'nummi','Denarius',WP+'Denarius')
V('v-medicus-aegrotum','empire',2,'Medicus aegrōtum cūrat.','The doctor treats the sick man.',
 "Many doctors in Rome were Greeks, and some had begun as slaves. They used bronze probes, scalpels and spatulas like these, found at Pompeii. Aegrōtum, 'the sick man', is the accusative object of cūrat.",
 "The House of the Surgeon at Pompeii was named after the instruments found in it. Galen, the most famous doctor of the empire, was a Greek from Pergamum.",
 'Medicus|medicus|doctor|nom. sg. m.; aegrōtum|aegrōtus|sick man|acc. sg. m.; cūrat|cūrō|treats, cares for|3rd sg. pres.',
 ['accusative','nominative'],['present_tense'],'medicus','Medicine in ancient Rome',WP+'Medicine_in_ancient_Rome')
V('v-pistor-panem','empire',2,'Pistor pānem coquit.','The baker bakes bread.',
 "Pompeii had more than thirty bakeries. Donkeys turned the hourglass-shaped stone mills to grind grain, and the bread was baked in a domed oven. Pānem is the accusative object of coquit.",
 "Carbonised loaves were found at Pompeii, round and divided into eight sections. The baker's word pistor first meant 'pounder', from grinding grain by hand.",
 'Pistor|pistor|baker|nom. sg. m.; pānem|pānis|bread|acc. sg. m.; coquit|coquō|cooks, bakes|3rd sg. pres.',
 ['accusative','nominative'],['present_tense'],'pistrinum','Ancient Roman cuisine',WP+'Ancient_Roman_cuisine')
V('v-fullo-togam','empire',2,'Fullō togam lavat.','The fuller washes the toga.',
 "A fullō cleaned and finished woollen cloth, treading it in tubs of water mixed with urine, which worked like ammonia. The fullery of Stephanus at Pompeii still has its rinsing basins. Togam is the accusative object of lavat.",
 "The emperor Vespasian taxed the urine collected from public toilets for fullers. Fullers' guilds were powerful in Roman towns.",
 'Fullō|fullō|fuller, laundryman|nom. sg. m.; togam|toga|toga|acc. sg. f.; lavat|lavō|washes|3rd sg. pres.',
 ['accusative','nominative'],['present_tense'],'fullonica','Fulling',WP+'Fulling')

# ---------------- UNIT 11: Scholae ----------------
K('q-fulbert-chorus','quote','high_medieval',11,'Chorus novae Ierūsalem novam melī dulcēdinem prōmat.','Let the choir of the new Jerusalem bring forth a new sweetness of song.',
 "Fulbert, bishop of Chartres, wrote this Easter hymn in the early 11th century, when his cathedral school was one of the best in Europe. Prōmat, 'let it bring forth', is a jussive subjunctive. Melī is the genitive of melos, a Greek word for 'song'.",
 "Fulbert rebuilt Chartres Cathedral after a fire in 1020, though the church standing today is later. The English hymn Ye choirs of new Jerusalem is a translation of this one.",
 'Fulbert of Chartres','Chorus novae Ierusalem (hymn)','stanza 1','early 11th century',LL+'hymni.html','verified','The source spells dulcidinem; here classical dulcēdinem.',
 'Chorus|chorus|choir|nom. sg. m.; novae|novus|new|gen. sg. f.; Ierūsalem|Ierūsalem|of Jerusalem|gen. (indecl.); novam|novus|new|acc. sg. f.; melī|melos|of song|gen. sg. n.; dulcēdinem|dulcēdō|sweetness|acc. sg. f.; prōmat|prōmō|let it bring forth|3rd sg. pres. subj.',
 ['jussive_subjunctive','genitive'],[],'chartres','Fulbert of Chartres',WP+'Fulbert_of_Chartres',register='ecclesiastical')
K('q-bernard-cluny-hora','quote','high_medieval',11,'Hōra novissima, tempora pessima sunt — vigilēmus.','It is the last hour, the times are very bad — let us keep watch.',
 "Bernard of Cluny opens his long poem On Contempt for the World, written around 1140, with this warning that the end is near. Novissima and pessima are superlatives, 'last' and 'worst'. Vigilēmus, 'let us keep watch', is a hortatory subjunctive.",
 "The poem uses a difficult metre with rhymes inside every line. Umberto Eco took the last line of the same poem for the end of The Name of the Rose.",
 'Bernard of Cluny','Bernard of Cluny, De contemptu mundi','1.1','about 1140',LL+'bernardcluny1.html','verified',None,
 'Hōra|hōra|hour|nom. sg. f.; novissima|novus|last|superl. nom. sg. f.; tempora|tempus|times|nom. pl. n.; pessima|malus|worst, very bad|superl. nom. pl. n.; sunt|sum|are|3rd pl. pres.; vigilēmus|vigilō|let us keep watch|1st pl. pres. subj.',
 ['superlative','hortatory_subjunctive'],[],'bernardcluny','Bernard of Cluny',WP+'Bernard_of_Cluny',register='ecclesiastical',related=['q-bernard-stat-roma'])
K('q-anselm-doce','quote','high_medieval',11,'Docē mē quaerere tē et ostende tē quaerentī; quia nec quaerere tē possum, nisi tū doceās, nec invenīre, nisi tē ostendās.','Teach me to seek you, and show yourself to me as I seek; for I cannot seek you unless you teach me, nor find you unless you show yourself.',
 "In the first chapter of his Proslogion, Anselm prays before he begins to argue, asking God to help him search. Docē and ostende are imperatives. Doceās and ostendās are present subjunctives in the nisi clauses, the 'should … would' kind of condition: 'unless you should teach me'.",
 "Anselm wrote the Proslogion at the abbey of Bec in Normandy around 1077 to 1078, just before he became its abbot. Later in the work he gives his famous definition of God as that than which nothing greater can be thought.",
 'Anselm of Canterbury','Anselm, Proslogion','1','about 1078',LL+'anselmproslogion.html','verified',None,
 'Docē|doceō|teach|imperative sg.; mē|ego|me|acc. sg.; quaerere|quaerō|to seek|pres. inf.; tē|tū|you|acc. sg.; et|et|and|conj.; ostende|ostendō|show|imperative sg.; tē|tū|yourself|acc. sg.; quaerentī|quaerō|to (me) seeking|pres. part. dat. sg.; quia|quia|because|conj.; nec|nec|neither|conj.; quaerere|quaerō|to seek|pres. inf.; tē|tū|you|acc. sg.; possum|possum|I can|1st sg. pres.; nisi|nisi|unless|conj.; tū|tū|you|nom. sg.; doceās|doceō|you teach|2nd sg. pres. subj.; nec|nec|nor|conj.; invenīre|inveniō|to find|pres. inf.; nisi|nisi|unless|conj.; tē|tū|yourself|acc. sg.; ostendās|ostendō|you show|2nd sg. pres. subj.',
 ['subjunctive','imperative','possum_infinitive'],[],'anselmmathilde','Proslogion',WP+'Proslogion',register='ecclesiastical',related=['q-anselm-maius'])
K('q-aquinas-prima-via','quote','high_medieval',11,'Prīma autem et manifestior via est, quae sūmitur ex parte mōtūs.','The first and more obvious way is the one taken from motion.',
 "After saying that God's existence can be proved in five ways, Aquinas begins with the argument from change. Whatever moves is moved by something else, and the chain cannot go back forever, so there must be a first unmoved mover. Manifestior, 'more obvious', is a comparative.",
 "The argument comes from Aristotle's Physics and Metaphysics. Aquinas wrote this part of the Summa in Rome around 1266 to 1268.",
 'Thomas Aquinas','Aquinas, Summa theologiae','I, q. 2, a. 3, co.','about 1266-1268','https://www.corpusthomisticum.org/sth1002.html','verified',None,
 'Prīma|prīmus|first|nom. sg. f.; autem|autem|and, now|conj.; et|et|and|conj.; manifestior|manifestus|more obvious|comp. nom. sg. f.; via|via|way|nom. sg. f.; est|sum|is|3rd sg. pres.; quae|quī|which|nom. sg. f.; sūmitur|sūmō|is taken|3rd sg. pres. pass.; ex|ex|from|prep. + abl.; parte|pars|side, part|abl. sg. f.; mōtūs|mōtus|of motion|gen. sg. m.',
 ['comparative','relative_clause','passive_voice'],[],'zurbaran','Unmoved mover',WP+'Unmoved_mover',register='medieval',related=['q-aquinas-quinque'])
K('q-dies-irae-quaerens','quote','high_medieval',11,'Quaerēns mē sēdistī lassus, redēmistī crucem passus; tantus labor nōn sit cassus.','Seeking me you sat down weary, you redeemed me by suffering the cross; let not such great labour be in vain.',
 "In this stanza of the Dies īrae the sinner reminds Christ of what he suffered to save him. Sit is a jussive subjunctive, and nōn sit means 'let it not be'. Passus is the perfect participle of the deponent verb patior, 'having suffered'.",
 "The first line recalls Jesus sitting tired at the well in John's Gospel. Mozart's Requiem sets this stanza in its Recordare.",
 'attrib. Thomas of Celano','Dies irae','stanza 10','13th century',LL+'hymni.html','verified','Authorship is uncertain; the poem is traditionally credited to Thomas of Celano.',
 'Quaerēns|quaerō|seeking|pres. part. nom. sg. m.; mē|ego|me|acc. sg.; sēdistī|sedeō|you sat|2nd sg. perf.; lassus|lassus|weary|nom. sg. m.; redēmistī|redimō|you redeemed|2nd sg. perf.; crucem|crux|cross|acc. sg. f.; passus|patior|having suffered|perf. part. nom. sg. m. (deponent); tantus|tantus|so great|nom. sg. m.; labor|labor|labour|nom. sg. m.; nōn|nōn|not|adv.; sit|sum|let it be|3rd sg. pres. subj.; cassus|cassus|empty, in vain|nom. sg. m.',
 ['jussive_subjunctive','present_participle','perfect_tense'],['deponent'],'crucifixion','Dies irae',WP+'Dies_irae',register='ecclesiastical',related=['q-dies-irae-quid-sum'])
K('q-angelus-conciperem','quote','late_medieval',11,'Quōmodo conciperem quae virum nōn cognōvī?','How could I conceive, I who have not known a man?',
 "In the carol Angelus ad virginem, Mary answers the angel Gabriel with this question, following Luke's Gospel. Conciperem is an imperfect subjunctive in a question about what could happen, 'how could I conceive?'. Quae, 'I who', is a relative pronoun whose antecedent is the speaker herself.",
 "The carol survives in a 14th-century manuscript from Dublin. Chaucer's Miller's Tale has the student Nicholas sing Angelus ad virginem to his harp.",
 'Anonymous','Angelus ad virginem (carol)','stanza 2','about 1360 (Dublin Troper)',LL+'hymni.html','verified',None,
 'Quōmodo|quōmodo|how|adv.; conciperem|concipiō|could I conceive|1st sg. impf. subj.; quae|quī|(I) who|nom. sg. f.; virum|vir|man|acc. sg. m.; nōn|nōn|not|adv.; cognōvī|cognōscō|I have known|1st sg. perf.',
 ['subjunctive','relative_clause'],[],'annunciation','Angelus ad virginem',WP+'Angelus_ad_virginem',register='ecclesiastical')
K('q-adeste-cantet','quote','early_modern',11,'Cantet nunc īō chorus angelōrum; cantet nunc aula caelestium.','Let the choir of angels now sing “io”; let the court of heaven now sing.',
 "Adeste fidēlēs was written in the 1740s, probably by John Francis Wade, an English Catholic who copied music for a living in France. Cantet, 'let it sing', is a jussive subjunctive, used twice. Īō is a Latin cry of joy.",
 "The English translation, O come, all ye faithful, dates from 1841. Caelestium is a genitive plural, 'of the heavenly ones'.",
 'John Francis Wade (attrib.)','Adeste fideles','stanza 3','1740s',LL+'hymni.html','verified',None,
 'Cantet|cantō|let it sing|3rd sg. pres. subj.; nunc|nunc|now|adv.; īō|īō|io! (cry of joy)|interj.; chorus|chorus|choir|nom. sg. m.; angelōrum|angelus|of angels|gen. pl. m.; cantet|cantō|let it sing|3rd sg. pres. subj.; nunc|nunc|now|adv.; aula|aula|court, hall|nom. sg. f.; caelestium|caelestis|of the heavenly ones|gen. pl. m.',
 ['jussive_subjunctive','genitive'],[],'adeste','O Come, All Ye Faithful',WP+'O_Come,_All_Ye_Faithful',register='ecclesiastical')
K('q-theodulf-gloria','quote','early_medieval',11,'Glōria, laus et honor tibi sit, rēx Chrīste redēmptor.','Glory, praise and honour be to you, Christ the king, redeemer.',
 "Theodulf, bishop of Orléans and a scholar at Charlemagne's court, wrote this Palm Sunday hymn in the early 9th century. Sit is a jussive subjunctive, 'let there be', and rēx Chrīste redēmptor is vocative. The hymn was sung in procession as the people carried palms into church.",
 "A story says Theodulf sang it from his prison window and won his release, but that legend is late. Its English version is All glory, laud and honour.",
 'Theodulf of Orléans','Gloria, laus et honor (hymn)','line 1','early 9th century',LL+'hymni.html','verified',None,
 'Glōria|glōria|glory|nom. sg. f.; laus|laus|praise|nom. sg. f.; et|et|and|conj.; honor|honor|honour|nom. sg. m.; tibi|tū|to you|dat. sg.; sit|sum|let (it) be|3rd sg. pres. subj.; rēx|rēx|king|voc. sg. m.; Chrīste|Chrīstus|Christ|voc. sg. m.; redēmptor|redēmptor|redeemer|voc. sg. m.',
 ['jussive_subjunctive','vocative','dative'],[],'aethelwold','All Glory, Laud and Honour',WP+'All_Glory,_Laud_and_Honour',register='ecclesiastical')
K('q-cb-veris-curramus','quote','high_medieval',11,'Zephyrus nectareō spīrāns in odōre, certātim prō brāviō currāmus in amōre.','With Zephyr breathing in nectar-sweet fragrance, let us race one another for the prize in love.',
 "Vēris laeta faciēs, 'the happy face of spring', is a song from the Carmina Burana that greets the warm west wind, Zephyrus. Currāmus, 'let us race', is a hortatory subjunctive. Brāvium is a medieval word for a race prize, borrowed from Greek.",
 "Carl Orff set this song in the spring section of his Carmina Burana. The manuscript was copied in the 13th century, probably in the Tyrol.",
 'Carmina Burana (anonymous)','Carmina Burana','138','13th century',WS+'Carmina_Burana_(Orff)/Veris_leta_facies','verified',None,
 'Zephyrus|Zephyrus|Zephyr, the west wind|nom. sg. m.; nectareō|nectareus|nectar-sweet|abl. sg. m.; spīrāns|spīrō|breathing|pres. part. nom. sg. m.; in|in|in|prep. + abl.; odōre|odor|fragrance|abl. sg. m.; certātim|certātim|in rivalry|adv.; prō|prō|for|prep. + abl.; brāviō|brāvium|prize|abl. sg. n.; currāmus|currō|let us run|1st pl. pres. subj.; in|in|in|prep. + abl.; amōre|amor|love|abl. sg. m.',
 ['hortatory_subjunctive','present_participle'],[],'manesse1','Carmina Burana',WP+'Carmina_Burana',related=['q-cb-ecce-gratum'])
K('q-cb-in-trutina','quote','high_medieval',11,'Sed ēligō quod videō, collum iugō praebeō.','But I choose what I see; I offer my neck to the yoke.',
 "In trutinā, 'in the balance', is a love song from the Carmina Burana in which a girl weighs desire against modesty. In the end she chooses love and accepts its yoke. Quod videō is a relative clause, 'what I see', and iugō is dative after praebeō.",
 "Orff gave this song to the soprano in his Carmina Burana, where it is one of the quietest moments. The yoke was a common image for love and marriage.",
 'Carmina Burana (anonymous)','Carmina Burana','70','13th century',WS+'Carmina_Burana_(Orff)/In_trutina','verified',None,
 'Sed|sed|but|conj.; ēligō|ēligō|I choose|1st sg. pres.; quod|quī|what|acc. sg. n.; videō|videō|I see|1st sg. pres.; collum|collum|neck|acc. sg. n.; iugō|iugum|to the yoke|dat. sg. n.; praebeō|praebeō|I offer|1st sg. pres.',
 ['relative_clause','dative'],[],'manesse2','Carmina Burana',WP+'Carmina_Burana')

# ---------------- UNIT 12: Regna ----------------
K('q-einhard-equitando','quote','early_medieval',12,'Exercēbātur assiduē equitandō ac vēnandō; quod illī gentīlicium erat.','He exercised constantly by riding and hunting, which was a family custom for him.',
 "Einhard describes Charlemagne's habits: riding and hunting, and swimming in the hot springs at Aachen. Equitandō and vēnandō are gerunds in the ablative, 'by riding and hunting'. Exercēbātur is an imperfect passive used in a reflexive sense, 'he trained himself'.",
 "Einhard adds that hardly any people on earth could match the Franks at it. Charlemagne built his palace at Aachen partly for its hot springs.",
 'Einhard','Einhard, Vita Karoli Magni','22','about 825',LL+'ein.html','verified','The sentence continues quia vix ulla in terris natio invenitur, quae in hac arte Francis possit aequari.',
 'Exercēbātur|exerceō|he exercised (himself)|3rd sg. impf. pass.; assiduē|assiduē|constantly|adv.; equitandō|equitō|by riding|gerund abl.; ac|ac|and|conj.; vēnandō|vēnor|by hunting|gerund abl. (deponent); quod|quī|which|nom. sg. n.; illī|ille|for him|dat. sg. m.; gentīlicium|gentīlicius|a family custom|nom. sg. n.; erat|sum|was|3rd sg. impf.',
 ['gerund','passive_voice','imperfect'],[],'statuette','Charlemagne',WP+'Charlemagne',register='medieval',related=['q-einhard-caenandum'])
K('q-einhard-discenda','quote','early_medieval',12,'In discendā grammaticā Petrum Pīsānum diāconem senem audīvit.','In learning grammar he listened to Peter of Pisa, an elderly deacon.',
 "Einhard says Charlemagne took lessons as an adult: grammar from Peter of Pisa, and the other arts from Alcuin of York. In discendā grammaticā uses a gerundive, literally 'in grammar to be learned', where English says 'in learning grammar'. The gerundive agrees with grammaticā.",
 "Alcuin taught Charlemagne rhetoric, logic and astronomy. Scholars at his court helped spread the clear handwriting called Carolingian minuscule.",
 'Einhard','Einhard, Vita Karoli Magni','25','about 825',LL+'ein.html','verified',None,
 'In|in|in|prep. + abl.; discendā|discō|(to be) learned|gerundive abl. sg. f.; grammaticā|grammatica|grammar|abl. sg. f.; Petrum|Petrus|Peter|acc. sg. m.; Pīsānum|Pīsānus|of Pisa|acc. sg. m.; diāconem|diāconus|deacon|acc. sg. m.; senem|senex|old|acc. sg. m.; audīvit|audiō|he listened to|3rd sg. perf.',
 ['gerundive','prep_ablative','perfect_tense'],[],'marville','Carolingian Renaissance',WP+'Carolingian_Renaissance',register='medieval',related=['q-einhard-equitando'])
K('q-kempis-moriendum','quote','late_medieval',12,'Beātus quī hōram mortis suae semper ante oculōs habet, et ad moriendum cotīdiē sē dispōnit.','Blessed is he who always keeps the hour of his death before his eyes and prepares himself daily for dying.',
 "Thomas à Kempis gives this advice in the chapter of the Imitation of Christ on thinking about death. Ad moriendum, 'for dying', uses the gerund after ad to show purpose. Est is understood with beātus.",
 "Moriendum comes from the deponent verb morior, 'to die'. The book became one of the most widely read Christian texts after the Bible.",
 'Thomas à Kempis','Thomas à Kempis, De imitatione Christi','1.23.2','about 1420',LL+'kempis/kempis1.shtml','verified','The source spells quotidie; here cotīdiē.',
 'Beātus|beātus|blessed|nom. sg. m.; quī|quī|who|nom. sg. m.; hōram|hōra|hour|acc. sg. f.; mortis|mors|of death|gen. sg. f.; suae|suus|his own|gen. sg. f.; semper|semper|always|adv.; ante|ante|before|prep. + acc.; oculōs|oculus|eyes|acc. pl. m.; habet|habeō|has, keeps|3rd sg. pres.; et|et|and|conj.; ad|ad|for|prep. + acc.; moriendum|morior|dying|gerund acc. (deponent); cotīdiē|cotīdiē|daily|adv.; sē|suī|himself|acc.; dispōnit|dispōnō|prepares|3rd sg. pres.',
 ['gerund','deponent','relative_clause'],[],'kempis','The Imitation of Christ',WP+'The_Imitation_of_Christ',register='ecclesiastical',related=['q-kempis-utinam'])
K('q-magna-carta-ecclesia','quote','high_medieval',12,'… quod Anglicāna ecclēsia lībera sit, et habeat iūra sua integra, et lībertātēs suās illaesās.','… that the English Church shall be free, and shall have its rights whole and its liberties unharmed.',
 "This is the first promise of Magna Carta: King John grants that the Church in England shall be free, above all to elect its own bishops. Sit and habeat are subjunctives in a clause after concessisse, expressing what is granted. The clause was meant to settle John's long quarrel with the pope.",
 "The 1225 reissue under Henry III became the version that entered English law. Clause 1 is one of the three clauses still in force.",
 'King John and the barons','Magna Carta','1','1215',LL+'magnacarta.html','verified','The manuscript spells jura and illesas.',
 'quod|quod|that|conj.; Anglicāna|Anglicānus|English|nom. sg. f.; ecclēsia|ecclēsia|church|nom. sg. f.; lībera|līber|free|nom. sg. f.; sit|sum|shall be|3rd sg. pres. subj.; et|et|and|conj.; habeat|habeō|shall have|3rd sg. pres. subj.; iūra|iūs|rights|acc. pl. n.; sua|suus|its own|acc. pl. n.; integra|integer|whole|acc. pl. n.; et|et|and|conj.; lībertātēs|lībertās|liberties|acc. pl. f.; suās|suus|its own|acc. pl. f.; illaesās|illaesus|unharmed|acc. pl. f.',
 ['subjunctive','neuter_plural'],[],'mc1225','Magna Carta',WP+'Magna_Carta',register='medieval-legal',related=['q-magna-carta-nulli'])
K('q-asser-loquebatur','quote','early_medieval',12,'… eō quod, ut loquēbātur, illō tempore lēctōrēs bonī in tōtō rēgnō Occidentālium Saxonum nōn erant.','… because, as he used to say, at that time there were no good teachers in the whole kingdom of the West Saxons.',
 "Asser explains why King Alfred learned to read so late: as a boy he longed for learning, but there were no good teachers in Wessex. Loquēbātur, 'he used to say', is an imperfect of the deponent verb loquor. Lēctōrēs here means teachers who read texts aloud with pupils.",
 "Alfred later invited scholars from Mercia, Wales and the Continent, among them Asser himself. He complained that by his time few priests south of the Humber could understand their Latin services.",
 'Asser','Asser, Vita Alfredi','24','893',LL+'asserius.html','verified','The sentence begins Sed, proh dolor! quod maxime desiderabat, liberalem scilicet artem, desiderio suo non suppetebat.',
 'eō|is|for this reason|abl. sg. n.; quod|quod|that, because|conj.; ut|ut|as|conj.; loquēbātur|loquor|he used to say|3rd sg. impf. (deponent); illō|ille|that|abl. sg. n.; tempore|tempus|time|abl. sg. n.; lēctōrēs|lēctor|readers, teachers|nom. pl. m.; bonī|bonus|good|nom. pl. m.; in|in|in|prep. + abl.; tōtō|tōtus|whole|abl. sg. n.; rēgnō|rēgnum|kingdom|abl. sg. n.; Occidentālium|occidentālis|western|gen. pl. m.; Saxonum|Saxō|of the Saxons|gen. pl. m.; nōn|nōn|not|adv.; erant|sum|were|3rd pl. impf.',
 ['deponent','imperfect','genitive'],[],'alfredstatue','Alfred the Great',WP+'Alfred_the_Great',register='medieval',related=['q-asser-candelas'])
K('q-oresme-subtilis','quote','late_medieval',12,'… haec autem impressiō dēbet esse subtīlis, et ad effigiendum seu contrafaciendum difficilis.','… but this stamp ought to be fine, and hard to copy or forge.',
 "Oresme argues that the ruler, as the most public person, should have the coins made and stamped with a detailed design. A fine design protects the community against forgers. Ad effigiendum and contrafaciendum are gerunds after ad, 'for copying or forging', with difficilis.",
 "Contrafaciō, 'to make against', is a medieval coinage that gives English counterfeit. Oresme also wrote on mathematics, physics and astronomy.",
 'Nicole Oresme','Oresme, De moneta','5','about 1356',LL+'oresmius.html','verified','Verbatim: ad effigiendum (for classical-style effigiandum, from medieval effigiāre).',
 'haec|hic|this|nom. sg. f.; autem|autem|but|conj.; impressiō|impressiō|stamp, impression|nom. sg. f.; dēbet|dēbeō|ought|3rd sg. pres.; esse|sum|to be|pres. inf.; subtīlis|subtīlis|fine, delicate|nom. sg. f.; et|et|and|conj.; ad|ad|for|prep. + acc.; effigiendum|effigiō (medieval effigiāre)|copying|gerund acc. (= effigiandum); seu|seu|or|conj.; contrafaciendum|contrafaciō|forging|gerund acc.; difficilis|difficilis|difficult|nom. sg. f.',
 ['gerund','infinitive'],[],'oresmespheres','Nicole Oresme',WP+'Nicole_Oresme',register='medieval',related=['q-oresme-quamvis'])
K('q-petrarch-carpsi','quote','late_medieval',12,'Vītam ego tuam carpsī, nōn ingenium aut linguam, ut quī illud mīrer, hanc stupeam.','It was your life I criticised, not your genius or your tongue, since I admire the one and am amazed by the other.',
 "In his second letter to Cicero, Petrarch makes clear that he faulted only Cicero's conduct in politics. Ut quī with the subjunctive gives a reason, 'as one who admires'. Mīrer comes from the deponent verb mīror, 'to admire'.",
 "Petrarch spent his last years in a house at Arquà in the hills near Padua. He died there in 1374, according to legend with his head on a book.",
 'Petrarch','Petrarch, Epistolae familiares','24.4','1345',LL+'petrarch.ep1.html','verified',None,
 'Vītam|vīta|life|acc. sg. f.; ego|ego|I|nom. sg.; tuam|tuus|your|acc. sg. f.; carpsī|carpō|I criticised|1st sg. perf.; nōn|nōn|not|adv.; ingenium|ingenium|genius, talent|acc. sg. n.; aut|aut|or|conj.; linguam|lingua|tongue, eloquence|acc. sg. f.; ut|ut|as|conj.; quī|quī|one who|nom. sg. m.; illud|ille|the former|acc. sg. n.; mīrer|mīror|I admire|1st sg. pres. subj. (deponent); hanc|hic|the latter|acc. sg. f.; stupeam|stupeō|I am amazed at|1st sg. pres. subj.',
 ['deponent','subjunctive','demonstratives'],[],'arqua','Petrarch',WP+'Petrarch',register='medieval',related=['q-petrarch-vixisti'])

# ---------------- UNIT 13: Ius ----------------
K('q-xii-legassit','quote','republic',13,'Utī lēgāssit super pecūniā tūtēlāve suae reī, ita iūs estō.','As a man has bequeathed concerning his money or the guardianship of his property, so shall the law be.',
 "This law of the Twelve Tables gave a Roman citizen the right to decide by will who would inherit his property. Estō is the future imperative of sum, 'it shall be'. Lēgāssit is an old future-perfect form of lēgō, 'to bequeath'.",
 "Roman wills were often read aloud and could be long and detailed. English legacy comes from the same verb lēgāre.",
 'Twelve Tables','Lex XII Tabularum','5.3','about 450 BC',LL+'12tables.html','verified','Preserved in later quotations, for example by Ulpian.',
 'Utī|utī|as|conj.; lēgāssit|lēgō|has bequeathed|3rd sg. fut. perf. (archaic); super|super|concerning|prep. + abl.; pecūniā|pecūnia|money|abl. sg. f.; tūtēlāve|tūtēla + -ve|or guardianship|abl. sg. f.; suae|suus|his own|gen. sg. f.; reī|rēs|of property|gen. sg. f.; ita|ita|so|adv.; iūs|iūs|law, right|nom. sg. n.; estō|sum|shall be|fut. imperative 3rd sg.',
 ['future_imperative','fifth_declension'],[],'institutiones','Twelve Tables',WP+'Twelve_Tables',related=['q-xii-venum'])
K('q-xii-calvitur','quote','republic',13,'Sī calvitur pedemve struit, manum endō iacitō.','If he tries to evade or runs off, the plaintiff shall lay hands on him.',
 "The first of the Twelve Tables deals with summoning someone to court. If the person summoned stalls or tries to slip away, the plaintiff may seize him. Iacitō is a future imperative, and endō is an old form of in.",
 "Roman trials began with the plaintiff bringing the defendant before the magistrate himself; there were no police to do it. Pedem struere, 'to arrange the foot', probably means to make ready to run.",
 'Twelve Tables','Lex XII Tabularum','1.2','about 450 BC',LL+'12tables.html','verified',None,
 'Sī|sī|if|conj.; calvitur|calvor|he tries to evade|3rd sg. pres. (deponent); pedemve|pēs + -ve|or the foot|acc. sg. m.; struit|struō|arranges, readies|3rd sg. pres.; manum|manus|hand|acc. sg. f.; endō|in|on|prep. (archaic); iacitō|iaciō|shall throw, lay|fut. imperative 3rd sg.',
 ['future_imperative','deponent'],[],'anaglypha','Twelve Tables',WP+'Twelve_Tables',related=['q-xii-in-ius'])
K('q-cicero-lex-loquens','quote','republic',13,'Vērēque dīcī potest, magistrātum esse lēgem loquentem, lēgem autem mūtum magistrātum.','It can truly be said that a magistrate is a speaking law, and a law a silent magistrate.',
 "In On the Laws, Cicero explains that magistrates rule the people just as the laws rule the magistrates. The officer gives voice to the law, and the law is an officer who cannot speak. Magistrātum esse is an indirect statement after dīcī potest.",
 "Medieval and modern writers on kingship often quoted this pair of phrases. Lēx loquēns became a stock title for a just ruler.",
 'Cicero','Cicero, De legibus','3.2','about 52 BC',LL+'cicero/leg3.shtml','verified',None,
 'Vērēque|vērē + -que|and truly|adv.; dīcī|dīcō|to be said|pres. pass. inf.; potest|possum|it can|3rd sg. pres.; magistrātum|magistrātus|magistrate|acc. sg. m.; esse|sum|to be|pres. inf.; lēgem|lēx|law|acc. sg. f.; loquentem|loquor|speaking|pres. part. acc. sg. f. (deponent); lēgem|lēx|law|acc. sg. f.; autem|autem|and, but|conj.; mūtum|mūtus|silent|acc. sg. m.; magistrātum|magistrātus|magistrate|acc. sg. m.',
 ['indirect_statement','passive_voice','present_participle'],['deponent'],'despuig','De Legibus',WP+'De_Legibus',register='classical',related=['q-cicero-sunto'])
K('q-cicero-paruerit','quote','republic',13,'Nam et quī bene imperat, pāruerit aliquandō necesse est.','For the man who commands well must at some time have obeyed.',
 "Cicero argues in On the Laws that a state needs rules for how citizens obey as well as how officials command. Good leaders learn by first serving under others. Necesse est is an impersonal expression, and pāruerit is a perfect subjunctive depending on it.",
 "Cicero adds that whoever obeys modestly seems worthy to command one day. Roman officials served one-year terms and then went back to being private citizens.",
 'Cicero','Cicero, De legibus','3.5','about 52 BC',LL+'cicero/leg3.shtml','verified',None,
 'Nam|nam|for|conj.; et|et|also, even|adv.; quī|quī|(he) who|nom. sg. m.; bene|bene|well|adv.; imperat|imperō|commands|3rd sg. pres.; pāruerit|pāreō|has obeyed|3rd sg. perf. subj.; aliquandō|aliquandō|at some time|adv.; necesse|necesse|necessary|indecl. adj.; est|sum|it is|3rd sg. pres. (impersonal)',
 ['impersonal_verb','subjunctive','relative_clause'],[],'sailkocicero','De Legibus',WP+'De_Legibus',register='classical',related=['q-cicero-lex-loquens'])
K('q-dig-definitio','quote','empire',13,'Omnis dēfīnītiō in iūre cīvīlī perīculōsa est: parum est enim, ut nōn subvertī posset.','Every definition in civil law is dangerous: for there is little that could not be overturned.',
 "The jurist Javolenus, writing around AD 100, warned against rigid definitions in law, because real cases always find exceptions. Justinian's lawyers placed his remark among the general rules at the end of the Digest. Subvertī is a present passive infinitive, 'to be overturned'.",
 "Lawyers still quote the first half of the sentence. Javolenus was head of one of the two Roman law schools, the Sabinians.",
 'Javolenus (Digest)','Digesta Iustiniani','50.17.202','about AD 100 (Digest 533)',LL+'justinian/digest50.shtml','verified',None,
 'Omnis|omnis|every|nom. sg. f.; dēfīnītiō|dēfīnītiō|definition|nom. sg. f.; in|in|in|prep. + abl.; iūre|iūs|law|abl. sg. n.; cīvīlī|cīvīlis|civil|abl. sg. n.; perīculōsa|perīculōsus|dangerous|nom. sg. f.; est|sum|is|3rd sg. pres.; parum|parum|little, too little|adv.; est|sum|it is|3rd sg. pres.; enim|enim|for|conj.; ut|ut|that|conj.; nōn|nōn|not|adv.; subvertī|subvertō|to be overturned|pres. pass. inf.; posset|possum|could|3rd sg. impf. subj.',
 ['subjunctive','passive_voice','third_declension'],[],'ulpianbeic','Digest (Roman law)',WP+'Digest_(Roman_law)',related=['q-dig-licet'])
K('q-dig-locupletiorem','quote','empire',13,'Iūre nātūrae aequum est nēminem cum alterius dētrīmentō et iniūriā fierī locuplētiōrem.','By the law of nature it is fair that no one should become richer through another person’s loss and injury.',
 "The jurist Pomponius states the principle behind what lawyers now call unjust enrichment. If you gain at someone else's expense without a legal reason, you must give it back. Aequum est is an impersonal expression, and locuplētiōrem is a comparative, 'richer'.",
 "Modern legal systems still build on this rule, from Germany to Scotland. Pomponius wrote in the 2nd century AD, and his works survive almost entirely through quotations in the Digest.",
 'Pomponius (Digest)','Digesta Iustiniani','50.17.206','2nd century AD (Digest 533)',LL+'justinian/digest50.shtml','verified',None,
 'Iūre|iūs|by law|abl. sg. n.; nātūrae|nātūra|of nature|gen. sg. f.; aequum|aequus|fair|nom. sg. n.; est|sum|it is|3rd sg. pres. (impersonal); nēminem|nēmō|no one|acc. sg.; cum|cum|with, through|prep. + abl.; alterius|alter|of another|gen. sg.; dētrīmentō|dētrīmentum|loss|abl. sg. n.; et|et|and|conj.; iniūriā|iniūria|injury|abl. sg. f.; fierī|fīō|to become|pres. inf.; locuplētiōrem|locuplēs|richer|comp. acc. sg. m.',
 ['impersonal_verb','comparative','indirect_statement'],[],'papinian','Unjust enrichment',WP+'Unjust_enrichment',related=['q-dig-nemo-plus'])
K('q-dig-res-iudicata','quote','empire',13,'Rēs iūdicāta prō vēritāte accipitur.','A matter that has been judged is accepted as the truth.',
 "Ulpian states the rule that a final judgement settles a case for good. Once a court has decided, the same dispute cannot be brought again. Accipitur is a present passive, and iūdicāta is a perfect passive participle, 'judged'.",
 "Lawyers today still speak of rēs iūdicāta in many countries. The rule protects people from being sued over and over for the same thing.",
 'Ulpian (Digest)','Digesta Iustiniani','50.17.207','early 3rd century AD (Digest 533)',LL+'justinian/digest50.shtml','verified',None,
 'Rēs|rēs|matter, case|nom. sg. f.; iūdicāta|iūdicō|judged|perf. pass. part. nom. sg. f.; prō|prō|as, for|prep. + abl.; vēritāte|vēritās|truth|abl. sg. f.; accipitur|accipiō|is accepted|3rd sg. pres. pass.',
 ['passive_voice','participle','fifth_declension'],[],'tabularium','Res judicata',WP+'Res_judicata',related=['q-dig-placuit'])
K('q-dig-desisse','quote','empire',13,'Nōn potest vidērī dēsīsse habēre, quī numquam habuit.','A man who never had something cannot be considered to have stopped having it.',
 "The jurist Paul states a point of logic that matters in cases about property and inheritance. Losing something presupposes that you once had it. Dēsīsse is a shortened perfect infinitive of dēsinō, 'to have stopped'.",
 "Medieval commentators such as Bartolus of Sassoferrato wrote long explanations of rules like this. Paul wrote in the early 3rd century AD.",
 'Paul (Digest)','Digesta Iustiniani','50.17.208','early 3rd century AD (Digest 533)',LL+'justinian/digest50.shtml','verified',None,
 'Nōn|nōn|not|adv.; potest|possum|can|3rd sg. pres.; vidērī|videō|to seem, be considered|pres. pass. inf.; dēsīsse|dēsinō|to have stopped|perf. inf. (= dēsiisse); habēre|habeō|having|pres. inf.; quī|quī|(he) who|nom. sg. m.; numquam|numquam|never|adv.; habuit|habeō|had|3rd sg. perf.',
 ['perfect_infinitive','possum_infinitive','relative_clause'],[],'bartolus','Bartolus de Saxoferrato',WP+'Bartolus_de_Saxoferrato',related=['q-dig-res-iudicata'])
K('q-dig-culpa','quote','empire',13,'Quod quis ex culpā suā damnum sentit, nōn intellegitur damnum sentīre.','Harm that someone suffers through his own fault is not considered to be harm suffered.',
 "Pomponius sets out the rule that you cannot claim damages for a loss you caused yourself. Intellegitur, 'is understood, is considered', is a present passive used like an impersonal. Quod … sentit is a relative clause, 'the harm which someone suffers'.",
 "Modern law still reduces damages when the victim was partly to blame. Roman civil cases like this were heard in halls such as the Basilica Julia in the Forum.",
 'Pomponius (Digest)','Digesta Iustiniani','50.17.203','2nd century AD (Digest 533)',LL+'justinian/digest50.shtml','verified',None,
 'Quod|quī|(the harm) which|acc. sg. n.; quis|quis|someone|nom. sg. m.; ex|ex|from, through|prep. + abl.; culpā|culpa|fault|abl. sg. f.; suā|suus|his own|abl. sg. f.; damnum|damnum|harm, loss|acc. sg. n.; sentit|sentiō|suffers, feels|3rd sg. pres.; nōn|nōn|not|adv.; intellegitur|intellegō|is understood|3rd sg. pres. pass.; damnum|damnum|harm|acc. sg. n.; sentīre|sentiō|to suffer|pres. inf.',
 ['relative_clause','passive_voice','infinitive'],[],'basilicajulia','Contributory negligence',WP+'Contributory_negligence',related=['q-dig-locupletiorem'])

# ---------------- UNIT 14: Scientia ----------------
K('q-newton-hypotheses','quote','early_modern',14,'Ratiōnem vērō hārum gravitātis proprietātum ex phaenomenīs nōndum potuī dēdūcere, et hypothesēs nōn fingō.','But I have not yet been able to deduce the cause of these properties of gravity from the phenomena, and I do not invent hypotheses.',
 "Newton added this to the General Scholium of the second edition of his Principia in 1713. His law of gravity predicted the motions of the planets, but he refused to guess what gravity itself was. Potuī dēdūcere is possum with an infinitive, 'I have been able to deduce'.",
 "Critics such as Leibniz complained that gravity acting at a distance sounded like magic. Newton's phrase became a motto for science that sticks to what can be shown.",
 'Isaac Newton','Newton, Principia, Scholium generale','—','1713 (text of 1726)',LL+'newton.scholium.html','verified',None,
 'Ratiōnem|ratiō|reason, cause|acc. sg. f.; vērō|vērō|but|adv.; hārum|hic|of these|gen. pl. f.; gravitātis|gravitās|of gravity|gen. sg. f.; proprietātum|proprietās|of properties|gen. pl. f.; ex|ex|from|prep. + abl.; phaenomenīs|phaenomenon|phenomena|abl. pl. n.; nōndum|nōndum|not yet|adv.; potuī|possum|I have been able|1st sg. perf.; dēdūcere|dēdūcō|to deduce|pres. inf.; et|et|and|conj.; hypothesēs|hypothesis|hypotheses|acc. pl. f.; nōn|nōn|not|adv.; fingō|fingō|I invent|1st sg. pres.',
 ['possum_infinitive','genitive','perfect_tense'],[],'kneller','General Scholium',WP+'General_Scholium',register='classical')
K('q-newton-regula1','quote','early_modern',14,'Causās rērum nātūrālium nōn plūrēs admittī dēbēre, quam quae et vērae sint et eārum phaenomenīs explicandīs sufficiant.','That no more causes of natural things should be admitted than are both true and sufficient to explain their phenomena.',
 "This is the first of Newton's Rules of Reasoning in Philosophy, set out in book 3 of the Principia. It is a version of the principle of economy: do not multiply causes beyond need. Phaenomenīs explicandīs is a gerundive in the dative, 'for explaining the phenomena', and plūrēs … quam is a comparison.",
 "Newton backs the rule with a saying of philosophers: nature does nothing in vain. The same idea is often called Ockham's razor.",
 'Isaac Newton','Newton, Principia, Regulae philosophandi','rule 1','1687 (text of 1726)',LL+'newton.regulae.html','verified','The rule is stated as an indirect statement, with an understood verb such as “we must hold”.',
 'Causās|causa|causes|acc. pl. f.; rērum|rēs|of things|gen. pl. f.; nātūrālium|nātūrālis|natural|gen. pl. f.; nōn|nōn|not|adv.; plūrēs|multus|more|comp. acc. pl. f.; admittī|admittō|to be admitted|pres. pass. inf.; dēbēre|dēbeō|ought|pres. inf.; quam|quam|than|conj.; quae|quī|which|nom. pl. f.; et|et|both|conj.; vērae|vērus|true|nom. pl. f.; sint|sum|are|3rd pl. pres. subj.; et|et|and|conj.; eārum|is|their|gen. pl. f.; phaenomenīs|phaenomenon|phenomena|dat. pl. n.; explicandīs|explicō|to be explained|gerundive dat. pl. n.; sufficiant|sufficiō|suffice|3rd pl. pres. subj.',
 ['gerundive','comparative','indirect_statement'],[],'principia',"Occam's razor",WP+"Occam's_razor",register='classical',related=['q-newton-hypotheses'])
K('q-newton-lex3','quote','early_modern',14,'Āctiōnī contrāriam semper et aequālem esse reāctiōnem.','To every action there is always an opposite and equal reaction.',
 "This is the third of Newton's laws of motion as he stated it in the Principia. When one body pushes on another, the second pushes back just as hard. Like the other laws, it is written as an indirect statement, so reāctiōnem is the accusative subject of esse, and āctiōnī is dative after contrāriam.",
 "The law explains how rockets work: gas is pushed backwards, and the rocket is pushed forwards. Newton published the Principia in 1687.",
 'Isaac Newton','Newton, Principia, Leges motus','law 3','1687 (text of 1726)',LL+'newton.leges.html','verified','The law continues sive corporum duorum actiones in se mutuo semper esse aequales et in partes contrarias dirigi.',
 'Āctiōnī|āctiō|to action|dat. sg. f.; contrāriam|contrārius|opposite|acc. sg. f.; semper|semper|always|adv.; et|et|and|conj.; aequālem|aequālis|equal|acc. sg. f.; esse|sum|to be|pres. inf.; reāctiōnem|reāctiō|reaction|acc. sg. f.',
 ['indirect_statement','dative'],[],'thornhill',"Newton's laws of motion",WP+"Newton's_laws_of_motion",register='classical',related=['q-newton-lex1'])
K('q-descartes-archimedes','quote','early_modern',14,'Nihil nisi pūnctum petēbat Archimēdēs, quod esset fīrmum et immōbile, ut integram terram locō dīmovēret.','Archimedes asked for nothing but one point that was firm and immovable, so that he could shift the whole earth from its place.',
 "In his second Meditation of 1641, Descartes looks for one certain truth on which to rebuild all knowledge. He compares himself to Archimedes, who said that with a fixed point to stand on he could move the earth with a lever. Esset is a subjunctive in a relative clause, and ut … dīmovēret is a purpose clause.",
 "Soon after this passage Descartes finds his fixed point: ego sum, ego existō. The Meditations were written in Latin for a learned audience across Europe.",
 'René Descartes','Descartes, Meditationes de prima philosophia','2.1','1641',LL+'descartes/des.med2.shtml','verified','The source prints & for et.',
 'Nihil|nihil|nothing|acc. sg. n.; nisi|nisi|except|conj.; pūnctum|pūnctum|point|acc. sg. n.; petēbat|petō|asked for|3rd sg. impf.; Archimēdēs|Archimēdēs|Archimedes|nom. sg. m.; quod|quī|which|nom. sg. n.; esset|sum|would be|3rd sg. impf. subj.; fīrmum|fīrmus|firm|nom. sg. n.; et|et|and|conj.; immōbile|immōbilis|immovable|nom. sg. n.; ut|ut|so that|conj.; integram|integer|whole|acc. sg. f.; terram|terra|earth|acc. sg. f.; locō|locus|from its place|abl. sg. m.; dīmovēret|dīmoveō|he could shift|3rd sg. impf. subj.',
 ['subjunctive','relative_clause','imperfect'],[],'halscopy','Meditations on First Philosophy',WP+'Meditations_on_First_Philosophy',register='classical',related=['q-descartes-existo'])
K('q-descartes-animadverti','quote','early_modern',14,'Animadvertī iam ante aliquot annōs quam multa, ineunte aetāte, falsa prō vērīs admīserim.','Some years ago now I noticed how many false things I had accepted as true in my early youth.',
 "These are the first words of Descartes' Meditations: he resolves to doubt everything he once believed and start again from the foundations. Quam multa … admīserim is an indirect question with the subjunctive. Ineunte aetāte, 'with life beginning', is an ablative absolute.",
 "Descartes published the Meditations in Paris in 1641 with objections from other thinkers and his replies. The French translation appeared in 1647.",
 'René Descartes','Descartes, Meditationes de prima philosophia','1.1','1641',LL+'descartes/des.med1.shtml','verified',None,
 'Animadvertī|animadvertō|I noticed|1st sg. perf.; iam|iam|now|adv.; ante|ante|ago, before|adv.; aliquot|aliquot|some|indecl.; annōs|annus|years|acc. pl. m.; quam|quam|how|adv.; multa|multus|many things|acc. pl. n.; ineunte|ineō|beginning|pres. part. abl. sg. f.; aetāte|aetās|life, age|abl. sg. f.; falsa|falsus|false|acc. pl. n.; prō|prō|as, for|prep. + abl.; vērīs|vērus|true things|abl. pl. n.; admīserim|admittō|I had accepted|1st sg. perf. subj.',
 ['indirect_question','ablative_absolute','neuter_plural'],[],'meditationes','Meditations on First Philosophy',WP+'Meditations_on_First_Philosophy',register='classical',related=['q-descartes-archimedes'])
K('q-spinoza-homo-liber','quote','early_modern',14,'Homō līber dē nūllā rē minus quam dē morte cōgitat, et ēius sapientia nōn mortis sed vītae meditātiō est.','A free man thinks of nothing less than of death, and his wisdom is a meditation not on death but on life.',
 "In part 4 of his Ethics, Spinoza describes the free man, who lives by reason and not by fear. Such a person aims at good directly instead of fleeing evil, so he does not dwell on death. Minus quam, 'less than', is a comparison.",
 "Spinoza lived from 1661 to 1663 in Rijnsburg near Leiden, where his small house is now a museum. He died in 1677 at the age of 44.",
 'Baruch Spinoza','Spinoza, Ethica','4.67','1677',LL+'spinoza.ethica4.html','verified','The source spells ejus.',
 'Homō|homō|man|nom. sg. m.; līber|līber|free|nom. sg. m.; dē|dē|about|prep. + abl.; nūllā|nūllus|no|abl. sg. f.; rē|rēs|thing|abl. sg. f.; minus|parum|less|comp. adv.; quam|quam|than|conj.; dē|dē|about|prep. + abl.; morte|mors|death|abl. sg. f.; cōgitat|cōgitō|thinks|3rd sg. pres.; et|et|and|conj.; ēius|is|his|gen. sg.; sapientia|sapientia|wisdom|nom. sg. f.; nōn|nōn|not|adv.; mortis|mors|of death|gen. sg. f.; sed|sed|but|conj.; vītae|vīta|of life|gen. sg. f.; meditātiō|meditātiō|meditation|nom. sg. f.; est|sum|is|3rd sg. pres.',
 ['comparative','fifth_declension','genitive'],[],'rijnsburg','Ethics (Spinoza)',WP+'Ethics_(Spinoza_book)',register='classical',related=['q-spinoza-praeclara'])
K('q-luther-thesis27','quote','early_modern',14,'Hominem praedicant, quī statim, ut iactus nummus in cistam tinnierit, ēvolāre dīcunt animam.','They preach human doctrine who say that the soul flies out of purgatory as soon as the coin thrown into the chest has clinked.',
 "In his 27th thesis of 1517, Luther attacks preachers of indulgences such as Johann Tetzel. People paid money hoping to free the souls of the dead from purgatory. Tinnierit is a future perfect, 'shall have clinked', and animam ēvolāre is an indirect statement after dīcunt.",
 "A popular rhyme put it in German: as soon as the coin in the coffer rings, the soul from purgatory springs. Hominem praedicant literally means 'they preach a man', that is, a merely human teaching.",
 'Martin Luther','Luther, 95 theses','27','1517',WS+'Disputatio_pro_declaratione_virtutis_indulgentiarum','verified',None,
 'Hominem|homō|human (teaching)|acc. sg. m.; praedicant|praedicō|they preach|3rd pl. pres.; quī|quī|who|nom. pl. m.; statim|statim|at once|adv.; ut|ut|as soon as|conj.; iactus|iaciō|thrown|perf. pass. part. nom. sg. m.; nummus|nummus|coin|nom. sg. m.; in|in|into|prep. + acc.; cistam|cista|chest|acc. sg. f.; tinnierit|tinniō|has clinked|3rd sg. fut. perf.; ēvolāre|ēvolō|to fly out|pres. inf.; dīcunt|dīcō|they say|3rd pl. pres.; animam|anima|soul|acc. sg. f.',
 ['indirect_statement','participle','relative_clause'],[],'chest','Ninety-five Theses',WP+'Ninety-five_Theses',register='ecclesiastical',related=['q-luther-thesis1'])
K('q-pico-superiora','quote','early_modern',14,'Poteris in īnferiōra quae sunt bruta dēgenerāre; poteris in superiōra quae sunt dīvīna ex tuī animī sententiā regenerārī.','You will be able to sink to the lower forms, which are the beasts; you will be able, by your own soul’s decision, to be reborn into the higher, which are divine.',
 "Pico's God tells Adam that humans have no fixed place in creation and must shape themselves. Poteris is the future of possum, followed by infinitives. Īnferiōra and superiōra are comparatives used as neuter plural nouns, 'the lower things' and 'the higher things'.",
 "Pico wrote the speech in 1486, aged 23. He planned to defend 900 theses in Rome, but the pope condemned some of them.",
 'Giovanni Pico della Mirandola','Pico, Oratio de hominis dignitate','23','1486',WS+'Oratio_de_hominis_dignitate','verified',None,
 'Poteris|possum|you will be able|2nd sg. fut.; in|in|into|prep. + acc.; īnferiōra|īnferus|lower things|comp. acc. pl. n.; quae|quī|which|nom. pl. n.; sunt|sum|are|3rd pl. pres.; bruta|brūtus|beasts|nom. pl. n.; dēgenerāre|dēgenerō|to sink, degenerate|pres. inf.; poteris|possum|you will be able|2nd sg. fut.; in|in|into|prep. + acc.; superiōra|superus|higher things|comp. acc. pl. n.; quae|quī|which|nom. pl. n.; sunt|sum|are|3rd pl. pres.; dīvīna|dīvīnus|divine|nom. pl. n.; ex|ex|by, from|prep. + abl.; tuī|tuus|your|gen. sg. m.; animī|animus|of soul, mind|gen. sg. m.; sententiā|sententia|judgement, decision|abl. sg. f.; regenerārī|regenerō|to be reborn|pres. pass. inf.',
 ['comparative','possum_infinitive','future_tense'],[],'picoaltissimo','Oration on the Dignity of Man',WP+'Oration_on_the_Dignity_of_Man',register='classical',related=['q-pico-adam'])
K('q-erasmus-querela','quote','early_modern',14,'Nam utcumque amantem ab sē prōpellere, inhūmānum est: bene merentem āversārī, ingrātum: parentem ac servātrīcem omnium afflīgere, impium.','For to drive away one who loves you is inhuman in any case; to turn from one who deserves well, ungrateful; to harm the parent and protector of all, wicked.',
 "In The Complaint of Peace of 1517, Erasmus lets Peace herself speak, lamenting that Christian princes keep driving her out with war. Each infinitive phrase is the subject of an understood est. Āversārī is a deponent infinitive, 'to turn away from'.",
 "Erasmus wrote the book when the Habsburg and French courts were discussing a general peace. He also popularised the saying dulce bellum inexpertīs, 'war is sweet to those who have not tried it'.",
 'Desiderius Erasmus','Erasmus, Querela pacis','2','1517',LL+'erasmus/querela.shtml','verified',None,
 'Nam|nam|for|conj.; utcumque|utcumque|in any case|adv.; amantem|amō|one who loves|pres. part. acc. sg. m.; ab|ā, ab|from|prep. + abl.; sē|suī|oneself|abl.; prōpellere|prōpellō|to drive away|pres. inf.; inhūmānum|inhūmānus|inhuman|nom. sg. n.; est|sum|is|3rd sg. pres.; bene|bene|well|adv.; merentem|mereō|one who deserves|pres. part. acc. sg. m.; āversārī|āversor|to turn away from|pres. inf. (deponent); ingrātum|ingrātus|ungrateful|nom. sg. n.; parentem|parēns|parent|acc. sg. m.; ac|ac|and|conj.; servātrīcem|servātrīx|protector (fem.)|acc. sg. f.; omnium|omnis|of all|gen. pl.; afflīgere|afflīgō|to harm|pres. inf.; impium|impius|wicked|nom. sg. n.',
 ['infinitive_as_subject','deponent','present_participle'],[],'erasmusng','The Complaint of Peace',WP+'Querela_pacis',register='classical',related=['q-erasmus-stultitia'])
K('q-erasmus-moriae','quote','early_modern',14,'Utcumque dē mē vulgō mortālēs loquuntur — neque enim sum nescia, quam male audiat Stultitia etiam apud stultissimōs …','However mortals commonly speak of me — for I am well aware how badly Folly is spoken of even among the greatest fools …',
 "Erasmus wrote The Praise of Folly in 1509 while staying with Thomas More, and Folly herself gives the speech. She begins by admitting her bad reputation before praising herself. Loquuntur is deponent, quam male audiat is an indirect question, and stultissimōs is a superlative.",
 "Male audīre, 'to hear badly', means 'to be spoken ill of'. The Greek title Moriae encomium plays on More's name.",
 'Desiderius Erasmus','Erasmus, Moriae encomium','1','1511',LL+'erasmus/moriae.shtml','verified','The sentence continues for several more lines.',
 'Utcumque|utcumque|however|adv.; dē|dē|about|prep. + abl.; mē|ego|me|abl. sg.; vulgō|vulgō|commonly|adv.; mortālēs|mortālis|mortals|nom. pl. m.; loquuntur|loquor|speak|3rd pl. pres. (deponent); neque|neque|nor, and not|conj.; enim|enim|for|conj.; sum|sum|I am|1st sg. pres.; nescia|nescius|unaware|nom. sg. f.; quam|quam|how|adv.; male|male|badly|adv.; audiat|audiō|is spoken of|3rd sg. pres. subj.; Stultitia|stultitia|Folly|nom. sg. f.; etiam|etiam|even|adv.; apud|apud|among|prep. + acc.; stultissimōs|stultus|the greatest fools|superl. acc. pl. m.',
 ['deponent','indirect_question','superlative'],[],'erasmusmassys','In Praise of Folly',WP+'In_Praise_of_Folly',register='classical',related=['q-erasmus-stultitia'])
K('q-galileo-medicea','quote','early_modern',14,'Quod sī illās prīmus indāgāvī, quis mē iūre reprehendat, sī iīsdem quoque nōmen imposuerō, ac Medicea Sīdera appellārō?','But if I was the first to find them, who could rightly blame me if I give them a name too, and call them the Medicean Stars?',
 "In 1610 Galileo turned his new telescope on Jupiter and saw four moons circling it. In the dedication of his Starry Messenger he names them after the Medici family of Florence, hoping for their patronage, and it worked. Reprehendat is a potential subjunctive, 'who would blame', and imposuerō and appellārō are future perfects.",
 "Cosimo II de' Medici soon made Galileo his court mathematician. Today the four moons are called the Galilean moons: Io, Europa, Ganymede and Callisto.",
 'Galileo Galilei','Galileo, Sidereus Nuncius, dedication','—','1610',LL+'galileo/galileo.sid.html','verified',None,
 'Quod|quod|but|conj.; sī|sī|if|conj.; illās|ille|them|acc. pl. f.; prīmus|prīmus|first|nom. sg. m.; indāgāvī|indāgō|I tracked down|1st sg. perf.; quis|quis|who|nom. sg. m.; mē|ego|me|acc. sg.; iūre|iūs|rightly|abl. sg. n.; reprehendat|reprehendō|would blame|3rd sg. pres. subj.; sī|sī|if|conj.; iīsdem|īdem|to the same|dat. pl. f.; quoque|quoque|also|adv.; nōmen|nōmen|name|acc. sg. n.; imposuerō|impōnō|I give|1st sg. fut. perf.; ac|ac|and|conj.; Medicea|Mediceus|Medicean|acc. pl. n.; Sīdera|sīdus|stars|acc. pl. n.; appellārō|appellō|I call|1st sg. fut. perf. (= appellāverō)',
 ['subjunctive','dative','neuter_plural'],[],'medicea','Sidereus Nuncius',WP+'Sidereus_Nuncius',register='classical')
K('q-melanchthon-duae-res','quote','early_modern',14,'Duae rēs sunt, quibus nihil melius ac dīvīnius habet hūmāna nātūra, vidēlicet vēritās et iūstitia.','There are two things than which human nature has nothing better or more divine: truth and justice.',
 "Philipp Melanchthon, Luther's colleague at Wittenberg, opens his speech In Praise of the Scholarly Life with this sentence. He argues that schools, which seek truth and justice, are as necessary to a state as churches and courts. Melius and dīvīnius are comparatives, and quibus is an ablative of comparison, 'than which'.",
 "Melanchthon reorganised schools and universities across Protestant Germany and was called the Teacher of Germany. He wrote much of the Augsburg Confession of 1530.",
 'Philipp Melanchthon','Melanchthon, De laude vitae scholasticae oratio','1','1536',LL+'melanchthon/laude.html','verified',None,
 'Duae|duo|two|nom. pl. f.; rēs|rēs|things|nom. pl. f.; sunt|sum|are|3rd pl. pres.; quibus|quī|than which|abl. pl. f. (comparison); nihil|nihil|nothing|acc. sg. n.; melius|bonus|better|comp. acc. sg. n.; ac|ac|and|conj.; dīvīnius|dīvīnus|more divine|comp. acc. sg. n.; habet|habeō|has|3rd sg. pres.; hūmāna|hūmānus|human|nom. sg. f.; nātūra|nātūra|nature|nom. sg. f.; vidēlicet|vidēlicet|namely|adv.; vēritās|vēritās|truth|nom. sg. f.; et|et|and|conj.; iūstitia|iūstitia|justice|nom. sg. f.',
 ['comparative','ablative_of_comparison','numerals'],[],'melanchthon','Philip Melanchthon',WP+'Philip_Melanchthon',register='classical')
