"""Remet accents et apostrophes dans les textes du carnet (ecrits sans accents a l origine).
Dictionnaire francais (pyspellchecker) pour les mots non ambigus + regles manuelles pour les cas ambigus."""
import re, json, os, unicodedata

_DIR = os.path.dirname(os.path.abspath(__file__))
_CACHE = os.path.join(_DIR, "fr_accents.json")


def _strip(w):
    return "".join(c for c in unicodedata.normalize("NFD", w) if unicodedata.category(c) != "Mn")


def _build_map():
    if os.path.exists(_CACHE):
        return json.load(open(_CACHE, encoding="utf-8"))
    from spellchecker import SpellChecker
    freq = SpellChecker(language="fr").word_frequency.dictionary
    best = {}
    for w, f in freq.items():
        s = _strip(w)
        if s != w and (s not in best or f > freq[best[s]]):
            best[s] = w
    m = {s: w for s, w in best.items() if s not in freq}   # seulement les mots sans forme non accentuee valide
    json.dump(m, open(_CACHE, "w", encoding="utf-8"), ensure_ascii=False)
    return m


AUTO = _build_map()
# mots ambigus tranches pour ce type de texte (participes passes, adjectifs)
FORCE = {
    "acceptes": "acceptés", "anime": "animé", "cale": "calé", "cite": "cité", "cites": "cités",
    "colores": "colorés", "confirme": "confirmé", "confirmes": "confirmés", "cultive": "cultivé",
    "donne": "donné", "ferme": "fermé", "grille": "grillé", "grilles": "grillés", "habitues": "habitués",
    "licencies": "licenciés", "loue": "loué", "parle": "parlé", "presses": "pressés", "prive": "privé",
    "publie": "publié", "publies": "publiés", "sale": "salé", "payes": "payés", "reserves": "réservés",
    "reserve": "réservé", "paye": "payé", "ile": "île", "iles": "îles", "etre": "être", "ete": "été",
    "ca": "ça", "apres": "après", "deja": "déjà", "tres": "très", "pres": "près", "a": "à",
    "fraiche": "fraîche", "fraiches": "fraîches", "fraicheur": "fraîcheur", "plait": "plaît",
    "gouter": "goûter", "cout": "coût", "couts": "coûts", "coute": "coûte", "boite": "boîte",
    "theatre": "théâtre", "creole": "créole", "capverdienne": "capverdienne", "noel": "Noël",
    "mieux": "mieux", "ole": "olé", "tete": "tête", "fenetre": "fenêtre", "foret": "forêt",
    "diner": "dîner", "diners": "dîners", "depot": "dépôt", "hote": "hôte", "hotes": "hôtes",
    "cedric": "cédric", "preenregistrement": "préenregistrement", "francoise": "françoise", "leao": "leão", "hotel": "hôtel", "hotels": "hôtels", "cotes": "côtes", "zone": "zone", "operateur": "opérateur",
}
# mots a laisser tels quels (verbes au present, noms) meme si le dictionnaire propose un accent
KEEP = {"ocean", "soul", "preta", "gata", "des", "du", "la", "ou", "sur", "mais", "ne", "de", "les", "notre", "contre", "entre", "repartir", "the"}
NOT_A = re.compile(r"\b(?:y|on|il|elle|qui|ça|ca|Il|On|Elle|cela|Cela|ce|Ce) a$")

PHRASES = [
    (r"\bmieux note\b", "mieux noté"), (r"\bmieux notee\b", "mieux notée"),
    (r"\b(d|D)(’| )ou\b", r"\1’où"), (r"\b[Oo]u se trouve", lambda m: ("Où" if m.group(0)[0] == "O" else "où") + " se trouve"),
    (r"\bOu trouver\b", "Où trouver"), (r"\bou l(’| )(eau|on)\b", r"où l’\2"),
    (r"\bou (les pecheurs|les pêcheurs|la mer|la lumiere|la lumière)\b", r"où \1"),
    (r"\bdes (l(’| )|que\b|maintenant\b|l arrivee|\d)", lambda m: "dès " + m.group(1)),
    (r"\bDes (l(’| )|que\b|\d)", lambda m: "Dès " + m.group(1)),
    (r"-la\b", "-là"), (r"\bla-bas\b", "là-bas"), (r"\bca et la\b", "çà et là"),
    (r"\bCam s\b", "Cam’s"), (r"\bFrankie s\b", "Frankie’s"), (r"\bOla Brasil\b", "Olá Brasil"),
    (r"\bPAYES\b", "PAYÉS"), (r"\bPAYE\b", "PAYÉ"), (r"\bRESERVES\b", "RÉSERVÉS"), (r"\bRESERVE\b", "RÉSERVÉ"),
    (r"\bA RESERVER\b", "À RÉSERVER"), (r"\bA reserver\b", "À réserver"), (r"\bA confirmer\b", "À confirmer"),
    (r"\bA negocier\b", "À négocier"), (r"\bA organiser\b", "À organiser"), (r"\bA pied\b", "À pied"),
    (r"\bA EMPORTER\b", "À EMPORTER"), (r"\bA faire\b", "À faire"), (r"\bA ne pas\b", "À ne pas"),
    (r"\bA (\d)", r"À \1"), (r"\bA l(’| )", "À l’"), (r"\bA la\b", "À la"), (r"\bA partir\b", "À partir"),
    (r"\bESPECES\b", "ESPÈCES"), (r"\bCHAUSSURES D EAU\b", "CHAUSSURES D’EAU"), (r"\bINDISPENSABLE\b", "INDISPENSABLE"),
    (r"\bse paye\b", "se paie"), (r"\ble paye\b", "le paie"),
    (r"\bEcran\b", "Écran"), (r"\bEte\b", "Été"), (r"\bEtre\b", "Être"), (r"\bEtape", "Étape"),
    (r"\bEviter\b", "Éviter"), (r"\bElectricite\b", "Électricité"), (r"\bEquipage\b", "Équipage"),
    (r"\bEglise\b", "Église"), (r"\bEspeces\b", "Espèces"), (r"\bEchelle\b", "Échelle"),
]
PHRASES += [(r"(\d) ?EUR\b", r"\1 €"), (r"\bEUR\b", "€")]
COTE_COAST = re.compile(r"\bcote (ouest|est|nord|sud|volcanique|rocheuse|sauvage|atlantique)\b")


def _case(src, dst):
    if src.isupper() and len(src) > 1:
        return dst.upper()
    if src[0].isupper():
        return dst[0].upper() + dst[1:]
    return dst


def fr(s):
    if not isinstance(s, str) or s.startswith("http") or re.search(r"\.(jpg|png|jpeg)$", s):
        return s
    s = re.sub(r"\bCam s\b", "Cam’s", s); s = re.sub(r"\bFrankie s\b", "Frankie’s", s)
    # apostrophes
    s = re.sub(r"(?<![\w’])(jusqu|lorsqu|puisqu|presqu|quelqu|aujourd|qu|Qu|[lLdDjJnNsScCmMtT]) (?=[aeiouyhAEIOUYHàâéèêëîïôûÀÂÉÈÊÎÔÛ])",
               lambda m: m.group(1) + "’", s)
    # cote / côté
    s = COTE_COAST.sub(lambda m: "côte " + m.group(1), s)
    s = re.sub(r"\bCote (ouest|est|nord|sud)\b", r"Côte \1", s)
    s = re.sub(r"\bcote\b", "côté", s)
    for pat, rep in PHRASES:
        s = re.sub(pat, rep, s)

    def word(m):
        w = m.group(0)
        lw = w.lower()
        if lw in KEEP:
            return w
        if lw == "a":
            pre = s[max(0, m.start() - 12):m.start()].rstrip()
            if NOT_A.search(pre + " a") or w == "A" or re.match(r" (ete|été|pas|deja|déjà|besoin|lieu|plus|rien|jamais|toujours)\b", s[m.end():m.end() + 10]):
                return w
            return "à"
        if lw in FORCE:
            return _case(w, FORCE[lw])
        if lw in AUTO:
            return _case(w, AUTO[lw])
        return w
    return re.sub(r"[^\W\d_]+", word, s)


def fr_deep(o, skip_keys=(), title_keys=False, _key=None):
    """title_keys=True : les cles du dictionnaire de premier niveau sont des titres d evenements (a traduire aussi).
    Les cles des dictionnaires imbriques sont des noms de champs : jamais modifiees."""
    if isinstance(o, str):
        return o if _key in skip_keys else fr(o)
    if isinstance(o, list):
        return [fr_deep(x, skip_keys, False, _key) for x in o]
    if isinstance(o, tuple):
        return tuple(fr_deep(x, skip_keys, False, _key) for x in o)
    if isinstance(o, dict):
        return {(fr(k) if title_keys and isinstance(k, str) else k): fr_deep(v, skip_keys, False, k) for k, v in o.items()}
    return o
