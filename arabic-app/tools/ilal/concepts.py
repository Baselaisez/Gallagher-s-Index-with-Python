"""(v348-F) the join's key: a topic of the app (a ledger entry, a grammar note) ↔ the commentaries' sections that treat it.
`ar` is matched on the entry's / note title's Arabic (normalised by common.norm), `lat` on a grammar note's id, `sec` per book on
the section's «bāb | title» (normalised). Order matters: the more specific topics come first, and an entry takes at most two.
`role` is the Illa346 role id the topic answers (for the reason chain's «family → state» step)."""

C = []


def c(cid, ar=None, lat=None, role=None, **sec):
    C.append({"id": cid, "ar": ar, "lat": lat, "role": role, "sec": sec})


# ── naḥw
c("naib-fail", ar=r"نايب (عن )?الفاعل|ما لم يسم فاعله|المجهول", lat=r"naib|majhul", role="naibFail",
  ibn_malik=r"النايب عن الفاعل", shaykhzade=r"النايب عن الفاعل")
c("fail", ar=r"(^|[^ا-ي])الفاعل|فاعله", lat=r"(^|-)fail(-|$)", role="fail", ibn_malik=r"باب الفاعل")
c("maful-mutlaq", ar=r"المفعول المطلق|مفعول مطلق", lat=r"mutlaq", role="mafulMutlaq", ibn_malik=r"المفعول المطلق")
c("maful-lah", ar=r"المفعول له|لاجله", lat=r"maful-lah|maful-fih-wal-maful-lah", role="mafulLah", ibn_malik=r"المفعول له")
c("maful-fih", ar=r"المفعول فيه|الظرف|ظرف", lat=r"maful-fih|zarf|zuruf", role="mafulFih", ibn_malik=r"المفعول فيه")
c("maful-maah", ar=r"المفعول معه", lat=r"maah", role="mafulMaah", ibn_malik=r"المفعول معه")
c("maful-bih", ar=r"المفعول به|مفعولا به|مفعولين|المتعدي|اللازم", lat=r"maful-bih|lazim|mutaaddi", role="mafulBih",
  ibn_malik=r"تعدي الفعل ولزومه|الافعال التي تنصب المبتدا|اعلم وما جري", shaykhzade=r"الواقعه مفعولا به")
c("tanazu", ar=r"التنازع", lat=r"tanazu", ibn_malik=r"التنازع")
c("ishtighal", ar=r"الاشتغال|اشتغال", lat=r"ishtighal", ibn_malik=r"اشتغال")
c("kana", ar=r"كان واخوات|الافعال الناقصه|اسم كان|خبر كان|الناقصه", lat=r"kana|naqis", role="ismKana",
  ibn_malik=r"الافعال الرافعه الاسم الناصبه الخبر")
c("ma-laysa", ar=r"المشبهه بليس|المشبهات بليس|عمل ليس", lat=r"ma-la-mushabbaha|laysa", role="ismMa", ibn_malik=r"المشبهات ب ليس")
c("muqaraba", ar=r"المقاربه|عسي|كاد", lat=r"muqaraba", ibn_malik=r"افعال المقاربه")
c("la-jins", ar=r"لا التي لنفي الجنس|نفي الجنس|اسم لا", lat=r"la-nafiya|nafy-al-jins", role="ismLa", ibn_malik=r"لا العامله عمل ان")
c("inna", ar=r"ان واخوات|المشبهه بالفعل|اسم ان|خبر ان", lat=r"inna|mushabbaha-bil-fil", role="ismInna",
  ibn_malik=r"الحروف الناصبه الاسم الرافعه الخبر")
c("zann", ar=r"ظن واخوات|افعال القلوب|التصيير", lat=r"zann|qulub|tasyir", ibn_malik=r"الافعال التي تنصب المبتدا|اجراء القول|اعلم وما جري")
c("mubtada", ar=r"المبتدا|مبتدا|الابتداء", lat=r"mubtada", role="mubtada", ibn_malik=r"باب الابتداء",
  shaykhzade=r"الجمله الابتداييه")
c("khabar", ar=r"الخبر|خبر المبتدا|خبرا", lat=r"khabar", role="khabar", ibn_malik=r"باب الابتداء", shaykhzade=r"الواقعه خبرا")
c("istithna", ar=r"الاستثناء|المستثني|(^|\s)الا($|\s)", lat=r"istithna|mustathna", role="mustathna", ibn_malik=r"الاستثناء")
c("hal", ar=r"(^|[^ا-ي])الحال($|[^ا-ي])|حالا|حاليه", lat=r"(^|-)hal(-|$)", role="hal", ibn_malik=r"باب الحال",
  shaykhzade=r"الواقعه حالا|الجمله الحاليه")
c("tamyiz", ar=r"التمييز|تمييز", lat=r"tamyiz|mubham", role="tamyiz", ibn_malik=r"باب التمييز|تمييز العدد")
c("idafa", ar=r"الاضافه|المضاف|مضافا", lat=r"idafa|mudaf", role="mudafIlayh", ibn_malik=r"باب الاضافه",
  shaykhzade=r"مضافا اليه|المخفوض بالاضافه")
c("jarr", ar=r"حروف الجر|حرف جر|الجار والمجرور|المجرور|الجر", lat=r"jarr|majrur", role="majrur", ibn_malik=r"باب حروف الجر",
  shaykhzade=r"الجار والمجرور")
c("qasam", ar=r"القسم", lat=r"qasam", ibn_malik=r"باب القسم", shaykhzade=r"جواب القسم")
c("masdar-amal", ar=r"اعمال المصدر|عمل المصدر", lat=r"masdar-fil-kafiya|amal-al-masdar", ibn_malik=r"اعمال المصدر")
c("ism-fail-amal", ar=r"اسم الفاعل|اسم المفعول", lat=r"ism-al-fail|ism-fail", ibn_malik=r"اعمال اسم الفاعل")
c("sifa-mushabbaha", ar=r"الصفه المشبهه", lat=r"sifa-mushabbaha|mushabbaha-vezin", ibn_malik=r"الصفه المشبهه", radi=r"الصفه المشبهه")
c("tajjub", ar=r"التعجب", lat=r"tajjub|taajjub", ibn_malik=r"التعجب")
c("madh", ar=r"نعم وبيس|المدح والذم", lat=r"madh|nima", ibn_malik=r"نعم وبيس")
c("tafdil", ar=r"التفضيل", lat=r"tafdil", ibn_malik=r"افعل التفضيل")
c("naat", ar=r"النعت|الصفه|نعت", lat=r"naat|sifa(?!-mushabbaha)", role="naat", ibn_malik=r"باب النعت|باب التوابع",
  shaykhzade=r"التابعه لمفرد")
c("tawkid", ar=r"التوكيد|التاكيد", lat=r"tawkid|takid", role="tawkid", ibn_malik=r"باب التوكيد")
c("badal", ar=r"البدل|بدل", lat=r"badal", role="badal", ibn_malik=r"باب البدل")
c("atf", ar=r"العطف|معطوف|عاطفه", lat=r"atf", role="atf", ibn_malik=r"باب العطف|عطف النسق", shaykhzade=r"الواو|حتي العاطفه")
c("nida", ar=r"النداء|المنادي|الندبه|الترخيم|الاستغاثه", lat=r"nida|munada|nudba|tarkhim", role="munada",
  ibn_malik=r"باب النداء|الاستغاثه|الندبه|الترخيم|الاختصاص|التحذير")
c("asma-afal", ar=r"اسماء الافعال|اسم فعل", lat=r"asma-al-afal|ism-fil", ibn_malik=r"اسماء الافعال")
c("nun-tawkid", ar=r"نون التوكيد|نوني التوكيد|التنوين", lat=r"nun-al-tawkid|tanwin", ibn_malik=r"نوني التوكيد")
c("mamnu", ar=r"لا ينصرف|الممنوع من الصرف|غير المنصرف|المنصرف", lat=r"munsarif|mamnu|sarf-wa", ibn_malik=r"ما ينصرف وما لا ينصرف")
c("jazm", ar=r"الجزم|جازم|مجزوم|الشرط|الجزاء", lat=r"jazm|majzum|shart", ibn_malik=r"باب عوامل الجزم|فصل في لما",
  shaykhzade=r"جوابا لشرط|لم حرف جزم")
c("law", ar=r"(^|[^ا-ي])لو($|[^ا-ي])|لولا|لوما", lat=r"(^|-)law", ibn_malik=r"فصل في لو|لولا", shaykhzade=r"^لو$|^لولا$")
c("irab-fil", ar=r"المضارع|النواصب|ينصب المضارع|اعراب الفعل", lat=r"mudari|nawasib|nasb-al-mudari", ibn_malik=r"باب اعراب الفعل",
  shaykhzade=r"ان المفتوحه حرف مصدري")
c("signs-dual-plural", ar=r"المثني|جمع المذكر|الجمع السالم|جمع المونث|بالالف والتاء|علي حده", lat=r"muthanna|jam-al-salim|salim|dual",
  ibn_malik=r"اعراب المثني|المجموع بالالف والتاء")
c("five-verbs", ar=r"الافعال الخمسه|الامثله الخمسه", lat=r"afal-khamsa", ibn_malik=r"اعراب ما اتصل به من الفعل")
c("five-nouns", ar=r"الاسماء السته|الاسماء الخمسه", lat=r"asma-sitta|asma-khamsa", ibn_malik=r"باب الاعراب والبناء")
c("muqaddar", ar=r"مقدر|المقصور|المنقوص|المعتل الاخر|التعذر|الثقل", lat=r"maqsur|manqus|muqaddar|taqdir", ibn_malik=r"اعراب المعتل")
c("irab-bina", ar=r"الاعراب|المعرب|المبني|البناء|مبني", lat=r"irab|murab|mabni", ibn_malik=r"باب الاعراب والبناء")
c("mudmar", ar=r"الضمير|المضمر|ضمير", lat=r"damir|mudmar|bariz", ibn_malik=r"فصل في المضمر|ضمير الشان|الضمير المسمي فصلا")
c("mawsul", ar=r"الموصول|صله", lat=r"mawsul", ibn_malik=r"فصل الموصول", shaykhzade=r"صله الموصول|اسما موصولا")
c("ishara", ar=r"الاشاره", lat=r"ishara|isharat", ibn_malik=r"اسماء الاشاره", shaykhzade=r"اسم اشاره")
c("alam", ar=r"العلم($|[^ا-ي])", lat=r"(^|-)alam(-|$)", ibn_malik=r"فصل العلم")
c("muarraf", ar=r"المعرفه|النكره|المعرف", lat=r"marifa|nakira|muarraf", ibn_malik=r"باب النكره والمعرفه|المعرف بالاداه")
c("adad", ar=r"العدد|كم الخبريه|كم الاستفهاميه", lat=r"adad|kam", ibn_malik=r"باب العدد|كم وكاين", shaykhzade=r"كم عند")
c("hikaya", ar=r"الحكايه|محكي", lat=r"hikaya", ibn_malik=r"باب الحكايه")
c("tanith", ar=r"المونث|التانيث", lat=r"muannath|tanith", ibn_malik=r"التذكير والتانيث|الف التانيث")
c("jumla", ar=r"الجمله|جمله|الجمل", lat=r"jumla|jumal|madi-wal-jumla", shaykhzade=r"الباب الاول في الجمله")
c("zaid", ar=r"الزايد|زايده|صله وتوكيد", lat=r"zaid|zaida", shaykhzade=r"الزايد|الحرف الزايد")
# ── ṣarf
c("taksir", ar=r"جمع التكسير|التكسير|جموع", lat=r"taksir|jumu", ibn_malik=r"جمع التكسير", radi=r"الاسم المجموع|جمع|تكسير")
c("tathniya", ar=r"التثنيه|تثنيه", lat=r"tathniya", ibn_malik=r"كيفيه التثنيه")
c("tasghir", ar=r"التصغير|المصغر", lat=r"tasghir", ibn_malik=r"التصغير", radi=r"المصغر|التصغير")
c("nasab", ar=r"النسب|المنسوب", lat=r"nisba|nasab", ibn_malik=r"باب النسب", radi=r"المنسوب")
c("imala", ar=r"الاماله", lat=r"imala", ibn_malik=r"باب الاماله", radi=r"الاماله")
c("waqf", ar=r"الوقف", lat=r"waqf", ibn_malik=r"باب الوقف", radi=r"^الوقف")
c("sakinayn", ar=r"التقاء الساكنين|الساكنين", lat=r"sakinayn", ibn_malik=r"التقاء الساكنين", radi=r"التقاء الساكنين")
c("zawaid", ar=r"حروف الزياده|الزوايد|همزه الوصل|المزيد", lat=r"ziyade|mazid|zawaid|wasl", ibn_malik=r"همزه الوصل",
  radi=r"حروف الزياده|الزايد|يضعف")
c("hamza", ar=r"الهمزه|مهموز|المهموز|الهمز", lat=r"hamz|mahmuz", ibn_malik=r"الهمزه المفرده", radi=r"الهمز|ابدال الهمزه")
c("idgham", ar=r"الادغام|ادغام|المضاعف|مضاعف", lat=r"idgham|mudaaf|muda-af", ibn_malik=r"الادغام", radi=r"ادغام|مخارج|صفات الحروف")
c("ilal", ar=r"الاعلال|اعلال|الاجوف|اجوف|الناقص|المثال|المعتل|اللفيف|قلب الواو|قلب الياء|قلبت|ابدال|الابدال",
  lat=r"ilal|ajwaf|naqis|mithal|mutall|muatal|lafif|ibdal", ibn_malik=r"باب الابدال|نوادر الاعلال",
  radi=r"الاعلال|اعلال|قلب|تصحيح العين|ما لا يعل|الواو المكسوره|ابدال|حروف الابدال")
c("hadhf", ar=r"الحذف|حذف", lat=r"hadhf", ibn_malik=r"فصل في الحذف", radi=r"^الحذف|حذف الواو")
c("abniya", ar=r"الميزان|ابنيه|بناء|الموزون|المجرد|الرباعي|الخماسي|الثلاثي", lat=r"mizan|abniya|bina|sahih",
  radi=r"الميزان|ابنيه|القلب المكاني|علامات القلب|الصحيح والمعتل|حد التصريف|انواع الابنيه|احوال الابنيه|رد بعض", ibn_malik=r"بناء مثال")
c("maani-abwab", ar=r"معاني|للتعديه|للمطاوعه|للمشاركه|للطلب", lat=r"maani|bablar|meanings", radi=r"معاني")
c("mudari-abwab", ar=r"المضارع|يفعل", lat=r"mudari-abwab|bab-", radi=r"الفعل المضارع وابوابه")
c("masdar", ar=r"المصدر|مصادر|مصدر", lat=r"masdar", ibn_malik=r"مصادر الفعل|تصريف الفعل غير الثلاثي", radi=r"المصدر|اسم المره")
c("mushtaqqat", ar=r"اسم الزمان|اسم المكان|اسم الاله|الاله|المشتقات|اسم المره", lat=r"ism-al-ala|zaman|makan|mushtaq|ishtiqaq",
  radi=r"المشتقات|اسماء الزمان|اسم الاله", ibn_malik=r"تصريف الافعال والاسماء المشتقه")
c("maqsur-mamdud", ar=r"المقصور والممدود|الممدود", lat=r"mamdud", ibn_malik=r"باب المقصور والممدود", radi=r"المقصور والممدود")
c("khatt", ar=r"الخط|الكتابه|الرسم", lat=r"khatt|imla", radi=r"^الخط")
