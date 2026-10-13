# Batch 5 card texts. Gloss format: "word|lemma|meaning|parse; ..."  (no semicolons inside meanings)
# K(id,type,era,unit,latin,translation,context,more,person,work,cit,date,source_url,conf,note,gloss,target,preview,img,lm_label,lm_url, **extra)
LL='https://www.thelatinlibrary.com/'
WP='https://en.wikipedia.org/wiki/'
CON='Constructed teaching sentence (not a quotation).'
CARDS=[]
def K(*a,**kw): CARDS.append((a,kw))

# ---------------- UNIT 3: Legio ----------------
K('q-caesar-garumna','quote','republic',3,'Gallōs ab Aquītānīs Garumna flūmen, ā Belgīs Matrona et Sēquana dīvidit.','The river Garonne divides the Gauls from the Aquitani, the Marne and the Seine from the Belgae.',
 "The second sentence of Caesar's Gallic War draws Gaul's borders with rivers: the Garonne in the south-west, the Marne and the Seine in the north. Caesar wrote these commentaries in the third person while his campaigns of 58–50 BC were still going on, partly as reports for readers in Rome. The verb is singular even though Matrona et Sēquana is a double subject, because the two rivers act together as one boundary.",
 "Garumna survives in the modern name Garonne, Sēquana in Seine and Matrona in Marne. Bordeaux, the Roman Burdigala, stands on the Garonne.",
 'Julius Caesar','Caesar, De bello Gallico','1.1.2','c. 50s BC',LL+'caesar/gall1.shtml','verified',None,
 'Gallōs|Gallus|the Gauls|acc. pl. m.; ab|ab|from|prep. + abl.; Aquītānīs|Aquītānus|the Aquitani|abl. pl. m.; Garumna|Garumna|the Garonne|nom. sg. f.; flūmen|flūmen|river|nom. sg. n.; ā|ab|from|prep. + abl.; Belgīs|Belgae|the Belgae|abl. pl. m.; Matrona|Matrona|the Marne|nom. sg. f.; et|et|and|conj.; Sēquana|Sēquana|the Seine|nom. sg. f.; dīvidit|dīvidō|divides|3rd sg. pres.',
 ['present_tense','accusative'],[],'garumna','Commentarii de Bello Gallico',WP+'Commentarii_de_Bello_Gallico')
K('q-caesar-castra-movent','quote','republic',3,'Posterō diē castra ex eō locō movent.','On the next day they move camp from that place.',
 "Caesar uses this formula again and again in the Gallic War, as the army marches on after the Helvetii in 58 BC. A Roman army on the march built a new fortified camp every evening, with a ditch and a rampart, and broke it up again in the morning. Castra is plural in form but means a single camp; here it is the neuter plural object of movent, whose unstated subject 'they' is Caesar's army.",
 "Posterō diē, 'on the following day', is an ablative of time. Many English place names ending in -chester, -caster or -cester come from castra.",
 'Julius Caesar','Caesar, De bello Gallico','1.15.1','c. 50s BC',LL+'caesar/gall1.shtml','verified',None,
 'Posterō|posterus|next, following|abl. sg. m.; diē|diēs|day|abl. sg. m.; castra|castra|camp|acc. pl. n.; ex|ex|out of, from|prep. + abl.; eō|is|that|abl. sg. m.; locō|locus|place|abl. sg. m.; movent|moveō|they move|3rd pl. pres.',
 ['third_person_plural','neuter_plural'],['ablative_of_time'],'castra','Roman military camp',WP+'Castra')
K('q-seneca-si-vales','quote','empire',3,'Sī valēs, bene est; ego valeō.','If you are well, that is good; I am well.',
 "Seneca tells his friend Lucilius that Romans 'up to my own time' opened letters with this greeting, so common it was often written as initials, S.V.B.E.E.V. Seneca jokes that the true version should be 'if you are doing philosophy, that is good', because only philosophy makes us truly well. The greeting is a neat pair of verb forms: valēs, 'you are well', and valeō, 'I am well'.",
 "The same root gives valē, 'goodbye' (literally 'be well'), and English valid and valiant. Cicero's letters often begin S.V.B.E.E.V. or S.V.B.E.",
 'Lucius Annaeus Seneca','Seneca, Epistulae morales','15.1','c. AD 64',LL+'sen/seneca.ep2.shtml','verified',None,
 'Sī|sī|if|conj.; valēs|valeō|you are well|2nd sg. pres.; bene|bene|well, good|adv.; est|sum|it is|3rd sg. pres.; ego|ego|I|nom. sg.; valeō|valeō|I am well|1st sg. pres.',
 ['present_tense','first_person'],[],'tablet','Seneca the Younger',WP+'Seneca_the_Younger',abbr='S.V.B.E.E.V.')
K('v-milites-aedificant','vocab','empire',3,'Mīlitēs arborēs caedunt et castra aedificant.','The soldiers cut down trees and build a camp.',
 "Roman legionaries were builders as much as fighters. Each man carried tools such as a pickaxe-axe (dolabra) and a basket for earth, and Trajan's Column shows soldiers felling trees, carrying timber and building forts during the Dacian Wars (AD 101–106). Both verbs here are plural because the subject, mīlitēs, is plural.",
 "Caedunt comes from caedō, 'cut, strike, kill', the root of English words such as homicide and incision.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Mīlitēs|mīles|soldiers|nom. pl. m.; arborēs|arbor|trees|acc. pl. f.; caedunt|caedō|they cut down|3rd pl. pres.; et|et|and|conj.; castra|castra|camp|acc. pl. n.; aedificant|aedificō|they build|3rd pl. pres.',
 ['third_person_plural','present_tense'],[],'legio',"Trajan's Column",WP+'Trajan%27s_Column',subtype='vocab')
K('v-pontem-faciunt','vocab','empire',3,'Mīlitēs flūmen trānseunt; pontem faciunt.','The soldiers cross the river; they make a bridge.',
 "Roman armies crossed rivers on bridges of boats lashed together, or built timber bridges on piles. Caesar boasts that in 55 BC his men bridged the Rhine in ten days, and Trajan's Column shows legionaries marching across the Danube on a pontoon bridge. Trānseunt, 'they go across', is a compound of eō, 'go', and the prefix trāns-, 'across'.",
 "Pōns, pontis gives English pontoon and pontiff. A pontifex was literally a 'bridge-maker', perhaps because priests once looked after the Tiber's sacred wooden bridge.",
 None,'Constructed','—','—',None,'constructed',CON,
 'Mīlitēs|mīles|soldiers|nom. pl. m.; flūmen|flūmen|river|acc. sg. n.; trānseunt|trānseō|they cross|3rd pl. pres.; pontem|pōns|bridge|acc. sg. m.; faciunt|faciō|they make|3rd pl. pres.',
 ['third_person_plural','accusative'],[],'bridge',"Caesar's Rhine bridges",WP+'Caesar%27s_Rhine_bridges',subtype='vocab')

# ---------------- UNIT 4: Daily Life ----------------
K('q-martial-thais','quote','empire',4,'Thāis habet nigrōs, niveōs Laecania dentēs. Quae ratiō est? Ēmptōs haec habet, illa suōs.','Thais has black teeth, Laecania snow-white ones. What is the reason? This one has bought teeth, that one her own.',
 "Martial's two-line epigrams often save the sting for the last word. Here the reader expects Laecania to come off better, until the punchline reveals that her perfect teeth are false. Gold dental bridges are known from Etruscan and Roman Italy, and Martial mocks false teeth more than once. Notice how the adjectives nigrōs, niveōs, ēmptōs and suōs all agree with dentēs, though they sit far from it.",
 "Haec ('this one') and illa ('that one') point back to the last-named and first-named women: haec is Laecania, illa is Thais.",
 'Martial','Martial, Epigrammata','5.43','c. AD 90',LL+'martial/mart5.shtml','verified','Quantity of the a in Laecania is uncertain and left unmarked.',
 'Thāis|Thāis|Thais (a woman\'s name)|nom. sg. f.; habet|habeō|has|3rd sg. pres.; nigrōs|niger|black|acc. pl. m.; niveōs|niveus|snow-white|acc. pl. m.; Laecania|Laecania|Laecania (a woman\'s name)|nom. sg. f.; dentēs|dēns|teeth|acc. pl. m.; Quae|quī|what|nom. sg. f. (interrog.); ratiō|ratiō|reason|nom. sg. f.; est|sum|is|3rd sg. pres.; Ēmptōs|emō|bought|acc. pl. m. (participle); haec|hic|this one|nom. sg. f.; illa|ille|that one|nom. sg. f.; suōs|suus|her own|acc. pl. m.',
 ['adjective_agreement','accusative'],['demonstratives'],'thais','Martial',WP+'Martial')
K('q-virgil-varium','quote','empire',4,'Varium et mūtābile semper fēmina.','A woman is always a fickle and changeable thing.',
 "In Aeneid 4 the god Mercury appears to Aeneas in a dream and urges him to sail from Carthage at once, before Queen Dido turns against him. These are the god's parting words. The adjectives are neuter even though fēmina is feminine: 'a fickle and changeable thing'. The verb est is left out, as often in Latin sayings, and the poem's sympathy lies with Dido, whom Aeneas abandons.",
 "The phrase was quoted for centuries as a proverb about women, usually without its context. Verdi's 'La donna è mobile' echoes the same idea.",
 'Virgil (speech of Mercury)','Virgil, Aeneid','4.569–70','c. 19 BC',LL+'vergil/aen4.shtml','verified','Spoken by Mercury in the poem, not by Virgil in his own voice.',
 'Varium|varius|changeable, fickle|nom. sg. n.; et|et|and|conj.; mūtābile|mūtābilis|changeable|nom. sg. n.; semper|semper|always|adv.; fēmina|fēmina|woman|nom. sg. f.',
 ['adjectives','nominative'],[],'dido','Dido',WP+'Dido')
K('q-cicero-praeclara','quote','republic',4,'Omnia praeclāra rāra.','All excellent things are rare.',
 "In his dialogue On Friendship (44 BC), Cicero has Laelius say that true friends are hard to find, as everything excellent is. The saying needs no verb: est or sunt is understood. All three words are neuter plural, 'all excellent things', a common Latin way to say 'things' without a noun. Spinoza ended his Ethics with a similar thought: everything excellent is as difficult as it is rare.",
 "Praeclārus means literally 'very bright' (prae + clārus), so 'brilliant, famous, excellent'.",
 'Cicero (speech of Laelius)','Cicero, De amicitia','79','44 BC',LL+'cicero/amic.shtml','verified','Spoken by Laelius in the dialogue.',
 'Omnia|omnis|all things|nom. pl. n.; praeclāra|praeclārus|excellent, brilliant|nom. pl. n.; rāra|rārus|rare|nom. pl. n.',
 ['adjectives','neuter_plural'],[],'cicerobust','Laelius de Amicitia',WP+'Laelius_de_Amicitia')
K('q-catullus-libellum','quote','republic',4,'Cui dōnō lepidum novum libellum?','To whom shall I give my charming new little book?',
 "This is the first line of Catullus's poetry book, around 55 BC. The answer comes at once: to Cornelius Nepos, the historian, who had always thought Catullus's trifles worth something. A libellus was a papyrus roll with its ends smoothed with pumice, and Catullus means the polished book in his reader's hands. Cui is the dative, 'to whom', and dōnō here means 'am I to give?'",
 "Libellus is a diminutive of liber, 'book', so 'little book'. English libel comes from the same word, through the sense of a small written statement.",
 'Catullus','Catullus, Carmina','1.1','c. 55 BC',LL+'catullus.shtml','verified',None,
 'Cui|quis|to whom|dat. sg. (interrog.); dōnō|dōnō|I give, am I to give|1st sg. pres.; lepidum|lepidus|charming, witty|acc. sg. m.; novum|novus|new|acc. sg. m.; libellum|libellus|little book|acc. sg. m.',
 ['dative','adjective_agreement'],[],'catullus','Catullus',WP+'Catullus')
K('q-juvenal-rara-avis','quote','empire',4,'Rāra avis in terrīs nigrōque simillima cycnō','a rare bird on earth, very like a black swan',
 "Juvenal's sixth satire (early 2nd century AD) mocks the idea of a perfect wife: such a woman would be 'a rare bird on earth, very like a black swan'. To a Roman a black swan meant something that did not exist. Europeans first saw real black swans in Australia in 1697. Rāra avis is still used in English for an unusual person or thing.",
 "Simillima is the superlative of similis, 'like', and it takes the dative: nigrō cycnō, 'to a black swan'. Nigrō and cycnō are both datives.",
 'Juvenal','Juvenal, Saturae','6.165','early 2nd c. AD',LL+'juvenal/6.shtml','verified',None,
 'Rāra|rārus|rare|nom. sg. f.; avis|avis|bird|nom. sg. f.; in|in|on|prep. + abl.; terrīs|terra|earth, lands|abl. pl. f.; nigrō|niger|black|dat. sg. m.; -que|-que|and|enclitic; simillima|similis|very like|nom. sg. f. (superl.); cycnō|cycnus|swan|dat. sg. m.',
 ['adjective_agreement','dative'],['superlative'],'swan','Rara avis',WP+'Rara_avis')

# ---------------- UNIT 5 ----------------
K('q-tacitus-reges','quote','empire',5,'Rēgēs ex nōbilitāte, ducēs ex virtūte sūmunt.','They choose kings for their noble birth, generals for their courage.',
 "In the Germania (AD 98), Tacitus describes how the German tribes picked their leaders: kings by descent, war-leaders by proven bravery. He adds that the kings had no unlimited power and that generals led by example rather than by command. The Germania often holds up the 'barbarians' as a mirror to Roman vices.",
 "Rēx, rēgis and dux, ducis are both third-declension nouns, and so are nōbilitās and virtūs. Dux gives English duke and Italian Duce.",
 'Tacitus','Tacitus, Germania','7.1','AD 98',LL+'tacitus/tac.ger.shtml','verified',None,
 'Rēgēs|rēx|kings|acc. pl. m.; ex|ex|from, on the basis of|prep. + abl.; nōbilitāte|nōbilitās|noble birth|abl. sg. f.; ducēs|dux|leaders, generals|acc. pl. m.; virtūte|virtūs|courage, merit|abl. sg. f.; sūmunt|sūmō|they choose, take|3rd pl. pres.',
 ['third_declension','third_conjugation','prep_ablative'],[],'germani','Germania (book)',WP+'Germania_(book)')
K('q-seneca-homo-sacra','quote','empire',5,'Homō, sacra rēs hominī.','A human being is a sacred thing to a human being.',
 "Seneca (Letter 95, about AD 64) sets this against the arena: 'a human being, a sacred thing to a human being, is now killed for sport and fun.' He is attacking the gladiator shows that most Romans enjoyed without a second thought. Rēs, 'thing', is a fifth-declension noun, and hominī is the dative: sacred 'to' another person.",
 "The phrase answers an old Latin proverb, homō hominī lupus, 'man is a wolf to man' (from Plautus).",
 'Lucius Annaeus Seneca','Seneca, Epistulae morales','95.33','c. AD 64',LL+'sen/seneca.ep14-15.shtml','verified',None,
 'Homō|homō|human being|nom. sg. m.; sacra|sacer|sacred|nom. sg. f.; rēs|rēs|thing|nom. sg. f.; hominī|homō|to a human being|dat. sg. m.',
 ['fifth_declension','third_declension','dative'],[],'gladiators','Seneca the Younger',WP+'Seneca_the_Younger')

# ---------------- UNIT 6: Empire ----------------
K('q-horace-ibam','quote','empire',6,'Ībam forte viā Sacrā, sīcut meus est mōs','I happened to be walking along the Sacred Way, as is my habit',
 "So begins Horace's satire about a bore (about 35 BC). Strolling through the Forum, the poet is grabbed by a social climber who will not let go until a lawsuit drags him away. Ībam is the imperfect, 'I was walking', which sets the scene for something to happen. The Via Sacra ran through the Forum past the temples and the Senate house.",
 "Viā Sacrā is an ablative of the route taken: 'by the Sacred Way'. Forte, 'by chance', is the ablative of fors, 'chance'.",
 'Horace','Horace, Sermones (Satires)','1.9.1','c. 35 BC',LL+'horace/serm1.shtml','verified',None,
 'Ībam|eō|I was walking|1st sg. impf.; forte|forte|by chance|adv.; viā|via|by the road|abl. sg. f.; Sacrā|sacer|Sacred|abl. sg. f.; sīcut|sīcut|just as|conj.; meus|meus|my|nom. sg. m.; est|sum|is|3rd sg. pres.; mōs|mōs|habit, custom|nom. sg. m.',
 ['imperfect','possessive_adjectives'],[],'viasacra','Via Sacra',WP+'Via_Sacra')
K('q-martial-diaulus','quote','empire',6,'Nūper erat medicus, nunc est vispillō Diaulus: quod vispillō facit, fēcerat et medicus.','Diaulus was a doctor until recently, now he is an undertaker: what he does as an undertaker, he had also done as a doctor.',
 "Martial (about AD 86) aims one of his best-known jokes at a bad doctor. A vispillō carried out the bodies of the poor for burial at night. The joke turns on tense: erat (imperfect, 'he was'), est (present) and fēcerat (pluperfect, 'he had done'). As a doctor Diaulus was already sending his patients to the grave.",
 "Roman doctors needed no licence, and many were Greek freedmen. Pliny the Elder complained that doctors learned by experimenting on patients' lives.",
 'Martial','Martial, Epigrammata','1.47','c. AD 86',LL+'martial/mart1.shtml','verified','The Latin Library text spells uispillo; vespillō is the more common spelling.',
 'Nūper|nūper|recently|adv.; erat|sum|was|3rd sg. impf.; medicus|medicus|doctor|nom. sg. m.; nunc|nunc|now|adv.; est|sum|is|3rd sg. pres.; vispillō|vispillō|undertaker|nom. sg. m.; Diaulus|Diaulus|Diaulus|nom. sg. m.; quod|quī|what|acc. sg. n.; facit|faciō|he does|3rd sg. pres.; fēcerat|faciō|he had done|3rd sg. plupf.; et|et|also|adv.; medicus|medicus|as a doctor|nom. sg. m.',
 ['imperfect','perfect_tense'],['relative_clause','pluperfect'],'surgical','Medicine in ancient Rome',WP+'Medicine_in_ancient_Rome')
K('q-resgestae-bis-ovans','quote','empire',6,'Bis ovāns triumphāvī, trīs ēgī curūlīs triumphōs.','Twice I celebrated an ovation, three times I held curule triumphs.',
 "In his Res Gestae, the record of his achievements set up at his death in AD 14, Augustus counts his honours like a ledger. A full triumph meant riding through Rome in a chariot. An ovation was a lesser triumph on foot or horseback. Both verbs are in the perfect, the tense of a finished career, and bis and tris are numerals.",
 "The best surviving copy is carved on the walls of a temple at Ancyra, modern Ankara. Trīs is an older form of trēs, and curūlīs of curūlēs.",
 'Augustus','Res Gestae Divi Augusti','4.1','AD 14',LL+'resgestae.html','verified',None,
 'Bis|bis|twice|adv.; ovāns|ovō|celebrating an ovation|nom. sg. m. pres. part.; triumphāvī|triumphō|I triumphed|1st sg. perf.; trīs|trēs|three|acc. pl. m.; ēgī|agō|I held|1st sg. perf.; curūlīs|curūlis|curule (in a chariot)|acc. pl. m.; triumphōs|triumphus|triumphs|acc. pl. m.',
 ['perfect_tense','numerals'],['present_participle'],'ancyra','Res Gestae Divi Augusti',WP+'Res_Gestae_Divi_Augusti')
K('q-cicero-abiit','quote','republic',6,'Abiit, excessit, ēvāsit, ērūpit.','He has gone, he has left, he has slipped away, he has broken out.',
 "Cicero opened his second speech against Catiline (9 November 63 BC) with four verbs in a row, the day after the conspirator fled Rome. Each is a perfect tense of a compound verb, and each is a little stronger than the last. Leaving out the 'and' (asyndeton) makes the list hit harder. Cicero told the people that Rome was now safe, though Catiline's allies were still in the city.",
 "All four verbs are compounds: ab-eō 'go away', ex-cēdō 'go out', ē-vādō 'escape', ē-rumpō 'burst out'. Catiline died in battle near Pistoria early in 62 BC.",
 'Cicero','Cicero, In Catilinam','2.1','63 BC',LL+'cicero/cat2.shtml','verified',None,
 'Abiit|abeō|he has gone away|3rd sg. perf.; excessit|excēdō|he has left|3rd sg. perf.; ēvāsit|ēvādō|he has escaped|3rd sg. perf.; ērūpit|ērumpō|he has broken out|3rd sg. perf.',
 ['perfect_tense'],[],'catiline','Catilinarian Orations',WP+'Catilinarian_orations')
K('q-pliny-misenum','quote','empire',6,'Erat Mīsēnī classemque imperiō praesēns regēbat.','He was at Misenum, in person commanding the fleet.',
 "Pliny the Younger begins his account of his uncle's death for the historian Tacitus with these words. In AD 79 Pliny the Elder, admiral of the fleet at Misenum on the Bay of Naples, saw a strange cloud rising over Vesuvius. He sailed toward the eruption to rescue people and died on the shore at Stabiae. The imperfects erat and regēbat set the calm scene before disaster.",
 "Mīsēnī is a locative, 'at Misenum'. Pliny the Elder also wrote the Natural History, a 37-book encyclopedia.",
 'Pliny the Younger','Pliny the Younger, Epistulae','6.16.4','c. AD 106',LL+'pliny.ep6.html','verified',None,
 'Erat|sum|he was|3rd sg. impf.; Mīsēnī|Mīsēnum|at Misenum|locative; classem|classis|fleet|acc. sg. f.; -que|-que|and|enclitic; imperiō|imperium|with command|abl. sg. n.; praesēns|praesēns|in person, present|nom. sg. m.; regēbat|regō|he was commanding|3rd sg. impf.',
 ['imperfect','enclitic_que'],[],'vesuvius','Eruption of Mount Vesuvius in 79 AD',WP+'Eruption_of_Mount_Vesuvius_in_79_AD')
# ---------------- UNIT 7 ----------------
K('q-martial-pauper','quote','empire',7,'Semper pauper eris, sī pauper es, Aemiliāne: dantur opēs nūllīs nunc nisi dīvitibus.','If you are poor, Aemilianus, you will always be poor: these days wealth is given to no one but the rich.',
 "Martial (about AD 89) complains that Roman generosity only flows towards people who are already rich, since gifts and legacies went to those who could return the favour. The line plays the future eris ('you will be') against the present es ('you are'). Aemiliāne is a vocative, addressing the man directly.",
 "Dantur, 'are given', is a passive verb. The thought matches the Gospel saying 'to everyone who has, more will be given'.",
 'Martial','Martial, Epigrammata','5.81','c. AD 89',LL+'martial/mart5.shtml','verified',None,
 'Semper|semper|always|adv.; pauper|pauper|poor|nom. sg. m.; eris|sum|you will be|2nd sg. fut.; sī|sī|if|conj.; pauper|pauper|poor|nom. sg. m.; es|sum|you are|2nd sg. pres.; Aemiliāne|Aemiliānus|Aemilianus|voc. sg. m.; dantur|dō|are given|3rd pl. pres. pass.; opēs|ops|wealth|nom. pl. f.; nūllīs|nūllus|to no one|dat. pl.; nunc|nunc|now|adv.; nisi|nisi|except|conj.; dīvitibus|dīves|the rich|dat. pl.',
 ['future_tense','vocative'],['passive_voice'],'hoard','Martial',WP+'Martial')

# ---------------- UNIT 8: Philosophers ----------------
K('q-seneca-servi','quote','empire',8,'"Servī sunt." Immō hominēs.','"They are slaves." No, they are human beings.',
 "Seneca's Letter 47 (about AD 64) praises Lucilius for living on friendly terms with his slaves. Seneca imagines a snobbish objector and answers each 'they are slaves' with a correction: no, they are human beings, companions, humble friends, fellow slaves under fortune. Seneca did not call for an end to slavery, but he insisted that slaves share the same nature as their masters.",
 "Immō corrects what was just said: 'no, rather'. Seneca himself was one of the richest men in Rome and owned many slaves.",
 'Lucius Annaeus Seneca','Seneca, Epistulae morales','47.1','c. AD 64',LL+'sen/seneca.ep5.shtml','verified',None,
 'Servī|servus|slaves|nom. pl. m.; sunt|sum|they are|3rd pl. pres.; Immō|immō|no, rather|adv.; hominēs|homō|human beings|nom. pl. m.',
 ['nominative','sum'],[],'herm','Seneca the Younger',WP+'Seneca_the_Younger')
K('q-seneca-naturam','quote','empire',8,'Prōpositum nostrum est secundum nātūram vīvere.','Our aim is to live according to nature.',
 "This is the Stoic motto, going back to Zeno of Citium, who taught in Athens around 300 BC. Seneca (Letter 5) warns Lucilius that it does not mean dressing in rags or showing off a rough life. For the Stoics 'nature' meant above all reason, so living by nature meant living rationally and virtuously. The infinitive vīvere works as a noun: 'to live' is our aim.",
 "Secundum, 'following', is a preposition taking the accusative. It comes from sequor, 'follow', the same root as English second.",
 'Lucius Annaeus Seneca','Seneca, Epistulae morales','5.4','c. AD 64',LL+'sen/seneca.ep1.shtml','verified',None,
 'Prōpositum|prōpositum|aim, purpose|nom. sg. n.; nostrum|noster|our|nom. sg. n.; est|sum|is|3rd sg. pres.; secundum|secundum|according to|prep. + acc.; nātūram|nātūra|nature|acc. sg. f.; vīvere|vīvō|to live|pres. inf.',
 ['infinitive','infinitive_as_subject'],[],'zeno','Stoicism',WP+'Stoicism')
K('q-seneca-brevitas','quote','empire',8,'Nōn exiguum temporis habēmus, sed multum perdidimus.','It is not that we have a short time, but that we have wasted much of it.',
 "On the Shortness of Life (about AD 49) opens by answering a common complaint: life is not short, we make it short by wasting it. Seneca lists the ways Romans throw away their days, from business and banquets to chasing other people's favour. The sentence sets a present (habēmus) against a perfect (perdidimus). Temporis is a partitive genitive: 'a small amount of time'.",
 "Seneca's addressee, Paulinus, was in charge of Rome's grain supply. Seneca urges him to retire and spend his time on philosophy.",
 'Lucius Annaeus Seneca','Seneca, De brevitate vitae','1.3','c. AD 49',LL+'sen/sen.brevita.shtml','verified',None,
 'Nōn|nōn|not|adv.; exiguum|exiguus|a small amount|acc. sg. n.; temporis|tempus|of time|gen. sg. n.; habēmus|habeō|we have|1st pl. pres.; sed|sed|but|conj.; multum|multus|much|acc. sg. n.; perdidimus|perdō|we have wasted|1st pl. perf.',
 ['perfect_tense','genitive'],[],'senecams','De Brevitate Vitae (Seneca)',WP+'De_Brevitate_Vitae_(Seneca)')
K('q-lucretius-nil-creari','quote','republic',8,'Nīl posse creārī dē nihilō','that nothing can be created out of nothing',
 "Lucretius's poem On the Nature of Things (about 55 BC) sets out the atomic theory of Epicurus, and this is its first principle. If things could come from nothing, he argues, anything could be born from anything, and men could spring from the sea. Everything is made of atoms that are never created or destroyed. In the poem the phrase depends on 'we shall see', so it is an indirect statement.",
 "Creārī is a passive infinitive, 'to be created'. Nīl is a short form of nihil.",
 'Lucretius','Lucretius, De rerum natura','1.155–56','c. 55 BC',LL+'lucretius/lucretius1.shtml','verified',None,
 'Nīl|nihil|nothing|acc. sg. n. (subject of inf.); posse|possum|to be able|pres. inf.; creārī|creō|to be created|pres. pass. inf.; dē|dē|out of, from|prep. + abl.; nihilō|nihil|nothing|abl. sg. n.',
 ['possum_infinitive','indirect_statement'],['passive_voice'],'lucretiusms','De rerum natura',WP+'De_rerum_natura')
K('q-lucretius-mors','quote','republic',8,'Nīl igitur mors est ad nōs neque pertinet hīlum.','So death is nothing to us and does not matter one bit.',
 "In Book 3 Lucretius argues that the soul is made of atoms and scatters at death, so there is no one left to suffer. Epicurus had put it in Greek: 'where death is, I am not.' Lucretius wanted to free his readers from the fear of punishment after death. Hīlum, 'a whit, the least bit', survives in the word nihil (ne + hīlum).",
 "Epicurean epitaphs summed up the idea: nōn fuī, fuī, nōn sum, nōn cūrō, 'I was not, I was, I am not, I don't care'.",
 'Lucretius','Lucretius, De rerum natura','3.830','c. 55 BC',LL+'lucretius/lucretius3.shtml','verified',None,
 'Nīl|nihil|nothing|nom. sg. n.; igitur|igitur|therefore|adv.; mors|mors|death|nom. sg. f.; est|sum|is|3rd sg. pres.; ad|ad|to|prep. + acc.; nōs|nōs|us|acc. pl.; neque|neque|and not|conj.; pertinet|pertineō|it concerns, matters|3rd sg. pres.; hīlum|hīlum|a whit, the least bit|acc. sg. n.',
 ['sum','present_tense','personal_pronouns'],[],'epicurus','Epicureanism',WP+'Epicureanism')
K('q-cicero-vitam-regit','quote','republic',8,'Vītam regit fortūna, nōn sapientia.','Fortune rules life, not wisdom.',
 "Cicero (Tusculan Disputations 5, 45 BC) reports that Theophrastus, Aristotle's successor, was attacked by every school for praising this saying in his book Callisthenes. Cicero, following the Stoics, argues the opposite: virtue alone is enough for a happy life. Here the object comes first: vītam is accusative, fortūna and sapientia nominative.",
 "Theophrastus's book mourned his friend Callisthenes, Aristotle's nephew, who died in Alexander the Great's custody. That gave the saying a bitter sense.",
 'Theophrastus (as reported by Cicero)','Cicero, Tusculanae disputationes','5.25','45 BC',LL+'cicero/tusc5.shtml','traditional','Cicero says Theophrastus praised this saying in his lost book Callisthenes. The Latin is Cicero\'s rendering of a Greek original.',
 'Vītam|vīta|life|acc. sg. f.; regit|regō|rules|3rd sg. pres.; fortūna|fortūna|fortune, chance|nom. sg. f.; nōn|nōn|not|adv.; sapientia|sapientia|wisdom|nom. sg. f.',
 ['word_order','accusative','third_conjugation'],[],'theophrastus','Theophrastus',WP+'Theophrastus')
K('q-cicero-socrates-caelo','quote','republic',8,'Sōcratēs autem prīmus philosophiam dēvocāvit ē caelō et in urbibus conlocāvit.','But Socrates was the first to call philosophy down from the sky and settle it in cities.',
 "Before Socrates (469–399 BC), Greek thinkers mostly studied the stars and the stuff of the universe. Cicero says Socrates brought philosophy down to earth, to questions of how to live, what is good and bad, and how cities should be run. The picture of philosophy as a goddess called down from heaven became famous. Both verbs are perfect, describing what Socrates did once and for all.",
 "Socrates wrote nothing himself, and we know him mainly through Plato and Xenophon. Conlocāvit is the older spelling of collocāvit.",
 'Cicero','Cicero, Tusculanae disputationes','5.10','45 BC',LL+'cicero/tusc5.shtml','verified',None,
 'Sōcratēs|Sōcratēs|Socrates|nom. sg. m.; autem|autem|but, however|conj.; prīmus|prīmus|the first|nom. sg. m.; philosophiam|philosophia|philosophy|acc. sg. f.; dēvocāvit|dēvocō|called down|3rd sg. perf.; ē|ex|from|prep. + abl.; caelō|caelum|sky, heaven|abl. sg. n.; et|et|and|conj.; in|in|in|prep. + abl.; urbibus|urbs|cities|abl. pl. f.; conlocāvit|collocō|placed, settled|3rd sg. perf.',
 ['perfect_tense','prep_ablative'],[],'socrates','Socrates',WP+'Socrates')
K('q-cicero-commentatio','quote','republic',8,'Tōta enim philosophōrum vīta, ut ait idem, commentātiō mortis est.','For the whole life of philosophers, as the same man says, is a preparation for death.',
 "'The same man' is Socrates as Plato portrays him in the Phaedo, spending his last day discussing the immortality of the soul before drinking the hemlock. Cicero translates the idea for Romans in Tusculan Disputations 1 (45 BC): philosophy trains the mind to separate itself from the body, as death will. Philosophōrum and mortis are both genitives.",
 "Commentātiō means 'careful practice, rehearsal'. Montaigne later wrote an essay titled 'That to philosophise is to learn to die'.",
 'Cicero (after Plato\'s Socrates)','Cicero, Tusculanae disputationes','1.74','45 BC',LL+'cicero/tusc1.shtml','verified','Cicero is paraphrasing Plato, Phaedo 64a and 67d.',
 'Tōta|tōtus|whole|nom. sg. f.; enim|enim|for|conj.; philosophōrum|philosophus|of philosophers|gen. pl. m.; vīta|vīta|life|nom. sg. f.; ut|ut|as|conj.; ait|aiō|says|3rd sg. pres.; idem|īdem|the same man|nom. sg. m.; commentātiō|commentātiō|preparation, rehearsal|nom. sg. f.; mortis|mors|of death|gen. sg. f.; est|sum|is|3rd sg. pres.',
 ['genitive','adjective_agreement'],[],'socdeath','Phaedo',WP+'Phaedo')
K('q-cicero-non-nobis','quote','republic',8,'Nōn nōbīs sōlum nātī sumus.','We were not born for ourselves alone.',
 "Cicero wrote On Duties in 44 BC for his son Marcus, who was studying in Athens. He credits the thought to Plato: our country, our friends and all humankind have a claim on us. The book became one of the most read works of moral philosophy in medieval and Renaissance Europe. Nōbīs is a dative, 'for us'.",
 "Nātī sumus comes from nāscor, a deponent verb: passive in form, active in meaning.",
 'Cicero (after Plato)','Cicero, De officiis','1.22','44 BC',LL+'cicero/off1.shtml','verified','Cicero introduces it as a saying of Plato (Letter 9, 358a).',
 'Nōn|nōn|not|adv.; nōbīs|nōs|for us|dat. pl.; sōlum|sōlum|only|adv.; nātī sumus|nāscor|we were born|1st pl. perf.',
 ['personal_pronouns','dative'],['deponent'],'offms','De Officiis',WP+'De_Officiis')

# ---------------- UNIT 9: Christian Rome & the Fall ----------------
K('q-tertullian-semen','quote','late_antiquity',9,'Plūrēs efficimur, quotiēns metimur ā vōbīs: sēmen est sanguis Chrīstiānōrum.','We become more numerous every time we are mown down by you: the blood of Christians is seed.',
 "Tertullian of Carthage wrote his Apology around AD 197, defending Christians against Roman magistrates. He turns persecution into a farming image: you cut us down like a harvest, and the blood you spill is seed for new Christians. Both verbs before the colon are passive: efficimur, 'we are made', and metimur, 'we are reaped'.",
 "The saying is usually quoted as 'the blood of the martyrs is the seed of the Church', but Tertullian's own words are shorter. Plūrēs is a comparative, 'more (numerous)'.",
 'Tertullian','Tertullian, Apologeticum','50.13','c. AD 197',LL+'tertullian/tertullian.apol.shtml','verified',None,
 'Plūrēs|plūs|more (numerous)|nom. pl. m. (comp.); efficimur|efficiō|we are made, become|1st pl. pres. pass.; quotiēns|quotiēns|as often as|conj.; metimur|metō|we are mown down|1st pl. pres. pass.; ā|ab|by|prep. + abl.; vōbīs|vōs|you|abl. pl.; sēmen|sēmen|seed|nom. sg. n.; est|sum|is|3rd sg. pres.; sanguis|sanguis|blood|nom. sg. m.; Chrīstiānōrum|Chrīstiānus|of Christians|gen. pl. m.',
 ['passive_voice','genitive'],['comparative'],'martyrs','Tertullian',WP+'Tertullian',register='ecclesiastical')
K('q-tertullian-athenis','quote','late_antiquity',9,'Quid ergō Athēnīs et Hierosolymīs? Quid acadēmiae et ecclēsiae?','What then has Athens to do with Jerusalem? What has the Academy to do with the Church?',
 "In On the Prescription of Heretics (about AD 200), Tertullian blames Greek philosophy for Christian heresies and asks this famous question. Athens stands for philosophy, Jerusalem for faith, the Academy for Plato's school. The Latin is very compressed: 'what (is there) to Athens and to Jerusalem?', with datives and no verb. Ironically, Tertullian himself was a highly educated rhetorician.",
 "The question framed centuries of argument about faith and reason. Augustine, Boethius and Anselm all gave much more welcoming answers to pagan philosophy.",
 'Tertullian','Tertullian, De praescriptione haereticorum','7.9','c. AD 200',LL+'tertullian/tertullian.praescrip.shtml','verified',None,
 'Quid|quis|what|nom. sg. n. (interrog.); ergō|ergō|then, therefore|adv.; Athēnīs|Athēnae|to Athens|dat. pl. f.; et|et|and|conj.; Hierosolymīs|Hierosolyma|to Jerusalem|dat. pl. n.; acadēmiae|acadēmia|to the Academy|dat. sg. f.; ecclēsiae|ecclēsia|to the Church|dat. sg. f.',
 ['dative'],[],'tertullian','Tertullian',WP+'Tertullian',register='ecclesiastical')
K('q-perpetua-christiana','quote','late_antiquity',9,'Hilariānus: "Chrīstiāna es?" inquit. Et ego respondī: "Chrīstiāna sum."','Hilarianus said: "Are you a Christian?" And I answered: "I am a Christian."',
 "Vibia Perpetua, a young mother of good family, was arrested in Carthage in AD 203. Her prison diary survives inside the Passion of Perpetua and Felicity, which makes it one of the earliest texts by a Christian woman. Before the governor Hilarianus she refused to sacrifice for the emperors and gave this answer. She was killed in the arena with her slave Felicity and others.",
 "Chrīstiāna is feminine, agreeing with the speaker. Her father begged her to give in, and the governor had him beaten for interrupting.",
 'Perpetua','Passio Sanctarum Perpetuae et Felicitatis','6.4','AD 203',LL+'perp.html','verified',None,
 'Hilariānus|Hilariānus|Hilarianus (the governor)|nom. sg. m.; Chrīstiāna|Chrīstiānus|a Christian (woman)|nom. sg. f.; es|sum|you are|2nd sg. pres.; inquit|inquam|he said|3rd sg.; Et|et|and|conj.; ego|ego|I|nom. sg.; respondī|respondeō|I answered|1st sg. perf.; Chrīstiāna|Chrīstiānus|a Christian (woman)|nom. sg. f.; sum|sum|I am|1st sg. pres.',
 ['sum','perfect_tense'],[],'perpetua','Perpetua and Felicity',WP+'Perpetua_and_Felicity',register='ecclesiastical')
K('q-augustine-carthago','quote','late_antiquity',9,'Vēnī Carthāginem, et circumstrepēbat mē undique sartāgō flāgitiōsōrum amōrum.','I came to Carthage, and all around me hissed a frying pan of shameful loves.',
 "Augustine opens Book 3 of his Confessions (about AD 400) with his arrival in Carthage as a student of seventeen. The pun Carthāginem / sartāgō, 'Carthage' and 'frying pan', captures the sizzling city. The perfect vēnī marks a single event, the imperfect circumstrepēbat the noise that went on around him.",
 "In Carthage he read Cicero's lost Hortensius, which first turned him to philosophy. T. S. Eliot borrowed the line in The Waste Land: 'To Carthage then I came'.",
 'Augustine of Hippo','Augustine, Confessiones','3.1.1','c. AD 400',LL+'augustine/conf3.shtml','verified',None,
 'Vēnī|veniō|I came|1st sg. perf.; Carthāginem|Carthāgō|to Carthage|acc. sg. f.; et|et|and|conj.; circumstrepēbat|circumstrepō|was roaring around|3rd sg. impf.; mē|ego|me|acc. sg.; undique|undique|on all sides|adv.; sartāgō|sartāgō|frying pan|nom. sg. f.; flāgitiōsōrum|flāgitiōsus|shameful|gen. pl. m.; amōrum|amor|of loves|gen. pl. m.',
 ['perfect_tense','imperfect'],[],'augustine','Confessions (Augustine)',WP+'Confessions_(Augustine)',register='ecclesiastical')
K('q-boethius-infortunii','quote','late_antiquity',9,'In omnī adversitāte fortūnae īnfēlīcissimum est genus īnfortūniī fuisse fēlīcem.','In every adversity of fortune, the unhappiest kind of misfortune is to have been happy.',
 "Boethius, a Roman senator and scholar, wrote the Consolation of Philosophy around AD 524 in prison, awaiting execution by the Ostrogothic king Theoderic. Here he complains to Lady Philosophy that his memory of past success hurts most. She answers that fortune's gifts were never truly his. The book was translated by Alfred the Great, Chaucer and Elizabeth I.",
 "Īnfēlīcissimum is a superlative, and fuisse a perfect infinitive, 'to have been'. Dante borrowed the thought for Francesca in Inferno 5.",
 'Boethius','Boethius, De consolatione Philosophiae','2, prose 4.2','c. AD 524','https://www2.hs-augsburg.de/~harsch/Chronologia/Lspost06/Boethius/boe_con2.html','verified',None,
 'In|in|in|prep. + abl.; omnī|omnis|every|abl. sg. f.; adversitāte|adversitās|adversity|abl. sg. f.; fortūnae|fortūna|of fortune|gen. sg. f.; īnfēlīcissimum|īnfēlīx|unhappiest|nom. sg. n. (superl.); est|sum|is|3rd sg. pres.; genus|genus|kind|nom. sg. n.; īnfortūniī|īnfortūnium|of misfortune|gen. sg. n.; fuisse|sum|to have been|perf. inf.; fēlīcem|fēlīx|happy|acc. sg. m.',
 ['infinitive_as_subject','genitive'],['superlative','perfect_infinitive'],'boethius','The Consolation of Philosophy',WP+'The_Consolation_of_Philosophy')
K('q-vulg-verbum-caro','quote','late_antiquity',9,'Et Verbum carō factum est et habitāvit in nōbīs.','And the Word became flesh and dwelt among us.',
 "This verse from John's Gospel states the Christian belief in the incarnation, that God became human in Jesus. Jerome's Latin translation, the Vulgate (late 4th century AD), spread it across the Latin West, and worshippers traditionally knelt at these words. Factum est is a perfect passive of fīō/faciō: 'was made, became'. Carō, 'flesh', is a third-declension noun, genitive carnis.",
 "Carō, carnis gives English carnal, carnival and incarnation. Verbum translates the Greek Logos.",
 'Jerome (Vulgate)','Biblia Sacra Vulgata, Gospel of John','1:14','late 4th c. AD',LL+'bible/john.shtml','verified',None,
 'Et|et|and|conj.; Verbum|verbum|the Word|nom. sg. n.; carō|carō|flesh|nom. sg. f.; factum est|fīō|became, was made|3rd sg. perf. pass.; et|et|and|conj.; habitāvit|habitō|dwelt|3rd sg. perf.; in|in|among|prep. + abl.; nōbīs|nōs|us|abl. pl.',
 ['perfect_passive','perfect_tense'],[],'kells','Incarnation (Christianity)',WP+'Incarnation_(Christianity)',register='ecclesiastical')
K('q-vulg-exiit-edictum','quote','late_antiquity',9,'Exiit ēdictum ā Caesare Augustō ut dēscrīberētur ūniversus orbis.','A decree went out from Caesar Augustus that the whole world should be registered.',
 "Luke's Christmas story begins by fixing the birth of Jesus in Roman history: a census ordered by Augustus. Historians debate the date, since the census of Quirinius in Judaea that Luke mentions next took place in AD 6. The verse shows how early Christians set their story inside the Roman Empire. Exiit is perfect, 'went out'.",
 "Dēscrīberētur, 'should be registered', is an imperfect subjunctive. Bruegel painted the scene as a snowy Flemish village.",
 'Jerome (Vulgate)','Biblia Sacra Vulgata, Gospel of Luke','2:1','late 4th c. AD',LL+'bible/luke.shtml','verified',None,
 'Exiit|exeō|went out|3rd sg. perf.; ēdictum|ēdictum|decree|nom. sg. n.; ā|ab|from|prep. + abl.; Caesare|Caesar|Caesar|abl. sg. m.; Augustō|Augustus|Augustus|abl. sg. m.; ut|ut|that|conj.; dēscrīberētur|dēscrībō|should be registered|3rd sg. impf. subj. pass.; ūniversus|ūniversus|whole|nom. sg. m.; orbis|orbis|world|nom. sg. m.',
 ['perfect_tense','prep_ablative'],['subjunctive'],'census','Census of Quirinius',WP+'Census_of_Quirinius',register='ecclesiastical')
K('q-creed-pilato','quote','early_medieval',9,'Passus sub Pontiō Pīlātō, crucifīxus, mortuus, et sepultus.','He suffered under Pontius Pilate, was crucified, died, and was buried.',
 "This line of the Apostles' Creed has been recited by Western Christians for over a thousand years. Pilate, the Roman prefect of Judaea (AD 26–36), is the only person besides Jesus and Mary named in it, which ties the faith to a datable moment in Roman rule. The four past participles tell the story in a row. The creed grew out of an older baptismal creed used at Rome.",
 "The standard text is attested in the 8th century. Passus and mortuus come from deponent verbs (patior, morior), while crucifīxus and sepultus are true passives.",
 'The early Church (anonymous)',"Symbolum Apostolorum (Apostles' Creed)",'—','8th c. AD (textus receptus)',LL+'creeds.html','verified',None,
 'Passus|patior|having suffered|nom. sg. m. perf. part.; sub|sub|under|prep. + abl.; Pontiō|Pontius|Pontius|abl. sg. m.; Pīlātō|Pīlātus|Pilate|abl. sg. m.; crucifīxus|crucifīgō|crucified|nom. sg. m. perf. pass. part.; mortuus|morior|dead|nom. sg. m. perf. part.; et|et|and|conj.; sepultus|sepeliō|buried|nom. sg. m. perf. pass. part.',
 ['participle','perfect_passive'],['deponent'],'creed',"Apostles' Creed",WP+'Apostles%27_Creed',register='ecclesiastical')
K('q-tacitus-christus','quote','empire',9,'Auctor nōminis eius Chrīstus Tiberiō imperitante per prōcūrātōrem Pontium Pīlātum suppliciō adfectus erat.','Christus, the founder of that name, had been executed in the reign of Tiberius by the procurator Pontius Pilate.',
 "Tacitus (Annals 15.44, about AD 116) explains who the Christians were whom Nero blamed for the Great Fire of Rome in AD 64. Nero had them torn by dogs, crucified, or burned as torches at night. This is the earliest non-Christian Roman reference to Jesus's execution, written by a historian who despised the new 'superstition'. Adfectus erat is a pluperfect passive.",
 "Tiberiō imperitante is an ablative absolute, 'with Tiberius ruling'. Pilate was in fact a prefect. 'Procurator' is the title used in Tacitus's own time.",
 'Tacitus','Tacitus, Annales','15.44.3','c. AD 116',LL+'tacitus/tac.ann15.shtml','verified','The Latin Library text has the misprint Tibero for Tiberio.',
 'Auctor|auctor|founder|nom. sg. m.; nōminis|nōmen|of the name|gen. sg. n.; eius|is|that, its|gen. sg.; Chrīstus|Chrīstus|Christus|nom. sg. m.; Tiberiō|Tiberius|Tiberius|abl. sg. m.; imperitante|imperitō|ruling|abl. sg. pres. part.; per|per|by, through|prep. + acc.; prōcūrātōrem|prōcūrātor|procurator|acc. sg. m.; Pontium|Pontius|Pontius|acc. sg. m.; Pīlātum|Pīlātus|Pilate|acc. sg. m.; suppliciō|supplicium|with punishment, execution|abl. sg. n.; adfectus erat|adficiō|had been afflicted|3rd sg. plupf. pass.',
 ['perfect_passive','present_participle'],['ablative_absolute'],'torches','Tacitus on Jesus',WP+'Tacitus_on_Jesus')
K('q-rutilius-patriam','quote','late_antiquity',9,'Fēcistī patriam dīversīs gentibus ūnam.','You have made one homeland for different peoples.',
 "Rutilius Namatianus, a pagan Gaul who had been prefect of Rome, left the city for home in AD 417, seven years after the Goths sacked it. His poem On His Return opens with a farewell hymn to Rome, addressed as a goddess. The next lines add: 'you made a city of what had been a world'. Fēcistī is a second-person perfect, spoken to Rome itself.",
 "The pun urbem / orbis ('city' / 'world') was a favourite of Roman poets. Rutilius writes as if Rome's empire were still whole.",
 'Rutilius Namatianus','Rutilius Namatianus, De reditu suo','1.63','AD 417',LL+'rutilius.html','verified',None,
 'Fēcistī|faciō|you have made|2nd sg. perf.; patriam|patria|homeland|acc. sg. f.; dīversīs|dīversus|different|dat. pl. f.; gentibus|gēns|for peoples|dat. pl. f.; ūnam|ūnus|one|acc. sg. f.',
 ['perfect_tense','dative'],[],'dearoma','Rutilius Claudius Namatianus',WP+'Rutilius_Claudius_Namatianus')
K('q-pliny-carmen-christo','quote','empire',9,'Carmen Chrīstō quasi deō dīcere sēcum invicem','to sing a hymn among themselves to Christ as if to a god',
 "Around AD 112, Pliny the Younger, governor of Bithynia, wrote to the emperor Trajan asking how to deal with Christians. Questioning people who had left the group, he learned that they met before dawn on a fixed day to sing to Christ and swear to do no crime. Pliny found nothing worse than 'a depraved, excessive superstition'. The infinitive dīcere depends on 'they declared', so it is part of an indirect statement.",
 "Trajan replied that Christians should not be hunted out, and anonymous accusations should be ignored. Those who were accused and refused to sacrifice were to be punished.",
 'Pliny the Younger','Pliny the Younger, Epistulae','10.96.7','c. AD 112',LL+'pliny.ep10.html','verified','Source reads carmenque … dicere, depending on adfirmabant. The card drops -que.',
 'Carmen|carmen|hymn, song|acc. sg. n.; Chrīstō|Chrīstus|to Christ|dat. sg. m.; quasi|quasi|as if|adv.; deō|deus|to a god|dat. sg. m.; dīcere|dīcō|to sing, say|pres. inf.; sēcum|sē + cum|with themselves|pron. + prep.; invicem|invicem|in turn, alternately|adv.',
 ['infinitive','indirect_statement','dative'],[],'pliny','Pliny the Younger on Christians',WP+'Pliny_the_Younger_on_Christians')

# ---------------- UNIT 10: Monks & Manuscripts ----------------
K('q-jerome-capitur-urbs','quote','late_antiquity',10,'Capitur urbs quae tōtum cēpit orbem.','The city is taken which took the whole world.',
 "In AD 412 Jerome, in Bethlehem, wrote a memorial to his friend Marcella, who died after the Goths sacked Rome in August 410. He describes how the news reached him while he was dictating: his voice stuck and sobs broke his words. The sentence sets a passive present, capitur, against an active perfect, cēpit, from the same verb. Quae introduces a relative clause describing urbs.",
 "Urbs and orbis, 'city' and 'world', make a pun Romans loved. Augustine began his City of God partly to answer pagans who blamed the sack on Christianity.",
 'Jerome','Jerome, Epistulae','127.12','AD 412','https://fgh.perseids.org/read/latinLit/stoa0162/stoa004/perseus-lat2/125.17-127.14','verified',None,
 'Capitur|capiō|is taken|3rd sg. pres. pass.; urbs|urbs|city|nom. sg. f.; quae|quī|which|nom. sg. f.; tōtum|tōtus|whole|acc. sg. m.; cēpit|capiō|took|3rd sg. perf.; orbem|orbis|world|acc. sg. m.',
 ['relative_clause','passive_voice'],[],'sack','Sack of Rome (410)',WP+'Sack_of_Rome_(410)',register='ecclesiastical')
K('q-bede-britannia','quote','early_medieval',10,'Brittania Ōceanī īnsula, cui quondam Albiōn nōmen fuit','Britain, an island of the Ocean, which once had the name Albion',
 "Bede finished his Ecclesiastical History of the English People at Jarrow in AD 731, and it opens with these words. He borrowed his geography from Roman writers such as Pliny and Orosius, placing Britain on the edge of the world-ocean. Cui ... nōmen fuit is a relative clause with a dative of possession: 'to which the name was'.",
 "Albion is probably a Celtic name, perhaps linked to the white cliffs of Dover. Bede also popularised dating years AD (annō Dominī).",
 'Bede','Bede, Historia ecclesiastica gentis Anglorum','1.1','AD 731',LL+'bede/bede1.shtml','verified','Bede\'s spelling Brittania is kept. Its vowel quantities are left unmarked.',
 'Brittania|Britannia|Britain|nom. sg. f.; Ōceanī|Ōceanus|of the Ocean|gen. sg. m.; īnsula|īnsula|island|nom. sg. f.; cui|quī|to which|dat. sg. f.; quondam|quondam|once, formerly|adv.; Albiōn|Albiōn|Albion|nom. sg. f.; nōmen|nōmen|name|nom. sg. n.; fuit|sum|was|3rd sg. perf.',
 ['relative_clause','dative'],[],'bedems','Ecclesiastical History of the English People',WP+'Ecclesiastical_History_of_the_English_People',register='ecclesiastical')
K('q-benedict-mortem','quote','early_medieval',10,'Mortem cotīdiē ante oculōs suspectam habēre.','To keep death daily before one\'s eyes as something to be expected.',
 "Chapter 4 of the Rule of Benedict (about AD 530) lists 'the tools of good works', each one a single infinitive phrase. This one asks the monk to remember death every day, so as to live each day well. The Rule became the standard guide for monasteries across medieval Europe. Every item in the list depends on an unspoken 'one must'.",
 "Suspectam here means 'looked out for, expected' (from suspiciō, 'look up at'). The oldest surviving copy of the Rule, Oxford MS Hatton 48, was written in England around 700.",
 'Benedict of Nursia','Regula Sancti Benedicti','4.47','c. AD 530',LL+'benedict.html','verified',None,
 'Mortem|mors|death|acc. sg. f.; cotīdiē|cotīdiē|daily|adv.; ante|ante|before|prep. + acc.; oculōs|oculus|eyes|acc. pl. m.; suspectam|suspiciō|expected, watched for|acc. sg. f. perf. pass. part.; habēre|habeō|to have, keep|pres. inf.',
 ['infinitive','participle'],[],'benedict','Rule of Saint Benedict',WP+'Rule_of_Saint_Benedict',register='ecclesiastical')
K('q-benedict-genera','quote','early_medieval',10,'Monachōrum quattuor esse genera manifestum est.','It is clear that there are four kinds of monks.',
 "The first chapter of Benedict's Rule sorts monks into four types. Cenobites live in a monastery under a rule and an abbot, and hermits live alone after long training, while sarabaites live with no rule and gyrovagues wander from house to house. Benedict writes for the first kind and scorns the last two. Esse is an infinitive in an indirect statement that depends on manifestum est.",
 "Monachus comes from Greek monos, 'alone', and gives English monk. Coenobium means 'common life'.",
 'Benedict of Nursia','Regula Sancti Benedicti','1.1','c. AD 530',LL+'benedict.html','verified',None,
 'Monachōrum|monachus|of monks|gen. pl. m.; quattuor|quattuor|four|indecl.; esse|sum|to be|pres. inf.; genera|genus|kinds|acc. pl. n.; manifestum|manifestus|clear|nom. sg. n.; est|sum|is|3rd sg. pres.',
 ['indirect_statement','numerals','genitive'],[],'monk','Rule of Saint Benedict',WP+'Rule_of_Saint_Benedict',register='ecclesiastical')
K('q-isidore-litterae','quote','early_medieval',10,'Litterae autem sunt indicēs rērum, signa verbōrum, quibus tanta vīs est, ut nōbīs dicta absentium sine vōce loquantur.','Letters are tokens of things, signs of words, and they have such power that they speak to us without a voice the sayings of people who are absent.',
 "Isidore, bishop of Seville (died AD 636), packed the learning of the ancient world into his Etymologies, an encyclopedia in twenty books. It was one of the most copied books of the Middle Ages, and it begins with grammar and the alphabet. This definition explains why monks copied books: writing lets the absent and the dead go on speaking. Quibus begins a relative clause, 'to which there is such power'.",
 "Loquantur is a subjunctive in a result clause, from the deponent loquor. Isidore's simple T-O world map comes from the same work.",
 'Isidore of Seville','Isidore, Etymologiae','1.3.1','c. AD 625',LL+'isidore/1.shtml','verified',None,
 'Litterae|littera|letters|nom. pl. f.; autem|autem|moreover|conj.; sunt|sum|are|3rd pl. pres.; indicēs|index|indicators, tokens|nom. pl. m.; rērum|rēs|of things|gen. pl. f.; signa|signum|signs|nom. pl. n.; verbōrum|verbum|of words|gen. pl. n.; quibus|quī|to which|dat. pl. f.; tanta|tantus|such great|nom. sg. f.; vīs|vīs|power|nom. sg. f.; est|sum|is|3rd sg. pres.; ut|ut|that|conj.; nōbīs|nōs|to us|dat. pl.; dicta|dictum|sayings|acc. pl. n.; absentium|absēns|of absent people|gen. pl.; sine|sine|without|prep. + abl.; vōce|vōx|voice|abl. sg. f.; loquantur|loquor|they speak|3rd pl. pres. subj.',
 ['relative_clause','genitive'],['subjunctive','deponent'],'tomap','Etymologiae',WP+'Etymologiae',register='ecclesiastical')
K('q-alcuin-vox-populi','quote','early_medieval',10,'Nec audiendī quī solent dīcere: "Vōx populī, vōx Deī."','Nor should we listen to those who keep saying: "The voice of the people is the voice of God."',
 "Alcuin of York, Charlemagne's leading scholar, wrote this advice to the emperor around AD 798. This is the earliest known appearance of the famous slogan, and Alcuin quotes it in order to reject it. He adds that the rowdiness of the crowd is always close to madness. Quī solent is a relative clause, 'who are accustomed'.",
 "Audiendī is a gerundive, 'are to be listened to'. The slogan was later used to support popular government.",
 'Alcuin of York','Alcuin, Epistolae (admonitio ad Carolum)','§9','c. AD 798','https://la.wikisource.org/wiki/Epistolae_(Alcuinus)','verified','The passage comes from a capitulary of advice sent to Charlemagne, printed among Alcuin\'s letters.',
 'Nec|nec|nor|conj.; audiendī|audiō|to be listened to|nom. pl. m. gerundive; quī|quī|who|nom. pl. m.; solent|soleō|are accustomed|3rd pl. pres.; dīcere|dīcō|to say|pres. inf.; Vōx|vōx|voice|nom. sg. f.; populī|populus|of the people|gen. sg. m.; vōx|vōx|voice|nom. sg. f.; Deī|deus|of God|gen. sg. m.',
 ['relative_clause','genitive'],['gerundive'],'alcuin','Vox populi',WP+'Vox_populi',register='ecclesiastical')
K('q-anselm-credo','quote','high_medieval',10,'Neque enim quaerō intelligere ut crēdam, sed crēdō ut intelligam.','For I do not seek to understand so that I may believe, but I believe so that I may understand.',
 "Anselm, a monk of Bec in Normandy and later Archbishop of Canterbury, wrote the Proslogion around 1077–78. In chapter 2 he gives his famous 'ontological argument' for God's existence. This line from chapter 1 sums up his approach: faith comes first, then reason explores it. It gives a much warmer answer than Tertullian's question about Athens and Jerusalem.",
 "Crēdam and intelligam are subjunctives of purpose after ut. Anselm's spelling intelligere is the medieval form of intellegere.",
 'Anselm of Canterbury','Anselm, Proslogion','1','c. 1077–78',LL+'anselmproslogion.html','verified',None,
 'Neque|neque|and not|conj.; enim|enim|for|conj.; quaerō|quaerō|I seek|1st sg. pres.; intelligere|intellegō|to understand|pres. inf.; ut|ut|so that|conj.; crēdam|crēdō|I may believe|1st sg. pres. subj.; sed|sed|but|conj.; crēdō|crēdō|I believe|1st sg. pres.; ut|ut|so that|conj.; intelligam|intellegō|I may understand|1st sg. pres. subj.',
 ['infinitive','first_person'],['subjunctive'],'anselm','Anselm of Canterbury',WP+'Anselm_of_Canterbury',register='ecclesiastical')
K('q-seneca-pauper','quote','empire',10,'Nōn quī parum habet, sed quī plūs cupit, pauper est.','The poor man is not the one who has too little, but the one who wants more.',
 "In his second letter to Lucilius, Seneca quotes Epicurus, 'cheerful poverty is an honourable thing', and then adds this correction of his own. Wealth, he says, is not measured by what you own but by what you need. The relative clauses act as the subjects of est: 'he who has little' and 'he who wants more'. Medieval monks copied Seneca's letters eagerly, and the Rule of Benedict shares this distrust of possessions.",
 "Seneca often quoted Epicurus, a rival school, to show that a good thought belongs to everyone. A forged medieval correspondence even made Seneca a friend of Saint Paul.",
 'Lucius Annaeus Seneca','Seneca, Epistulae morales','2.6','c. AD 64',LL+'sen/seneca.ep1.shtml','verified',None,
 'Nōn|nōn|not|adv.; quī|quī|he who|nom. sg. m.; parum|parum|too little|adv. / indecl.; habet|habeō|has|3rd sg. pres.; sed|sed|but|conj.; quī|quī|he who|nom. sg. m.; plūs|plūs|more|acc. sg. n.; cupit|cupiō|wants|3rd sg. pres.; pauper|pauper|poor|nom. sg. m.; est|sum|is|3rd sg. pres.',
 ['relative_clause'],[],'senecadying','Seneca the Younger',WP+'Seneca_the_Younger')
K('q-seneca-philologia','quote','empire',10,'Quae philosophia fuit, facta philologia est.','What used to be philosophy has become philology.',
 "Seneca (Letter 108) complains that students come to teachers to sharpen their wits, not to improve their souls. A philosopher reading Virgil looks for moral lessons, while a grammarian counts rare words and checks dates. Medieval schools inherited the same tension between studying texts and living by them. Quae begins a relative clause, and facta est is a perfect passive.",
 "Philologia meant 'love of words', especially the scholarly study of texts and language. Servius's Virgil commentary, studied all through the Middle Ages, is philology of exactly this kind.",
 'Lucius Annaeus Seneca','Seneca, Epistulae morales','108.23','c. AD 64',LL+'sen/seneca.ep17-18.shtml','verified',None,
 'Quae|quī|what, which|nom. sg. f.; philosophia|philosophia|philosophy|nom. sg. f.; fuit|sum|was|3rd sg. perf.; facta est|fīō|has become|3rd sg. perf. pass.; philologia|philologia|philology, the study of words|nom. sg. f.',
 ['relative_clause','perfect_passive'],[],'servius','Philology',WP+'Philology')
K('q-cicero-senex','quote','republic',10,'Nēmō enim est tam senex quī sē annum nōn putet posse vīvere.','For no one is so old that he does not think he can live another year.',
 "In On Old Age (44 BC), Cicero has the elder Cato, then 84, explain why old men still plant trees and make plans. Hope of one more year, he says, keeps everyone working. Medieval monasteries copied the dialogue widely as a guide to growing old well. Posse vīvere is an infinitive phrase in indirect statement after putet.",
 "Quī ... putet is a relative clause of result with the subjunctive. Cato quotes the line of the poet Caecilius: 'he plants trees to benefit another generation'.",
 'Cicero (speech of Cato)','Cicero, De senectute','24','44 BC',LL+'cicero/senectute.shtml','verified','Spoken by Cato the Elder in the dialogue.',
 'Nēmō|nēmō|no one|nom. sg.; enim|enim|for|conj.; est|sum|is|3rd sg. pres.; tam|tam|so|adv.; senex|senex|old (man)|nom. sg. m.; quī|quī|that he|nom. sg. m.; sē|sē|himself|acc. sg.; annum|annus|a year|acc. sg. m.; nōn|nōn|not|adv.; putet|putō|thinks|3rd sg. pres. subj.; posse|possum|to be able|pres. inf.; vīvere|vīvō|to live|pres. inf.',
 ['relative_clause','possum_infinitive','indirect_statement'],['subjunctive'],'oldman','Cato Maior de Senectute',WP+'Cato_Maior_de_Senectute')
K('q-horace-caelum','quote','empire',10,'Caelum, nōn animum mūtant, quī trāns mare currunt.','Those who hurry across the sea change their sky, not their mind.',
 "Horace writes to his friend Bullatius, who is touring the Greek islands (Epistles 1.11, about 20 BC): travel will not cure restlessness, only reason will. The saying was a favourite with medieval monks, whose vow of stability bound them to one monastery for life. Quī trāns mare currunt is a relative clause that works as the subject: 'those who run across the sea'.",
 "Seneca makes the same point in Letter 28: 'you need a change of soul, not of climate'.",
 'Horace','Horace, Epistulae','1.11.27','c. 20 BC',LL+'horace/epist1.shtml','verified',None,
 'Caelum|caelum|sky, climate|acc. sg. n.; nōn|nōn|not|adv.; animum|animus|mind|acc. sg. m.; mūtant|mūtō|they change|3rd pl. pres.; quī|quī|those who|nom. pl. m.; trāns|trāns|across|prep. + acc.; mare|mare|sea|acc. sg. n.; currunt|currō|they run|3rd pl. pres.',
 ['relative_clause','third_person_plural'],[],'ship','Epistles (Horace)',WP+'Epistles_(Horace)')
