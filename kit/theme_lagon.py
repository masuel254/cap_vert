# -*- coding: utf-8 -*-
"""
theme_lagon.py - charte « Lagon » pour les carnets MTO (validee sur le carnet Cap-Vert, oct. 2026)

A appliquer EN DERNIER sur le index.html final (apres injection des donnees et mto_patch),
juste avant de l ecrire sur disque :

    import theme_lagon
    html = theme_lagon.apply(html, {
        "cover_photo": "ile-de-sal.jpg",              # photo plein ecran de la couverture (fournie par Samuel)
        "cover_label": "☀️ AVANT LES PIEDS DANS LE SABLE",   # libelle du compte a rebours avant depart
        "day_photos": {1: "angulo.jpg", 2: "bikini.jpg"},  # id du jour -> photo (bandeau liste + en-tete du jour)
        "resa_view": RESA_VIEW,                        # optionnel : vue « billets » des reservations (voir CHARTE_LAGON.md)
        "chk_deadlines": {"vols": "PAYÉ", ...},          # optionnel : texte de secours du detail d un billet (id -> deadline)
        "icon": True,                                  # declare apple-touch-icon.png et icon-512.png
    })

Ce que fait le theme (rien dans les donnees ni dans le moteur ne change) :
  1. Couverture : photo plein ecran, degrade bleu nuit, chiffres sable, bouton turquoise.
  2. Interieur « Lagon de nuit » : variables :root (ink bleu nuit, accents turquoise, sable sur fond sombre).
  3. Finitions : icones au trait (barre du bas, accueil, recherche, pastilles Maps/Infos/Web),
     etiquettes de jour (Petit-dej, Plage, Visite, Restos, Soiree), cartes creme a liseré par type,
     pastilles unifiees, photos dans la liste des jours et les en-tetes de jour.
  4. Reservations en « billets » (si resa_view fourni) : a reserver groupees par date avec action
     directe (WhatsApp / lien), reservations faites en billets (talon date, ref, Paye/Reserve, Especes).
  5. Passe finale : plus aucun or ni brun hors logo MTO (le T du logo reste or #B8923D).
Les couleurs de sens ne bougent pas : rouge « A reserver », vert « Reserve », ambre « Especes ».
"""
import json, re

PALETTE = {
    "nuit": "#0F1B23", "nuit_2": "#17303D", "nuit_3": "#24414F",
    "turquoise": "#1F8FA6", "turquoise_clair": "#2BB3C0", "turquoise_fonce": "#177688",
    "sable": "#F2D08A", "papier": "#F5F1E8", "carte": "#FFFEFA",
    "trajet": "#1F8FA6", "visite": "#E0A93B", "repas": "#D9654B", "logement": "#2E8B6E", "soiree": "#3B5A8C",
}

DAY_TAGS_DEFAULT = {"☕": ["coffee", "Petit-déj"], "🏖️": ["beach", "Plage"], "🧭": ["compass", "Visite"],
                    "🍽️": ["fork", "Restos"], "🍹": ["glass", "Soirée"]}

COVER_CSS = r"""#cover{background:#0f1b23;justify-content:flex-start;padding-top:max(env(safe-area-inset-top),34px)}
#cover::before,#cover::after{display:none}
#cover>.cv-photo{position:absolute;left:0;right:0;top:0;height:66%;z-index:0;opacity:1;animation:none;
  background:url(__COVER_PHOTO__) 30% center/cover no-repeat}
#cover>.cv-shade{position:absolute;inset:0;z-index:0;opacity:1;animation:none;
  background:linear-gradient(180deg,rgba(10,20,28,.7) 0%,rgba(10,20,28,0) 24%,rgba(10,20,28,0) 36%,rgba(14,26,34,.8) 50%,#0f1b23 64%)}
#cover #mtoLogo{margin:0 auto auto;max-width:72%;filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))}
#cover .cv-line{display:none}
#cover .cv-tag{color:#F2D08A;margin-bottom:12px;text-shadow:0 1px 6px rgba(0,0,0,.5)}
#cover .cv-big{text-shadow:0 2px 14px rgba(0,0,0,.35)}
#cover .cv-amp{color:#F2D08A}
#cover .cv-date{color:#CFE7EC;margin-top:16px}
#cover .cv-stats{margin-top:18px}
#cover .cv-stat{background:rgba(255,255,255,.07);border-color:rgba(242,208,138,.35)}
#cover .cv-sn{color:#F2D08A}
#cover .cv-sl{color:#B9CDD3}
#cover .cv-route{margin-top:14px}
#cover .cv-route span{color:#9FB6BD}
#cover .cv-hl{color:#CFE7EC !important}
#cover .cv-dot{background:#2BB3C0;opacity:.9}
#cover #cd-label{color:#9FB6BD !important;font-size:10px !important}
#cover #countdown>div>div{background:rgba(255,255,255,.08) !important}
#cover #cd-days,#cover #cd-hours,#cover #cd-mins{color:#F2D08A !important;font-family:Georgia,serif;font-weight:400 !important}
#cover #countdown>div>div>div:last-child{color:#B9CDD3 !important}
#cover #startBtn{margin-top:24px;margin-bottom:12px;background:linear-gradient(90deg,#2BB3C0,#1F8FA6);color:#fff;box-shadow:0 8px 26px rgba(43,179,192,.35)}
#cover #startBtn:active{box-shadow:0 4px 14px rgba(43,179,192,.3)}
"""
INTERIOR_CSS = r""":root{--ink:#0F1B23;--ink-soft:#24414F;--gold:#1F8FA6;--gold-deep:#177688;--gold-soft:#F2D08A;--gold-tint:#E2F2F4;--paper:#F5F1E8;--paper-2:#FAF7F0;--line:#DCE6E4;--muted:#7C8A8E;--muted-2:#9AA9AD;--c-sg:#1F8FA6}
#topbar{background:linear-gradient(180deg,#132531,#0F1B23)!important}
.ch,.noteb,.chk-head{background:linear-gradient(135deg,#17303D,#0F1B23)!important}
#homeBtn,#prevBtn,#searchBtn,#backBtn{background:#1D3441!important;color:#F2D08A!important}
#nextBtn{color:#fff!important}
#topbar [id=topSub],#topbar div div:last-child{color:#F2D08A}
"""
FINISH_CSS = r""".nb-i{filter:none!important;color:#8E9A9D;display:flex;justify-content:center}
.nb.on .nb-i{color:#1F8FA6}.nb.on .nb-l{color:#1F8FA6!important}
#homeBtn,#searchBtn{display:flex;align-items:center;justify-content:center}
.dic{display:flex;gap:6px;flex-wrap:wrap;letter-spacing:0}
.dic-i{display:inline-flex;align-items:center;gap:4px;background:#E7F3F4;color:#177688;border-radius:20px;padding:4px 9px 4px 7px}
.dic-i b{font:600 10.5px -apple-system,sans-serif;letter-spacing:.3px}
.db[style*="#2A6B7C"],.ch-n[style*="#2A6B7C"]{background:linear-gradient(135deg,#2BB3C0,#1A7F94)!important}
.db[style*="#8A6D3B"],.ch-n[style*="#8A6D3B"],.dh[style*="#8A6D3B"]{background:#24414F!important}
.ch-d[style*="#2A6B7C"]{color:#7FD3D6!important}.ch-d[style*="#8A6D3B"]{color:#9FB6BD!important}
.dh[style*="#2A6B7C"]{background:linear-gradient(135deg,#1F8FA6,#17607A)!important}
.tc{background:#FFFEFA!important;border:1px solid #E8E2D6!important;border-left:3px solid var(--tk)!important;box-shadow:0 1px 2px rgba(15,27,35,.04),0 4px 14px rgba(15,27,35,.05)!important}
.tp{--tk:#1F8FA6}.ta{--tk:#E0A93B}.tm{--tk:#D9654B}.th{--tk:#2E8B6E}.ts{--tk:#3B5A8C}
.tp .tld,.ta .tld,.tm .tld,.th .tld,.ts .tld{background:var(--tk)!important;color:var(--tk)!important}
.tp .tt,.ta .tt,.tm .tt,.th .tt,.ts .tt{color:var(--tk)!important}
.tp .tlln,.ta .tlln,.tm .tlln,.th .tlln,.ts .tlln{background:#DCE6E4!important}
.maps-btn,.info-btn,.web-btn{background:#fff!important;color:#16313D!important;box-shadow:inset 0 0 0 1px #D3DCDB!important;display:inline-flex!important;align-items:center;gap:5px}
.maps-btn svg,.info-btn svg,.web-btn svg{color:#1F8FA6}
.plane-btn{background:#fff!important;color:#16313D!important;box-shadow:inset 0 0 0 1px #D3DCDB!important}
.tipb{border-left-color:#1F8FA6!important;background:linear-gradient(135deg,#E9F5F6,#FAF7F0)!important}
.brief span{background:#F3F1EB}
.dh2[style*="#2A6B7C"]{background:linear-gradient(135deg,#1F8FA6,#17607A)!important}
.dh2[style*="#8A6D3B"]{background:linear-gradient(135deg,#24414F,#0F1B23)!important}
.dc.dc-hasph{overflow:hidden}
.dc-ph{height:110px;background:center/cover no-repeat;position:relative}
.dc-hasph .db{margin-top:-30px;box-shadow:0 0 0 3px #FFFEFA,0 4px 10px rgba(15,27,35,.25)!important;position:relative}
.dh2.dh2-ph{background-size:cover!important;background-position:center!important}
.tb{color:#fff!important}
"""
THEME_JS = r"""window.__theme=function(v){
const S=(p,w)=>'<svg viewBox="0 0 24 24" width="'+(w||22)+'" height="'+(w||22)+'" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'+p+'</svg>';
const I={
 cal:'<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
 pin:'<path d="M12 21s-6.5-6.2-6.5-11a6.5 6.5 0 0 1 13 0c0 4.8-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/>',
 plane:'<path d="M10.5 13.5 4 11l1.5-1.5 7 1 4-4c.9-.9 2.6-1.2 3.2-.6.6.6.3 2.3-.6 3.2l-4 4 1 7L14.6 21l-2.5-6.5-3 3v2.5L7.6 21.4 6 18l-3.4-1.6L4 15h2.5z"/>',
 tool:'<path d="M14.5 6.5a4 4 0 0 0 5 5l-8.8 8.8a2 2 0 0 1-2.9-2.9L16.6 8.6"/><path d="M14.5 6.5 17 4l3 3-2.5 2.5"/>',
 map:'<path d="M3.5 6.5 9 4l6 2.5L20.5 4v13.5L15 20l-6-2.5-5.5 2.5z"/><path d="M9 4v13.5M15 6.5V20"/>',
 home:'<path d="M4 11 12 4l8 7"/><path d="M6 9.5V20h12V9.5"/><path d="M10 20v-5h4v5"/>',
 search:'<circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.4-4.4"/>',
 coffee:'<path d="M4 9h12v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/><path d="M16 10.5h1.5a2.5 2.5 0 0 1 0 5H16M8 3.5v2.5M12 3.5v2.5"/>',
 beach:'<path d="M4 20h16"/><path d="M12 9v11"/><path d="M4 9a8 8 0 0 1 16 0z"/>',
 compass:'<circle cx="12" cy="12" r="8.5"/><path d="m15.5 8.5-2 5-5 2 2-5z"/>',
 fork:'<path d="M7 3v8M5 3v5a2 2 0 0 0 4 0V3M7 11v10"/><path d="M17 21V3c-2 1.5-3 4-3 7h3"/>',
 glass:'<path d="M5 4h14l-7 8z"/><path d="M12 12v8M8 20h8"/><path d="M15.5 4 18 1.5"/>',
 info:'<circle cx="12" cy="12" r="8.5"/><path d="M12 11v5M12 8h.01"/>',
 globe:'<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.5 2.6 2.5 14.4 0 17M12 3.5c-2.5 2.6-2.5 14.4 0 17"/>'};
const nav={'n-it':'cal','n-td':'pin','n-in':'plane','n-ti':'tool','n-pl':'map'};
for(const k in nav){const e=document.querySelector('#'+k+' .nb-i');if(e&&!e.querySelector('svg'))e.innerHTML=S(I[nav[k]]);}
const hb=document.getElementById('homeBtn');if(hb&&!hb.querySelector('svg'))hb.innerHTML=S(I.home,19);
const sb=document.getElementById('searchBtn');if(sb&&!sb.querySelector('svg'))sb.innerHTML=S(I.search,19);
const em=__DAY_TAGS__;
document.querySelectorAll('.dic').forEach(d=>{if(d.dataset.th)return;d.dataset.th=1;const parts=d.textContent.trim().split(/\s+/);d.innerHTML=parts.map(x=>{const m=em[x]||em[x+'️'];return m?'<span class="dic-i">'+S(I[m[0]],15)+'<b>'+m[1]+'</b></span>':x}).join('')});
document.querySelectorAll('.maps-btn,.info-btn,.web-btn').forEach(b=>{if(b.dataset.th)return;b.dataset.th=1;const ic=b.classList.contains('maps-btn')?'pin':b.classList.contains('info-btn')?'info':'globe';b.innerHTML=S(I[ic],14)+b.textContent.replace(/^[^A-Za-zÀ-ÿ]+/,'')});
if(v==='B'){const ph=__DAY_PHOTOS__,pp=__DAY_POS__;
 document.querySelectorAll('.dc').forEach(c=>{if(c.querySelector('.dc-ph'))return;const n=+((c.getAttribute('onclick')||'').match(/\d+/)||[0])[0];if(!ph[n])return;const d=document.createElement('div');d.className='dc-ph';d.style.backgroundImage='url('+ph[n]+')';if(pp[n])d.style.backgroundPosition=pp[n];c.insertBefore(d,c.firstChild);c.classList.add('dc-hasph');});
 const h=document.querySelector('.dh2');if(h&&typeof curDay!=='undefined'&&curDay!=null){const n=(curDay.id!=null?curDay.id:curDay);if(ph[n]){h.classList.add('dh2-ph');h.style.setProperty('background','linear-gradient(90deg,rgba(15,27,35,.88),rgba(15,27,35,.45)),url('+ph[n]+')','important');if(pp[n])h.style.setProperty('background-position',pp[n],'important');}}}
};

(function(){var busy=false;function run(){if(busy)return;busy=true;try{__theme('B')}catch(e){}busy=false}
var mo=new MutationObserver(function(){clearTimeout(run.t);run.t=setTimeout(run,0)});
document.addEventListener('DOMContentLoaded',function(){run();mo.observe(document.getElementById('app')||document.body,{childList:true,subtree:true})});})();
"""
RESA_RENDER_JS = r"""
  var RV=RESA_VIEW, resaDetails = loadResaDetails();
  var _todo=chkItems.filter(function(i){return !chkState[i.id]}), _ok=chkItems.filter(function(i){return chkState[i.id]});
  var _k=function(i){return (RV[i.id]&&RV[i.id].k)||'9'};
  _todo.sort(function(a,b){return _k(a)<_k(b)?-1:1}); _ok.sort(function(a,b){return _k(a)<_k(b)?-1:1});
  var _veille=_todo.filter(function(i){return RV[i.id]&&/veille/.test(RV[i.id].j||'')}).length;
  var _pct=Math.round(doneCount/chkItems.length*94);
  hChk+='<div class="rv-hero"><svg width="58" height="58" viewBox="0 0 36 36"><circle cx="18" cy="18" r="15" fill="none" stroke="rgba(255,255,255,.15)" stroke-width="4"/><circle cx="18" cy="18" r="15" fill="none" stroke="#2BB3C0" stroke-width="4" stroke-linecap="round" stroke-dasharray="'+_pct+' 94" transform="rotate(-90 18 18)"/><text x="18" y="21" text-anchor="middle" font-size="9" font-weight="800" fill="#fff" font-family="-apple-system,sans-serif">'+doneCount+'/'+chkItems.length+'</text></svg>'
    +'<div><div class="rv-h1">'+(_todo.length?(_todo.length<=4?'Presque tout est calé':'Ça avance'):'Tout est réservé')+'</div><div class="rv-h2">'
    +(_todo.length?('Plus que '+_todo.length+' réservation'+(_todo.length>1?'s':'')+(_veille?(', dont '+_veille+' à faire la veille sur place'):'')):'Il ne reste plus qu’à profiter')+'</div></div><span class="chk-progress" style="display:none"></span></div>';
  var _acc={todo:true,ok:false}; try{var _sa=JSON.parse(localStorage.getItem('rv_acc')||'{}'); for(var _q in _sa)_acc[_q]=_sa[_q];}catch(x){}
  window.rvAcc=function(d){try{var o=JSON.parse(localStorage.getItem('rv_acc')||'{}');o[d.getAttribute('data-acc')]=d.open;localStorage.setItem('rv_acc',JSON.stringify(o));}catch(x){}};
  var _g='';
  if(_todo.length) hChk+='<details class="rv-acc" data-acc="todo" ontoggle="rvAcc(this)"'+(_acc.todo?' open':'')+'><summary class="rv-sum rv-sum-todo"><span>&#128221; À réserver</span><span class="rv-pill rv-red">'+_todo.length+'</span><i class="rv-chev"></i></summary><div class="rv-accb">';
  _todo.forEach(function(item){
    var v=RV[item.id]||{};
    var g=v.when||item.date;
    if(g!==_g){ _g=g; hChk+='<div class="rv-grp">'+e(g)+(v.j?' <span class="rv-pill rv-red">'+e(v.j)+'</span>':'')+'</div>'; }
    var act='';
    if(v.wa) act='<a class="rv-act rv-wa" href="https://wa.me/'+v.wa+'" target="_blank" rel="noopener" onclick="event.stopPropagation()">&#128172; WhatsApp</a>';
    else if(v.url) act='<a class="rv-act rv-url" href="'+v.url+'" target="_blank" rel="noopener" onclick="event.stopPropagation()">&#128279; '+e(v.lbl||'Réserver')+'</a>';
    hChk+='<div class="chk-item rv-row" data-chkid="'+item.id+'"><div class="chk-box"><span class="chk-check">&#10003;</span></div>'
      +'<div style="flex:1;min-width:0"><div class="chk-name rv-t">'+(v.ico?v.ico+' ':'')+e(v.t||item.name)+'</div><div class="rv-s">'+e(v.sub||item.deadline)+'</div></div>'+act+'</div>';
  });
  if(_todo.length) hChk+='</div></details>';
  if(_ok.length){
    hChk+='<details class="rv-acc" data-acc="ok" ontoggle="rvAcc(this)"'+(_acc.ok?' open':'')+'><summary class="rv-sum rv-sum-ok"><span>&#127915; Vos billets</span><span class="rv-pill rv-ok">'+_ok.length+'</span><i class="rv-chev"></i></summary><div class="rv-accb">';
    _ok.forEach(function(item){
      var v=RV[item.id]||{}, det=resaDetails[item.id]||{};
      var ref=v.ref||det.num||det.site||'';
      var st=v.st||'Réservé';
      hChk+='<div class="chk-item rv-tk" data-chkid="'+item.id+'">'
        +'<div class="rv-stub"><div class="rv-dw">'+e(v.dw||'')+'</div><div class="rv-dn">'+e(v.dn||'✓')+'</div><div class="rv-dw">'+e(v.m||'')+'</div></div>'
        +'<div class="rv-perf"></div>'
        +'<div class="chk-viewbtn rv-body" data-resaid="'+item.id+'"><div style="display:flex;justify-content:space-between;gap:6px"><div class="chk-name rv-t" style="font-size:14px">'+(v.ico?v.ico+' ':'')+e(v.t||item.name)+'</div><span class="rv-pill rv-ok" style="align-self:flex-start;white-space:nowrap">&#10003; '+e(st)+'</span></div>'
        +'<div class="rv-s">'+e(v.line||item.date)+'</div>'
        +'<div style="margin-top:6px;display:flex;gap:6px;align-items:center;flex-wrap:wrap">'+(ref?'<span class="rv-ref">'+e(ref)+'</span>':'')+(v.cash?'<span class="rv-pill rv-cash">Espèces</span>':'')+'<span class="rv-more">Détails &#8250;</span></div></div></div>';
    });
      hChk+='</div></details>';
  }
"""
RESA_CSS = r""".rv-hero{display:flex;align-items:center;gap:14px;margin:2px 0 6px;padding:12px;background:linear-gradient(135deg,#17303D,#0F1B23);border-radius:14px;color:#fff}
.rv-h1{font:700 16px Georgia,serif}.rv-h2{font:12px -apple-system,sans-serif;color:#B9CDD3;margin-top:3px;line-height:1.35}
.rv-grp{font:800 11px -apple-system,sans-serif;letter-spacing:1.5px;color:#1a1a1a;margin:16px 0 8px;display:flex;align-items:center;gap:8px;text-transform:uppercase}
.rv-pill{font:700 10px -apple-system,sans-serif;padding:3px 8px;border-radius:10px;letter-spacing:.3px;text-transform:none}
.rv-red{background:#FBE9E5;color:#C8573F}.rv-ok{background:#E8F4EE;color:#2E6B3E}.rv-cash{background:#FCF6EA;color:#9A6A1E;box-shadow:inset 0 0 0 1px #E8D3A8}
.chk-item.rv-row{display:flex;gap:11px;background:#fff;border:1px solid #ece5d8;border-left:4px solid #C8573F;border-radius:12px;padding:11px 12px;align-items:flex-start;margin-bottom:8px;cursor:pointer}
.rv-row .chk-box{width:22px;height:22px;flex-shrink:0;margin-top:1px}
.rv-t{font:700 14.5px Georgia,serif!important;color:#1a1a1a!important;text-decoration:none!important}
.rv-s{font:12px -apple-system,sans-serif;color:#6d655b;margin-top:2px;line-height:1.4}
.rv-act{flex-shrink:0;align-self:center;font:700 11px -apple-system,sans-serif;padding:6px 10px;border-radius:14px;text-decoration:none;white-space:nowrap}
.rv-wa{background:#25A244;color:#fff}.rv-url{background:#fff;color:#16313D;box-shadow:inset 0 0 0 1px #D3DCDB}
.chk-item.rv-tk{display:flex;background:#fff;border:1px solid #ece5d8;border-radius:14px;margin-bottom:9px;overflow:hidden;box-shadow:0 2px 8px rgba(15,27,35,.05);padding:0;cursor:pointer}
.rv-stub{width:62px;flex-shrink:0;background:linear-gradient(180deg,#1F8FA6,#17607A);color:#fff;text-align:center;padding:10px 0;display:flex;flex-direction:column;justify-content:center}
.rv-dw{font:700 9px -apple-system,sans-serif;letter-spacing:1.5px;opacity:.85}.rv-dn{font:400 26px Georgia,serif;line-height:1.05}
.rv-perf{width:0;border-left:2px dashed #E6DFD2;margin:8px 0}
.chk-viewbtn.rv-body{display:block!important;flex:1;min-width:0;padding:10px 12px;background:none!important;border-radius:0!important;color:inherit!important;text-align:left;font:inherit}
.rv-ref{font:600 11px ui-monospace,Menlo,monospace;color:#177688;background:#E7F3F4;border-radius:6px;padding:2px 6px}
.rv-more{margin-left:auto;font:600 11px -apple-system,sans-serif;color:#1F8FA6}
.chk-item.rv-tk{align-items:stretch!important}.rv-tk .rv-stub{align-self:stretch}

.rv-acc{background:#fff;border:1px solid #ece5d8;border-radius:14px;margin:12px 0 0;overflow:hidden;box-shadow:0 2px 8px rgba(15,27,35,.04)}
.rv-sum{list-style:none;display:flex;align-items:center;gap:8px;padding:13px 14px;cursor:pointer;font:800 12px -apple-system,sans-serif;letter-spacing:1.4px;text-transform:uppercase;color:#1a1a1a;-webkit-tap-highlight-color:transparent}
.rv-sum::-webkit-details-marker{display:none}.rv-sum-ok{color:#2E6B3E}.rv-sum-todo{color:#C8573F}
.rv-chev{margin-left:auto;width:9px;height:9px;border-right:2px solid #1F8FA6;border-bottom:2px solid #1F8FA6;transform:rotate(45deg);transition:transform .2s;margin-top:-4px}
.rv-acc[open] .rv-chev{transform:rotate(-135deg);margin-top:4px}
.rv-accb{padding:0 10px 4px;border-top:1px solid #f1ebdf}
.rv-accb .rv-grp:first-child{margin-top:12px}
"""


def _one(html, old, new, label):
    n = html.count(old)
    if n < 1:
        raise SystemExit("theme_lagon : ancre introuvable (%s) : %r" % (label, old[:80]))
    return html.replace(old, new, 1)


def apply(html, cfg):
    cfg = dict(cfg or {})
    style_end = "</style>\n</head>"
    # 1. couverture
    html = _one(html, '<div class="cv-line" id="cv-line-top"></div>',
                '<div class="cv-photo" aria-hidden="true"></div><div class="cv-shade" aria-hidden="true"></div>'
                '<div class="cv-line" id="cv-line-top"></div>', "couverture")
    if cfg.get("cover_label"):
        html = html.replace('label.textContent = "AVANT LE DÉPART";', 'label.textContent = %s;' % json.dumps(cfg["cover_label"], ensure_ascii=False), 1)
    html = html.replace('<div class="cv-sl">Ile</div>', '<div class="cv-sl">Île</div>')
    css = COVER_CSS.replace("__COVER_PHOTO__", cfg.get("cover_photo", "couverture.jpg")) + INTERIOR_CSS + FINISH_CSS
    # 4. billets
    if cfg.get("resa_view") is not None:
        s = "  hChk+='<div class=\"chk-card\" style=\"margin:0\">';"
        e = "  hChk+='</div>';\n  h+=acc('&#9989; Checklist"
        i = html.index(s); j = html.index(e, i)
        html = html[:i] + RESA_RENDER_JS + "  h+=acc('&#9989; Checklist" + html[j + len(e):]
        html = re.sub(r"h\+=acc\('&#9989; Checklist r[^']*\('", "h+=acc('&#9989; Réservations ('", html, 1)
        html = _one(html, "var chkState = loadChkState();",
                    "var chkState = loadChkState();\n  var RESA_VIEW = " + json.dumps(cfg["resa_view"], ensure_ascii=False) + ";"
                    + "\n  window.RV_DEAD = " + json.dumps(cfg.get("chk_deadlines") or {}, ensure_ascii=False) + ";", "chkState")
        html = html.replace("  closeResaModal();\n", "  closeResaModal();\n  try{ buildInfo(); }catch(_e){}\n", 1)
        vd = "  currentViewId = id;\n  var details = {};\n  var details = loadResaDetails();\n  var det = details[id] || {};\n"
        if vd in html:
            html = html.replace(vd, vd + "  if(!det.num && !det.site && !det.info && window.RV_DEAD && RV_DEAD[id]) det = {info: RV_DEAD[id]};\n", 1)
        html = html.replace("function updateProgress(){", "function updateProgress(){ if(typeof chkItems===\"undefined\") return;", 1)
        css += RESA_CSS
    html = _one(html, style_end, css + "\n" + style_end, "fin des styles")
    # 3. script des finitions (icones, etiquettes, photos)
    js = THEME_JS.replace("__DAY_POS__", json.dumps({str(k): v for k, v in (cfg.get("day_pos") or {}).items()}))
    js = js.replace("__DAY_PHOTOS__", json.dumps({str(k): v for k, v in (cfg.get("day_photos") or {}).items()}, ensure_ascii=False))
    js = js.replace("__DAY_TAGS__", json.dumps(cfg.get("day_tags") or DAY_TAGS_DEFAULT, ensure_ascii=False))
    html = _one(html, "</body>", "<script>" + js + "</script>\n</body>", "body")
    # icone d ecran d accueil
    if cfg.get("icon", True) and "apple-touch-icon" not in html:
        html = re.sub(r'(<meta name="apple-mobile-web-app-title"[^>]*>)',
                      r'\1<link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="icon" type="image/png" sizes="512x512" href="icon-512.png">', html, 1)
    # 5. passe finale : plus d or ni de brun hors logo
    html = html.replace("#C9A84C", "#1F8FA6").replace("#c9a84c", "#1F8FA6")
    html = re.sub(r'(?<!fill=")(?<!stroke=")#B8923D', "#1F8FA6", html)
    html = html.replace("%23B8923D", "%231F8FA6").replace("#8a6a24", "#177688")
    html = html.replace("rgba(184,146,61", "rgba(31,143,166").replace("rgba(201,168,76", "rgba(31,143,166")
    html = html.replace(style_end, '#topSub{color:#F2D08A!important}.noteb [style*="#1F8FA6"]{color:#F2D08A!important}\n' + style_end, 1)
    return html


ICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180" width="180" height="180">
  <defs>
    <linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E9774A"/><stop offset=".55" stop-color="#F4B261"/><stop offset="1" stop-color="#F9D98C"/></linearGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A8FA6"/><stop offset="1" stop-color="#17607A"/></linearGradient>
  </defs>
  <rect width="180" height="180" fill="url(#sk)"/>
  <circle cx="98" cy="104" r="34" fill="#FFF3D1"/>
  <rect y="104" width="180" height="76" fill="url(#sea)"/>
  <g fill="#FFF3D1" opacity=".75"><rect x="70" y="112" width="56" height="3" rx="1.5"/><rect x="78" y="121" width="40" height="3" rx="1.5"/><rect x="86" y="130" width="24" height="3" rx="1.5"/></g>
  <path d="M0 152 Q50 138 100 148 T180 146 L180 180 L0 180 Z" fill="#F3DDAF"/>
  <g fill="#3B2A1E">
    <path d="M40 152 Q44 110 36 70 L41 70 Q50 110 46 152 Z"/>
    <path d="M38 70 Q16 62 4 76 Q22 66 38 74 Z"/><path d="M38 70 Q20 48 6 52 Q26 56 38 72 Z"/>
    <path d="M38 70 Q48 44 66 44 Q50 54 40 72 Z"/><path d="M38 70 Q64 60 76 74 Q58 68 40 74 Z"/><path d="M38 70 Q36 50 28 40 Q42 50 40 72 Z"/>
  </g>
</svg>"""


def make_icons(out_dir, svg=ICON_SVG):
    """Ecrit apple-touch-icon.png (180) et icon-512.png dans out_dir. Necessite playwright (chromium)."""
    import os
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        for n, name in ((180, "apple-touch-icon.png"), (512, "icon-512.png")):
            pg = b.new_page(viewport={"width": n, "height": n})
            pg.set_content('<body style="margin:0">' + svg.replace('width="180" height="180"', 'width="%d" height="%d"' % (n, n)) + "</body>")
            pg.screenshot(path=os.path.join(out_dir, name), clip={"x": 0, "y": 0, "width": n, "height": n})
            pg.close()
        b.close()
