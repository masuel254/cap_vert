# Kit maquettes Cap-Vert (charte Lagon)

Référence : carnet Cap-Vert, île de Sal, 14 au 21 novembre 2026 (masuel254.github.io/cap_vert, dépôt masuel254/cap_vert).
Catalogue visuel avec une capture par composant : https://claude.ai/artifact/Fuv2TpKebvXqe61PDUyYdq

## Comment s'en servir dans un nouveau carnet

Samuel demande les composants par leur code : « charte Lagon, reprends le kit Cap-Vert : K06, K07, K08, K12 ».
Claude, dans l'ordre :
1. lit ce fichier, puis récupère les sources du kit dans le dépôt GitHub `masuel254/cap_vert`, dossier `kit/` (`git clone https://github.com/masuel254/cap_vert` ; le code de chaque composant est dans `build_capvert.py`, les données d'exemple dans `capvert_data.py`, le carnet final est `index.html` à la racine) ;
2. remplit les tables de données du composant pour le nouveau voyage (noms entre parenthèses ci-dessous) ;
3. montre une maquette du composant avec les vraies données AVANT de l'intégrer ;
4. intègre, vérifie dans un navigateur (zéro erreur JS), livre ou pousse sur le dépôt du voyage.

## Fichiers du kit (dépôt masuel254/cap_vert)

| Fichier | Rôle |
|---|---|
| `kit/build_capvert.py` | Générateur : part du modèle (`MODELE/index.html`), injecte les données et TOUS les composants du kit (JS + CSS), applique la charte Lagon, écrit `index.html` + `sw.js`. Usage : `python3 build_capvert.py MODELE/index.html out` |
| `kit/capvert_data.py` | Données complètes du Cap-Vert : exemple vivant de chaque table (DAYS, INFO, WEB, PAY, TAXI_ROUTES, CALL_CARDS, WALKS, BUDGET, TODO...). À copier puis vider pour un nouveau voyage. |
| `kit/theme_lagon.py`, `fr_text.py`, `mto_patch.py` | Versions à jour des outils (charte Lagon, accents, patchs du moteur). Plus récentes que celles de `OUTILS/`. Les billets (K10) sont dans `theme_lagon.py` (RESA_VIEW). `fr_text.py` reconstruit son dictionnaire d'accents au premier lancement (`pip install pyspellchecker --break-system-packages`). |
| `index.html`, `sw.js` (racine du dépôt) | Le carnet Cap-Vert final, pour comparer le rendu. |

## Les composants

| Code | Composant | Zone | Ce qu'il fait | Données | Règle validée |
|---|---|---|---|---|---|
| K01 | Couverture photo | couverture | Photo plein cadre, titre du voyage, chiffres clés (jours, voyageurs, îles, nuits), accroche « Avant les pieds dans le sable » et compte à rebours. | `theme_lagon : cover_photo, cover_label ; var depart` | Photo de couverture fournie par toi, eau ou ciel dans le tiers haut. |
| K02 | Liste des jours en photos | itinéraire | Une carte par jour avec sa photo, le numéro du jour, le logement et les puces de thème (Plage, Visite, Restos). | `theme_lagon : day_photos, day_pos` | Une photo par jour, cadrée sur le sujet (day_pos pour régler le cadrage). |
| K03 | En-tête de journée et puces du jour | journée | Bandeau photo du jour, puis les puces : budget espèces et carte par couple, rappels du jour (tenue, valises, horaire clé). | `DAYS[i].brief` | En haut de journée, seulement l’icône carte ou espèces, pas de phrase longue. |
| K04 | Carte événement et ses pastilles | journée | Icône discrète devant le titre, ligne de déplacement, texte replié « Lire la suite », puis les pastilles Maps, paiement, Infos, Web et la note Tripadvisor en vert. | `ICON, DEPLACEMENT, PAY, WEB, TA_EVENTS, MAPS_URLS` | Ordre des liens : site web, Instagram, puis Maps. Pas de Facebook. Toujours une pastille de paiement. |
| K05 | Pastilles de statut | journée | À RÉSERVER en rouge, RÉSERVÉ, PAYÉ ou FAIT en vert, SANS RÉSA en gris, OPTION, GRATUIT. Prix en ~ seulement pour les taxis et chauffeurs. | `RESA_TODO, LOCKED, ev.cost` | Prix taxis légèrement gonflés (tarif touriste). Pas de €/pers sur les restaurants. |
| K05b | Pastille Sans résa et paiement incertain | journée | Repas sans réservation en gris, et la pastille « Espèces ? » quand les avis se contredisent. | `PAY = plutot / verifier` | Ne jamais parler du plafond de retrait de la carte. |
| K06 | Carte d’appel ou de réservation taxi | transport | Carte verte placée environ 30 min avant le trajet, boutons WhatsApp par chauffeur plus Autre, message prérempli. Badge rouge À FAIRE qui passe en FAIT vert d’un tap. | `CALL_CARDS, CALL_IDS, TAXI_LIST` | Message en français puis traduction anglaise dessous, dispo et prix, retours à la ligne, dates en lettres, pas de « / ». Les liens ouvrent l’appli WhatsApp. |
| K07 | Trajet taxi | transport | Encadré départ → arrivée avec durée, badge lié à sa carte d’appel (APPEL 12H05 ›), prix du trajet. Le texte donne les infos pratiques sans redire qui appeler. | `TAXI_ROUTES` | Un taxi d’arrivée sans réservation, appelé à l’atterrissage. Les autres réservés la veille. |
| K08 | Carte balade | activité | Distance et durée, encadré rouge « Partir avec de l’eau », vignettes photo qui défilent avec une explication et un lien Maps par étape, bouton « Itinéraire complet dans Maps » en points GPS. Le glissement sur les vignettes ne change pas de jour. | `WALKS, WALK_IMGS` | Balade au choix (pastille OPTION) : le reste de la journée ne bouge pas. Distances mesurées dans Maps par toi. |
| K09 | Fiche Infos | fiche | Fenêtre de détail : photo (ou vidéo TikTok), WhatsApp si le numéro est un mobile sinon Appeler, Web, Maps, Tripadvisor, horaires, tarifs, conseil. | `INFO, WEB, TA_EVENTS` | Seulement tes photos. Les mobiles ouvrent WhatsApp. |
| K10 | Réservations en billets | infos | Jauge des réservations faites, liste « À réserver » groupée par échéance, puis les billets avec talon date, référence et statut. | `RESA_VIEW (theme_lagon), CHK_ITEMS` | Les cases cochées restent dans le téléphone : ne jamais renommer un id sans migrer. |
| K11 | À faire daté | infos | Liste des choses à faire avec échéance (J-x), rappel, et lien direct vers la carte du jour concernée. | `TODO` | Les à-faire taxis sont liés aux cartes d’appel. |
| K12 | Budget sur place par couple | infos | Tableau jour par jour espèces et carte, avec le détail des postes et le total par couple. | `BUDGET` | Budgets par couple, estimation généreuse. |
| K13 | Accordéon Restaurants | infos | Vue synthétique des repas jour par jour, avec moyen de paiement et statut de réservation. | `RESTO_SHORT, PAY, RESA_TODO` |  |
| K14 | Bon à savoir | journée | Encadré de fin de journée : budget, conseils pratiques, points d’attention. | `DAYS[i].tip` |  |
| K14b | Demain | journée | Bandeau sombre qui annonce le lendemain : heure de départ, quoi prévoir. | `DAYS[i].note` |  |
| K15 | Outils | outils | Change à parité fixe, calculette, météo, température de la mer, horloges. | `onglet Outils, Open-Meteo Marine` | Seuls la météo et la mer appellent le réseau, avec repli hors ligne. |
| K16 | Plan | plan | Plan de l’île touchable pour agrandir, puis les zones décrites (sud, ouest, nord). | `onglet Plan, plan-sal.jpg` |  |

## Règles validées sur le Cap-Vert (à appliquer par défaut)

- Toujours une maquette avant de modifier le carnet ; Samuel valide, puis Claude code.
- Textes en français naturel, écrits sans accents dans les données et remis par `fr()`. Attention : `fr()` transforme « ferme » en « fermé » et « Dores » en « Dorés » ; changer de mot ou corriger après coup.
- Pas de tirets cadratins.
- « À réserver » en rouge ; « Réservé », « Payé », « Fait » en vert ; « Sans résa » en gris ; « Option » pour ce qui est au choix.
- Une pastille de paiement sur chaque événement ; en haut de journée, seulement l'icône carte ou espèces.
- Budgets par couple ; pas de €/pers sur les restaurants.
- Prix seulement sur les taxis et chauffeurs, un peu gonflés (tarif touriste).
- Liens dans l'ordre : site web, Instagram, Maps. Pas de Facebook. Pas de pastilles Calendrier, Copier ni Voiture.
- Numéros mobiles : WhatsApp, ouvert dans l'appli (whatsapp://).
- Messages WhatsApp préremplis : français puis traduction anglaise, demander disponibilité et prix, retours à la ligne, dates en lettres, pas de « / ».
- Cartes d'appel ou de réservation (K06) environ 30 min avant le trajet, badge À FAIRE basculé en FAIT par Samuel.
- Balades (K08) : distance mesurée par Samuel dans Maps, encadré eau obligatoire, liens Maps par étape (fiche du lieu ou lien fourni), itinéraire GPS par coordonnées (un départ et une arrivée différents, sinon Maps refuse la boucle).
- Seulement les photos fournies par Samuel ; nouveau nom de fichier quand une photo change (sinon le cache du téléphone garde l'ancienne).
- L'état du téléphone (cases cochées, à faire, rappels) est conservé : ne jamais renommer un id sans migrer.
- Jamais de données privées publiées (code confidentiel, email ou téléphone perso de Samuel).
- Claude pousse lui-même sur le dépôt du voyage et vérifie que le déploiement GitHub Pages est « success ».
