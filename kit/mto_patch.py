"""Evolutions du moteur MTO (octobre 2026, carnet Cap-Vert), applicables a tout carnet.

1. Pastille rouge A RESERVER : RESA_TODO = {titre d evenement: id de la checklist}.
   La pastille remplace le cout tant que la case de la checklist n est pas cochee,
   puis devient verte (RESERVE) une fois la case cochee. Un cout "Paye" ou "Reserve" s affiche aussi en vert.
2. Pastille Web : WEB_DATA = {titre: {name, sub, tel, wa, telLabel, telPretty, links:[[libelle, url]]}}.
   Ouvre une fenetre en bas d ecran : appel direct, WhatsApp, liens.
3. Icone discrete devant le titre : THEME_EVENTS = {titre: emoji}.
   Conventions : cafe petit-dejeuner, assiette restaurant, cocktail bar/apero, parasol farniente,
   boussole visite, taxi, voiture. THEME_UP = emojis a remonter de 3 px pour l alignement.
4. Numeros WhatsApp cliquables : tout numero de mobile ecrit au format international
   (+238 9xx xx xx, +351 9xx xxx xxx, +33 6 xx xx xx xx...) devient un lien wa.me
   dans les textes des etapes, des fiches et des listes. WA_EXTRA = autres numeros a lier.

Usage : html = mto_patch.apply(html, resa_todo={}, icons={}, web={}, wa_extra=[])
"""
import json

THEME_UP = ["\U0001F695", "\U0001F697", "☕"]

CSS = (".web-btn{background:#fff;color:var(--c-sg);box-shadow:inset 0 0 0 1.5px var(--c-sg)}\n"
       ".web-btn:active{transform:scale(.94)}\n"
       ".thi{display:inline-block;font-size:15px;line-height:1;margin-right:6px;vertical-align:-1px}.thi.thi-up{vertical-align:2px}\n"
       ".tc2.tc2-resa{background:var(--c-osaka)!important;color:#fff!important;max-width:none;letter-spacing:.4px;font-weight:800}\n"
       ".tc2.tc2-ok{background:#2E6B3E!important;color:#fff!important;max-width:none;letter-spacing:.4px;font-weight:800}\n"
       ".wsv{position:fixed;inset:0;background:rgba(0,0,0,.38);z-index:9998}\n"
       ".wsh{position:fixed;left:0;right:0;bottom:0;background:#fff;border-radius:22px 22px 0 0;box-shadow:0 -8px 30px rgba(0,0,0,.25);padding:18px 18px calc(22px + env(safe-area-inset-bottom));z-index:9999;max-height:80vh;overflow:auto;font-family:-apple-system,sans-serif}\n"
       ".wsh h3{font-family:Georgia,'Times New Roman',serif;font-size:19px;margin:0 34px 4px 0;color:#1d1d1d}\n"
       ".wsh .wsub{font-size:12px;color:#777;margin-bottom:14px;line-height:1.5}\n"
       ".wsh a{display:flex;align-items:center;gap:10px;padding:13px 14px;border-radius:12px;margin-bottom:9px;text-decoration:none;font-weight:700;font-size:14px}\n"
       ".wsh .w-tel{background:#2E6B3E;color:#fff}.wsh .w-wa{background:var(--c-sg);color:#fff}.wsh .w-lnk{background:#f2f2f2;color:#333}\n"
       ".wsh .wx{position:absolute;top:14px;right:14px;width:32px;height:32px;border-radius:50%;border:none;background:#f0f0f0;font-size:16px;color:#555}\n"
       ".pay-btn{cursor:default;background:#fff;color:#3d4350;box-shadow:inset 0 0 0 1px #d9d4c7}.pay-cash{color:#9A6A1E;box-shadow:inset 0 0 0 1px #E8D3A8;background:#FCF6EA}.pay-card{color:#2E6B3E;box-shadow:inset 0 0 0 1px #BFDCC8;background:#F1F8F3}\n"
       ".wa-lnk{color:#2E6B3E;font-weight:700;text-decoration:underline;white-space:nowrap}.tel-lnk{color:var(--c-sg);font-weight:700;text-decoration:underline;white-space:nowrap}")

JS = r"""function closeWeb(){var a=document.getElementById('wsv'),b=document.getElementById('wsh');if(a)a.remove();if(b)b.remove();}
function openWeb(btn){
  var d=WEB_DATA[btn.getAttribute('data-key')]; if(!d) return; closeWeb();
  function esc(t){return String(t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');}
  var h='<button class="wx" onclick="closeWeb()">&#10005;</button><h3>'+esc(d.name)+'</h3><div class="wsub">'+esc(d.sub||'')+'</div>';
  if(d.tel){
    var pretty=d.telPretty||d.tel.replace(/^\+238(\d{3})(\d{2})(\d{2})$/,'+238 $1 $2 $3');
    h+='<a class="w-tel" href="tel:'+d.tel+'">&#128222; '+esc(d.telLabel||'Appeler pour reserver')+' : '+esc(pretty)+'</a>';
    if(d.wa) h+='<a class="w-wa" href="https://wa.me/'+d.tel.replace(/\D/g,'')+'" target="_blank" rel="noopener">&#128172; WhatsApp</a>';
  }
  (d.links||[]).forEach(function(l){h+='<a class="w-lnk" href="'+esc(l[1])+'" target="_blank" rel="noopener">&#127760; '+esc(l[0])+'</a>';});
  var v=document.createElement('div');v.id='wsv';v.className='wsv';v.onclick=closeWeb;
  var s=document.createElement('div');s.id='wsh';s.className='wsh';s.innerHTML=h;
  document.body.appendChild(v);document.body.appendChild(s);
}
// Numeros de mobile au format international -> lien WhatsApp
var WA_RE=/\+(?:238 [59]\d{2} \d{2} \d{2}|351 9\d{2} \d{3} \d{3}|33 [67](?: \d{2}){4}|34 [67]\d{2}(?: \d{3}){2}|39 3\d{2} \d{3} \d{3,4}|44 7\d{3} \d{6}|65 [89]\d{3} \d{4}|81 [789]0(?:[ -]\d{4}){2})/g;
function waA(m){return '<a class="wa-lnk" href="https://wa.me/'+m.replace(/\D/g,'')+'" target="_blank" rel="noopener" onclick="event.stopPropagation()">&#128172; '+m+'</a>';}
// Tout numero international : mobile -> WhatsApp, fixe -> appel direct
var PH_RE=/\+\d{2,3}(?:[ -]\d{1,4}){2,5}/g;
var WA_TEST=new RegExp('^(?:'+WA_RE.source+')$');
function telA(m){return '<a class="tel-lnk" href="tel:'+m.replace(/[^\d+]/g,'')+'" onclick="event.stopPropagation()">&#128222; '+m+'</a>';}
function waLink(h){
  var extra=(typeof WA_EXTRA!=="undefined"?WA_EXTRA:[]);
  return String(h).replace(PH_RE,function(m){return (WA_TEST.test(m)||extra.indexOf(m)>=0)?waA(m):telA(m);})
    .replace(/\[([^\]]+)\]\((https:[^)\s]+)\)/g,'<a href="$2" target="_blank" rel="noopener" onclick="event.stopPropagation()" style="color:#B8923D;font-weight:700;text-decoration:underline">$1</a>');
}
"""


def apply(html, resa_todo=None, icons=None, web=None, wa_extra=None, pay=None):
    def rep(old, new):
        nonlocal html
        n = html.count(old)
        if n != 1:
            raise SystemExit("mto_patch : ancre trouvee %d fois : %r" % (n, old[:90]))
        html = html.replace(old, new)

    rep(".maps-btn,.info-btn,.share-btn,.walk-btn,.uber-btn,.grab-btn,.copy-btn,.boat-btn,.train-btn,.plane-btn,.cal-btn,.car-btn,.nav-btn{",
        ".maps-btn,.info-btn,.share-btn,.walk-btn,.uber-btn,.grab-btn,.copy-btn,.boat-btn,.train-btn,.plane-btn,.cal-btn,.car-btn,.nav-btn,.web-btn,.pay-btn{")
    rep(".car-btn{background:var(--ink);color:#fff;cursor:default}",
        ".car-btn{background:var(--ink);color:#fff;cursor:default}\n" + CSS)
    rep("""    var cost=(ev.cost&&ev.cost!=="---")?'<div class="tc2">'+e(ev.cost)+'</div>':"";""",
        """    var cost=(ev.cost&&ev.cost!=="---")?'<div class="tc2">'+e(ev.cost)+'</div>':"";
    if(/^(R[ée]serv[ée]|Pay[ée])/i.test(ev.cost||"")) cost='<div class="tc2 tc2-ok">&#10003; '+e(ev.cost).toUpperCase()+'</div>';
    if(typeof RESA_TODO!=="undefined" && RESA_TODO[ev.title]) cost=loadChkState()[RESA_TODO[ev.title]]?'<div class="tc2 tc2-ok">&#10003; RESERVE</div>':'<div class="tc2 tc2-resa">A RESERVER</div>';
    var themeBtn="";
    if(typeof THEME_EVENTS!=="undefined" && THEME_EVENTS[ev.title]) themeBtn='<span class="thi'+(THEME_UP.indexOf(THEME_EVENTS[ev.title])>=0?' thi-up':'')+'">'+THEME_EVENTS[ev.title]+'</span>';
    var payBtn="", _p=(typeof PAY_EVENTS!=="undefined")?PAY_EVENTS[ev.title]:null;
    if(_p){var _pl={carte:["pay-card","&#128179; Carte"],especes:["pay-cash","&#128182; Esp&egrave;ces"],plutot:["pay-cash","&#128182; Esp&egrave;ces ?"],les2:["pay-card","&#128179; Carte ou esp&egrave;ces"],verifier:["","&#10068; &Agrave; v&eacute;rifier"]}[_p]; if(_pl) payBtn='<span class="pay-btn '+_pl[0]+'">'+_pl[1]+'</span>';}
    var webBtn="";
    if(typeof WEB_DATA!=="undefined" && WEB_DATA[ev.title]) webBtn='<button class="web-btn" onclick="openWeb(this)" data-key="'+ev.title.replace(/"/g,"&quot;")+'">&#127760; Web</button>';""")
    rep("""+navBtn+infoBtn+calBtn+'</div>""", """+navBtn+payBtn+infoBtn+webBtn+calBtn+'</div>""")
    rep("""<div class="tti">'+e(ev.title)+'</div>""", """<div class="tti">'+themeBtn+e(ev.title)+'</div>""")
    rep("""<div class="tb2">'+e(ev.body)+'</div>""", """<div class="tb2">'+waLink(e(ev.body))+'</div>""")
    rep("""<div class="elv">'+e(es.val)+'</div>""", """<div class="elv">'+waLink(e(es.val))+'</div>""")
    rep("""<span>'+infoEsc(lignes[i])+'</span>""", """<span>'+waLink(infoEsc(lignes[i]))+'</span>""")
    rep("""<div class="tipt">'+e(curDay.tip)+'</div>""", """<div class="tipt">'+waLink(e(curDay.tip))+'</div>""")
    rep("""white-space:pre-wrap">' + infoEsc(d.intro) + '</div>';""", """white-space:pre-wrap">' + waLink(infoEsc(d.intro)) + '</div>';""")
    rep("""        + infoEsc(d.conseil) + '</div>';""", """        + waLink(infoEsc(d.conseil)) + '</div>';""")
    tables = ("// === Evolutions MTO : pastilles A RESERVER / Web, icones de titre, liens WhatsApp ===\n"
              "var RESA_TODO = " + json.dumps(resa_todo or {}, ensure_ascii=False) + ";\n"
              "var THEME_EVENTS = " + json.dumps(icons or {}, ensure_ascii=False) + ";\n"
              "var THEME_UP = " + json.dumps(THEME_UP, ensure_ascii=False) + ";\n"
              "var WEB_DATA = " + json.dumps(web or {}, ensure_ascii=False) + ";\n"
              "var WA_EXTRA = " + json.dumps(wa_extra or [], ensure_ascii=False) + ";\n"
              "var PAY_EVENTS = " + json.dumps(pay or {}, ensure_ascii=False) + ";\n")
    rep("var DEFAULT_RESA_DONE =", tables + JS + "var DEFAULT_RESA_DONE =")
    return html


# ---------------------------------------------------------------- confort de lecture et navigation (oct. 2026)
UX_CSS = (".tdep{font-family:-apple-system,sans-serif;font-size:11.5px;color:#8a8478;margin:2px 0 6px;line-height:1.45}\n"
          ".tb2.clamp{display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}.tb2.clamp.open{display:block}\n"
          ".more-btn{background:none;border:none;padding:0 0 2px;margin:-2px 0 0;font-family:-apple-system,sans-serif;font-size:12px;font-weight:700;color:var(--gold-deep);cursor:pointer}\n"
          ".brief{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 14px;padding:10px 12px;background:#fff;border-radius:14px;box-shadow:0 2px 8px rgba(0,0,0,.05)}\n"
          ".brief span{font-family:-apple-system,sans-serif;font-size:12px;font-weight:600;color:#3d4350;background:#f6f3ec;border-radius:20px;padding:5px 10px;line-height:1.3}\n"
          ".brief span.br-resa{background:#FBEDE9;color:var(--c-osaka)}\n"
          ".dic{font-size:16px;letter-spacing:4px}\n"
          ".di-s{font-family:-apple-system,sans-serif;font-size:10px;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:#8a8478;margin-top:3px;line-height:1.35}\n"
          ".dd-l{white-space:normal!important;overflow:visible!important}\n"
          ".chk-done-wrap summary{list-style:none;cursor:pointer;padding:12px 14px;font-family:-apple-system,sans-serif;font-size:12px;font-weight:700;color:#2E6B3E;border-top:1px solid #eee}\n"
          ".chk-done-wrap summary::-webkit-details-marker{display:none}\n"
          ".iact{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 10px}\n"
          ".iact a{font-family:-apple-system,sans-serif;display:inline-flex;align-items:center;gap:5px;border-radius:20px;padding:6px 12px;font-size:12px;font-weight:700;text-decoration:none}\n"
          ".iact .ia-tel{background:#2E6B3E;color:#fff}.iact .ia-wa{background:var(--c-sg);color:#fff}.iact .ia-web{background:#fff;color:var(--c-sg);box-shadow:inset 0 0 0 1.5px var(--c-sg)}.iact .ia-map{background:#E7F0F2;color:var(--c-sg)}\n")

LABELS = [("BON A SAVOIR", "BON À SAVOIR"), ("AUJOURD HUI", "AUJOURD’HUI"), ("Decouvrir<", "Découvrir<"),
          ("A ne pas manquer", "À ne pas manquer"), ("Duree conseillee", "Durée conseillée"),
          ('it:"Itineraire"', 'it:"Itinéraire"'), (">Itineraire<", ">Itinéraire<"), ("Vols et Reservations", "Vols et Réservations"),
          ("Meteo en direct", "Météo en direct"), ("Chargement de la meteo", "Chargement de la météo"),
          ("Meteo non disponible", "Météo non disponible"), ("Aucun detail enregistre", "Aucun détail enregistré"),
          ("Confirmation de reservation", "Confirmation de réservation"), ("la derniere version", "la dernière version"),
          ("RESERVATIONS ESSENTIELLES", "RÉSERVATIONS ESSENTIELLES"), ("Checklist Reservations", "Checklist réservations"),
          ("&#10003; Reserve !", "&#10003; Réservé !"), ("&#129406; A pied", "&#129406; À pied"),
          ("Voir details", "Voir détails"), ('>A RESERVER<', '>À RÉSERVER<'), ('&#10003; RESERVE<', '&#10003; RÉSERVÉ<'), ("Parite fixe avec l euro", "Parité fixe avec l’euro"), (" - Details reservation", " - Détails réservation")]


def apply_ux(html, budget=None):
    def rep(old, new, count=1):
        nonlocal html
        n = html.count(old)
        if n != count:
            raise SystemExit("mto_patch.ux : ancre trouvee %d fois : %r" % (n, old[:90]))
        html = html.replace(old, new)

    rep("border:none;border-radius:20px;padding:6px 12px;font-size:11px;font-weight:600;cursor:pointer;",
        "border:none;border-radius:20px;padding:6px 10px;font-size:11px;font-weight:600;cursor:pointer;")
    rep("var DEFAULT_RESA_DONE =", "var BUDGET_DATA = " + json.dumps(budget or {}, ensure_ascii=False) + ";\nvar DEFAULT_RESA_DONE =")
    # Mes notes : les numeros de telephone ecrits dans la note deviennent des boutons WhatsApp / appel sous la zone de texte
    rep("""'<div id="dayNoteStatus" style="font-size:10px;color:#BBB;margin-top:5px;min-height:12px"></div>'+""",
        """'<div id="dayNoteLinks" style="display:flex;flex-wrap:wrap;gap:8px;margin-top:8px"></div>'+
    '<div id="dayNoteStatus" style="font-size:10px;color:#BBB;margin-top:5px;min-height:12px"></div>'+""")
    rep("""  var status=document.getElementById("dayNoteStatus");
  var timer=null;""", """  var status=document.getElementById("dayNoteStatus");
  var timer=null;
  noteLinks(ta.value);""")
    rep("""    var val=ta.value;
    timer=setTimeout(function(){""", """    var val=ta.value;
    noteLinks(val);
    timer=setTimeout(function(){""")
    rep("function bindDayNote(){", """function noteLinks(val){
  var box=document.getElementById("dayNoteLinks"); if(!box) return;
  var seen={}, h="", extra=(typeof WA_EXTRA!=="undefined"?WA_EXTRA:[]);
  (String(val||"").match(PH_RE)||[]).forEach(function(m){
    var k=m.replace(/\D/g,""); if(seen[k]) return; seen[k]=1;
    var wa=WA_TEST.test(m)||extra.indexOf(m)>=0;
    h+=wa?'<a href="https://wa.me/'+k+'" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:6px;font-family:-apple-system,sans-serif;background:#25D366;color:#fff;font-weight:700;font-size:13px;padding:8px 13px;border-radius:20px;text-decoration:none">&#128172; WhatsApp '+m+'</a>'
         :'<a href="tel:'+m.replace(/[^\d+]/g,"")+'" style="display:inline-flex;align-items:center;gap:6px;font-family:-apple-system,sans-serif;background:#2E6B3E;color:#fff;font-weight:700;font-size:13px;padding:8px 13px;border-radius:20px;text-decoration:none">&#128222; Appeler '+m+'</a>';
  });
  box.innerHTML=h; box.style.display=h?"flex":"none";
}
function bindDayNote(){""")
    rep(".scroll-top{position:fixed;bottom:calc(72px + env(safe-area-inset-bottom,0px));right:16px;width:44px;height:44px;",
        ".scroll-top{position:fixed;bottom:calc(72px + env(safe-area-inset-bottom,0px));left:10px;width:38px;height:38px;")
    rep(".car-btn{background:var(--ink);color:#fff;cursor:default}", ".car-btn{background:var(--ink);color:#fff;cursor:default}\n" + UX_CSS)
    # 2. carte : ligne deplacement + texte replie a 3 lignes
    rep("""<div class="tb2">'+waLink(e(ev.body))+'</div>""",
        """'+_dep+'<div class="tb2'+(_long?' clamp':'')+'">'+waLink(e(_bd))+'</div>'+(_long?'<button class="more-btn" onclick="var b=this.previousElementSibling;b.classList.toggle(\\'open\\');this.innerHTML=b.classList.contains(\\'open\\')?\\'R&eacute;duire &#9652;\\':\\'Lire la suite &#9662;\\'">Lire la suite &#9662;</button>':'')+'""")
    rep("""    var themeBtn="";""", """    var _bd=ev.body||"",_dep="",_mm=_bd.match(/^D[e\\u00e9]placement : (.+?)\\.(?:\\s+|$)/);
    if(_mm){_dep='<div class="tdep">'+e(_mm[1])+'</div>';_bd=_bd.slice(_mm[0].length);}
    var _long=_bd.length>190;
    var themeBtn="";""")
    # 3. encart du jour en haut
    rep("""  var tip=curDay.tip?""", """  var _br=(curDay.brief||[]).slice(), _nr=0, _cs=loadChkState();
  if(typeof RESA_TODO!=="undefined") curDay.events.forEach(function(ev){ if(RESA_TODO[ev.title] && !_cs[RESA_TODO[ev.title]]) _nr++; });
  var brief=(_br.length||_nr)?'<div class="brief">'+(_nr?'<span class="br-resa">&#128308; '+_nr+' &agrave; r&eacute;server</span>':'')+_br.map(function(x){return '<span>'+e(x)+'</span>'}).join('')+'</div>':'';
  var tip=curDay.tip?""")
    rep("""'<div class="tl">'+evh+tip+note+perso+'</div>'""", """'<div class="tl">'+brief+evh+tip+note+perso+'</div>'""")
    # 4. liste des jours : icones des temps forts, theme du jour, hotel seulement quand il change
    rep("""  var h="",last=null,tid=getTid();\n  DYS.forEach(function(day){""", """  var h="",last=null,tid=getTid(),_prevH=null;\n  DYS.forEach(function(day){""")
    rep("""    var pills=types.map(function(t){return'<span class="pl '+pcls(t)+'">'+plbl(t)+'</span>'}).join("");
    var more=day.events.length-4;""", """    var _ic=[],_sn={};
    day.events.forEach(function(ev){var x=(typeof THEME_EVENTS!=="undefined")&&THEME_EVENTS[ev.title];if(x&&!_sn[x]&&x!=="\\uD83D\\uDE95"&&x!=="\\uD83D\\uDE97"){_sn[x]=1;_ic.push(x)}});
    var pills=_ic.length?'<span class="dic">'+_ic.join(' ')+'</span>':types.map(function(t){return'<span class="pl '+pcls(t)+'">'+plbl(t)+'</span>'}).join("");
    var more=_ic.length?0:day.events.length-4;
    var _sub=day.label.split(" - ").slice(1).join(" - ");
    var _showH=(day.hotel!==_prevH); _prevH=day.hotel;""")
    rep("""<div class="di-l">'+e(day.location)+'</div>""", """'+(_ic.length&&_sub?'<div class="di-s">'+e(_sub)+'</div>':'<div class="di-l">'+e(day.location)+'</div>')+'""")
    rep("""    h+='<div class="dh" style="background:'+ch.color+'">'+e(day.hotel.replace(" *****",""))+'</div></div>';""",
        """    h+=(_showH?'<div class="dh" style="background:'+ch.color+'">'+e(day.hotel.replace(" *****",""))+'</div>':'')+'</div>';""")
    # 5. barre du haut : bouton retour compact (le logo ne deborde plus)
    rep(""">&#8592; Retour</button>""", """ aria-label="Retour">&#8592;</button>""")
    # pastille Calendrier retiree (sans interet a l usage)
    rep("""+infoBtn+webBtn+calBtn+'</div>""", """+infoBtn+webBtn+'</div>""")
    # la pastille "A pied" fait doublon avec la ligne de deplacement : on la retire quand cette ligne existe
    rep("""'+mapsHtml+planeBtn+walkBtn+""", """'+mapsHtml+planeBtn+(_dep?'':walkBtn)+""")
    # 6. checklist : a faire d abord, deja fait replie
    rep("""  chkItems.forEach(function(item){
    var done = !!chkState[item.id];""", """  var _row=function(item){
    var done = !!chkState[item.id];""")
    rep("""    hChk += '</div></div>';
  });
  hChk+='</div>';""", """    hChk += '</div></div>';
  };
  var _todo=chkItems.filter(function(i){return !chkState[i.id]}), _ok=chkItems.filter(function(i){return chkState[i.id]});
  _todo.forEach(_row);
  if(_ok.length){ hChk+='<details class="chk-done-wrap"><summary>&#10003; D&eacute;j&agrave; r&eacute;serv&eacute; ('+_ok.length+') &#9662;</summary>'; _ok.forEach(_row); hChk+='</details>'; }
  hChk+='</div>';""")
    # 8. bouton Aujourd hui dans la barre du bas
    rep("""<span class="nb-l">Jours</span></button>""", """<span class="nb-l">Jours</span></button>
    <button class="nb" id="n-td" onclick="goToday()"><span class="nb-i">&#128205;</span><span class="nb-l">Aujourd&rsquo;hui</span></button>""")
    rep("""function goBack(){showS("it")}""", """function goBack(){showS("it")}
function goToday(){var t=getTid();var d=t?DYS.find(function(x){return x.id===t}):null;if(!d){d=DYS.find(function(x){return x.chap!==DYS[0].chap})||DYS[0];}openDay(d.id);}""")
    # 8. fiche : barre d actions en haut (appeler, WhatsApp, site, Maps)
    rep("""    <div id="infoImg" style="display:none;margin:12px 0 4px"></div>""",
        """    <div id="infoAct" class="iact"></div>\n    <div id="infoImg" style="display:none;margin:12px 0 4px"></div>""")
    rep("""  var body = document.getElementById("infoBody");""", """  var _ia=document.getElementById("infoAct");
  if(_ia){
    var _w=(typeof WEB_DATA!=="undefined")?WEB_DATA[key]:null, _a="";
    if(_w&&_w.tel){_a+='<a class="ia-tel" href="tel:'+_w.tel+'">&#128222; Appeler</a>'; if(_w.wa)_a+='<a class="ia-wa" href="https://wa.me/'+_w.tel.replace(/\\D/g,'')+'" target="_blank" rel="noopener">&#128172; WhatsApp</a>';}
    if(_w&&_w.links&&_w.links.length&&_w.links[0][1].indexOf('google.com/maps')<0)_a+='<a class="ia-web" href="'+_w.links[0][1]+'" target="_blank" rel="noopener">&#127760; Web</a>';
    var _mu=d.mapsUrl||("https://www.google.com/maps/search/?api=1&query="+encodeURIComponent(d.title));
    _a+='<a class="ia-map" href="'+_mu+'" target="_blank" rel="noopener">&#128205; Maps</a>';
    _ia.innerHTML=_a;
  }
  var body = document.getElementById("infoBody");""")
    # accordeon Budget par couple (onglet Infos), si BUDGET_DATA est rempli
    rep("""  h+=acc('&#9989; Checklist Reservations ('+doneCount+'/'+chkItems.length+')', hChk, true);""",
        """  h+=acc('&#9989; Checklist Reservations ('+doneCount+'/'+chkItems.length+')', hChk, true);
  if(typeof BUDGET_DATA!=="undefined" && BUDGET_DATA && BUDGET_DATA.days && BUDGET_DATA.days.length){
    var B=BUDGET_DATA, fm=function(n){return Math.round(n).toLocaleString('fr-FR').replace(/\s/g,'&#8239;')+'&nbsp;&euro;'};
    var td='padding:7px 6px;border-bottom:1px solid #f0ece2;font-size:12.5px;color:#3d4350', tn=';text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums;width:62px;vertical-align:top', th='padding:6px;font-size:10px;font-weight:800;letter-spacing:.8px;text-transform:uppercase;color:#8a8478;text-align:right';
    var se=0, sc=0, hb='<div style="font-size:12px;color:#777;line-height:1.6;margin-bottom:10px">'+e(B.intro||'')+'</div>';
    hb+='<table style="width:100%;border-collapse:collapse"><tr><th style="'+th+';text-align:left">Sur place</th><th style="'+th+';width:62px;white-space:nowrap">&#128182;<br>Esp&egrave;ces</th><th style="'+th+';width:62px;white-space:nowrap">&#128179;<br>Carte</th></tr>';
    B.days.forEach(function(r){ se+=r[1]; sc+=r[2]; hb+='<tr><td style="'+td+'"><b>'+e(r[0])+'</b><div style="font-size:11px;color:#999;line-height:1.4">'+e(r[3]||'')+'</div></td><td style="'+td+tn+'">'+fm(r[1])+'</td><td style="'+td+tn+'">'+fm(r[2])+'</td></tr>'; });
    var tt=';border-top:2px solid #d9d2c2;border-bottom:none;padding-top:10px;font-weight:800;font-size:13.5px';
    hb+='<tr><td style="'+td+tt+'">Total par couple</td><td style="'+td+tn+tt+';color:#9A6A1E">'+fm(se)+'</td><td style="'+td+tn+tt+';color:#2E6B3E">'+fm(sc)+'</td></tr></table>';
    var tot=se+sc;
    [['paid','D&eacute;j&agrave; pay&eacute;'],['before','Avant le d&eacute;part (estimation)']].forEach(function(g){
      var L=B[g[0]]||[]; if(!L.length) return; var st=0;
      hb+='<div style="margin-top:14px;font-size:10px;font-weight:800;letter-spacing:.8px;text-transform:uppercase;color:#8a8478">'+g[1]+'</div><table style="width:100%;border-collapse:collapse">';
      L.forEach(function(r){ st+=r[1]; hb+='<tr><td style="'+td+'">'+e(r[0])+(r[2]?'<div style="font-size:11px;color:#999">'+e(r[2])+'</div>':'')+'</td><td style="'+td+tn+'">'+fm(r[1])+'</td></tr>'; });
      hb+='</table>'; tot+=st;
    });
    hb+='<div style="margin-top:14px;background:#1d1d1d;color:#F6F1E7;border-radius:12px;padding:12px 14px;display:flex;justify-content:space-between;align-items:center"><span style="font-size:12px;font-weight:700;letter-spacing:.5px">'+((B.paid&&B.paid.length)||(B.before&&B.before.length)?'TOTAL DU S&Eacute;JOUR PAR COUPLE':'TOTAL SUR PLACE PAR COUPLE')+'</span><span style="font-size:18px;font-weight:800;color:#C9A84C;white-space:nowrap;font-variant-numeric:tabular-nums">'+fm(tot)+'</span></div>';
    hb+='<div style="margin-top:8px;font-size:11.5px;color:#666;line-height:1.6">Sur place : '+fm(se)+' en esp&egrave;ces et '+fm(sc)+' par carte. '+e(B.note||'')+'</div>';
    h+=acc('&#128182; '+(B.title?e(B.title):'Budget par couple'), hb, false);
  }""")
    for a, b in LABELS:
        html = html.replace(a, b)
    return html
