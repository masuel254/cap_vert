# -*- coding: utf-8 -*-
"""Genere le carnet Cap-Vert a partir du modele (carnet Singapour & Japon).
Seules les donnees et les reglages propres au voyage sont remplaces.
Usage : python3 build_capvert.py MODELE/index.html sortie_dir"""
import json, re, sys, os, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import capvert_data as D
# ---------------------------------------------------------------- accents et apostrophes sur tous les textes affiches
from fr_text import fr, fr_deep
_SK = ("id", "chap", "type", "color", "image", "video", "mapsUrl", "jp", "tel", "maps", "ics")
D.DATA = fr_deep(D.DATA, _SK)
D.INFO = fr_deep(D.INFO, _SK, title_keys=True)
D.CITY = fr_deep(D.CITY, _SK)
D.MAPS_ALWAYS = [fr(t) for t in D.MAPS_ALWAYS]
D.MAPS_URLS = {fr(k): v for k, v in D.MAPS_URLS.items()}
D.COPYDEST = {fr(k): v for k, v in D.COPYDEST.items()}
D.CAL_MAP = {fr(k): v for k, v in D.CAL_MAP.items()}
D.PLANE = [fr(t) for t in D.PLANE]
D.WALK = [fr(t) for t in D.WALK]
D.CAR = [fr(t) for t in D.CAR]
D.CHK_ITEMS = fr_deep(D.CHK_ITEMS, _SK)
D.RESA_DETAILS = {k: fr_deep(v, _SK) for k, v in D.RESA_DETAILS.items()}
D.HEBERGEMENTS = fr_deep(D.HEBERGEMENTS, _SK)
D.RESA_TODO = {fr(k): v for k, v in D.RESA_TODO.items()}
D.ICON = {fr(k): v for k, v in D.ICON.items()}
D.WEB = fr_deep(D.WEB, _SK, title_keys=True)
D.PAY = {fr(k): v for k, v in D.PAY.items()}
D.BUDGET = fr_deep(D.BUDGET, _SK)

src, out_dir = sys.argv[1], sys.argv[2]
html = open(src, encoding="utf-8").read()
STAMP = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
PREFIX = "carnet-capvert-"
J = lambda o: json.dumps(o, ensure_ascii=False, indent=1)

def rep(old, new, count=1):
    global html
    n = html.count(old)
    if n != count:
        raise SystemExit("Ancre trouvee %d fois (attendu %d) : %r" % (n, count, old[:90]))
    html = html.replace(old, new)

def rep_span(start, end, new, keep_end=True):
    """Remplace de `start` (inclus) jusqu a `end` (exclu si keep_end)."""
    global html
    i = html.find(start)
    if i < 0 or html.count(start) != 1:
        raise SystemExit("Debut introuvable/ambigu : %r" % start[:80])
    j = html.find(end, i + len(start))
    if j < 0:
        raise SystemExit("Fin introuvable : %r" % end[:80])
    if not keep_end:
        j += len(end)
    html = html[:i] + new + html[j:]

# ---------------------------------------------------------------- titres
rep('<meta name="apple-mobile-web-app-title" content="SG Japon 2026">',
    '<meta name="apple-mobile-web-app-title" content="Cap-Vert 2026">')
rep('<title>Singapour et Japon 2026</title>', '<title>Cap-Vert - Ile de Sal 2026</title>')
rep('SINGAPOUR &amp; JAPON 2026</div>', 'CAP-VERT - ILE DE SAL 2026</div>')

# ---------------------------------------------------------------- couverture
rep_span('  <div class="cv-big">SINGAPOUR</div>', '\n  <div id="countdown"', '''  <div class="cv-big">CAP-VERT</div>
  <div class="cv-amp">ile de</div>
  <div class="cv-big">SAL</div>
  <div class="cv-line"></div>
  <div class="cv-date">14 - 21 NOVEMBRE 2026</div>
  <div class="cv-stats">
    <div class="cv-stat"><div class="cv-sn">8</div><div class="cv-sl">Jours</div></div>
    <div class="cv-stat"><div class="cv-sn">4</div><div class="cv-sl">Voyageurs</div></div>
    <div class="cv-stat"><div class="cv-sn">1</div><div class="cv-sl">Île</div></div>
    <div class="cv-stat"><div class="cv-sn">7</div><div class="cv-sl">Nuits</div></div>
  </div>
  <div class="cv-route">
    <span class="cv-hl">Paris Orly</span><div class="cv-dot"></div>
    <span>Sal</span><div class="cv-dot"></div>
    <span class="cv-hl">Santa Maria</span>
  </div>
''')

# ---------------------------------------------------------------- onglet Plan (remplace la carte JR Pass)
def plan_block(title, color, bg, lines):
    return ('        <div style="margin-top:10px;background:%s;border-left:3px solid %s;border-radius:10px;padding:12px 14px">\n'
            '          <div style="font-size:10px;font-weight:700;color:%s;letter-spacing:1px;margin-bottom:6px">%s</div>\n'
            '          <div style="font-size:12px;color:#444;line-height:1.9">\n            %s\n          </div>\n        </div>\n'
            % (bg, color, color, fr(title), "<br>\n            ".join(fr(l) for l in lines)))
plan = ('    <div class="scr" id="s-pl">\n      <div style="padding:14px">\n'
        '        <div style="font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#C9A84C;padding:4px 0 12px;display:flex;align-items:center;gap:8px">Plan de l ile de Sal<span style="flex:1;height:1px;background:rgba(201,168,76,.2)"></span></div>\n'
        '        <a href="./plan-sal.jpg" target="_blank" rel="noopener" style="display:block;background:#fff;border-radius:14px;padding:8px;box-shadow:0 2px 8px rgba(0,0,0,.07)"><img src="./plan-sal.jpg" alt="Plan de l ile de Sal" style="width:100%;height:auto;display:block;border-radius:10px"></a>\n'
        '        <div style="font-size:11px;color:#999;text-align:center;margin:6px 0 4px">Toucher le plan pour l agrandir</div>\n'
        + plan_block("LE SUD : SANTA MARIA, NOTRE BASE", "#C9A84C", "#FBF6EA", [
            "Santa Maria, tout au sud : le logement, la plage, le ponton, les restos et les bars, tout a pied",
            "Praia Antonio de Sousa (Angulo) a l est du centre, les hotels a l ouest",
            "Praia Ponta Preta, a l ouest : le coucher de soleil du jeudi",
            "Baia do Algodoeiro : le Bikini Beach Club (brunch du dimanche, White Party du vendredi)",
            "Ponta de Sino, la pointe sud et son phare, reserve naturelle"])
        + plan_block("LE CENTRE : ESPARGOS ET L AEROPORT", "#2A6B7C", "#EEF5F7", [
            "Aeroport Amilcar Cabral : arrivee et depart, a 18 km de Santa Maria",
            "Espargos : la vraie ville de l ile, traversee pendant le tour du nord (mardi)",
            "La seule grande route goudronnee relie Santa Maria, l aeroport et Espargos"])
        + plan_block("L OUEST ET LE NORD-OUEST", "#C8573F", "#FBEDE9", [
            "Porto de Palmeira : le port de peche, dejeuner au Gata Fish (mardi)",
            "Buracona et l Oeil Bleu, au nord de Palmeira : piscines dans la lave (mardi, piste)",
            "Monte Leao (la tete de lion) : arret baignade de certaines croisieres en catamaran",
            "Baia da Murdeira : plages calmes et reserve marine"])
        + plan_block("L EST : PEDRA DE LUME ET SHARK BAY", "#2E6B3E", "#EEF5F0", [
            "Salinas de Pedra de Lume : le lac sale dans le cratere (mardi apres-midi)",
            "Port de Pedra de Lume : Area Docas, poisson face aux salines (idee de dejeuner)",
            "Baia da Parda, au sud de Pedra de Lume : Shark Bay et les requins citrons (mardi, piste)",
            "Costa da Fragata, plus au sud : cote sauvage et reserve naturelle"])
        + plan_block("TEMPS DE TRAJET EN TAXI DEPUIS SANTA MARIA", "#5B3A7E", "#F2ECF8", [
            "Ponta Preta ou Bikini Beach : ~10 min",
            "Aeroport : 20 a 25 min - Espargos : ~25 min",
            "Pedra de Lume ou Shark Bay : 25 a 30 min - Palmeira : ~35 min",
            "Buracona : ~45 min, fin en piste, chauffeur en 4x4",
            "Nuit noire vers 18h30 en novembre : rentrer des pistes avant"])
        + plan_block("REPERES", "#999999", "#F5F5F5", [
            "Sal mesure environ 30 km du nord au sud et 12 km d est en ouest",
            "Ile plate et desertique, alizes forts en novembre, surtout cote est",
            "Coucher du soleil vers 17h58 a la mi-novembre"])
        + '        <div style="height:20px"></div>\n      </div>\n    </div>\n  </div>\n  ')
rep_span('    <div class="scr" id="s-pl">', '<div id="bnav">', plan)

# ---------------------------------------------------------------- INFO_DATA / DATA / CITY_INFO
rep_span('var INFO_DATA={', 'var DATA={', 'var INFO_DATA=' + J(D.INFO) + ';\n')
rep_span('var DATA={', '\nvar CHS=DATA.CHAPTERS', 'var DATA=' + json.dumps(D.DATA, ensure_ascii=False) + ';')
rep_span('var CITY_INFO = {', 'var curDay=null;', 'var CITY_INFO = ' + J(D.CITY) + ';\n')

# ---------------------------------------------------------------- compte a rebours / jour actif / progression
rep('  var depart = new Date(2026, 7, 13, 8, 30, 0); // 13 août 2026 08h30 (depart chez Thomas, heure France)',
    '  var depart = new Date(2026, 10, 14, 0, 15, 0); // 14 novembre 2026 00h15 (depart de la maison vers Orly, heure France)')
rep('  // Retour : decollage HND le 29/08 a 16h35 heure de Tokyo (JST = UTC+9) => 07h35 UTC.',
    '  // Retour : decollage SID le 21/11 a 11h40 heure du Cap-Vert (UTC-1) => 12h40 UTC.')
rep('  // le fuseau ou se trouve le voyageur (France, Singapour ou Japon).',
    '  // le fuseau ou se trouve le voyageur (France ou Cap-Vert).')
rep('  var retour = new Date(Date.UTC(2026, 7, 29, 7, 35, 0));',
    '  var retour = new Date(Date.UTC(2026, 10, 21, 12, 40, 0));')
rep('function getTid(){var n=new Date(),s=new Date(2026,7,14),d=Math.floor((n-s)/86400000);return(d>=0&&d<16)?d+1:null}',
    'function getTid(){var n=new Date(),s=new Date(2026,10,14),d=Math.floor((n-s)/86400000);return(d>=0&&d<8)?d+1:null}')
rep('(t?(t-1)/16*100:0)', '(t?(t-1)/8*100:0)')

# ---------------------------------------------------------------- liens Maps
rep('    var mapsAlwaysTitles=["Depart chez Thomas","Depart vers parking Roissy"];',
    '    var mapsAlwaysTitles=' + json.dumps(D.MAPS_ALWAYS, ensure_ascii=False) + ';')
rep_span('      var customUrls={', '      var q=encodeURIComponent', '      var customUrls=' + json.dumps(D.MAPS_URLS, ensure_ascii=False) + ';\n')

# ---------------------------------------------------------------- reservations
rep_span('var DEFAULT_RESA_DONE =', 'function loadChkState(){',
         'var DEFAULT_RESA_DONE = ' + json.dumps({k: True for k in D.LOCKED}) + ';\n'
         '// Reservations deja payees/confirmees : verrouillees, impossible a decocher.\n'
         'var LOCKED_RESA = ' + json.dumps({k: True for k in D.LOCKED}) + ';\n'
         'var DEFAULT_RESA_DETAILS = ' + J(D.RESA_DETAILS) + ';\n')
rep_span('  var chkItems = [', '  var doneCount', '  var chkItems = ' + J(D.CHK_ITEMS) + ';\n')

# ---------------------------------------------------------------- formalites
FORM = r"""  var hForm='';
  hForm+='<div style="background:#faf6ec;border-left:3px solid #B8923D;border-radius:0 8px 8px 0;padding:10px 12px;font-size:12px;color:#5a4a22;line-height:1.6;margin-bottom:12px">'
    +'Pour 4 voyageurs francais. Pas de visa pour un sejour touristique de moins de 30 jours, mais un <b>preenregistrement en ligne obligatoire</b> (EASE) avec une taxe aeroport.</div>';

  hForm+='<div style="font-size:13px;font-weight:700;color:#1a1a1a;margin:6px 0 6px">&#128188; Passeport</div>';
  hForm+='<div style="font-size:12.5px;color:#444;line-height:1.7;margin-bottom:14px">'
    +'Passeport obligatoire pour chacun, en cours de validite. La regle la plus prudente : valide au moins 6 mois apres le retour, soit apres le <b>21 mai 2027</b>. Regle exacte a verifier sur France Diplomatie avant le depart.<br>'
    +'Billet retour obligatoire (deja reserve).</div>';

  hForm+='<div style="font-size:13px;font-weight:700;color:#2A6B7C;margin:6px 0 6px">&#127464;&#127483; Cap-Vert - preenregistrement EASE + taxe TSA</div>';
  hForm+='<div style="font-size:12.5px;color:#444;line-height:1.7;margin-bottom:6px">'
    +'<b>Obligatoire</b> pour chaque voyageur, a faire <b>au moins 5 jours avant l arrivee</b>, soit au plus tard le <b>9 novembre</b>.<br>'
    +'Taxe de securite aeroportuaire (TSA) : <b>3 400 CVE, environ 31 EUR par personne</b>, payee en ligne par carte.<br>'
    +'Utiliser uniquement le site officiel ease.gov.cv : des intermediaires facturent jusqu au double.<br>'
    +'Renseigner le vol TO3232 et l adresse du logement (Rua 15 Agosto 108, Santa Maria).<br>'
    +'Garder le recu ou le QR code de chacun en capture d ecran pour le controle a l arrivee.</div>';
  hForm+='<a href="https://www.ease.gov.cv" target="_blank" rel="noopener" style="display:inline-block;background:#2A6B7C;color:#fff;text-decoration:none;font-size:12px;font-weight:700;padding:8px 14px;border-radius:10px;margin-bottom:16px">&#127760; ease.gov.cv</a>';

  hForm+='<div style="font-size:13px;font-weight:700;color:#C8573F;margin:6px 0 6px">&#128663; Conduite</div>';
  hForm+='<div style="font-size:12.5px;color:#444;line-height:1.7;margin-bottom:6px">'
    +'Permis francais valide. Certains loueurs demandent ou conseillent le permis international : verifier aupres du loueur choisi au moment de reserver.</div>';

  hForm+='<div style="font-size:13px;font-weight:700;color:#5B3A7E;margin:10px 0 6px">&#127973; Sante</div>';
  hForm+='<div style="font-size:12.5px;color:#444;line-height:1.7;margin-bottom:6px">'
    +'Aucun vaccin obligatoire en venant de France. Vaccins habituels a jour. La carte europeenne d assurance maladie ne marche pas au Cap-Vert : verifier l assistance de la carte bancaire (frais medicaux + rapatriement).</div>';
  hForm+='<a href="https://www.diplomatie.gouv.fr/fr/conseils-aux-voyageurs/conseils-par-pays-destination/cap-vert/" target="_blank" rel="noopener" style="display:inline-block;background:#5B3A7E;color:#fff;text-decoration:none;font-size:12px;font-weight:700;padding:8px 14px;border-radius:10px;margin:6px 0">&#127760; Conseils aux voyageurs - Cap-Vert</a>';
  hForm+='<div style="font-size:11px;color:#999;line-height:1.6;margin-top:8px">S inscrire sur Ariane (France Diplomatie) avant le depart pour recevoir les alertes de securite.</div>';

"""
rep_span("  var hForm='';", "  h+=acc('&#128196; Formalites administratives', hForm, false);", FORM)

# ---------------------------------------------------------------- vols : references
rep_span('  var volLinks = {', '  VLS.forEach(function(v){',
         '  var volLinks = {\n'
         '    "ALLER":  {ref:"PNR K6UNPB - ref client 40-1068303696 - PAYE", site:"transavia.com - Ma reservation", url:"https://www.transavia.com"},\n'
         '    "RETOUR": {ref:"PNR K6UNPB - ref client 40-1068303696 - PAYE", site:"transavia.com - Ma reservation", url:"https://www.transavia.com"},\n'
         '  };\n')
rep("    hVols+='<div class=\"vo\">Confirme</div></div></div>';",
    "    hVols+='<div class=\"vo\">Paye - 2 426,00 EUR pour 4</div></div></div>';")

# ---------------------------------------------------------------- hebergements
rep_span('  [\n   {dates:"14-17 AOUT"', '  ].forEach(function(hh){', '  ' + J(D.HEBERGEMENTS) + '\n', keep_end=True)
rep('  ].forEach(function(hh){', '  .forEach(function(hh){')

# ---------------------------------------------------------------- onglet Outils
TIPS = r"""function buildTips(){
  // Partage des frais : Tricount du groupe
  var h='<div class="st">Partage des frais</div>';
  h+='<a href="https://tricount.com/tEQVBeyiPUfUmuZgCJ" target="_blank" rel="noopener" style="display:flex;align-items:center;gap:12px;background:#fff;border-radius:14px;padding:14px 16px;margin-bottom:14px;box-shadow:0 2px 8px rgba(0,0,0,.07);text-decoration:none">';
  h+='<div style="width:42px;height:42px;border-radius:12px;background:#2A6B7C;display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0">&#128184;</div>';
  h+='<div style="flex:1;min-width:0"><div style="font-size:15px;font-weight:800;color:#1a1a1a">Ouvrir le Tricount du voyage</div>';
  h+='<div style="font-size:11px;color:#777;margin-top:2px;line-height:1.4">Noter chaque depense des qu elle est payee. Les depenses sont partagees entre les 2 couples.</div></div>';
  h+='<div style="font-size:18px;color:#C9A84C;font-weight:800">&#8250;</div></a>';
  // Tripadvisor : restaurants et activités de Santa Maria
  h+='<div class="st">Avis et bonnes adresses</div>';
  h+='<div style="background:#fff;border-radius:14px;padding:14px 16px;margin-bottom:14px;box-shadow:0 2px 8px rgba(0,0,0,.07)">';
  h+='<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px"><div style="width:42px;height:42px;border-radius:12px;background:#00AA6C;display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0">&#129417;</div>';
  h+='<div style="flex:1;min-width:0"><div style="font-size:15px;font-weight:800;color:#1a1a1a">Tripadvisor Santa Maria</div>';
  h+='<div style="font-size:11px;color:#777;margin-top:2px;line-height:1.4">Pour trouver une table ou une activité sur place et lire les derniers avis.</div></div></div>';
  h+='<div style="display:flex;gap:8px">';
  h+='<a href="https://www.tripadvisor.fr/Restaurants-g482848-Santa_Maria_Ilha_do_Sal.html" target="_blank" rel="noopener" style="flex:1;text-align:center;padding:10px 6px;border-radius:10px;background:#00AA6C;color:#fff;font-size:12px;font-weight:700;text-decoration:none">Restaurants</a>';
  h+='<a href="https://www.tripadvisor.fr/Attractions-g482848-Activities-Santa_Maria_Ilha_do_Sal.html" target="_blank" rel="noopener" style="flex:1;text-align:center;padding:10px 6px;border-radius:10px;background:#E8F7F0;color:#00704A;font-size:12px;font-weight:700;text-decoration:none">Activités</a>';
  h+='<a href="https://www.tripadvisor.fr/Tourism-g482848-Santa_Maria_Ilha_do_Sal-Vacations.html" target="_blank" rel="noopener" style="flex:1;text-align:center;padding:10px 6px;border-radius:10px;background:#E8F7F0;color:#00704A;font-size:12px;font-weight:700;text-decoration:none">Santa Maria</a>';
  h+='</div></div>';
  // Change : escudo a parite fixe avec l euro
  h+='<div class="st">Taux de change</div>';
  h+='<div id="currencyBox" style="display:flex;gap:10px;margin-bottom:14px">';
  h+='<div style="flex:1;background:#fff;border-radius:14px;padding:14px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.07)">';
  h+='<div style="font-size:10px;font-weight:700;color:#C9A84C;letter-spacing:1px;margin-bottom:6px">CAP-VERT</div>';
  h+='<div style="font-size:11px;color:#666;margin-bottom:4px">1 EUR =</div>';
  h+='<div id="cveRate" style="font-size:28px;font-weight:800;color:#1a1a1a;line-height:1">110,265</div>';
  h+='<div style="font-size:11px;font-weight:600;color:#2A6B7C;margin-top:4px">CVE (escudo)</div>';
  h+='</div>';
  h+='<div style="flex:1;background:#fff;border-radius:14px;padding:14px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.07)">';
  h+='<div style="font-size:10px;font-weight:700;color:#C9A84C;letter-spacing:1px;margin-bottom:6px">REPERE</div>';
  h+='<div style="font-size:11px;color:#666;margin-bottom:4px">1 000 CVE =</div>';
  h+='<div style="font-size:28px;font-weight:800;color:#1a1a1a;line-height:1">9,07</div>';
  h+='<div style="font-size:11px;font-weight:600;color:#C8573F;margin-top:4px">EUR</div>';
  h+='</div>';
  h+='</div>';
  h+='<div id="rateInfo" style="font-size:10px;color:#AAA;text-align:center;margin-bottom:10px">Parite fixe avec l euro</div>';
  h+='<div style="background:#fff;border-radius:14px;padding:14px 16px;margin-bottom:14px;box-shadow:0 2px 8px rgba(0,0,0,.06)">';
  h+='<div style="font-size:10px;font-weight:700;color:#C9A84C;letter-spacing:1px;margin-bottom:10px">CALCULATRICE DE CHANGE</div>';
  h+='<div style="display:flex;gap:8px;align-items:center;margin-bottom:8px">';
  h+='<input id="calcInput" type="number" placeholder="Montant" oninput="calcChange()" style="flex:1;border:1.5px solid #f0ead4;border-radius:10px;padding:10px 12px;font-size:16px;font-weight:600;color:#1a1a1a;outline:none;-webkit-appearance:none">';
  h+='<div style="display:flex;flex-direction:column;gap:4px">';
  h+='<button data-cur="EUR" id="btnEUR" class="cur-btn" style="padding:6px 10px;border-radius:8px;border:none;font-size:11px;font-weight:700;cursor:pointer;background:#C9A84C;color:#1a1a1a">EUR</button>';
  h+='<button data-cur="CVE" id="btnCVE" class="cur-btn" style="padding:6px 10px;border-radius:8px;border:none;font-size:11px;font-weight:700;cursor:pointer;background:#f0f0f0;color:#666">CVE</button>';
  h+='</div></div>';
  h+='<div id="calcResult" style="font-size:13px;color:#444;line-height:1.9;min-height:44px">Entrez un montant ci-dessus</div>';
  h+='</div>';

  // ── FUSEAUX HORAIRES ──
  h+='<div class="st">Fuseaux Horaires</div>';
  h+='<div style="display:flex;gap:8px;margin-bottom:6px" id="clockBox">';
  h+='<div style="flex:1;background:#fff;border-radius:14px;padding:12px 8px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.06)">';
  h+='<div style="font-size:9px;font-weight:700;color:#AAA;letter-spacing:1px;margin-bottom:4px">PARIS</div>';
  h+='<div id="clock-paris" style="font-size:22px;font-weight:800;color:#1a1a1a;line-height:1;font-variant-numeric:tabular-nums">--:--</div>';
  h+='<div style="font-size:9px;color:#AAA;margin-top:3px">UTC+1</div>';
  h+='</div>';
  h+='<div style="flex:1;background:#fff;border-radius:14px;padding:12px 8px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.06)">';
  h+='<div style="font-size:9px;font-weight:700;color:#2A6B7C;letter-spacing:1px;margin-bottom:4px">ILE DE SAL</div>';
  h+='<div id="clock-sal" style="font-size:22px;font-weight:800;color:#2A6B7C;line-height:1;font-variant-numeric:tabular-nums">--:--</div>';
  h+='<div style="font-size:9px;color:#AAA;margin-top:3px">UTC-1</div>';
  h+='</div>';
  h+='</div>';
  h+='<div style="font-size:10px;color:#AAA;text-align:center;margin-bottom:14px">Sal = Paris moins 2 heures en novembre</div>';

  h+='<div class="st">Meteo en direct</div>';
  h+='<div id="weatherBox" style="display:flex;flex-direction:column;gap:10px;margin-bottom:6px">';
  h+='<div style="text-align:center;padding:16px;color:#AAA;font-size:12px">Chargement de la meteo...</div>';
  h+='</div>';
  h+='<div id="seaBox" style="margin-bottom:6px"></div>';
  h+='<div style="font-size:10px;color:#AAA;text-align:center;margin-bottom:14px">Normales de novembre : 28 C le jour, 22 C la nuit, mer a 26 C, soleil jusqu a 17h58</div>';

  // ── INFOS PRATIQUES CAP-VERT ──
  var prat=[
    ["Urgences","Police 132 - Hopital 130 - Pompiers 131"],
    ["Ambassade de France (Praia)","+238 260 45 35 - urgence absolue +238 991 21 29"],
    ["Plongee - Cabo Verde Diving","+238 595 37 96 (tel et WhatsApp)"],
    ["Chauffeurs de taxi","Ady (chauffeur de l hote Airbnb, organise aussi les visites de l ile) : +238 952 97 19 (WhatsApp). Plan B : Taxi Sal Island, +238 599 59 73 (WhatsApp), tres bien note. Pas de compteur : fixer le prix avant de monter, especes uniquement."],
    ["Argent","Escudo (CVE), parite fixe 1 EUR = 110,265 CVE. Euro accepté dans les lieux touristiques avec un taux moins bon. Carte refusee dans certains petits commerces : garder des especes."],
    ["Telephone","Le Cap-Vert est hors Union europeenne : le forfait francais facture le roaming. Prendre une eSIM ou une carte SIM locale, ou rester en wifi."],
    ["Electricite","220 V, memes prises qu en France. Pas d adaptateur."],
    ["Eau","Boire de l eau en bouteille."],
    ["Soleil","Indice UV jusqu a 9. Creme, chapeau, lunettes meme quand le vent rafraichit."],
    ["Mer","Vent et courants parfois forts selon les plages. La baie de Santa Maria, cote ponton, est la plus abritee pour se baigner."],
    ["Langue","Portugais officiel, creole au quotidien. Francais et anglais compris dans le tourisme a Sal."],
    ["Securite","Ile calme. Ne rien laisser sans surveillance sur la plage ni dans les taxis."]
  ];
  h+='<div class="st">Infos pratiques Cap-Vert</div><div class="el" style="margin-bottom:14px">';
  prat.forEach(function(p){
    var v=waLink(e(p[1]));
    if(p[0]==="Urgences") v=v.replace(/\b(13[0-2])\b/g,'<a class="tel-lnk" href="tel:$1">&#128222; $1</a>');
    h+='<div class="er"><div class="edd"></div><div><div class="ela">'+e(p[0])+'</div><div class="elv">'+v+'</div></div></div>';
  });
  h+='</div>';

  h+='<div class="st">Phrases utiles en portugais</div><div class="phl">';"""
TIPS = re.sub(r'^(\s*\[)"([^"]*)","([^"]*)"(\],?)$', lambda m: '%s"%s","%s"%s' % (m.group(1), fr(m.group(2)), fr(m.group(3)), m.group(4)), TIPS, flags=re.M)
for _a, _b in [("Normales de novembre : 28 C le jour, 22 C la nuit, mer a 26 C, soleil jusqu a 17h58", "Normales de novembre : 28 °C le jour, 22 °C la nuit, mer à 26 °C, soleil jusqu’à 17h58"),
               ("Noter chaque depense des qu elle est payee. Les depenses sont partagees entre les 2 couples.", "Noter chaque dépense dès qu’elle est payée. Les dépenses sont partagées entre les 2 couples."),
               (">ILE DE SAL<", ">ÎLE DE SAL<"), ("Parite fixe avec l euro : le taux ne varie pas (fonctionne hors ligne)", "Parité fixe avec l’euro : le taux ne varie pas (fonctionne hors ligne)")]:
    TIPS = TIPS.replace(_a, _b)
rep_span('function buildTips(){', "  PHS.forEach(function(p){", TIPS + "\n")

# ---------------------------------------------------------------- calculatrice
CALC = r"""var calcCurrency = "EUR";
var cachedRates = {CVE: 110.265};

function setCalcCurrency(cur) {
  calcCurrency = cur;
  ["EUR","CVE"].forEach(function(c){
    var btn = document.getElementById("btn"+c);
    if(btn) {
      btn.style.background = (c===cur) ? "#C9A84C" : "#f0f0f0";
      btn.style.color = (c===cur) ? "#1a1a1a" : "#666";
    }
  });
  calcChange();
}

function calcChange() {
  var input = document.getElementById("calcInput");
  var result = document.getElementById("calcResult");
  if(!input || !result) return;
  var val = parseFloat(input.value);
  if(!val || isNaN(val)) {
    result.innerHTML = "Entrez un montant ci-dessus";
    return;
  }
  var cve = cachedRates.CVE || 110.265;
  var html = "";
  if(calcCurrency === "EUR") {
    html = "<b style='color:#2A6B7C'>" + Math.round(val * cve).toLocaleString("fr-FR") + " CVE</b>";
    html += "<br><span style='font-size:11px;color:#AAA'>" + val.toFixed(2) + " EUR</span>";
  } else {
    html = "<b style='color:#C9A84C'>" + (val / cve).toFixed(2) + " EUR</b>";
    html += "<br><span style='font-size:11px;color:#AAA'>" + Math.round(val).toLocaleString("fr-FR") + " CVE</span>";
  }
  result.innerHTML = html;
}

"""
rep_span('var calcCurrency = "EUR";', 'var BOAT_EVENTS', CALC)

# ---------------------------------------------------------------- horloges / meteo
rep_span('function updateClocks(){', 'updateClocks();\nsetInterval', r"""function updateClocks(){
  var now = new Date();
  var paris = new Date(now.toLocaleString("en-US", {timeZone:"Europe/Paris"}));
  var sal   = new Date(now.toLocaleString("en-US", {timeZone:"Atlantic/Cape_Verde"}));
  function fmt(d){ return String(d.getHours()).padStart(2,"0")+":"+String(d.getMinutes()).padStart(2,"0"); }
  var cp = document.getElementById("clock-paris");
  var cs = document.getElementById("clock-sal");
  if(cp) cp.textContent = fmt(paris);
  if(cs) cs.textContent = fmt(sal);
}
""")
rep_span('var WEATHER_CITIES = [', 'function weatherIcon(code){', """var WEATHER_CITIES = [
  {name:"Santa Maria", lat:16.5977, lon:-22.9045, color:"#2A6B7C"},
  {name:"Espargos",    lat:16.7550, lon:-22.9440, color:"#C8573F"}
];

""")

# ---------------------------------------------------------------- tables de puces
def tbl(name, keys, val="true"):
    return "var %s = {\n%s\n};\n" % (name, ",\n".join('  %s: %s' % (json.dumps(k, ensure_ascii=False), val if val else json.dumps(keys[k], ensure_ascii=False)) for k in keys))
TABLES = ("var BOAT_EVENTS = {};\n\nvar TRAIN_EVENTS = {};\n\n"
          "// Correspondance titre d'event timeline -> index du trajet dans la section Trains (DATA.TRAINS)\n"
          "var TRAIN_EVENT_TO_IDX = {};\n\n"
          + tbl("PLANE_EVENTS", D.PLANE) + "\n"
          + tbl("WALK_EVENTS", D.WALK) + "\n"
          + "var UBER_EVENTS = {};\n\n"
          + tbl("CAR_EVENTS", D.CAR)
          + "var NAV_EVENTS = {};\nvar GRAB_EVENTS = {};\n\n"
          + "// Adresse de destination a copier (GPS, taxi)\n"
          + tbl("GRABDEST_EVENTS", D.COPYDEST, val=None) + "\n")
rep_span('var BOAT_EVENTS = {', 'function copyDest(btn){', TABLES)

# ---------------------------------------------------------------- calendrier
cal_js = "var CAL_MAP = " + json.dumps(D.CAL_MAP, ensure_ascii=False, indent=1) + ";\n\nvar CAL_EVENTS = [\n"
cal_js += ",\n".join('  {id:%s, title:%s, ics:`%s`}' % (json.dumps(c["id"]), json.dumps(c["title"], ensure_ascii=False), c["ics"]) for c in D.CAL_EVENTS)
cal_js += "\n];\n\n"
rep_span('var CAL_MAP = {', 'function addToCalendar(id) {', cal_js)

# ---------------------------------------------------------------- taux (parite fixe, pas d appel reseau)
rep_span("// Affiche les taux (SGD/JPY)", "</script>", r"""// Escudo : parite fixe avec l euro (1 EUR = 110,265 CVE), aucun appel reseau necessaire.
function renderRates(rates, offlineTs){
  var el = document.getElementById("cveRate");
  if(el) el.textContent = "110,265";
  var el_info = document.getElementById("rateInfo");
  if(el_info) el_info.textContent = "Parite fixe avec l euro : le taux ne varie pas (fonctionne hors ligne)";
}

function fetchRates() {
  cachedRates = {CVE: 110.265};
  renderRates(cachedRates, null);
  calcChange();
}
""")

# ---------------------------------------------------------------- isolation (meme domaine github.io que le carnet Japon)
for k in ["lastDayId", "dayNotes", "chkState", "resaDetails", "lastWeather", "lastRates"]:
    html = html.replace('localStorage.getItem("%s")' % k, 'localStorage.getItem("capvert26_%s")' % k)
    html = html.replace('localStorage.setItem("%s"' % k, 'localStorage.setItem("capvert26_%s"' % k)
rep('return x.indexOf("carnet-voyage-")===0;', 'return x.indexOf("' + PREFIX + '")===0;')
rep('// raw attendu : carnet-voyage-YYYYMMDD-HHMMSS', '// raw attendu : ' + PREFIX + 'YYYYMMDD-HHMMSS')

# ---------------------------------------------------------------- textes generiques du moteur
rep("'Notez ici : resto conseille, code wifi, quai de gare...'".replace("'", '"'),
    '"Notez ici : resto conseille, code wifi, code de la porte..."')


rep('pl:"Plan JR Pass"};tt.textContent=nm[k]||"";ts.textContent="SINGAPOUR & JAPON 2026"}',
    'pl:"Plan de l ile"};tt.textContent=nm[k]||"";ts.textContent="CAP-VERT - ILE DE SAL 2026"}')
rep('text += "\\n\U0001F5FE Singapour & Japon 2026";', 'text += "\\n\U0001F3DD Cap-Vert - Ile de Sal 2026";')

os.makedirs(out_dir, exist_ok=True)

# ---------------------------------------------------------------- evolutions moteur MTO (pastilles, icones, WhatsApp)
import mto_patch
# ---------------------------------------------------------------- notes pre-remplies (Mes notes), modifiables par l utilisateur
rep('function loadDayNote(id){\n  try{ var v=localStorage.getItem("capvert26_dayNotes"); if(v){ var o=JSON.parse(v); return o[id]||""; } }catch(e){}\n  return "";\n}',
    'var DEFAULT_DAY_NOTES = ' + json.dumps({str(k): fr(v) for k, v in D.DEFAULT_DAY_NOTES.items()}, ensure_ascii=False) + ';\n'
    'function loadDayNote(id){\n  try{ var v=localStorage.getItem("capvert26_dayNotes"); if(v){ var o=JSON.parse(v); if(Object.prototype.hasOwnProperty.call(o,id)) return o[id]; } }catch(e){}\n  return DEFAULT_DAY_NOTES[id]||"";\n}')
rep('if(text && text.trim()!==""){ o[id]=text; } else { delete o[id]; }',
    'if(text && text.trim()!==""){ o[id]=text; } else if(DEFAULT_DAY_NOTES[id]){ o[id]=""; } else { delete o[id]; }')
# ---------------------------------------------------------------- temperature de la mer (Open-Meteo Marine), sous la meteo
SEA_JS = """var SEA_POINT = {name:"Baie de Santa Maria", lat:16.585, lon:-22.905};
function fetchSea(){
  var box=document.getElementById("seaBox"); if(!box) return;
  var url="https://marine-api.open-meteo.com/v1/marine?latitude="+SEA_POINT.lat+"&longitude="+SEA_POINT.lon+"&hourly=sea_surface_temperature&timezone=auto&forecast_days=2";
  fetch(url).then(function(r){return r.json();}).then(function(d){
    if(!d||!d.hourly||!d.hourly.sea_surface_temperature) throw 0;
    try{ localStorage.setItem("capvert26_lastSea", JSON.stringify({d:d, ts:Date.now()})); }catch(e){}
    renderSea(d, null);
  }).catch(function(){
    var c=null; try{ var v=localStorage.getItem("capvert26_lastSea"); if(v) c=JSON.parse(v); }catch(e){}
    if(c&&c.d) renderSea(c.d, c.ts); else box.innerHTML="";
  });
}
function renderSea(d, ts){
  var box=document.getElementById("seaBox"); if(!box) return;
  var t=d.hourly.time, v=d.hourly.sea_surface_temperature, byDay={}, order=[];
  for(var i=0;i<t.length;i++){ if(v[i]==null) continue; var k=t[i].slice(0,10); if(!byDay[k]){byDay[k]=[];order.push(k);} byDay[k].push(v[i]); }
  if(!order.length){ box.innerHTML=""; return; }
  function avg(a){ var s=0; a.forEach(function(x){s+=x;}); return Math.round(s/a.length*10)/10; }
  var labels=["Aujourd\\u2019hui","Demain"], cells="";
  order.slice(0,2).forEach(function(k,j){
    cells+='<div style="flex:1;text-align:center;padding:12px 6px'+(j?';border-left:1px solid #f0ebe0':'')+'">'
      +'<div style="font-size:10px;letter-spacing:1.5px;color:#999;text-transform:uppercase">'+labels[j]+'</div>'
      +'<div style="font-family:Georgia,serif;font-size:30px;color:#2A6B7C;margin-top:4px">'+String(avg(byDay[k])).replace(".",",")+'<span style="font-size:15px">\\u00b0C</span></div></div>';
  });
  var off=ts?'<div style="font-size:10px;color:#AAA;text-align:center;padding:0 0 8px">Derni\\u00e8re mesure en m\\u00e9moire (hors ligne)</div>':'';
  box.innerHTML='<div style="background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 2px 10px rgba(0,0,0,.06)">'
    +'<div style="background:#1F5D73;color:#fff;padding:12px 16px;font-family:Georgia,serif;letter-spacing:2px;font-size:15px">\\ud83c\\udf0a TEMP\\u00c9RATURE DE LA MER</div>'
    +'<div style="display:flex">'+cells+'</div>'
    +'<div style="font-size:11px;color:#999;text-align:center;padding:0 10px 10px">Moyenne de la journ\\u00e9e, baie de Santa Maria</div>'+off+'</div>';
}
"""
rep('function fetchWeather(){\n  var box = document.getElementById("weatherBox");', SEA_JS + 'function fetchWeather(){\n  fetchSea();\n  var box = document.getElementById("weatherBox");')
rep('var days = ["Aujourd hui","Demain"];', 'var days = ["Aujourd\\u2019hui","Demain"];')
html = mto_patch.apply(html, resa_todo=D.RESA_TODO, icons=D.ICON, web=D.WEB, pay=D.PAY)

# ---------------------------------------------------------------- todo datee (sous les reservations)
rep("  h+=acc('&#9989; Checklist Reservations ('+doneCount+'/'+chkItems.length+')', hChk, true);",
    "  h+=acc('&#9989; Checklist Reservations ('+doneCount+'/'+chkItems.length+')', hChk, true);\n"
    "  var _tc=todoCount();\n"
    "  h+=acc('&#128221; À faire ('+_tc[0]+'/'+_tc[1]+')', renderTodo(), true);")
rep("function loadChkState(){", "var todoItems = " + J(fr_deep(D.TODO_ITEMS)) + ";\nvar todoGroups = " + J(fr_deep(D.TODO_GROUPS)) + r""";
function loadTodoState(){
  var s={}; try{ var v=localStorage.getItem("capvert26_todoState"); if(v) s=JSON.parse(v); }catch(e){}
  // reprise des cases cochees quand ces actions etaient dans la checklist reservations
  try{ var c=JSON.parse(localStorage.getItem("capvert26_chkState")||"{}"); todoItems.forEach(function(i){ if(!(i.id in s) && c[i.id]) s[i.id]=true; }); }catch(e){}
  // ancienne case unique "Ady : reserver les trajets" : reportee sur les 5 trajets
  if(s.ady_resa){ ["ady_aller","ady_nord","ady_vendredi","ady_white","ady_retour"].forEach(function(k){ if(!(k in s)) s[k]=true; }); }
  return s;
}
function todoDays(iso){
  var p=iso.split("-"), d=new Date(+p[0],+p[1]-1,+p[2]), n=new Date(); n.setHours(0,0,0,0);
  return Math.round((d-n)/86400000);
}
function todoDone(i,st){ return i.subs ? i.subs.every(function(x){return st[x.id]}) : !!st[i.id]; }
function todoCount(){ var st=loadTodoState(); return [todoItems.filter(function(i){return todoDone(i,st)}).length, todoItems.length]; }
function todoJ(iso){ var j=todoDays(iso); return j>0?"J-"+j:(j===0?"Aujourd’hui":"En retard"); }
function todoDate(iso){ var p=iso.split("-"), d=new Date(Date.UTC(+p[0],+p[1]-1,+p[2])); return (RP_J[d.getUTCDay()]+" "+(+p[2])+" "+RP_M[+p[1]-1].replace(/\.$/,"")).toUpperCase(); }
function rpBell(i){
  var r=rpLoad()[i.id], ic="&#128276;", op="1", bg="transparent";
  if(r && r.st==="off"){ ic="&#128277;"; op=".35"; }
  else if(r && r.st==="on"){ bg="#E6F0E8"; }
  return '<span class="rp-chip" data-rp="'+i.id+'" style="flex-shrink:0;font-size:18px;line-height:1;cursor:pointer;opacity:'+op+';background:'+bg+';border-radius:10px;padding:5px 6px;align-self:flex-start">'+ic+'</span>';
}
function rpLine(i){
  var r=rpLoad()[i.id]; if(!(r && r.st==="on")) return "";
  return '<div class="rp-chip" data-rp="'+i.id+'" style="font-family:-apple-system,sans-serif;font-size:11px;font-weight:700;color:#2E6B3E;margin-top:4px;cursor:pointer">&#10003; Rappel '+e(rpLabel(r.d,r.t))+(i.evd?" &middot; "+rpRel(r.d,i.evd):"")+'</div>';
}
function renderTodo(){
  var st=loadTodoState(), F="font-family:-apple-system,sans-serif;", h='';
  var box=function(done){ return '<div class="chk-box'+(done?' done':'')+'" style="flex-shrink:0;width:22px;height:22px;margin-top:1px"><span class="chk-check">&#10003;</span></div>'; };
  var col=function(i,done){ var j=todoDays(i.due); return done?"#9a948a":(j<0?"#B3261E":i.color); };
  var hdr=function(i,done){ var c=col(i,done); return '<div style="display:flex;align-items:baseline;gap:8px;margin:12px 2px 5px;'+F+'"><span style="font-size:12px;font-weight:800;letter-spacing:1px;color:#1a1a1a">'+todoDate(i.due)+'</span><span style="font-size:10px;font-weight:800;color:'+c+';background:'+c+'1A;border-radius:20px;padding:1px 7px">'+(done?'Fait':todoJ(i.due))+'</span></div>'; };
  var card=function(i,done){
    return '<div class="todo-row" data-todoid="'+i.id+'" style="display:flex;gap:11px;background:#fff;border:1px solid #ece5d8;border-left:4px solid '+col(i,done)+';border-radius:12px;padding:11px 12px;cursor:pointer">'+box(done)
      +'<div style="flex:1;min-width:0"><div class="chk-name'+(done?' done':'')+'" style="font-size:14.5px">'+(i.ico?i.ico+' ':'')+e(i.name)+'</div>'
      +(done?'':'<div style="'+F+'font-size:12px;color:#6d655b;margin-top:2px;line-height:1.4">'+e(i.sub)+'</div>'+rpLine(i))+'</div>'+(done?'':rpBell(i))+'</div>';
  };
  var solo=todoItems.filter(function(i){return !i.group}), groups={};
  todoItems.forEach(function(i){ if(i.group){ (groups[i.group]=groups[i.group]||[]).push(i); } });
  var byDue=function(a,b){ return a.due<b.due?-1:a.due>b.due?1:0; };
  var open=solo.filter(function(i){return !todoDone(i,st)}).sort(byDue), done=solo.filter(function(i){return todoDone(i,st)}).sort(byDue);
  open.forEach(function(i){ h+=hdr(i,false)+card(i,false); });
  Object.keys(groups).forEach(function(g){
    var G=todoGroups[g]||{name:g}, L=groups[g].sort(byDue);
    h+='<div style="margin-top:16px;background:#fff;border:1px solid #ece5d8;border-left:4px solid #C8573F;border-radius:12px;overflow:hidden">';
    h+='<div style="display:flex;align-items:center;gap:10px;padding:11px 12px;background:#fbf4ef;border-bottom:1px solid #f1e6dc"><div style="font-size:22px">'+(G.ico||'')+'</div>'
      +'<div style="flex:1;min-width:0"><div style="font-family:Georgia,serif;font-size:15.5px;font-weight:700;color:#1a1a1a">'+e(G.name)+'</div><div style="'+F+'font-size:11.5px;color:#6d655b">'+e(G.sub||'')+'</div></div>'
      +(G.pick?'<a href="#" onclick="event.preventDefault();event.stopPropagation();taxiPick(\'\')" style="'+F+'font-size:11px;font-weight:800;color:#fff;background:#25a244;border-radius:20px;padding:6px 11px;text-decoration:none;white-space:nowrap">&#128172; WhatsApp</a>':'')+(G.wa?'<a href="https://wa.me/'+G.wa+'" target="_blank" rel="noopener" style="'+F+'font-size:11px;font-weight:800;color:#fff;background:#25a244;border-radius:20px;padding:6px 11px;text-decoration:none;white-space:nowrap">&#128172; WhatsApp</a>':'')+'</div>';
    L.forEach(function(i,k){
      var dn=todoDone(i,st), c=col(i,dn);
      h+='<div class="todo-row" data-todoid="'+i.id+'" style="display:flex;gap:10px;padding:10px 12px;cursor:pointer;'+(k?'border-top:1px solid #f1ebe0':'')+'">'+box(dn)+'<div style="flex:1;min-width:0">'
        +'<div style="'+F+'font-size:10.5px;font-weight:800;letter-spacing:.8px;color:'+c+'">'+todoDate(i.due)+' &middot; '+(dn?'FAIT':todoJ(i.due).toUpperCase())+'</div>'
        +'<div class="chk-name'+(dn?' done':'')+'" style="font-size:14px;margin-top:1px">'+e(i.name)+'</div>';
      if(i.sub && !dn) h+='<div style="'+F+'font-size:12px;color:#6d655b;margin-top:2px;line-height:1.4">'+e(i.sub)+'</div>';
      if(i.go) h+='<a href="#" onclick="event.preventDefault();event.stopPropagation();todoGo('+i.go[0]+',\''+i.go[1].replace(/'/g,"\\'")+'\')" style="'+F+'display:inline-block;margin-top:6px;font-size:11.5px;font-weight:800;color:#1C9C4F;background:#E7F8EE;border-radius:14px;padding:4px 10px;text-decoration:none">&#128242; Ouvrir la carte et le message &#8250;</a>';
      (i.subs||[]).forEach(function(x){
        var xd=!!st[x.id];
        h+='<div class="todo-sub" data-todoid="'+x.id+'" style="display:flex;align-items:center;gap:8px;padding:6px 0;'+F+'font-size:12px;border-top:1px dashed #eadfcd;margin-top:3px;cursor:pointer">'
          +'<span style="width:17px;height:17px;border:1.8px solid '+(xd?'#2E6B3E':'#d9cfbf')+';background:'+(xd?'#2E6B3E':'#fff')+';color:#fff;border-radius:5px;flex-shrink:0;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:700">'+(xd?'&#10003;':'')+'</span>'
          +'<span style="font-weight:800;color:'+(xd?'#9a948a':'#333')+';white-space:nowrap">'+e(x.when)+'</span><span style="color:'+(xd?'#9a948a':'#6d655b')+';'+(xd?'text-decoration:line-through':'')+'">'+e(x.what)+'</span></div>';
      });
      if(!dn) h+=rpLine(i);
      h+='</div>'+(dn?'':rpBell(i))+'</div>';
    });
    if(G.foot) h+='<div style="'+F+'font-size:11px;color:#8a8378;padding:8px 12px;background:#faf7f2;border-top:1px solid #f1ebe0">'+e(G.foot)+'</div>';
    h+='</div>';
  });
  if(done.length){ h+='<details class="chk-done-wrap" style="margin-top:12px;border:1px solid #ece5d8;border-radius:12px;background:#fff"><summary>&#10003; D&eacute;j&agrave; fait ('+done.length+') &#9662;</summary><div style="padding:0 10px 10px">'; done.forEach(function(i){ h+='<div style="margin-top:8px">'+card(i,true)+'</div>'; }); h+='</div></details>'; }
  return h;
}
function toggleTodo(id){
  var s=loadTodoState(), it=null; todoItems.forEach(function(i){ if(i.id===id) it=i; });
  if(it && it.subs){ var v=!todoDone(it,s); it.subs.forEach(function(x){ s[x.id]=v; }); s[id]=v; }
  else s[id]=!s[id];
  try{ localStorage.setItem("capvert26_todoState", JSON.stringify(s)); }catch(e){}
  buildInfo();
}
// ---------------------------------------------------------------- rappels iPhone (fichier .ics)
var RP_KEY="capvert26_rappels", RP_J=["dim.","lun.","mar.","mer.","jeu.","ven.","sam."], RP_M=["janv.","févr.","mars","avr.","mai","juin","juil.","août","sept.","oct.","nov.","déc."];
function rpLoad(){ var s={}; try{ var v=localStorage.getItem(RP_KEY); if(v) s=JSON.parse(v)||{}; }catch(x){} return s; }
function rpSave(s){ try{ localStorage.setItem(RP_KEY, JSON.stringify(s)); }catch(x){} }
function rpItem(id){ for(var k=0;k<todoItems.length;k++) if(todoItems[k].id===id) return todoItems[k]; return null; }
function rpAddDays(iso,n){ var p=iso.split("-"), d=new Date(Date.UTC(+p[0],+p[1]-1,+p[2]+n)); return d.toISOString().slice(0,10); }
function rpSal(iso){ return iso>="2026-11-14" && iso<"2026-11-21"; }   // sur place : heure du Cap-Vert
function rpUtc(iso,hm){ var p=iso.split("-"), t=hm.split(":"); return Date.UTC(+p[0],+p[1]-1,+p[2],+t[0],+t[1]) - (rpSal(iso)?-1:1)*3600000; }
function rpLabel(iso,hm){ var p=iso.split("-"), d=new Date(Date.UTC(+p[0],+p[1]-1,+p[2])); return RP_J[d.getUTCDay()]+" "+(+p[2])+" "+RP_M[+p[1]-1]+" à "+hm.replace(":","h")+(rpSal(iso)?" (heure de Sal)":""); }
function rpRel(d,evd){
  var a=d.split("-"), b=evd.split("-"), n=Math.round((Date.UTC(+b[0],+b[1]-1,+b[2])-Date.UTC(+a[0],+a[1]-1,+a[2]))/86400000);
  return n===0?"le jour même":(n===1?"la veille":(n>1?n+" jours avant":(-n)+(n===-1?" jour après":" jours après")));
}
function rpChip(i){
  var r=rpLoad()[i.id], st="background:#F4EBD6;color:#8a6a24;border:1.5px solid #B8923D", tx="&#128276; Rappel ?";
  if(r && r.st==="on"){ st="background:#E6F0E8;color:#2E6B3E;border:1.5px solid #2E6B3E"; tx="&#10003; Rappel &middot; "+e(rpLabel(r.d,r.t))+(i.evd?" &middot; "+rpRel(r.d,i.evd):""); }
  else if(r && r.st==="off"){ st="background:#fff;color:#aaa;border:1.5px dashed #ccc"; tx="&#128277; Pas de rappel"; }
  return '<span class="rp-chip" data-rp="'+i.id+'" style="display:inline-flex;align-items:center;gap:5px;margin-top:7px;padding:5px 11px;border-radius:20px;font-family:-apple-system,sans-serif;font-size:11px;font-weight:700;cursor:pointer;'+st+'">'+tx+'</span>';
}
function rpIcs(i,iso,hm){
  var u=new Date(rpUtc(iso,hm)), f=function(x){ return x.toISOString().replace(/[-:]/g,"").replace(/\.\d{3}/,""); };
  var esc=function(x){ return String(x).replace(/\\/g,"\\\\").replace(/;/g,"\;").replace(/,/g,"\\,").replace(/\n/g,"\\n"); };
  return ["BEGIN:VCALENDAR","VERSION:2.0","PRODID:-//MTO//Carnet Cap-Vert//FR","CALSCALE:GREGORIAN","METHOD:PUBLISH","BEGIN:VEVENT",
    "UID:"+i.id+"-"+Date.now()+"@mto-capvert","DTSTAMP:"+f(new Date()),"DTSTART:"+f(u),"DTEND:"+f(new Date(u.getTime()+15*60000)),
    "SUMMARY:"+esc("Cap-Vert : "+i.name),"DESCRIPTION:"+esc(i.sub||(i.subs||[]).map(function(x){return x.when+" "+x.what}).join(" / ")),
    "BEGIN:VALARM","ACTION:DISPLAY","DESCRIPTION:"+esc(i.name),"TRIGGER:PT0M","END:VALARM","END:VEVENT","END:VCALENDAR"].join("\r\n");
}
function rpDownload(i,iso,hm){
  var blob=new Blob([rpIcs(i,iso,hm)],{type:"text/calendar;charset=utf-8"}), url=URL.createObjectURL(blob), a=document.createElement("a");
  a.href=url; a.download="rappel-"+i.id+".ics"; document.body.appendChild(a); a.click();
  setTimeout(function(){ document.body.removeChild(a); URL.revokeObjectURL(url); },4000);
}
function rpCalUrl(iso,hm){ return "calshow:"+Math.round((rpUtc(iso,hm)-Date.UTC(2001,0,1))/1000); }
var rpCur=null, rpMode="edit";
function rpSheet(){
  var o=document.getElementById("rpSheet"); if(o) return o;
  o=document.createElement("div"); o.id="rpSheet";
  o.style.cssText="display:none;position:fixed;inset:0;z-index:10000;background:rgba(0,0,0,.45);align-items:flex-end;justify-content:center";
  o.addEventListener("click",function(ev){ if(ev.target===o) rpClose(); });
  document.body.appendChild(o); return o;
}
function rpClose(){ var o=document.getElementById("rpSheet"); if(o) o.style.display="none"; rpCur=null; buildInfo(); }
function rpOpen(id, mode){
  rpCur=id; var i=rpItem(id), r=rpLoad()[id]; if(!i) return;
  rpMode = mode || ((r && r.st==="on") ? "saved" : "edit");
  var o=rpSheet(), B='font-family:-apple-system,sans-serif;', h='';
  h+='<div style="'+B+'width:100%;max-width:480px;background:#fff;border-radius:22px 22px 0 0;padding:10px 18px calc(22px + env(safe-area-inset-bottom))">';
  h+='<div style="width:40px;height:5px;background:#ddd;border-radius:3px;margin:0 auto 12px"></div>';
  if(rpMode==="saved"){
    h+='<div style="font-size:11px;font-weight:700;letter-spacing:1.2px;color:#2E6B3E">&#10003; RAPPEL</div>';
    h+='<div style="font-family:Georgia,serif;font-size:17px;font-weight:600;color:#1a1a1a;margin:3px 0 6px">'+e(i.name)+'</div>';
    h+='<div style="font-size:14px;color:#444;margin-bottom:'+(i.sub?'4':'16')+'px">'+e(rpLabel(r.d,r.t))+(i.evd?', '+rpRel(r.d,i.evd):'')+'</div>';
    if(i.sub) h+='<div style="font-size:12px;color:#6d655b;margin-bottom:16px">'+e(i.sub)+'</div>';
    h+='<div style="display:flex;gap:8px"><button onclick="rpOpen(\''+id+'\',\'edit\')" style="'+B+'flex:1;border:1.5px solid #B8923D;border-radius:12px;background:#fff;color:#8a6a24;font-size:14px;font-weight:700;padding:12px 0">Changer l&rsquo;heure</button>';
    h+='<button onclick="rpCancel()" style="'+B+'flex:1;border:1.5px solid #C8573F;border-radius:12px;background:#fff;color:#C8573F;font-size:14px;font-weight:700;padding:12px 0">Annuler le rappel</button></div>';
  } else if(rpMode==="clean"){
    var old=rpSheet()._old;
    h+='<div style="font-size:11px;font-weight:700;letter-spacing:1.2px;color:#C8573F">DERNIÈRE ÉTAPE</div>';
    h+='<div style="font-family:Georgia,serif;font-size:17px;font-weight:600;color:#1a1a1a;margin:3px 0 8px">'+e(i.name)+'</div>';
    h+='<div style="font-size:13px;color:#555;line-height:1.5;margin-bottom:14px">'+(rpSheet()._why==="cancel"?'Le rappel est retiré du carnet.':'Le nouveau rappel est ajouté.')+' Il reste à supprimer l&rsquo;ancien dans ton Calendrier : <b>'+e(rpLabel(old.d,old.t))+'</b>. Touche le rappel, puis &laquo;&nbsp;Supprimer l&rsquo;événement&nbsp;&raquo;.</div>';
    h+='<a href="'+rpCalUrl(old.d,old.t)+'" style="'+B+'display:block;text-align:center;text-decoration:none;border-radius:12px;background:#1a1a1a;color:#fff;font-size:14px;font-weight:700;padding:12px 0;margin-bottom:8px">&#128197; Ouvrir le Calendrier à cette date</a>';
    h+='<button onclick="rpClose()" style="'+B+'width:100%;border:1.5px solid #e3ddd2;border-radius:12px;background:#fff;color:#888;font-size:13px;font-weight:600;padding:10px 0">Terminé</button>';
  } else {
    var d0=(r&&r.d)||i.due, t0=(r&&r.t)||i.rt||"09:00", veille=rpAddDays(i.due,-1);
    var pre=function(lbl,d,t){ var on=(d===d0&&t===t0); return '<button class="rp-pre" data-pd="'+d+'" data-pt="'+t+'" onclick="rpPreset(\''+d+'\',\''+t+'\')" style="'+B+'flex:1;border:none;border-radius:10px;padding:9px 0;font-size:12px;font-weight:'+(on?'700':'600')+';background:'+(on?'#1a1a1a':'#f3efe7')+';color:'+(on?'#fff':'#555')+'">'+lbl+'</button>'; };
    h+='<div style="font-size:11px;font-weight:700;letter-spacing:1.2px;color:#B8923D">RAPPEL</div>';
    h+='<div style="font-family:Georgia,serif;font-size:17px;font-weight:600;color:#1a1a1a;margin:3px 0 '+(i.sub?'4':'12')+'px">'+(i.ico?i.ico+' ':'')+e(i.name)+'</div>';
    if(i.sub) h+='<div style="font-size:12px;font-weight:600;color:#6d655b;margin-bottom:12px">'+e(i.sub)+'</div>';
    h+='<div style="display:flex;gap:6px;margin-bottom:12px">'+pre("La veille 18h",veille,"18:00")+pre("Le jour 9h",i.due,"09:00")+'<button onclick="document.getElementById(\'rpD\').focus()" style="'+B+'flex:1;border:none;border-radius:10px;padding:9px 0;font-size:12px;font-weight:600;background:#f3efe7;color:#555">Autre&hellip;</button></div>';
    h+='<div style="display:flex;gap:8px;margin-bottom:6px"><label style="flex:1.4;border:1px solid #e3ddd2;border-radius:10px;padding:7px 10px"><div style="font-size:10px;color:#999;font-weight:600">DATE</div><input id="rpD" type="date" value="'+d0+'" oninput="rpHint()" style="'+B+'border:none;background:none;font-size:15px;font-weight:700;color:#1a1a1a;width:100%;padding:0"></label>';
    h+='<label style="flex:1;border:1px solid #e3ddd2;border-radius:10px;padding:7px 10px"><div style="font-size:10px;color:#999;font-weight:600">HEURE</div><input id="rpT" type="time" value="'+t0+'" oninput="rpHint()" style="'+B+'border:none;background:none;font-size:15px;font-weight:700;color:#1a1a1a;width:100%;padding:0"></label></div>';
    h+='<div id="rpHintBox" style="font-size:11px;color:#888;margin-bottom:14px;min-height:15px"></div>';
    h+='<button onclick="rpAdd()" style="'+B+'width:100%;border:none;border-radius:12px;background:#B8923D;color:#fff;font-size:14px;font-weight:700;padding:13px 0;margin-bottom:8px">&#128197; Ajouter à mon agenda</button>';
    h+='<button onclick="rpOff()" style="'+B+'width:100%;border:1.5px solid #e3ddd2;border-radius:12px;background:#fff;color:#888;font-size:13px;font-weight:600;padding:10px 0">'+((r&&r.st==="on")?'Garder le rappel actuel':'Pas de rappel pour cette action')+'</button>';
  }
  h+='</div>';
  o.innerHTML=h; o.style.display="flex"; if(rpMode==="edit") rpHint();
}
function rpPreset(d,t){ document.getElementById("rpD").value=d; document.getElementById("rpT").value=t; rpHint(); }
function rpHint(){
  var d=document.getElementById("rpD").value, t=document.getElementById("rpT").value, el=document.getElementById("rpHintBox"); if(!el||!d||!t) return;
  var hh=+t.split(":")[0], msg=rpSal(d)?"Heure de Sal (2 h de moins qu&rsquo;en France).":"Heure de France.";
  [].forEach.call(document.querySelectorAll(".rp-pre"),function(b){ var on=b.getAttribute("data-pd")===d&&b.getAttribute("data-pt")===t; b.style.background=on?"#1a1a1a":"#f3efe7"; b.style.color=on?"#fff":"#555"; b.style.fontWeight=on?"700":"600"; });
  var it=rpItem(rpCur); if(it && it.evd) msg='<b style="color:#1a1a1a">Rappel '+rpRel(d,it.evd)+'.</b> '+msg;
  if(hh>=22||hh<7) msg+=' <b style="color:#C8573F">Attention, rappel en pleine nuit.</b>';
  if(rpUtc(d,t)<Date.now()) msg+=' <b style="color:#C8573F">Cette date est déjà passée.</b>';
  el.innerHTML=msg;
}
function rpAdd(){
  var d=document.getElementById("rpD").value, t=document.getElementById("rpT").value; if(!d||!t) return;
  var i=rpItem(rpCur), s=rpLoad(), prev=s[rpCur];
  rpDownload(i,d,t);
  s[rpCur]={st:"on",d:d,t:t}; rpSave(s);
  if(prev && prev.st==="on" && (prev.d!==d||prev.t!==t)){ rpSheet()._old=prev; rpSheet()._why="change"; rpOpen(rpCur,"clean"); }
  else rpClose();
}
function rpOff(){
  var s=rpLoad(); if(s[rpCur] && s[rpCur].st==="on"){ rpOpen(rpCur,"saved"); return; }
  s[rpCur]={st:"off"}; rpSave(s); rpClose();
}
function rpCancel(){
  var s=rpLoad(), prev=s[rpCur]; s[rpCur]={st:"off"}; rpSave(s);
  rpSheet()._old=prev; rpSheet()._why="cancel"; rpOpen(rpCur,"clean");
}
document.addEventListener("click",function(ev){
  var cp=ev.target.closest&&ev.target.closest(".rp-chip"); if(cp){ ev.stopPropagation(); ev.preventDefault(); rpOpen(cp.getAttribute("data-rp")); return; }
  var sb=ev.target.closest&&ev.target.closest(".todo-sub"); if(sb){ ev.stopPropagation(); toggleTodo(sb.getAttribute("data-todoid")); return; }
  if(ev.target.closest&&ev.target.closest("a[href]")) return;
  var r=ev.target.closest&&ev.target.closest(".todo-row"); if(!r) return;
  ev.stopPropagation(); toggleTodo(r.getAttribute("data-todoid"));
},true);
function loadChkState(){""")
# les pastilles A RESERVER des taxis suivent la case "Ady : reserver les trajets" de la todo
rep("  for(var lk in LOCKED_RESA){ if(LOCKED_RESA[lk]) s[lk]=true; }\n  return s;",
    "  for(var lk in LOCKED_RESA){ if(LOCKED_RESA[lk]) s[lk]=true; }\n  var ts=loadTodoState(); for(var tk in ts){ if(ts[tk]) s[tk]=true; }\n  return s;")
# compteur reservations : ne compter que les ids encore dans la checklist
rep('  var doneCount = Object.values(allState).filter(Boolean).length;\n  var prog = document.querySelector(".chk-progress");',
    '  var doneCount = chkItems.filter(function(i){ return allState[i.id]; }).length;\n  var prog = document.querySelector(".chk-progress");')
rep(".chk-item:last-child{border-bottom:none}", ".chk-item:last-child{border-bottom:none}\n"
    ".todo-cal{flex-shrink:0;width:46px;text-align:center;border:1.5px solid;border-radius:9px;overflow:hidden;font-family:-apple-system,sans-serif;background:#fff}\n"
    ".todo-cal-m{color:#fff;font-size:9px;font-weight:700;letter-spacing:1px;padding:2px 0}\n"
    ".todo-cal-d{font-size:18px;font-weight:700;color:#1a1a1a;line-height:1.2;padding-top:2px}\n"
    ".todo-cal-j{font-size:9px;color:#888;padding-bottom:3px;font-weight:600}")

html = mto_patch.apply_ux(html, budget=D.BUDGET)
for _a, _b in [("CAP-VERT - ILE DE SAL 2026", "CAP-VERT - ÎLE DE SAL 2026"), ('<div class="cv-amp">ile de</div>', '<div class="cv-amp">île de</div>'),
               ('pl:"Plan de l ile"', 'pl:"Plan de l’île"'), (">Plan de l ile de Sal<", ">Plan de l’île de Sal<"),
               ("Toucher le plan pour l agrandir", "Toucher le plan pour l’agrandir"), ("Phrases utiles en portugais", "Phrases utiles en portugais")]:
    html = html.replace(_a, _b)

# ---------------------------------------------------------------- accordeon Restaurants (vue synthetique)
_rows=[]
for _d in D.DAYS:
    for _e in _d["events"]:
        if _e["type"]!="meal": continue
        _t=_e["title"]; _h=int(_e["time"][:2])
        _rows.append({"d": fr(_d["date"]).title().replace(" Nov"," nov"), "t": _e["time"], "n": D.RESTO_SHORT.get(_t, fr(_t)),
                      "k": fr(_t), "pay": D.PAY.get(_t, D.PAY.get(fr(_t),"")), "bf": _h<11,
                      "st": "ok" if str(_e.get("cost","")).lower().startswith("reserv") or str(_e.get("cost","")).startswith("Réserv") else ("todo" if (_t in D.RESA_TODO or fr(_t) in D.RESA_TODO) else "free"),
                      "chk": D.RESA_TODO.get(_t, D.RESA_TODO.get(fr(_t),""))})
RESTO_JS = "var restoRows = " + json.dumps(_rows, ensure_ascii=False) + r""";
function renderRestos(){
  var cs=loadChkState(), sb=false; try{ sb=localStorage.getItem("capvert26_restoBf")==="1"; }catch(x){}
  var P={carte:"&#128179;",especes:"&#128182;",plutot:"&#128182;?"}, S={ok:["#2E6B3E","#E6F0E8","&#10003; Réservé"],todo:["#C8573F","#FBE9E4","À réserver"],free:["#8a8378","#f1ede6","Sans résa"]};
  var F="font-family:-apple-system,sans-serif;", rows=restoRows.map(function(r){ var st=r.st; if(st==="todo" && cs[r.chk]) st="ok"; return {r:r,st:st}; });
  var nok=rows.filter(function(x){return x.st==="ok"}).length, nto=rows.filter(function(x){return x.st==="todo"}).length;
  var h='<div style="display:flex;gap:6px;align-items:center;margin-bottom:10px;'+F+'font-size:11px;font-weight:700"><span style="background:#E6F0E8;color:#2E6B3E;border-radius:20px;padding:4px 10px">&#10003; '+nok+' réservés</span>'+(nto?'<span style="background:#FBE9E4;color:#C8573F;border-radius:20px;padding:4px 10px">'+nto+' à réserver</span>':'')
    +'<span id="restoBfBtn" style="margin-left:auto;color:#B8923D;cursor:pointer;padding:4px 0">'+(sb?'&minus; petits-déj.':'+ petits-déj.')+'</span></div>';
  h+='<div style="border:1px solid #efe9df;border-radius:12px;overflow:hidden;background:#fff">';
  var cur=null;
  rows.forEach(function(x){
    var r=x.r; if(r.bf && !sb) return;
    if(r.d!==cur){ h+='<div style="background:#f7f2e9;padding:6px 12px;'+F+'font-size:10.5px;font-weight:800;letter-spacing:1.2px;color:#8a6a24;border-top:1px solid #efe9df">'+e(r.d.toUpperCase())+'</div>'; cur=r.d; }
    var s=S[x.st], cl=(typeof INFO_DATA!=="undefined" && INFO_DATA[r.k]);
    h+='<div class="resto-row"'+(cl?' data-key="'+e(r.k).replace(/"/g,"&quot;")+'"':'')+' style="display:flex;align-items:center;gap:9px;padding:9px 12px;border-top:1px solid #f3eee5;'+F+(cl?'cursor:pointer':'')+'">'
      +'<span style="width:40px;flex-shrink:0;font-size:12px;font-weight:700;color:#555">'+e(r.t)+'</span>'
      +'<span style="flex:1;min-width:0;font-family:Georgia,serif;font-size:14px;font-weight:600;color:'+(r.bf?'#6d655b':'#1a1a1a')+'">'+e(r.n)+'</span>'
      +'<span style="font-size:12px;flex-shrink:0">'+(P[r.pay]||'')+'</span>'
      +'<span style="flex-shrink:0;font-size:10px;font-weight:800;color:'+s[0]+';background:'+s[1]+';border-radius:20px;padding:3px 8px;white-space:nowrap">'+s[2]+'</span></div>';
  });
  return h+'</div><div style="'+F+'font-size:10.5px;color:#999;margin-top:7px">&#128179; carte &middot; &#128182; espèces &middot; &#128182;? espèces probables &middot; toucher un restaurant pour sa fiche</div>';
}
document.addEventListener("click",function(ev){
  if(!ev.target.closest) return;
  if(ev.target.closest("#restoBfBtn")){ var v="0"; try{ v=localStorage.getItem("capvert26_restoBf")==="1"?"0":"1"; localStorage.setItem("capvert26_restoBf",v); }catch(x){} var dd=ev.target.closest("details"); if(dd && dd.lastElementChild) dd.lastElementChild.innerHTML=renderRestos(); return; }
  var r=ev.target.closest(".resto-row[data-key]"); if(r) openInfo(r);
});
"""
rep("function loadChkState(){", RESTO_JS + "function loadChkState(){")
_RS = "  var _rn=restoRows.filter(function(r){return r.st!=='free'}).length, _rc=loadChkState(), _ro=restoRows.filter(function(r){return r.st==='ok'||(r.st==='todo'&&_rc[r.chk])}).length;\n  h+=acc('&#127869;&#65039; Restaurants ('+_ro+'/'+_rn+' réservés)', renderRestos(), false);\n"
# ---------------------------------------------------------------- fiches Infos : bouton de reservation en ligne (resaUrl / resaLabel)
_MU = """    if (d.mapsUrl) h += '<a href="' + infoEsc(d.mapsUrl) + '" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:5px;margin-top:12px;background:#fff;border:1.5px solid ' + GOLD + ';color:#8a6d2f;border-radius:20px;padding:7px 14px;font-size:12px;font-weight:700;text-decoration:none">&#128205; ' + infoEsc(d.mapsLabel || "Itineraire Maps") + '</a>';"""
assert html.count(_MU) == 1, "ancre mapsUrl fiche"
html = html.replace(_MU, """    if (d.resaUrl) h += '<a href="' + infoEsc(d.resaUrl) + '" target="_blank" rel="noopener" style="display:flex;align-items:center;justify-content:center;gap:7px;margin-top:12px;background:#1a1a1a;color:#fff;border-radius:12px;padding:12px 14px;font-size:14px;font-weight:700;text-decoration:none">&#128197; ' + infoEsc(d.resaLabel || "Reserver en ligne") + '</a>';
""" + _MU)
# la liste A faire juste sous la checklist reservations (avant le budget)
_TD = "  var _tc=todoCount();\n  h+=acc('&#128221; À faire ('+_tc[0]+'/'+_tc[1]+')', renderTodo(), true);\n"
assert html.count(_TD) == 1, "bloc todo introuvable"
html = html.replace(_TD, "")
_CK = "  h+=acc('&#9989; Checklist réservations ('+doneCount+'/'+chkItems.length+')', hChk, true);\n"
assert html.count(_CK) == 1, "checklist introuvable"
html = html.replace(_CK, _CK + _TD + _RS)
# ---- pastille grise "Sans resa" sur les repas sans reservation
_PL = """':'<div class="tc2 tc2-resa">À RÉSERVER</div>';\n"""
assert html.count(_PL) >= 1, "ligne RESA_TODO introuvable"
html = html.replace(_PL, _PL + """    if(!cost && ev.type==="meal") cost='<div class="tc2 tc2-free">SANS RÉSA</div>';\n""", 1)
# ---- badge turquoise TAXI A APPELER (WhatsApp) et prix du taxi garde sous le badge
html = html.replace(_PL, _PL + """    var _px=(ev.cost&&/^~/.test(ev.cost))?'<div class="tc2 tc2-px">'+e(ev.cost)+'</div>':"", _pp='<div class="tc2">'+e(ev.cost||"")+'</div>';
    if(typeof CALL_TAXI!=="undefined" && CALL_TAXI[ev.title]) cost='<a class="tc2-call" href="#" onclick="event.preventDefault();event.stopPropagation();taxiPick(this.dataset.k)" data-k="'+ev.title.replace(/"/g,"&quot;")+'">&#128242; TAXI À APPELER</a>';
    if(_px && cost && cost!==_pp) cost='<div class="tc2-stk">'+cost+_px+'</div>';\n""", 1)
html = html.replace("var RESA_TODO = ", "var CALL_CARDS = " + json.dumps({fr(k): {"sub": fr(v[2]), "msg": fr(v[3]) + "\n\n" + v[4], "id": D.CALL_IDS[k], "px": D.CALL_PX.get(k) or next((e["cost"] for d in D.DAYS for e in d["events"] if e["title"] in (v[0], fr(v[0]))), "")} for k, v in D.CALL_CARDS.items()}, ensure_ascii=False) + ";\nvar RESA_TODO = ", 1)
_EVA = """    evh+='<div class="tr '+tclass(ev.type)+'" id="ev-'+curDay.id+'-'+i+'">';\n"""
_TX = {}
for _t, (_f, _to, _du, _cd) in D.TAXI_ROUTES.items():
    _dd = next(d for d in D.DAYS for e in d["events"] if e["title"] == _cd)
    _h = next(e["time"] for e in _dd["events"] if e["title"] == _cd).upper()
    _rs = _cd.startswith("Reserver")
    _TX[fr(_t)] = {"f": fr(_f), "t": fr(_to), "d": fr(_du), "id": D.CALL_IDS[_cd], "go": [_dd["id"], fr(_cd)],
                   "a": ("RÉSA " + _dd["date"].split()[0] + ". " + _h) if _rs else ("APPEL " + _h),
                   "b": ("RÉSERVÉ " + _dd["date"].split()[0] + ". " + _h) if _rs else ("APPELÉ " + _h)}
html = html.replace("var RESA_TODO = ", "var TAXI_EV = " + json.dumps(_TX, ensure_ascii=False) + ";\nvar RESA_TODO = ", 1)

assert html.count(_EVA) == 1, "ancre carte evenement"
html = html.replace(_EVA, """    var _trx="";if(typeof TAXI_EV!=="undefined" && TAXI_EV[ev.title]){var _x=TAXI_EV[ev.title],_dn=loadTodoState()[_x.id];
      _dep='<div class="tx-rt"><span>&#128205;</span><div>'+e(_x.f)+' <i>&#8594;</i> '+e(_x.t)+'<small>'+e(_x.d)+'</small></div></div>';
      cost='<div class="tc2-stk"><a href="#" class="tc2 tx-st '+(_dn?'tc2-ok':'tc2-resa')+'" onclick="event.preventDefault();event.stopPropagation();todoGo('+_x.go[0]+',\\''+_x.go[1].replace(/'/g,"\\\\'")+'\\')">'+(_dn?'&#10003; '+_x.b:'&#128242; '+_x.a)+' &#8250;</a>'+(ev.cost&&/^~/.test(ev.cost)?'<div class="tc2 tc2-px">'+e(ev.cost)+'</div>':'')+'</div>';_trx=" tx-on";}
    if(typeof CALL_CARDS!=="undefined" && CALL_CARDS[ev.title]){var _cc=CALL_CARDS[ev.title],_cb='';
      TAXI_LIST.concat([["Autre","","","","Bonjour !"]]).forEach(function(t){_cb+='<a class="cc-wa" href="https://wa.me/'+t[2]+'?text='+encodeURIComponent(_cc.msg.replace('{oi}',t[4]))+'" target="_blank" rel="noopener" onclick="event.stopPropagation()">&#128172; '+t[0]+'</a>';});
      evh+='<div class="tr tp tcall" style="--tk:#25D366" id="ev-'+curDay.id+'-'+i+'"><div class="tll"><div class="tld"></div>'+(last?"":'<div class="tlln"></div>')+'</div><div class="tc"><div class="tc2-stk"><a href="#" class="tc2 cc-st '+(loadTodoState()[_cc.id]?'tc2-ok':'tc2-resa')+'" onclick="event.preventDefault();event.stopPropagation();ccToggle(this,\\''+_cc.id+'\\')">'+(loadTodoState()[_cc.id]?'&#10003; FAIT':'À FAIRE')+'</a>'+(_cc.px&&/^~/.test(_cc.px)?'<div class="tc2 tc2-px">'+e(_cc.px)+'</div>':'')+'</div><div class="tt" style="color:#1C9C4F">'+e(ev.time)+'</div><div class="tti">&#128242; '+e(ev.title)+'</div><div class="cc-sub">'+e(_cc.sub)+'</div><div class="cc-row">'+_cb+'</div></div></div>';
      return;}
""" + _EVA.replace("tclass(ev.type)+'", "tclass(ev.type)+_trx+'"))
html = html.replace(".tc2.tc2-ok{", ".tc2.cc-st{text-decoration:none;max-width:none;letter-spacing:.4px;font-weight:800}.tx-rt{display:flex;align-items:center;gap:7px;background:#EEF5F7;border-radius:10px;padding:7px 10px;margin:4px 0 8px;font-family:-apple-system,sans-serif;font-size:13px;font-weight:700;color:#0F1B23;line-height:1.35}.tx-rt i{font-style:normal;color:#1F8FA6;font-weight:800}.tx-rt small{display:block;font-weight:600;font-size:11.5px;color:#7C8A8E;margin-top:1px}.tx-on .tti{padding-right:150px!important}.tc2.tx-st{text-decoration:none;max-width:none;letter-spacing:.4px;font-weight:800}.cc-sub{padding-right:84px;font-family:-apple-system,sans-serif;font-size:12.5px;font-weight:600;color:#7C8A8E;margin:-2px 0 9px}.cc-row{display:flex;gap:6px;flex-wrap:wrap}.cc-wa{font-family:-apple-system,sans-serif;background:#25D366;color:#fff;border-radius:20px;padding:6px 12px;font-size:12.5px;font-weight:700;text-decoration:none;white-space:nowrap}\n.tc2.tc2-ok{", 1)
html = html.replace("var RESA_TODO = ", "var TAXI_LIST = " + json.dumps([[fr(x[0]), fr(x[1]), x[2], x[3], fr(x[4])] for x in D.TAXI_LIST], ensure_ascii=False) + ";\n"
  + "document.addEventListener('click',function(ev){var a=ev.target.closest&&ev.target.closest('a[href^=\"https://wa.me/\"]');if(!a)return;try{var u=new URL(a.href),ph=u.pathname.replace(/\\D/g,''),t=u.searchParams.get('text'),q=[];if(ph)q.push('phone='+ph);if(t!==null)q.push('text='+encodeURIComponent(t));ev.preventDefault();ev.stopPropagation();window.location.href='whatsapp://send?'+q.join('&');}catch(x){}},true);\n"
  + "function todoGo(d,t){openDay(d);setTimeout(function(){var c=[].slice.call(document.querySelectorAll(\".tcall\")).filter(function(x){return x.textContent.indexOf(t)>=0;})[0];if(c)c.scrollIntoView({behavior:\"smooth\",block:\"center\"});},450);}\n"
  + "function ccToggle(el,id){var s=loadTodoState();s[id]=!s[id];try{localStorage.setItem(\"capvert26_todoState\",JSON.stringify(s));}catch(x){}el.className=\"tc2 cc-st \"+(s[id]?\"tc2-ok\":\"tc2-resa\");el.innerHTML=s[id]?\"&#10003; FAIT\":\"À FAIRE\";}\n"
  + "function taxiPick(k){var m=(typeof CALL_TAXI!==\"undefined\"&&CALL_TAXI[k])||{};var o=document.getElementById('taxiPk');if(!o){o=document.createElement('div');o.id='taxiPk';o.className='tpk';o.onclick=function(e){if(e.target===o)o.classList.remove('open');};document.body.appendChild(o);}"
  + "var h='<div class=\"tpk-s\"><div class=\"tpk-t\">&#128661; Appeler un taxi</div>';TAXI_LIST.concat([[\"Autre\",\"Un autre chauffeur, choisi dans WhatsApp\",\"\",\"\",\"Bonjour !\"]]).forEach(function(t){h+='<a class=\"tpk-r\" href=\"https://wa.me/'+t[2]+(m.msg?'?text='+encodeURIComponent(m.msg.replace('{oi}',t[4])):'')+'\" target=\"_blank\" rel=\"noopener\"><span><b>'+t[0]+'</b><i>'+t[1]+(t[3]?' - '+t[3]:'')+'</i></span><span class=\"tpk-wa\">&#128172; WhatsApp</span></a>';});"
  + "if(m.fr)h+='<div class=\"tpk-m\"><b>Message pré-rempli, à relire avant d’envoyer</b> (français, puis anglais dessous) : '+m.fr.replace(/\\{oi\\}\\s*/,'')+'</div>';h+='<div class=\"tpk-n\">Pas de compteur : fixer le prix avant de monter. Espèces uniquement.</div><button class=\"tpk-x\" onclick=\"document.getElementById(\\'taxiPk\\').classList.remove(\\'open\\')\">Fermer</button></div>';o.innerHTML=h;o.classList.add('open');}\nvar RESA_TODO = ", 1)
html = html.replace(".tc2.tc2-ok{", ".tpk{display:none;position:fixed;inset:0;z-index:99999;background:rgba(15,27,35,.5);align-items:flex-end;justify-content:center}.tpk.open{display:flex}.tpk-s{background:#FAF7F0;border-radius:22px 22px 0 0;padding:20px 18px 36px;width:100%;max-width:480px;box-sizing:border-box;font-family:-apple-system,sans-serif}.tpk-t{font:600 17px Georgia,serif;color:#0F1B23;margin-bottom:14px}.tpk-r{display:flex;align-items:center;justify-content:space-between;gap:10px;background:#fff;border:1px solid #DCE6E4;border-radius:14px;padding:12px 14px;margin-bottom:9px;text-decoration:none;color:#0F1B23}.tpk-r b{display:block;font-size:15px}.tpk-r i{display:block;font-style:normal;font-size:12px;color:#7C8A8E;margin-top:2px}.tpk-wa{background:#25D366;color:#fff;font-weight:700;font-size:13px;border-radius:18px;padding:7px 12px;white-space:nowrap}.tpk-m{white-space:pre-line;font-size:12.5px;color:#24414F;background:#E2F2F4;border-radius:12px;padding:10px 12px;margin:4px 0 8px;line-height:1.4}.tpk-m b{color:#177688}.tpk-n{font-size:12px;color:#7C8A8E;margin:6px 2px 12px}.tpk-x{width:100%;border:1.5px solid #DCE6E4;background:#fff;border-radius:12px;padding:12px;font-weight:700;font-size:14px;color:#0F1B23}\n.tc2.tc2-ok{", 1)
html = html.replace("var RESA_TODO = ", "var CALL_TAXI = {};var _CALL_TAXI_OFF = " + json.dumps({fr(k): {"fr": fr(v["fr"]), "msg": fr(v["fr"]) + "\n\n" + v["en"]} for k, v in D.CALL_TAXI.items()}, ensure_ascii=False) + ";\nvar RESA_TODO = ", 1)
html = html.replace(".tc2.tc2-ok{", ".tc2-stk{position:absolute;top:11px;right:11px;display:flex;flex-direction:column;align-items:flex-end;gap:5px;z-index:2}\n.tc2-stk .tc2,.tc2-stk .tc2-call{position:static}\n.tc2-call{font-family:-apple-system,sans-serif;position:absolute;top:11px;right:11px;font-size:10px;font-weight:800;letter-spacing:.4px;padding:3px 9px;border-radius:20px;white-space:nowrap;background:#E2F2F4;color:#177688;border:1.5px solid #1F8FA6;text-decoration:none}\n.tc2.tc2-ok{", 1)

# ---- balades du matin : distance, eau, vignettes photos des etapes et itineraire GPS
_WK = {fr(k): {"km": v["km"], "dur": v["dur"], "gps": v["gps"], "eau": fr(v["eau"]),
               "stops": [[s[0], fr(s[1]).replace("Dorés", "Dores"), fr(s[2]).replace("Dorés", "Dores"), s[3]] for s in v["stops"]]} for k, v in D.WALKS.items()}
html = html.replace("var RESA_TODO = ", "var WALKS = " + json.dumps(_WK, ensure_ascii=False) + ";\nvar RESA_TODO = ", 1)
_WKA = """+'<div style="display:flex;gap:6px;flex-wrap:wrap">'+mapsHtml"""
assert html.count(_WKA) == 1, "ancre ligne de pastilles"
html = html.replace(_WKA, """+_wk""" + _WKA)
html = html.replace(_EVA.replace("tclass(ev.type)+'", "tclass(ev.type)+_trx+'"), """    var _wk="";if(typeof WALKS!=="undefined" && WALKS[ev.title]){var _w=WALKS[ev.title],_sc="";
      _w.stops.forEach(function(s,n){var _im=s[0]?'<img src="./'+s[0]+'" alt="" loading="lazy">':'<div class="wk-ph">&#128248;</div>';
        _sc+=(s[3]?'<a class="wk-c" href="'+s[3]+'" target="_blank" rel="noopener" onclick="event.stopPropagation()">':'<div class="wk-c">')+_im+'<b>'+(n+1)+'. '+e(s[1])+'</b><span>'+e(s[2])+'</span>'+(s[3]?'<i>&#128205; Maps</i></a>':'</div>');});
      mapsHtml="";_wk='<div class="wk"><div class="wk-h">&#129406; '+e(_w.km)+' &middot; '+e(_w.dur)+' &middot; boucle depuis le logement</div>'
        +'<div class="wk-eau"><b>&#128167; Partir avec de l&#8217;eau</b>'+e(_w.eau)+'</div>'
        +'<div class="wk-s">'+_sc+'</div>'
        +'<a class="wk-gps" href="'+_w.gps+'" target="_blank" rel="noopener" onclick="event.stopPropagation()">&#128506;&#65039; Itin&eacute;raire complet dans Maps</a></div>';}
""" + _EVA.replace("tclass(ev.type)+'", "tclass(ev.type)+_trx+'"), 1)
html = html.replace(".tc2.tc2-ok{", ".tc{min-width:0}.wk{min-width:0;max-width:100%;margin:8px 0 10px;font-family:-apple-system,sans-serif}.wk-h{font-size:13px;font-weight:800;color:#0F1B23;margin-bottom:7px}.wk-eau{background:#FDEBE6;border-left:4px solid #C8573F;border-radius:10px;padding:8px 10px;font-size:12.5px;line-height:1.4;color:#5A2A1E;margin-bottom:9px}.wk-eau b{display:block;color:#C8573F;font-size:13px;margin-bottom:2px}.wk-s{display:flex;gap:8px;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:4px;-webkit-overflow-scrolling:touch}.wk-c{flex:0 0 152px;scroll-snap-align:start;background:#fff;border:1px solid #DCE6E4;border-radius:12px;overflow:hidden;text-decoration:none;color:#0F1B23;display:flex;flex-direction:column}.wk-c img,.wk-ph{width:100%;height:96px;object-fit:cover;display:block}.wk-ph{background:linear-gradient(135deg,#BFE6EC,#F3E4C6);display:flex;align-items:center;justify-content:center;font-size:26px;opacity:.8}.wk-c b{font-size:12.5px;padding:7px 8px 2px;line-height:1.25}.wk-c span{font-size:11.5px;color:#55636A;padding:0 8px 6px;line-height:1.35;flex:1}.wk-c i{font-style:normal;font-size:11px;font-weight:700;color:#1F8FA6;padding:0 8px 8px}.wk-gps{display:inline-block;margin-top:8px;background:#1F8FA6;color:#fff;border-radius:20px;padding:7px 13px;font-size:12.5px;font-weight:700;text-decoration:none}\\n.tc2.tc2-ok{", 1)

# ---- balades : un glissement horizontal sur les vignettes fait defiler les photos, sans changer de jour
_SW1 = """  swipeStartX = e.touches[0].clientX;\n"""
_SW2 = """  if(!curDay) return;\n  var dx = e.changedTouches[0].clientX - swipeStartX;"""
assert html.count(_SW1) == 1 and html.count(_SW2) == 1, "ancre swipe"
html = html.replace(_SW1, """  window._swNo = !!(e.target.closest && e.target.closest('.wk-s'));\n""" + _SW1)
html = html.replace(_SW2, """  if(!curDay || window._swNo) return;\n  var dx = e.changedTouches[0].clientX - swipeStartX;""")

# ---- fiche Infos : WhatsApp seul quand le numero est un mobile, et pastille Tripadvisor
_IA_OLD = """    if(_w&&_w.tel){_a+='<a class="ia-tel" href="tel:'+_w.tel+'">&#128222; Appeler</a>'; if(_w.wa)_a+='<a class="ia-wa" href="https://wa.me/'+_w.tel.replace(/\\D/g,'')+'" target="_blank" rel="noopener">&#128172; WhatsApp</a>';}"""
_IA_NEW = """    if(_w&&_w.tel){if(_w.wa)_a+='<a class="ia-wa" href="https://wa.me/'+_w.tel.replace(/\\D/g,'')+'" target="_blank" rel="noopener">&#128172; WhatsApp</a>'; else _a+='<a class="ia-tel" href="tel:'+_w.tel+'">&#128222; Appeler</a>';}"""
assert html.count(_IA_OLD) == 1, "ancre infoAct"
html = html.replace(_IA_OLD, _IA_NEW)
_IM = """    _a+='<a class="ia-map" href="'+_mu+'" target="_blank" rel="noopener">&#128205; Maps</a>';"""
assert html.count(_IM) == 1, "ancre ia-map"
html = html.replace(_IM, _IM + """\n    if(typeof TA_EVENTS!=="undefined"&&TA_EVENTS[key]){var _t2=TA_EVENTS[key];_a+='<a class="ia-ta" href="'+_t2[0]+'" target="_blank" rel="noopener"><i></i>'+(_t2[1]||'Avis')+'</a>';}""")
html = html.replace(".tc2.tc2-ok{", ".iact .ia-ta{background:#00AA6C!important;color:#fff!important;display:inline-flex;align-items:center;gap:6px}.iact .ia-ta i{width:6px;height:6px;border-radius:50%;background:#fff;display:block}\n.tc2.tc2-ok{", 1)


# ---- video TikTok : pastille « Voir la video » posee sur la photo de la fiche
_VI = """      ii.style.display = "block";
    } else { ii.innerHTML = ""; ii.style.display = "none"; }"""
assert html.count(_VI) == 1, "ancre infoImg"
html = html.replace(_VI, """      ii.style.display = "block";
      ii.style.position = "relative";
      if (d.video && navigator.onLine!==false) ttResolve(d.video);
      if (d.video) ii.innerHTML += '<a class="iv-tt" href="' + d.video + '" target="_blank" rel="noopener" onclick="return playTT(this)"><span class="iv-pl"><i></i></span>Voir la vid&eacute;o<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.6 5.8A4.3 4.3 0 0 1 15.5 3h-3.1v12.4a2.6 2.6 0 1 1-2.6-2.6c.3 0 .5 0 .8.1V9.7a5.7 5.7 0 1 0 4.9 5.7V9a7.3 7.3 0 0 0 4.3 1.4V7.3a4.3 4.3 0 0 1-3.2-1.5z"/></svg></a>';
    } else if (d.video) {
      ttResolve(d.video); ii.style.display = "block"; ii.style.position = "relative";
      ii.innerHTML = '<div class="iv-ph"></div><a class="iv-tt iv-tt-c" href="' + d.video + '" target="_blank" rel="noopener" onclick="return playTT(this)"><span class="iv-pl"><i></i></span>Voir la vid&eacute;o</a>';
    } else { ii.innerHTML = ""; ii.style.display = "none"; }""")
html = html.replace(".tc2.tc2-ok{", ".iv-tt{position:absolute;left:12px;bottom:12px;display:inline-flex;align-items:center;gap:8px;padding:8px 14px 8px 8px;border-radius:24px;background:rgba(15,27,35,.82);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);color:#fff!important;text-decoration:none;font:700 13px -apple-system,sans-serif}\n.iv-ph{height:460px;border-radius:12px;background:linear-gradient(160deg,#17303D,#0F1B23)}.iv-tt.iv-tt-c{left:50%;top:50%;bottom:auto;transform:translate(-50%,-50%);padding:12px 18px 12px 12px;font-size:15px}\n.iv-pl{width:24px;height:24px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center}.iv-pl i{width:0;height:0;border-left:8px solid #0F1B23;border-top:5px solid transparent;border-bottom:5px solid transparent;margin-left:2px}\n.tc2.tc2-ok{", 1)


# lecteur TikTok integre dans le cadre de la photo (numero de video trouve via l oEmbed TikTok, sinon ouverture de TikTok)
_PTT = r"""
var TT_IDS={};
function ttResolve(url,cb){
  var m=url.match(/\/video\/(\d+)/); if(m){TT_IDS[url]=m[1];cb&&cb(m[1]);return;}
  if(TT_IDS[url]){cb&&cb(TT_IDS[url]);return;}
  fetch('https://www.tiktok.com/oembed?url='+encodeURIComponent(url)).then(function(r){return r.json()}).then(function(j){
    var id=j.embed_product_id||((j.html||'').match(/data-video-id="(\d+)"/)||[])[1];
    if(id) TT_IDS[url]=id; cb&&cb(id||null);
  }).catch(function(){cb&&cb(null);});
}
// le player TikTok signale qu il est pret : on demande le son et la lecture
window.addEventListener('message',function(e){
  if(!/tiktok\.com$/.test((e.origin||'').replace(/^https?:\/\//,'')))return;
  var d=e.data; try{if(typeof d==='string')d=JSON.parse(d);}catch(x){return;}
  if(!d||!d['x-tiktok-player'])return;
  if(d.type==='onPlayerReady'){var f=document.querySelector('.iv-fr iframe');if(f){
    f.contentWindow.postMessage({type:'unMute','x-tiktok-player':true},'*');
    f.contentWindow.postMessage({type:'play','x-tiktok-player':true},'*');}}
});
function playTT(a){
  var box=a.parentNode, img=box.querySelector('img,.iv-ph'); if(!img) return true;
  var url=a.getAttribute('href'), h=Math.round(img.getBoundingClientRect().height)||420;
  function show(id){
    box.dataset.keep=box.innerHTML;
    box.innerHTML='<div class="iv-fr" style="height:'+h+'px"><iframe src="https://www.tiktok.com/player/v1/'+id+'?autoplay=1&loop=1&rel=0&music_info=0&description=0&volume_control=1" allow="autoplay; fullscreen; encrypted-media" allowfullscreen></iframe><button class="iv-x" onclick="var b=this.closest(\'#infoImg\');b.innerHTML=b.dataset.keep" aria-label="Revenir a la photo">&#10005;</button></div>';
  }
  if(TT_IDS[url]){show(TT_IDS[url]);return false;}
  if(navigator.onLine===false){a.querySelector('.iv-pl').nextSibling.textContent='Pas de r\u00e9seau ';return false;}
  a.style.opacity='.6';
  ttResolve(url,function(id){a.style.opacity='';if(id)show(id);else window.open(url,'_blank');});
  return false;
}
"""
assert html.count("function openInfo(") == 1, "ancre openInfo"
html = html.replace("function openInfo(", _PTT + "function openInfo(", 1)
html = html.replace(".tc2.tc2-ok{", ".iv-fr{position:relative;width:100%;border-radius:12px;overflow:hidden;background:#000}.iv-fr iframe{width:100%;height:100%;border:0;display:block}.iv-x{position:absolute;top:10px;right:10px;width:34px;height:34px;border-radius:50%;border:0;background:rgba(15,27,35,.8);color:#fff;font-size:15px}\n.tc2.tc2-ok{", 1)

# ---- pastille Tripadvisor (note + lien direct), juste apres Web
_TA = {fr(k): v for k, v in D.TA_EVENTS.items()}
_WL = """    if(typeof WEB_DATA!=="undefined" && WEB_DATA[ev.title]) webBtn="""
assert html.count(_WL) == 1, "ancre webBtn"
_i = html.index(_WL); _j = html.index("\n", _i) + 1
html = html[:_j] + """    if(typeof TA_EVENTS!=="undefined" && TA_EVENTS[ev.title]){var _ta=TA_EVENTS[ev.title];webBtn+='<a class="ta-btn" href="'+_ta[0]+'" target="_blank" rel="noopener" onclick="event.stopPropagation()" aria-label="Avis Tripadvisor"><i></i>'+(_ta[1]||'Avis')+'</a>';}\n""" + html[_j:]
html = html.replace("var WEB_DATA = ", "var TA_EVENTS=" + json.dumps(_TA, ensure_ascii=False) + ";\nvar WEB_DATA = ", 1)
assert "var TA_EVENTS=" in html, "ancre WEB_DATA"
html = html.replace(".tc2.tc2-ok{", ".ta-btn{display:inline-flex;align-items:center;gap:5px;box-sizing:border-box;height:26px;margin:9px 0 0;background:#00AA6C;color:#fff!important;border-radius:20px;padding:6px 10px;font-family:-apple-system,sans-serif;font-size:11px;font-weight:700;line-height:1;text-decoration:none;box-shadow:none;letter-spacing:.2px}\n.ta-btn i{width:6px;height:6px;border-radius:50%;background:#fff;display:block;flex-shrink:0}\n/* pastilles de l etape sur une seule ligne : texte sans icone, espacement resserre */\n.tc .maps-btn,.tc .info-btn,.tc .web-btn,.tc .pay-btn,.tc .ta-btn{padding:6px 9px!important;gap:4px!important}\n.tc .maps-btn svg,.tc .info-btn svg,.tc .web-btn svg{display:none!important}\n.tc div:has(>.maps-btn,>.info-btn,>.web-btn,>.pay-btn){gap:5px!important}\n.tc2.tc2-ok{", 1)
html = html.replace(".tc2.tc2-ok{", ".tc2.tc2-free{background:#ECE9E2!important;color:#6d655b!important;max-width:none;letter-spacing:.4px;font-weight:700}\n.tc2.tc2-ok{", 1)
# ---- charte Lagon (OUTILS/theme_lagon.py), appliquee en dernier
import theme_lagon
html = theme_lagon.apply(html, {
    "cover_photo": "ile-de-sal.jpg",
    "cover_label": "☀️ AVANT LES PIEDS DANS LE SABLE",
    "day_photos": {0: "transavia.jpg", 1: "angulo.jpg", 2: "bikini-piscine.jpg", 3: "ponton-santa-maria.jpg", 4: "oeil-bleu.jpg",
                   5: "catamaran-voile.jpg", 6: "pecheur-plage.jpg", 7: "white-party.jpg", 8: "ile-de-sal.jpg"},
    "day_pos": {2: "center 72%", 5: "center 88%", 6: "center 66%"},
    "resa_view": D.RESA_VIEW,
    "chk_deadlines": {c["id"]: fr(c["deadline"]) for c in D.CHK_ITEMS},
    "icon": True,
})
open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8").write(html)

# ---------------------------------------------------------------- sw.js (base : sw du modele)
SW = """const CACHE = '%s%s';
const PREFIX = '%s';

const CORE = [
  './',
  './index.html',
];

// Photos des fiches : ajouter ici './nom-du-fichier.jpg' une fois deposees sur GitHub.
const IMAGES = [
%s];

self.addEventListener('message', e => {
  if (e.data === 'skipWaiting') self.skipWaiting();
});

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(cache =>
      cache.addAll(CORE).then(() =>
        Promise.all(IMAGES.map(url => cache.add(url).catch(() => null)))
      )
    )
  );
  self.skipWaiting();
});

// Ne purge que les anciennes versions DE CE CARNET : les autres carnets
// heberges sur le meme compte GitHub (meme domaine) gardent leur cache.
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k.indexOf(PREFIX) === 0 && k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  const isImage = /\\.(jpg|jpeg|png|webp|gif|svg)$/i.test(url.pathname);

  if (isImage) {
    // Images : cache-first (elles ne changent pas, rapide + hors-ligne)
    e.respondWith(
      caches.match(req).then(cached =>
        cached || fetch(req).then(resp => {
          if (resp && resp.status === 200 && resp.type === 'basic') {
            const clone = resp.clone();
            caches.open(CACHE).then(cache => cache.put(req, clone));
          }
          return resp;
        }).catch(() => cached)
      )
    );
    return;
  }

  // HTML / code / reste : NETWORK-FIRST
  // => a chaque ouverture en ligne, on recupere la derniere version GitHub.
  // Hors-ligne : on sert la derniere version mise en cache.
  e.respondWith(
    fetch(req).then(resp => {
      if (resp && resp.status === 200 && resp.type === 'basic') {
        const clone = resp.clone();
        caches.open(CACHE).then(cache => cache.put(req, clone));
      }
      return resp;
    }).catch(() =>
      caches.match(req).then(cached => cached || caches.match('./index.html'))
    )
  );
});
""" % (PREFIX, STAMP, PREFIX, "".join("  './%s',\n" % f for f in sorted({v["image"] for v in D.INFO.values() if isinstance(v, dict) and v.get("image")} | {"plan-sal.jpg", "ile-de-sal.jpg", "transavia.jpg"} | set(D.WALK_IMGS))))
open(os.path.join(out_dir, "sw.js"), "w", encoding="utf-8").write(SW)
print("OK", STAMP, len(html) // 1024, "Ko")
