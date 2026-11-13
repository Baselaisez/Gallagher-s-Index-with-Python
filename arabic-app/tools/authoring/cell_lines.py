"""cell_lines.py — the iʿrāb of a RECITED paradigm cell, by its place in the paradigm (wave 165).

A ṣarf matn recites whole paradigms («نَصَرَ نَصَرَا نَصَرُوا …»، «لَمْ يَنْصُرْ لَمْ يَنْصُرَا …»، «اُنْصُرَنَّ اُنْصُرَانِّ …»). The sentence
engines read syntax, and a recited row has none: each word is a cell quoted for its own sake. What the cell IS, however, is
exact — the stored paradigm names it — and the classical iʿrāb of each of the fourteen persons is a finite table. This
module is that table: find the cell (tense, person, mood) in the verb's stored paradigm, keep the row's order where one form
serves two persons, and return the line in three languages. Nothing is guessed: a form the paradigm does not hold gets no
line from here.

Person order of every list (the corpus's own): 0 هُوَ 1 هُمَا 2 هُمْ 3 هِيَ 4 هُمَا(ث) 5 هُنَّ 6 أَنْتَ 7 أَنْتُمَا 8 أَنْتُمْ 9 أَنْتِ 10 أَنْتُمَا(ث) 11 أَنْتُنَّ 12 أَنَا 13 نَحْنُ;
the imperative: 0 أَنْتَ 1 أَنْتُمَا 2 أَنْتُمْ 3 أَنْتِ 4 أَنْتُمَا(ث) 5 أَنْتُنَّ."""
import re, unicodedata
N = lambda s: unicodedata.normalize("NFC", s or "")
MARKS = "ً-ْٰ"
def fin(s):
    """letters and marks compared the same whatever order the marks were typed in; a waṣl alif's own vowel is not compared"""
    s = N(s).replace("ٱ", "ا")
    s = re.sub(r"^ا[َ-ِ]", "ا", s)
    return s
HIDDEN = {0: ("هُوَ", "he", "o"), 3: ("هِيَ", "she", "o (dişil)"), 6: ("أَنْتَ", "you", "sen"), 12: ("أَنَا", "I", "ben"), 13: ("نَحْنُ", "we", "biz")}
WHO = ["هُوَ", "هُمَا", "هُمْ", "هِيَ", "هُمَا", "هُنَّ", "أَنْتَ", "أَنْتُمَا", "أَنْتُمْ", "أَنْتِ", "أَنْتُمَا", "أَنْتُنَّ", "أَنَا", "نَحْنُ"]
WHO_EN = ["he", "the two of them", "they (m.)", "she", "the two of them (f.)", "they (f.)", "you (m. sg.)", "you two", "you (m. pl.)", "you (f. sg.)", "you two (f.)", "you (f. pl.)", "I", "we"]
WHO_TR = ["o", "o ikisi", "onlar (eril)", "o (dişil)", "o ikisi (dişil)", "onlar (dişil)", "sen", "siz ikiniz", "siz (eril)", "sen (dişil)", "siz ikiniz (dişil)", "siz (dişil)", "ben", "biz"]

def _prefix_swap(model, cell):
    """the stored 3ms governed form with this cell's own prefix letter (يَصُنْ → أَصُنْ، نَصُنْ، تَصُنْ)"""
    return N(cell)[0] + N(model)[1:] if model and cell else None

def moods(e, i):
    """the three moods of muḍāriʿ cell i: {rafʿ, naṣb, jazm} → form"""
    c = N(e["mudari"][i]); out = {"raf": c}
    if i in (5, 11): out["nasb"] = c; out["jazm"] = c; return out
    if i in (1, 4, 7, 10) and c.endswith("نِ"): out["nasb"] = out["jazm"] = c[:-2]; return out
    if i in (2, 8) and c.endswith("نَ"): out["nasb"] = out["jazm"] = c[:-2] + "ا"; return out
    if i == 9 and c.endswith("نَ"): out["nasb"] = out["jazm"] = c[:-2]; return out
    ms, mj = e.get("mansub"), e.get("majzum")
    if ms: out["nasb"] = _prefix_swap(ms, c)
    if mj: out["jazm"] = _prefix_swap(mj, c)
    return out

def candidates(e, host):
    """every (tense, index, mood) of paradigm e that writes this host"""
    h = fin(host); out = []
    for i, c in enumerate(e.get("mazi") or []):
        if fin(c) == h: out.append(("mazi", i, None))
    if e.get("mudari"):
        for i in range(14):
            for mood, f in moods(e, i).items():
                if f and fin(f) == h: out.append(("mudari", i, mood))
    for i, c in enumerate(e.get("amr") or []):
        if fin(c) == h: out.append(("amr", i, None))
    return out

# ------------------------------------------------------------------------------------------------ the lines
def _weak_end(c):
    b = re.sub(f"[{MARKS}]", "", N(c))
    return b[-1] if b and b[-1] in "ويىا" else ""

def mazi_line(e, i):
    c0 = N(e["mazi"][0]); maqsur = _weak_end(c0) in ("ى", "ا") and not re.search(r"[َُِ]$", c0)
    if i == 0:
        if maqsur: return ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ.", "A past verb built on a fatḥa estimated on the alif; its doer is a hidden «he».", "Elif üzerinde takdîrî fetha üzere mebnî mâzî fiil; fâili gizli «o».")
        return ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ.", "A past verb built on fatḥa; its doer is a hidden «he».", "Fetha üzere mebnî mâzî fiil; fâili gizli «o».")
    if i == 1: return ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْأَلِفُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "A past verb built on fatḥa; the alif of the dual is its doer.", "Fetha üzere mebnî mâzî fiil; tesniye elifi fâil.")
    if i == 2:
        if N(e["mazi"][2]).endswith("َوْا"): return ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "A past verb built on a ḍamma estimated on the alif that dropped where two quiescent letters met; the wāw of the group is its doer.", "İki sâkinin buluşmasıyla düşen elif üzerinde takdîrî zamme üzere mebnî mâzî fiil; cemâat vâvı fâil.")
        return ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "A past verb built on ḍamma because the wāw of the group is attached; the wāw is its doer.", "Cemâat vâvına bitiştiği için zamme üzere mebnî mâzî fiil; vâv fâil.")
    if i in (3, 4):
        base = "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ" if maqsur else "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ"
        ben = "A past verb built on a fatḥa estimated on the alif that dropped where two quiescent letters met" if maqsur else "A past verb built on fatḥa"
        btr = "İki sâkinin buluşmasıyla düşen elif üzerinde takdîrî fetha üzere mebnî mâzî fiil" if maqsur else "Fetha üzere mebnî mâzî fiil"
        if i == 3: return (base + "، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ.", ben + "; the tāʾ marks the feminine; its doer is a hidden «she».", btr + "; tâ te'nîs alâmeti; fâili gizli «o (dişil)».")
        return (base + "، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْأَلِفُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", ben + "; the tāʾ marks the feminine and the alif of the dual is its doer.", btr + "; tâ te'nîs alâmeti, tesniye elifi fâil.")
    S = "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ رَفْعٍ مُتَحَرِّكٍ"
    SE, ST = "A past verb built on sukūn because a vowelled subject pronoun is attached", "Harekeli ref' zamirine bitiştiği için sükûn üzere mebnî mâzî fiil"
    if i == 5: return ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "A past verb built on sukūn because the women's nūn is attached; the nūn is its doer.", "Nûn-ı nisveye bitiştiği için sükûn üzere mebnî mâzî fiil; nûn fâil.")
    tail = {6: ("، وَالتَّاءُ ضَمِيرُ الْمُخَاطَبِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "; the tāʾ of the one addressed is its doer.", "; muhâtab tâ'sı fâil."),
            7: ("، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْمِيمُ وَالْأَلِفُ عَلَامَةُ التَّثْنِيَةِ.", "; the tāʾ is its doer, and the mīm and alif mark the dual.", "; tâ fâil, mîm ile elif tesniye alâmeti."),
            8: ("، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْمِيمُ عَلَامَةُ الْجَمْعِ.", "; the tāʾ is its doer, and the mīm marks the plural.", "; tâ fâil, mîm cemi alâmeti."),
            9: ("، وَالتَّاءُ ضَمِيرُ الْمُخَاطَبَةِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "; the tāʾ of the woman addressed is its doer.", "; muhâtaba tâ'sı fâil."),
            10: ("، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْمِيمُ وَالْأَلِفُ عَلَامَةُ التَّثْنِيَةِ.", "; the tāʾ is its doer, and the mīm and alif mark the dual.", "; tâ fâil, mîm ile elif tesniye alâmeti."),
            11: ("، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالنُّونُ عَلَامَةُ جَمْعِ الْإِنَاثِ.", "; the tāʾ is its doer, and the doubled nūn marks the feminine plural.", "; tâ fâil, şeddeli nûn cemi müennes alâmeti."),
            12: ("، وَالتَّاءُ ضَمِيرُ الْمُتَكَلِّمِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "; the tāʾ of the speaker is its doer.", "; mütekellim tâ'sı fâil."),
            13: ("، وَ«نَا» ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "; «nā» is its doer.", "; «nâ» fâil.")}[i]
    return (S + tail[0], SE + tail[1], ST + tail[2])

GOV = {"اما": ("بِـ«إِنِ» الشَّرْطِيَّةِ الْمُدْغَمَةِ فِي «مَا»", "by the conditional «in» merged into «mā»", "«mâ»ya idgam edilmiş şart «in»i ile"), "لم": ("بِـ«لَمْ»", "by «lam»", "«lem» ile"), "لن": ("بِـ«لَنْ»", "by «lan»", "«len» ile"), "لا": ("بِـ«لَا» النَّاهِيَةِ", "by the prohibiting «lā»", "nehiy «lâ»sı ile"),
       "ل": ("بِلَامِ الْأَمْرِ", "by the lām of command", "emir lâmı ile"), "": ("", "", "")}

def mudari_line(e, i, mood, gov=""):
    c = N(e["mudari"][i]); g = GOV.get(gov, GOV[""])
    gar, gen, gtr = (" " + g[0] if g[0] else ""), (" " + g[1] if g[1] else ""), (" " + g[2] if g[2] else "")
    if i in (5, 11):
        mah = {"jazm": ("، فِي مَحَلِّ جَزْمٍ" + gar, ", in the place of jazm" + gen, "; cezm mahallinde" + gtr), "nasb": ("، فِي مَحَلِّ نَصْبٍ" + gar, ", in the place of naṣb" + gen, "; nasb mahallinde" + gtr)}.get(mood if gov else "", ("", "", ""))
        return ("فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ" + mah[0] + "، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
                "A present verb built on sukūn because the women's nūn is attached" + mah[1] + "; the nūn is its doer.", "Nûn-ı nisveye bitiştiği için sükûn üzere mebnî muzâri" + mah[2] + "; nûn fâil.")
    five = i in (1, 4, 7, 10, 2, 8, 9)
    doer = (("وَالْأَلِفُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "the alif of the dual is its doer", "tesniye elifi fâil") if i in (1, 4, 7, 10) else
            ("وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "the wāw of the group is its doer", "cemâat vâvı fâil") if i in (2, 8) else
            ("وَالْيَاءُ ضَمِيرُ الْمُخَاطَبَةِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "the yāʾ of the woman addressed is its doer", "muhâtaba yâ'sı fâil") if i == 9 else None)
    if not doer:
        w = HIDDEN[i]; wj = "وُجُوبًا " if i in (6, 12, 13) else ""
        doer = (f"وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ {wj}تَقْدِيرُهُ {w[0]}", f"its doer is a hidden «{w[1]}»", f"fâili gizli «{w[2]}»")
    we = _weak_end(c)
    if mood == "raf":
        if five: sign = ("ثُبُوتُ النُّونِ", "the keeping of the nūn", "nûnun sübûtu")
        elif we == "و": sign = ("الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْوَاوِ لِلثِّقَلِ", "a ḍamma estimated on the wāw, too heavy to pronounce", "vâv üzerinde, ağırlıktan dolayı takdîrî zamme")
        elif we == "ي": sign = ("الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْيَاءِ لِلثِّقَلِ", "a ḍamma estimated on the yāʾ, too heavy to pronounce", "yâ üzerinde, ağırlıktan dolayı takdîrî zamme")
        elif we in ("ى", "ا"): sign = ("الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "a ḍamma estimated on the alif, which carries no vowel", "elif üzerinde takdîrî zamme")
        else: sign = ("الضَّمَّةُ الظَّاهِرَةُ", "the written ḍamma", "zâhir zamme")
        return (f"فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ {sign[0]}، {doer[0]}.", f"A present verb in rafʿ, its sign {sign[1]}; {doer[1]}.", f"Merfû muzâri; ref' alâmeti {sign[2]}; {doer[2]}.")
    if mood == "nasb":
        if five: sign = ("حَذْفُ النُّونِ", "the dropping of the nūn", "nûnun hazfi")
        elif we in ("ى", "ا"): sign = ("الْفَتْحَةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "a fatḥa estimated on the alif", "elif üzerinde takdîrî fetha")
        else: sign = ("الْفَتْحَةُ الظَّاهِرَةُ", "the written fatḥa", "zâhir fetha")
        return (f"فِعْلٌ مُضَارِعٌ مَنْصُوبٌ{gar}، وَعَلَامَةُ نَصْبِهِ {sign[0]}، {doer[0]}.", f"A present verb in naṣb{gen}, its sign {sign[1]}; {doer[1]}.", f"Mansûb muzâri{gtr}; nasb alâmeti {sign[2]}; {doer[2]}.")
    jz = N(moods(e, i).get("jazm") or "")
    if five: sign = ("حَذْفُ النُّونِ", "the dropping of the nūn", "nûnun hazfi")
    elif we: sign = ("حَذْفُ حَرْفِ الْعِلَّةِ", "the dropping of the weak letter", "illet harfinin hazfi")
    elif re.search(r"ّ", jz[-3:]) and not jz.endswith("ْ"): sign = ("سُكُونٌ مُقَدَّرٌ مَنَعَ مِنْ ظُهُورِهِ الْإِدْغَامُ", "a sukūn estimated, hidden by the idghām", "idgamın gizlediği takdîrî sükûn")
    else: sign = ("السُّكُونُ", "the sukūn", "sükûn")
    return (f"فِعْلٌ مُضَارِعٌ مَجْزُومٌ{gar}، وَعَلَامَةُ جَزْمِهِ {sign[0]}، {doer[0]}.", f"A present verb in jazm{gen}, its sign {sign[1]}; {doer[1]}.", f"Meczûm muzâri{gtr}; cezm alâmeti {sign[2]}; {doer[2]}.")

def amr_line(e, i):
    c = N(e["amr"][i]); md = N((e.get("mudari") or [""])[0]); weak = _weak_end(md)
    if i == 0:
        if weak: on = ("حَذْفِ حَرْفِ الْعِلَّةِ", "the dropping of the weak letter", "illet harfinin hazfi")
        elif not c.endswith("ْ"): on = ("سُكُونٍ مُقَدَّرٍ مَنَعَ مِنْ ظُهُورِهِ الْإِدْغَامُ", "a sukūn estimated, hidden by the idghām", "idgamın gizlediği takdîrî sükûn")
        else: on = ("السُّكُونِ", "sukūn", "sükûn")
        return (f"فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى {on[0]}، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ أَنْتَ.", f"An imperative built on {on[1]}; its doer is a hidden «you».", f"{on[2].capitalize()} üzere mebnî emir fiili; fâili gizli «sen».")
    if i in (1, 4): return ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْأَلِفُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "An imperative built on the dropping of the nūn; the alif of the dual is its doer.", "Nûnun hazfi üzere mebnî emir fiili; tesniye elifi fâil.")
    if i == 2: return ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "An imperative built on the dropping of the nūn; the wāw of the group is its doer.", "Nûnun hazfi üzere mebnî emir fiili; cemâat vâvı fâil.")
    if i == 3: return ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْيَاءُ ضَمِيرُ الْمُخَاطَبَةِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "An imperative built on the dropping of the nūn; the yāʾ of the woman addressed is its doer.", "Nûnun hazfi üzere mebnî emir fiili; muhâtaba yâ'sı fâil.")
    return ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "An imperative built on sukūn because the women's nūn is attached; the nūn is its doer.", "Nûn-ı nisveye bitiştiği için sükûn üzere mebnî emir fiili; nûn fâil.")

def line(e, tense, i, mood=None, gov=""):
    return mazi_line(e, i) if tense == "mazi" else amr_line(e, i) if tense == "amr" else mudari_line(e, i, mood or "raf", gov)

# ------------------------------------------------------------------------------------------------ the two nūns of emphasis
def tawkid_line(host, gov=""):
    """a verb wearing the heavy or the light nūn, read off its own ending — the ʿIzzī's rule: fatḥa before the nūn for the single
    man and woman, ḍamma for the men (their wāw dropped unless a fatḥa stands before it), kasra for the woman addressed (her yāʾ
    likewise), the alif of the two kept with a kasra on the nūn, and an alif parting the women's nūn from the heavy one."""
    h = N(host); b = re.sub(f"[{MARKS}]", "", h)
    heavy = bool(re.search(r"ن[َِ]?ّ[َِ]?$", h)); light = (not heavy) and h.endswith("نْ")
    if not (heavy or light) or len(b) < 2: return None
    core = re.sub(r"ن[َِ]?ّ[َِ]?$", "", h) if heavy else h[:-2]
    amr = not re.match(r"^[يتنأ][َُ]", h) or bool(re.match(r"^ا", b))
    kind = ("فِعْلُ أَمْرٍ", "An imperative", "Emir fiili") if amr else ("فِعْلٌ مُضَارِعٌ", "A present verb", "Muzâri fiil")
    g = GOV.get(gov, GOV[""]); nn = ("الثَّقِيلَةِ", "heavy", "şeddeli (sakîle)") if heavy else ("الْخَفِيفَةِ", "light", "sâkin (hafîfe)")
    nun = (f"وَالنُّونُ حَرْفُ تَوْكِيدٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ", f"the {nn[1]} nūn is a particle of emphasis", f"{nn[2]} nûn te'kid harfi")
    if heavy and re.search(r"ْنَا$", core):
        return (f"{kind[0]} مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْأَلِفُ فَاصِلَةٌ بَيْنَ النُّونَاتِ، وَنُونُ التَّوْكِيدِ {nn[0]} مَكْسُورَةٌ بَعْدَهَا.",
                f"{kind[1]} built on sukūn because the women's nūn is attached; that nūn is its doer, an alif parts the nūns, and the heavy nūn of emphasis follows with a kasra.",
                f"{kind[2]}; nûn-ı nisveye bitiştiği için sükûn üzere mebnî, nûn fâil; elif nûnların arasını ayırır, ardından kesreli şeddeli te'kid nûnu gelir.")
    if heavy and core.endswith("َا"):
        st = ("مَبْنِيٌّ عَلَى حَذْفِ النُّونِ", "built on the dropping of the nūn", "nûnun hazfi üzere mebnî") if amr else (f"مَجْزُومٌ{(' ' + g[0]) if g[0] else ''}، وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ", f"in jazm{(' ' + g[1]) if g[1] else ''}, its sign the dropping of the nūn", f"meczûm{(' ' + g[2]) if g[2] else ''}, cezm alâmeti nûnun hazfi")
        return (f"{kind[0]} {st[0]}، وَالْأَلِفُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَنُونُ التَّوْكِيدِ {nn[0]} مَكْسُورَةٌ بَعْدَ الْأَلِفِ.",
                f"{kind[1]} {st[1]}; the alif of the dual is its doer, and the heavy nūn of emphasis takes a kasra after the alif.", f"{kind[2]}, {st[2]}; tesniye elifi fâil, şeddeli te'kid nûnu eliften sonra kesrelidir.")
    last = core[-1:] if core else ""
    if last == "ُ":
        kept = core.endswith("وُ")
        d = ("وَوَاوُ الْجَمَاعَةِ فَاعِلٌ، حُرِّكَتْ بِالضَّمِّ لِانْفِتَاحِ مَا قَبْلَهَا", "the wāw of the group is its doer, kept and given a ḍamma because a fatḥa stands before it", "cemâat vâvı fâil; öncesi fethalı olduğu için düşmemiş, zammelenmiştir") if kept else ("وَوَاوُ الْجَمَاعَةِ الْمَحْذُوفَةُ لِالْتِقَاءِ السَّاكِنَيْنِ فَاعِلٌ، وَالضَّمَّةُ دَلِيلٌ عَلَيْهَا", "the wāw of the group, dropped where two quiescent letters met, is its doer — the ḍamma points to it", "iki sâkinin buluşmasıyla düşen cemâat vâvı fâil; zamme ona delildir")
    elif last == "ِ":
        kept = core.endswith("يِ")
        d = ("وَيَاءُ الْمُخَاطَبَةِ فَاعِلٌ، حُرِّكَتْ بِالْكَسْرِ لِانْفِتَاحِ مَا قَبْلَهَا", "the yāʾ of the woman addressed is its doer, kept and given a kasra because a fatḥa stands before it", "muhâtaba yâ'sı fâil; öncesi fethalı olduğu için düşmemiş, kesrelenmiştir") if kept else ("وَيَاءُ الْمُخَاطَبَةِ الْمَحْذُوفَةُ لِالْتِقَاءِ السَّاكِنَيْنِ فَاعِلٌ، وَالْكَسْرَةُ دَلِيلٌ عَلَيْهَا", "the yāʾ of the woman addressed, dropped where two quiescent letters met, is its doer — the kasra points to it", "iki sâkinin buluşmasıyla düşen muhâtaba yâ'sı fâil; kesre ona delildir")
    elif last == "َ":
        st = "مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ " + nn[0]
        who = ("أَنْتَ", "you", "sen") if amr or re.match(r"^تَ|^تُ", h) and gov == "لا" else ("هُوَ", "he", "o") if re.match(r"^ي", b) else ("هِيَ أَوْ أَنْتَ", "she / you", "o (dişil) / sen") if re.match(r"^ت", b) else ("أَنْتَ", "you", "sen")
        mah = (f"، فِي مَحَلِّ جَزْمٍ {g[0]}", f", in the place of jazm {g[1]}", f"; {g[2]} cezm mahallinde") if (g[0] and not amr) else ("", "", "")
        return (f"{kind[0]} {st}{mah[0]}، {nun[0]}، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ {who[0]}.",
                f"{kind[1]} built on fatḥa because the {nn[1]} nūn of emphasis is attached{mah[1]}; {nun[1]}; its doer is a hidden «{who[1]}».", f"{kind[2]}; {nn[2]} te'kid nûnuna bitiştiği için fetha üzere mebnî{mah[2]}; {nun[2]}; fâili gizli «{who[2]}».")
    else: return None
    st = (("مَبْنِيٌّ عَلَى حَذْفِ النُّونِ", "built on the dropping of the nūn", "nûnun hazfi üzere mebnî") if amr else
          (f"مَجْزُومٌ {g[0]}، وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ", f"in jazm {g[1]}, its sign the dropping of the nūn", f"{g[2]} meczûm, cezm alâmeti nûnun hazfi") if g[0] else
          ("مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ ثُبُوتُ النُّونِ الْمَحْذُوفَةِ لِتَوَالِي الْأَمْثَالِ", "in rafʿ, its sign the keeping of a nūn that was then dropped because three nūns met", "merfû; ref' alâmeti, üç nûn art arda geldiği için düşen nûnun sübûtu"))
    return (f"{kind[0]} {st[0]}، {d[0]}، {nun[0]}.", f"{kind[1]} {st[1]}; {d[1]}; {nun[1]}.", f"{kind[2]}, {st[2]}; {d[2]}; {nun[2]}.")
