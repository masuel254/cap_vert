# -*- coding: utf-8 -*-
"""Donnees du carnet Cap-Vert (ile de Sal) - 14 au 21 novembre 2026.
Convention du modele : pas d accents ni d apostrophes dans les textes."""

AIRBNB = "Airbnb Sal Sol & Mar"
TAXI_BLOC = {"titre": "Taxis : mode d emploi", "lignes": ["Pas d Uber ni de Bolt sur Sal : taxis classiques, licencies et controles par la police", "Pas de compteur : annoncer la destination et FIXER LE PRIX AVANT DE MONTER", "Tarifs officiels de la mairie (grille fev. 2024, jour / nuit, par voiture) :", "Dans Santa Maria : 150 / 200 CVE", "Santa Maria - route des hotels (Hilton) : 250 / 350 CVE", "Santa Maria - hotels Melia (Bikini Beach) : 350 / 450 CVE", "Santa Maria - Ponta Preta : 500 / 700 CVE", "Santa Maria - Palmeira ou Pedra de Lume : 1 400 / 1 600 CVE", "Aeroport - Santa Maria centre : 1 000 / 1 200 CVE", "Aeroport - Santa Maria Antonio Sousa (Angulo) : 1 100 / 1 300 CVE", "100 CVE = environ 0,90 EUR. ESPECES UNIQUEMENT, pas de carte bancaire : escudos ou euros, petites coupures (rendu de monnaie souvent en escudos)", "Retirer des escudos au distributeur de l aeroport des l arrivee, avant de prendre le premier taxi", "Chauffeur recommande par l hote Airbnb : Ady, +238 952 97 19 (WhatsApp)", "Plan B si Ady ne repond pas : Taxi Sal Island, +238 599 59 73 (WhatsApp), base a Santa Maria, 5/5 sur 72 avis Google, parle anglais et un peu francais", "Ou trouver un taxi : appeler Ady, le faire appeler par le restaurant ou le bar, ou en arreter un dans le centre et devant les hotels", "A chaque course, garder le numero ou le WhatsApp des chauffeurs sympas : c est comme ca qu on reserve sur l ile"]}
ADR_AIRBNB = "Rua 15 Agosto 108, Santa Maria, Sal 4111, Cap-Vert"

CHAPTERS = [
    {"id": "fr", "num": 0, "city": "DEPART", "subtitle": "France - Paris Orly",
     "dates": "Nuit du 13 au 14 novembre 2026", "color": "#8A6D3B"},
    {"id": "sal", "num": 1, "city": "ILE DE SAL", "subtitle": "Santa Maria, sable blanc et alizes",
     "dates": "14 - 21 novembre 2026", "color": "#2A6B7C"},
]

def ev(time, title, body, typ, cost="---"):
    return {"time": time, "title": title, "body": body, "type": typ, "cost": cost}

def libre(i, date, jour):
    return {
        "id": i, "chap": "sal", "dayNum": i, "date": date,
        "label": date + " - JOURNEE LIBRE",
        "location": jour + " - a programmer",
        "hotel": AIRBNB,
        "events": [],
        "tip": "Journee encore libre. Les idees de sorties (lac sale de Pedra de Lume, Shark Bay, Buracona, Palmeira, Kite Beach) sont dans la page ILE DE SAL : bouton Decouvrir en haut de la liste des jours.",
        "note": "",
    }

DAYS = [
    {
        "id": 0, "chap": "fr", "dayNum": 0, "date": "SAM 14 NOV",
        "brief": ["🛂 Passeports + reçus EASE", "🧳 Dépôt des bagages avant 5h15"],
        "label": "SAM 14 NOV - DEPART DE NUIT VERS ORLY",
        "location": "Marck - Paris Orly Terminal 3",
        "hotel": "Vol TO3232",
        "events": [
            ev("00h05", "Depart de Marck vers Orly",
               "Depart de Marck (62730) avec la voiture de Cedric. Environ 305 km par l A26 puis l A1, compter 3h15 de route. Arrivee a l aeroport d Orly vers 03h30 (parking), au Terminal 3 a 04h00 au plus tard. Dans le sac : passeports, recus EASE, carte bancaire, une centaine d euros en petites coupures.",
               "transport", "---"),
            ev("03h30", "Parking Orly - depot voiture",
               "Arrivee a l aeroport d Orly vers 03h30. Parking pour la voiture de Cedric [A reserver] : parking officiel de l aeroport ou parking prive avec navette. Avec une navette, ajouter 15 a 20 min et partir de Marck plus tot.",
               "transport"),
            ev("04h00", "Arrivee aeroport Orly T3 - Depot bagages",
               "Arrivee au Terminal 3 a 04h00 au plus tard. Transavia demande d arriver au minimum 2h30 avant un vol hors Schengen. Le depot des bagages en soute ferme 75 min avant le depart, soit a 05h15 precises : au-dela, les bagages sont refuses.",
               "transport"),
            ev("04h45", "Securite et controle des passeports",
               "Le Cap-Vert est hors Schengen : passage par la police aux frontieres en plus de la securite. Passeports et cartes d embarquement en main.",
               "transport"),
            ev("05h15", "Petit-dejeuner a Orly",
               "Apres la securite et la police, en zone d embarquement : cafe, viennoiserie ou sandwich dans une des boutiques ouvertes tot (a verifier sur place). Rien n est inclus a bord : Transavia vend des en-cas et des boissons payants. Prochain vrai repas : le dejeuner a Angulo vers 12h30, heure locale.",
               "meal"),
            ev("06h00", "Embarquement",
               "Heure et porte exactes sur la carte d embarquement [A verifier]. Etre devant la porte des l ouverture de l embarquement.",
               "transport"),
            ev("06h30", "Vol Transavia TO3232 Orly vers Sal",
               "Vol direct de 6h15 en Boeing 737-800, classe economique. Arrivee a 10h45 heure du Cap-Vert (12h45 a Paris). Ref compagnie K6UNPB. Ref client 40-1068303696. PAYE : 2 426,00 EUR pour les 4 passagers (aller et retour).",
               "transport", "Paye"),
        ],
        "tip": "Decalage horaire : le Cap-Vert a 2h de moins que Paris en novembre (UTC-1 contre UTC+1). Les telephones se reglent seuls a l atterrissage. Enregistrement en ligne Transavia ouvert 30h avant le vol, soit le vendredi 13/11 a 00h30.",
        "note": "Atterrissage 10h45, taxi vers 11h45, dejeuner et transats a Angulo jusqu a 16h00, logement a 16h15, diner reserve Chez Pastis a 18h30 (table dans la cour, especes).",
    },
    {
        "id": 1, "chap": "sal", "dayNum": 1, "date": "SAM 14 NOV",
        "brief": ["💶 ~110 € / couple", "💳 ~90 € / couple", "🏧 Retirer des escudos à l’aéroport", "🩱 Maillots dans le sac cabine"],
        "label": "SAM 14 NOV - ARRIVEE A SAL",
        "location": "Aeroport Amilcar Cabral - Santa Maria",
        "hotel": AIRBNB,
        "events": [
            ev("10h45", "Atterrissage a Sal - Aeroport Amilcar Cabral",
               "Arrivee a l aeroport de Sal a 10h45 heure locale (12h45 a Paris). Aeroport Amilcar Cabral (SID), pres d Espargos. Compter une bonne heure pour la police (recu EASE de chacun), les bagages et la douane.",
               "transport"),
            ev("11h45", "Taxi de l aeroport vers le logement",
               "Taxi demande a la sortie des bagages (carte verte de 11h15). S il tarde, la file des taxis officiels est juste devant la sortie de l aerogare. Tarif officiel aeroport - Santa Maria centre : 1 000 CVE le jour (environ 9 EUR) par voiture. A 4 avec les valises, il faut un grand taxi ou 2 taxis. Prix fixe avant de monter, ESPECES UNIQUEMENT : retirer des escudos au distributeur de l aerogare avant de sortir. 18 km de route droite vers le sud, environ 20 minutes, arrivee vers 12h10.",
               "transport", "~15 €/taxi"),
            ev("12h15", "Depot des bagages au logement",
               "L hote est d accord pour garder les bagages au logement a 12h15, avant le check-in. On pose les valises et on part dejeuner les mains libres. Rua 15 Agosto 108.",
               "hotel"),
            ev("12h30", "Dejeuner pieds dans le sable et transats a Angulo",
               "Premier moment de vacances des l arrivee : beach bar-restaurant directement sur la plage Antonio de Sousa, face a la mer. Dejeuner (poisson, pates, pizzas, salades, cocktails, biere pression locale), puis transats et parasols jusqu a 16h00. Transats gratuits si on consomme au bar, sinon environ 5 EUR (avis 2024). Ouvert tous les jours de 8h00 a 22h00, service du midi jusque vers 15h00 : ne pas arriver apres 14h00. Plan B : Barracuda, sur la plage pres du ponton, tables dans le sable, especes uniquement. PAIEMENT : carte acceptee.",
               "meal"),
            ev("16h15", "Check-in " + AIRBNB,
               "PAYE sur Airbnb (1 800,00 EUR) - code de confirmation HMYTYQTCD3. Hote : +351 961 976 139, telephone et WhatsApp. Bagages deja deposes a 12h15 avec l accord de l hote. Arrivee possible a partir de 15h00, on revient vers 16h15. Prevenir l hote de l heure d arrivee. " + ADR_AIRBNB + ". Procedure d arrivee detaillee dans l appli Airbnb.",
               "hotel", "Paye"),
            ev("17h00", "Premiere balade - plage et ponton de Santa Maria",
               "Le ponton des pecheurs est le coeur de la ville : retour de peche et découpe du poisson en fin de journee. La grande plage de Santa Maria s etend de part et d autre.",
               "activity", "GRATUIT"),
            ev("17h45", "Coucher de soleil",
               "Le soleil se couche vers 17h58 a la mi-novembre. Nuit noire vers 18h30.",
               "activity", "GRATUIT"),
            ev("18h30", "Premier diner chez Chez Pastis",
               "Diner tot pour une premiere soiree calme : on prend le premier service de 18h30, retour au logement vers 20h30. Petite adresse intime dans une ruelle du centre, cour sous un arbre a la bougie, cuisine capverdienne et poisson frais (steak de thon grille, filet de boeuf). 4,4/5 sur 365 avis Google. Ouvert du lundi au samedi de 18h30 a 23h00, deux services (18h30 et 20h45). RESERVE par WhatsApp au nom de Morieux : samedi 14/11 a 18h30, 4 personnes, table dans la cour. PAIEMENT : ESPECES UNIQUEMENT, pas de carte. Tel et WhatsApp +238 984 36 96.",
               "meal", "Reserve"),
        ],
        "tip": "BUDGET PAR COUPLE (estimation genereuse, on se fait plaisir) : especes ~110 EUR (taxis ~6 €, Chez Pastis ~100 €), carte ~90 EUR (petit-déjeuner à Orly ~20 €, déjeuner et transats à Angulo ~70 €). Angulo prend la carte. Pas de location de voiture : tout se fait a pied dans Santa Maria et en taxi pour le reste (tarifs officiels dans les fiches Infos des taxis). Les valises sont deposees au logement a 12h15 : on dejeune les mains libres. Tous les repas sont prevus au restaurant. L eau du robinet ne se boit pas : eau en bouteille au resto. Monnaie : escudo du Cap-Vert (CVE), parite fixe 1 EUR = 110,265 CVE. Retirer quelques escudos au distributeur pour les petites depenses (douche de Pedra de Lume, pourboires, marches). L euro passe dans beaucoup de commerces touristiques, mais avec un taux moins bon.",
        "note": "Dimanche : grasse matinee, piscine sur le toit, brunch reserve au Bikini Beach Club a 13h00, diner reserve a l Atlantic a 19h45.",
    },
    {
        "id": 2, "chap": "sal", "dayNum": 2, "date": "DIM 15 NOV",
        "brief": ["💶 ~5 € / couple", "💳 ~280 € / couple", "🎒 Maillot, serviette, crème"],
        "label": "DIM 15 NOV - BIKINI BEACH CLUB",
        "location": "Santa Maria - Plage d Algodoeiro",
        "hotel": AIRBNB,
        "events": [
            ev("10h00", "Grasse matinee et cafe au logement",
               "Pas de reveil ce matin : on recupere de la nuit blanche de l aller. Juste un cafe et un fruit au logement, le brunch du Bikini est a 13h00 et il n y a pas besoin de manger avant. Envie d un cafe dehors quand meme : Papaya Cafe, sur la rue pietonne principale, a 5 minutes a pied (jus presses, smoothies, carte acceptee).",
               "hotel"),
            ev("11h00", "Piscine sur le toit de l immeuble",
               "Montee sur le toit : piscine et vue sur la mer, juste en face de l immeuble. Une heure et demie pour se baigner au calme avant de se changer pour le Bikini Beach Club. Garder le maillot sous les vetements : on se baigne aussi au club l apres-midi.",
               "activity", "GRATUIT"),
            ev("12h35", "Route vers le Bikini Beach Club",
               "Le taxi passe nous prendre au logement. Annoncer Bikini Beach Club, a cote du Melia Llana, sur la plage d Algodoeiro (zone touristique ZDTI), a environ 4 km du centre. Environ 10 minutes. Tarif officiel Santa Maria - hotels Melia : 350 CVE le jour (environ 3 EUR). Une source evoque un court transfert en bateau pour la derniere partie : a verifier sur place. Prix fixe avant de monter, especes uniquement.",
               "transport", "~5 €/taxi"),
            ev("13h00", "Brunch au Bikini Beach Club",
               "RESERVE (Resos) au nom de Morieux - dimanche 15/11, 13h00 a 14h30, 4 personnes, zone Restaurant. Table garantie 1h30. Non prepaye : reglement sur place par carte bancaire ou Apple Pay uniquement, pas d especes.",
               "meal", "Reserve"),
            ev("14h30", "Apres-midi piscine et plage",
               "L acces a la piscine a ete demandé dans le message de reservation, mais le club n a pas repondu par ecrit : a confirmer a l arrivee (transats, eventuel minimum de consommation). Fermeture a 20h00 le dimanche.",
               "activity", "A confirmer"),
            ev("17h30", "Taxi retour du Bikini Beach",
               "Le taxi nous prend devant l entree du club. Plan B : l accueil du club appelle un taxi, ou il y en a devant le Melia Llana voisin. Environ 10 minutes jusqu au logement. Tarif officiel : 350 CVE le jour (environ 3 EUR). Douche au logement et on se change avant la soiree. Especes uniquement.",
               "transport", "~5 €/taxi"),
            ev("18h30", "Apero caipirinha au Ola Brasil",
               "Beach bar sur la plage de Santa Maria, ambiance bresilienne, caipirinhas reputees, happy hour sur les boissons. 4,8/5 sur 316 avis Google. Ouvert de 11h00 a 21h30 (ferme le mercredi). PAIEMENT : carte bancaire acceptee.",
               "show"),
            ev("19h45", "Diner et karaoke a l Atlantic Piano Bar & Grill",
               "Le dimanche soir, l Atlantic organise un karaoke dans la rue : l ambiance la plus festive du dimanche a Santa Maria. Viandes grillees (entrecote, T-bone, tomahawk), poulpe, carpaccio, cocktails. RESERVE (TableHelm) au nom de Morieux : dimanche 15/11 a 19h45, 4 personnes. Table gardee 15 minutes seulement : en cas de retard, prevenir sur WhatsApp au +238 975 51 53. Modifier ou annuler avec le lien du mail de confirmation TableHelm. PAIEMENT : carte bancaire acceptee.",
               "meal", "Reserve"),
        ],
        "tip": "BUDGET PAR COUPLE (estimation genereuse, on se fait plaisir) : especes ~5 EUR (taxis ~3 €), carte ~280 EUR (brunch et piscine au Bikini Beach ~160 €, apéro au Olá Brasil ~30 €, Atlantic ~90 €). Le brunch se paye par carte ou Apple Pay uniquement. Avant dimanche, envoyer un message au club depuis la page Resos pour faire confirmer l acces piscine apres le brunch. Le club est ferme le lundi.",
        "note": "Lundi : plongee pour Samuel et Cedric, RDV 08h30. Ne pas se coucher trop tard !",
    },
    {
        "id": 3, "chap": "sal", "dayNum": 3, "date": "LUN 16 NOV",
        "brief": ["💶 ~10 € / couple", "💳 ~160 € / couple", "🤿 Plongée : RDV 8h30 (Samuel, Cédric)"],
        "label": "LUN 16 NOV - JOURNEE PLONGEE",
        "location": "Santa Maria - Cabo Verde Diving",
        "hotel": AIRBNB,
        "events": [
            ev("07h30", "Petit-dejeuner chez Cam s",
               "Cam s ouvre a 07h30 : arriver a l ouverture pour etre au centre de plongee a 08h30. Pour les plongeurs, leger mais consistant et bien s hydrater. Cam s Restaurante e Cafetaria, Rua 15 de Agosto, dans la meme rue que le logement. Ouvert du lundi au samedi des 07h30 (ferme le dimanche). Le petit-dejeuner local : cachupa guisada (restes de cachupa revenus a la poele avec chorizo et oeuf, environ 4 EUR), jus de fruits frais presses, cafe. 4,5/5 sur Google (1 080 avis), 4,3/5 sur Tripadvisor. Petits prix. PAIEMENT : carte bancaire (aucune mention d especes uniquement dans les avis).",
               "meal"),
            ev("08h30", "RDV Cabo Verde Diving - Porto Antigo 1",
               "Samuel et Cedric. RESERVE ET PAYE : 226,72 EUR pour les 2. Rendez-vous au Porto Antigo 1, Santa Maria. Centre Cabo Verde Diving Aquarium, sur le front de mer de Santa Maria. Tel et WhatsApp +238 595 37 96.",
               "activity", "Paye"),
            ev("09h00", "Briefing et entrainement plongee",
               "De 09h00 a 11h30 : briefing securite, materiel, exercices.",
               "activity"),
            ev("10h30", "Angulo Beach Bar - journee transat",
               "Pour Francoise et Virginie : transat, parasol et dejeuner les pieds dans le sable. Angulo est sur la plage Antonio de Sousa, a l est du centre de Santa Maria. Ouvert tous les jours de 8h00 a 22h00. Transats gratuits si on consomme au bar, sinon environ 5 EUR (selon un avis de 2024, a verifier). PAIEMENT : carte acceptee.",
               "activity"),
            ev("11h30", "Pause dejeuner",
               "Samuel et Cedric : repas leger, sans alcool. Reprise a 14h00. Possibilite de rejoindre Francoise et Virginie a Angulo.",
               "meal"),
            ev("14h00", "Plongee en mer",
               "De 14h00 a 16h30. Maillot, serviette et creme solaire.",
               "activity"),
            ev("19h30", "Diner en musique a l Ocean Cafe",
               "RESERVE par WhatsApp au nom de Morieux : lundi 16/11 a 19h30, 4 personnes (terrasse pres des musiciens demandee, a redemander en arrivant). L adresse la plus animee du centre : musique live presque tous les soirs (guitaristes et chanteurs locaux), terrasse, cuisine simple (poisson grille, calamars, pizzas, burgers). Ouvert tous les jours de 7h00 a 1h00. Tel et WhatsApp +238 580 35 05. Ensuite, retour au logement et au lit : deux plongees dans la journee pour Samuel et Cedric, et chauffeur demain a 10h00. PAIEMENT : carte bancaire (aucune mention d especes uniquement dans les avis).",
               "meal", "Reserve"),
        ],
        "tip": "BUDGET PAR COUPLE (estimation genereuse, on se fait plaisir) : especes ~10 EUR (pourboires, petites depenses), carte ~160 EUR (Cam’s ~16 €, déjeuner plongeur ~20 €, Ocean Café ~90 €, Angulo pour Françoise ou Virginie ~35 €). Plongee deja payee. Plongee : bien dormir, pas d alcool la veille, boire beaucoup d eau. Un questionnaire medical est en general demande : signaler avant tout souci d oreilles, de coeur ou d asthme. Le centre impose au moins 12h entre la derniere plongee et un vol : largement respecte (vol le 21/11).",
        "note": "Demain mardi : tour du nord de l ile avec Shark Bay, depart 10h00 (grasse matinee). Chaussures d eau, maillot, serviette et especes.",
    },
    {
        "id": 4, "chap": "sal", "dayNum": 4, "date": "MAR 17 NOV",
        "brief": ["💶 ~240 € / couple", "💳 ~130 € / couple", "🚕 Chauffeur à 10h00", "🎒 Chaussures d’eau, vieux maillot", "💶 Marea 19h00 : espèces uniquement (€ ou escudos)"],
        "label": "MAR 17 NOV - TOUR DU NORD DE L ILE",
        "location": "Buracona - Palmeira - Shark Bay - Pedra de Lume",
        "hotel": AIRBNB,
        "events": [
            ev("09h15", "Petit-dejeuner au Cape Fruit",
               "Grasse matinee : le chauffeur passe a 10h00. Mettre le maillot sous les vetements. Cape Fruit, Rua 15 de Agosto, dans la meme rue que le logement. Ouvert tous les jours de 08h00 a 16h00. Le cafe-brunch le mieux note de Santa Maria : pancakes, crepes banane-chocolat, bols de fruits, assiettes au saumon, smoothies et jus frais. 4,6/5 sur Tripadvisor (1 253 avis), 4,4/5 sur Google (1 035 avis). PAIEMENT : prevoir des ESPECES (Tripadvisor indique especes uniquement, un avis de 2024 dit que la carte passe).",
               "meal"),
            ev("10h00", "Chauffeur de la journee - depart",
               "Pas de voiture : on prend un chauffeur de taxi pour la journee, en 4x4 ou pick-up a cause de la piste de Buracona (beaucoup de taxis classiques refusent la piste). Il nous suit toute la journee et attend a chaque arret. Reserve la veille a la pause dejeuner, avec le programme : Buracona, Palmeira, Shark Bay, Pedra de Lume, retour vers 17h30. Pas de tarif officiel pour une journee : de l ordre de 80 a 120 EUR la voiture (estimation), en especes a la fin. Route du matin : Santa Maria, Espargos (distributeur possible en passant), Palmeira, puis la piste de cailloux vers le nord jusqu a Buracona, environ 45 min. Alternative cle en main : tour prive en 4x4 chez Cabomundo, 190 EUR la demi-journee ou 260 EUR la journee pour 3-4 personnes, dejeuner compris, entrees en plus.",
               "transport", "~50 €/couple"),
            ev("10h45", "Buracona et l Oeil Bleu",
               "Piscines naturelles dans la lave noire et grotte ou l eau devient bleu electrique quand le soleil est au plus haut, entre 11h et 13h. Entree environ 3 EUR par personne, en ESPECES (euros ou escudos). Chaussures fermees ou chaussures d eau : la lave est coupante. Baignade dans le bassin seulement si la mer est calme.",
               "activity"),
            ev("12h30", "Dejeuner de poisson a Palmeira",
               "RESERVE par WhatsApp au nom de Morieux : mardi 17/11 vers 12h30, 4 personnes. Gata Fish & Yacht Club, sur le port de Palmeira : le restaurant de poisson le mieux note du village (4,4/5 sur Tripadvisor, 120 avis, Travellers Choice 2026). Langouste, thon, buzios, cachupa. Ouvert tous les jours de 9h00 a 17h00, carte bancaire acceptee. Tel et WhatsApp +238 950 13 28. Service lent : compter 1h30. Plan B a cote : Esplanada Rotterdam.",
               "meal", "Reserve"),
            ev("14h05", "Route vers Shark Bay",
               "Depuis Palmeira, retour vers Espargos puis la cote est, environ 35 min, et la piste de sable cote mer jusqu a l epave d un grand bateau echoue, le point de repere. Le chauffeur attend pres de l epave pendant la visite.",
               "transport"),
            ev("14h40", "Shark Bay - les requins citrons",
               "On marche dans l eau jusqu aux genoux, a 50 ou 100 m du bord, et les jeunes requins citrons tournent autour de soi. Inoffensifs : rester immobile, ne pas les toucher. Visite programmee juste apres la maree haute (14h01 ce jour-la), quand l eau est assez profonde et les requins proches du bord. CHAUSSURES D EAU obligatoires (roches volcaniques, oursins), location possible sur place environ 3 EUR. Pas de droit d entree officiel : refuser poliment les guides insistants. Toilettes 1 EUR.",
               "activity", "GRATUIT"),
            ev("15h45", "Route vers Pedra de Lume",
               "Depuis Shark Bay, environ 10 min par la piste puis la route de la cote est. En fin d apres-midi, les cars d excursions (surtout entre 10h et 14h) sont repartis : le lac est plus calme.",
               "transport"),
            ev("16h00", "Lac sale de Pedra de Lume",
               "On flotte sans effort dans la saumure d un ancien cratere volcanique. Entree 5 a 6 EUR par personne, en ESPECES (la carte passe mal). Douche d eau douce 1 EUR en pieces. CHAUSSURES D EAU indispensables : les cristaux de sel coupent. 20 a 30 min dans l eau maximum. Fermeture a 17h45.",
               "activity"),
            ev("17h00", "Retour a Santa Maria",
               "Le chauffeur nous depose au logement vers 17h30, on le paye a ce moment-la (prix fixe le matin). Douche pour enlever le sel avant le diner. Retour bien avant la nuit (18h30).",
               "transport"),
            ev("19h00", "Diner gastronomique au Marea",
               "RESERVE par WhatsApp au nom de Morieux : mardi 17/11 a 19h00, 4 personnes. PAIEMENT : ESPECES UNIQUEMENT, en euros ou en escudos, pas de carte (confirme par le restaurant). Prevoir assez d especes pour 4 avant de partir du logement. Le restaurant le mieux note de Santa Maria : 4,8/5 sur 1 127 avis Tripadvisor et 299 avis Google. Produits de la mer travailles avec des touches de cuisine moleculaire (tagliatelles au thon, vitello tonnato). Cadre intime, a l ecart du boulevard, peu de tables. Service de 19h00 a 21h00, ferme le dimanche. Tel et WhatsApp +238 982 21 65.",
               "meal", "Reserve"),
            ev("21h15", "Dernier verre au Buddy Bar",
               "Pour finir en musique : groupe live presque tous les soirs, funana et reggae. A quelques minutes a pied. PAIEMENT : carte bancaire (aucune mention d especes uniquement dans les avis).",
               "show"),
        ],
        "tip": "BUDGET PAR COUPLE (estimation genereuse, on se fait plaisir) : especes ~240 EUR (Cape Fruit ~36 €, chauffeur Ady 40 à 60 €, entrées ~20 €, Shark Bay ~8 €, Marea ~120 €), carte ~130 EUR (Gata Fish ~90 €, Buddy Bar ~40 €). Le Gata Fish prend la carte. Diner au Marea RESERVE a 19h00 : ESPECES UNIQUEMENT, euros ou escudos. CHAUFFEUR : Ady (+238 952 97 19, WhatsApp), reserve la veille. A EMPORTER : chaussures d eau pour chacun (Buracona, Shark Bay, Pedra de Lume), maillot, serviette, vieux maillot pour le lac sale, chapeau, creme solaire, eau, bouteille d eau douce pour se rincer les yeux. Les entrees se payent en euros ou en escudos, en petites coupures et en pieces.",
        "note": "Mercredi : catamaran reserve (Viator). RENDEZ-VOUS CONFIRME a 08h20 au Palm Beach Restaurant, le chauffeur n attend que 5 minutes. Petit-dejeuner rapide chez Cam s a 07h30, depart vers 07h55. Diner reserve chez Il Gobbo a 19h30.",
    },
    {
        "id": 5, "chap": "sal", "dayNum": 5, "date": "MER 18 NOV",
        "brief": ["💶 ~15 € / couple", "💳 ~207 € / couple", "⛵ RDV 8h20 au Palm Beach Restaurant (5 min d’attente max)", "🎒 Maillot, crème, coupe-vent, anti-mal de mer"],
        "label": "MER 18 NOV - CROISIERE EN CATAMARAN",
        "location": "Santa Maria - en mer sur la cote sud-ouest",
        "hotel": AIRBNB,
        "events": [
            ev("07h30", "Petit-dejeuner chez Cam s avant la croisiere",
               "Petit-dejeuner rapide avant le rendez-vous de 08h20 au Palm Beach Restaurant : Cam s ouvre a 07h30, etre des l ouverture et repartir vers 07h55. Cachupa guisada, jus frais, cafe. Rua 15 de Agosto, dans la meme rue que le logement. PAIEMENT : carte bancaire (aucune mention d especes uniquement dans les avis).",
               "meal"),
            ev("08h20", "Rendez-vous au Palm Beach Restaurant",
               "RENDEZ-VOUS CONFIRME par Cape Verde Sailing : mercredi 18/11 a 08h20 au Palm Beach Restaurant, Santa Maria. Le ponton de Santa Maria est en travaux : le bateau part de l un de leurs deux points de depart selon le vent et la mer, et leur chauffeur nous y conduit depuis le Palm Beach. Au retour, ils nous redeposent au Palm Beach Restaurant. ETRE A L HEURE : le chauffeur attend 5 minutes maximum, ensuite il part. Viser 08h10 sur place. Transfert compris dans la reservation Viator. Billet dans Apple Wallet (iPhone de Samuel) et dans l appli Viator. Contact : WhatsApp +238 933 95 10.",
               "transport", "Compris"),
            ev("08h30", "Croisiere en catamaran - Cape Verde Sailing",
               "Demi-journee en catamaran a voile avec Cape Verde Sailing, depart a 08h30, environ 3h30 en mer : navigation le long de la cote sud-ouest, passage au large de Ponta do Sino, arret baignade et snorkeling selon la mer. Dauphins, tortues ou baleines parfois, jamais garantis. A bord : en-cas, biere, vin, sodas et eau a volonte, masques et tubas fournis. 4,8/5 sur 290 avis Tripadvisor. Le matin, la mer est en general plus calme que l apres-midi, quand les alizes forcissent. 25 personnes maximum. RESERVE sur Viator au nom de Samuel Morieux, 4 adultes, reference 1460555133, guide en anglais. Annulation gratuite jusqu au mardi 17/11 a 08h30 (heure du Cap-Vert), ensuite non remboursable. Report ou remboursement si meteo defavorable.",
               "activity", "Paye"),
            ev("12h30", "Dejeuner au LobStar, au pied du ponton",
               "Le catamaran nous redepose au Palm Beach Restaurant, et on reste au bord de l eau : LobStar, cabane en pierre sur le front de mer, au pied du ponton ou les pecheurs debarquent. Specialite de langouste (risotto, langouste grillee a la cap-verdienne) et poisson du jour. 4,3/5 sur pres de 920 avis Tripadvisor. Pas de en-cas copieux a bord : prevoir un vrai dejeuner. PAIEMENT : carte bancaire (aucune mention d especes uniquement dans les avis).",
               "meal"),
            ev("14h30", "Sieste et plage",
               "Apres-midi sans programme : sieste au logement, puis plage de Santa Maria cote ponton, la plus abritee pour se baigner. Le soleil a deja bien tape en mer : creme et ombre.",
               "activity", "GRATUIT"),
            ev("19h30", "Diner chez Il Gobbo",
               "RESERVE par WhatsApp au nom de Morieux : mercredi 18/11 a 19h30, 4 personnes. Petit restaurant italien tres bien note, Rua 15 de Agosto, dans la rue du logement : 4,9/5 sur 233 avis Google. Pates fraiches et poisson, cuisine soignee, langouste a la catalane. Ouvert le mercredi de 18h00 a 22h00 (ferme le mardi). PAIEMENT : carte bancaire (aucune mention d especes uniquement dans les avis). Tel et WhatsApp +238 952 41 29.",
               "meal", "Reserve"),
        ],
        "tip": "BUDGET PAR COUPLE (estimation genereuse, on se fait plaisir) : especes ~15 EUR (pourboire equipage), carte ~207 EUR (catamaran déjà payé sur Viator, Cam’s ~16 €, LobStar ~90 €, Il Gobbo ~100 €). À emporter sur le bateau : maillot sous les vetements, serviette, creme solaire, chapeau, lunettes, coupe-vent leger, un comprime contre le mal de mer pour ceux qui y sont sensibles (a prendre avant d embarquer). Telephone dans une pochette etanche.",
        "note": "Jeudi : farniente, transats, coucher de soleil a Ponta Preta et diner reserve au Barracuda a 19h00, table en bord de mer (especes uniquement).",
    },
    {
        "id": 6, "chap": "sal", "dayNum": 6, "date": "JEU 19 NOV",
        "brief": ["💶 ~250 € / couple", "💳 ~110 € / couple", "🌅 Coucher de soleil 17h57"],
        "label": "JEU 19 NOV - FARNIENTE ET HOMARD GRILLE",
        "location": "Plage de Santa Maria",
        "hotel": AIRBNB,
        "events": [
            ev("09h30", "Petit-dejeuner tranquille au Cape Fruit",
               "Grasse matinee, puis petit-dejeuner sans se presser. Cape Fruit, Rua 15 de Agosto, dans la meme rue que le logement. Ouvert tous les jours de 08h00 a 16h00. Le cafe-brunch le mieux note de Santa Maria : pancakes, crepes banane-chocolat, bols de fruits, assiettes au saumon, smoothies et jus frais. 4,6/5 sur Tripadvisor (1 253 avis), 4,4/5 sur Google (1 035 avis). PAIEMENT : prevoir des ESPECES (Tripadvisor indique especes uniquement, un avis de 2024 dit que la carte passe).",
               "meal"),
            ev("10h30", "Transats a Angulo Beach Bar",
               "Angulo Beach Bar, Praia Antonio de Sousa, a l est du centre de Santa Maria (tel +238 970 11 71). Transats et parasols gratuits si on consomme au bar, sinon environ 5 EUR (avis 2024, a verifier). Arriver tot pour avoir les transats au premier rang. Baignade, lecture, sieste.",
               "activity"),
            ev("12h30", "Dejeuner au Palm Beach Restaurant",
               "Sur la plage de Santa Maria, au niveau du ponton (tel +238 242 26 43, reservation sur palmbeachsal.com) : poisson frais, fruits de mer et pizzas, desserts maison. 4,2/5 sur pres de 1 000 avis Google. Ouvert tous les jours de 11h00 a 22h00 en continu. PAIEMENT : prevoir des ESPECES. Tripadvisor indique la carte acceptee, mais deux avis d octobre 2026 parlent de paiement en especes uniquement.",
               "meal"),
            ev("14h30", "Apres-midi transats a Angulo",
               "Retour aux transats d Angulo, Praia Antonio de Sousa, a 10 minutes a pied du Palm Beach. Rien de prevu, c est le but. OPTION MORABEZA : le Morabeza Beach Club est ferme temporairement apres des degats causés par une tempete. Vers le 10/11, regarder sur Google Maps s il a rouvert. Si oui, on passe l apres-midi la-bas plutot qu a Angulo, sur la meme plage de Santa Maria, plus pres du ponton. [Voir le Morabeza sur Google Maps](https://www.google.com/maps/search/?api=1&query=Morabeza+Beach+Club+Santa+Maria+Sal)",
               "activity"),
            ev("17h15", "Taxi vers Ponta Preta",
               "Le taxi passe nous prendre a l Angulo Beach Bar. Annoncer Ponta Preta, restaurant Ponta Preta, a l ouest de Santa Maria. 10 a 15 minutes. Tarif officiel Santa Maria - Ponta Preta : 500 CVE le jour (environ 5 EUR). Le retour de 18h20 est demande dans le meme message : le reconfirmer au chauffeur en descendant, peu de taxis passent a Ponta Preta a la nuit tombee. Especes uniquement.",
               "transport", "~7 €/taxi"),
            ev("17h30", "Coucher de soleil a Ponta Preta",
               "Juste un verre, pas de repas : on s installe en terrasse au Restaurant Ponta Preta, directement sur la plage de Ponta Preta, sur la cote ouest : ici le soleil se couche dans l ocean, sans rien devant (vers 17h57). C est LE spot coucher de soleil de l ile, cite dans tous les avis. 4,1/5 sur 382 avis Tripadvisor. Tel +238 991 86 13. Conseil des habitues : s installer en haut l apres-midi, puis descendre au premier rang en bord de plage pour le coucher de soleil. PAIEMENT : carte bancaire (aucune mention d especes uniquement dans les avis).",
               "show"),
            ev("18h20", "Retour de Ponta Preta",
               "Le meme chauffeur revient nous chercher a 18h20, comme convenu a l aller, et nous depose au logement. Tarif officiel de nuit : 700 CVE (environ 6 EUR). Plan B : le restaurant appelle un taxi. Le reste de la soiree se fait a pied. Paiement en especes uniquement, pas de carte.",
               "transport", "~7 €/taxi"),
            ev("19h00", "Diner homard grille au Barracuda",
               "RESERVE par WhatsApp au nom de Morieux : jeudi 19/11 a 19h00, 4 personnes, table en bord de mer. Tables dans le sable, au bord de la plage de Santa Maria pres du ponton : le poisson est debarque juste devant. Specialite : homard et langouste grilles, poisson du jour, sauces maison. 4,1/5 sur 1 844 avis Tripadvisor. Ouvert de 19h00 a 23h00. ESPECES UNIQUEMENT : demander le prix du homard (souvent au poids) avant de commander. Tel et WhatsApp +238 599 04 50.",
               "meal", "Reserve"),
            ev("21h30", "Dernier verre en musique",
               "Au choix : Ocean Cafe sur la place centrale ou Buddy Bar, tous deux avec musique live le plus souvent. PAIEMENT : carte bancaire (aucune mention d especes uniquement dans les avis).",
               "show"),
        ],
        "tip": "BUDGET PAR COUPLE (estimation genereuse, on se fait plaisir) : especes ~250 EUR (Cape Fruit ~36 €, Palm Beach ~70 €, taxis ~6 €, Barracuda ~140 €), carte ~110 EUR (boissons à Angulo ~40 €, Ponta Preta ~30 €, dernier verre ~40 €). Prevoir large pour un homard pour 4 (prix au poids, a demander) : retirer des escudos ou prendre des euros dans la journee.",
        "note": "Vendredi : piscine, poisson au Sol Doce a 12h30, plage, sieste, puis diner et White Party. CE SOIR : reserver le taxi de demain soir (21h40 et 01h30), carte verte de 18h45.",
    },
    {
        "id": 7, "chap": "sal", "dayNum": 7, "date": "VEN 20 NOV",
        "brief": ["💶 ~60 € / couple", "💳 ~215 € / couple", "💶 Sol Doce : espèces uniquement", "👕 Tenue blanche ce soir", "🧳 Valises bouclées avant 19h"],
        "label": "VEN 20 NOV - FARNIENTE ET DERNIERE SOIREE",
        "location": "Santa Maria",
        "hotel": AIRBNB,
        "events": [
            ev("09h00", "Enregistrement en ligne vol retour",
               "Ouvert depuis 05h40 (30h avant le vol). Telecharger les 4 cartes d embarquement sur les telephones.",
               "transport"),
            ev("10h00", "Dernier petit-dejeuner chez Cam s",
               "Journee sans programme jusqu au soir : dernier petit-dejeuner cap-verdien, cachupa guisada pour finir en beaute. Cam s Restaurante e Cafetaria, Rua 15 de Agosto, dans la meme rue que le logement. Ouvert du lundi au samedi des 07h30 (ferme le dimanche). Le petit-dejeuner local : cachupa guisada (restes de cachupa revenus a la poele avec chorizo et oeuf, environ 4 EUR), jus de fruits frais presses, cafe. 4,5/5 sur Google (1 080 avis), 4,3/5 sur Tripadvisor. Petits prix. PAIEMENT : carte bancaire (aucune mention d especes uniquement dans les avis).",
               "meal"),
            ev("11h00", "Piscine sur le toit de l immeuble",
               "Derniere matinee au calme sur le toit : baignade, vue sur la mer, rien a organiser.",
               "activity", "GRATUIT"),
            ev("12h30", "Dejeuner de poisson au Sol Doce",
               "Petite adresse de poisson au bord de la plage, pres du ponton : on choisit son poisson du jour, cuit devant soi. Les plus cites : poisson grille (pargo), tataki et tartare de thon, lapas, frites maison. 4,6/5 sur 412 avis Tripadvisor, Travellers Choice 2026. Cadre simple, sans nappe ; des palissades de chantier entourent en ce moment le ponton. Ouvert de 10h00 a 18h00, ferme le mercredi. Sans reservation : on y va directement. Arriver vers 12h30, quand le poisson arrive ; s il n y a plus de table, attendre un peu ou revenir apres un tour sur la plage. Contact au besoin : +238 994 65 62 (WhatsApp). PAIEMENT : ESPECES UNIQUEMENT.",
               "meal"),
            ev("14h15", "Apres-midi plage, transats et baignade",
               "Deux options selon l envie. Plan A, au calme : rester sur la plage du ponton, la partie la plus abritee de la baie, sable fin et peu de vagues ; louer des transats si des loueurs sont presents (a demander sur place), sinon serviettes sur le sable. Plan B, avec transats assures : 10 minutes a pied vers l est jusqu a Angulo, transats et parasols gratuits si on consomme au bar (sinon environ 5 EUR) ; mer plus agitee, kitesurfeurs au large, se baigner pres du bord. Retour au logement vers 16h15.",
               "activity"),
            ev("16h15", "Sieste avant la derniere soiree",
               "Retour au logement : douche et sieste. La soiree finit a 01h30 et le reveil sonne a 07h00 demain, cette sieste n est pas un luxe.",
               "activity", "GRATUIT"),
            ev("18h00", "Valises bouclees avant la soiree",
               "Boucler les valises MAINTENANT, avant de sortir : depart du logement demain a 08h00 et personne n aura envie de faire les sacs a 1h du matin. Confirmer aussi le taxi de demain matin pour l aeroport (08h00, minivan pour 4 avec valises).",
               "transport"),
            ev("19h00", "Diner de fete au Soul Kitchen",
               "Sans reservation : on y va directement vers 19h00, en blanc pour la White Party. Soul Kitchen, sur la plage de Santa Maria, a l etage de La Villa Beach Lounge : terrasse face a l ocean, pieds presque dans le sable. Musique live tous les soirs a partir de 19h00. Cuisine mediterraneenne et poisson : pates aux fruits de mer, poisson du jour, pizzas, vrai menu vegetarien. 4,6/5 sur 816 avis Tripadvisor, tres bons avis en septembre et octobre 2026. Ouvert tous les jours jusqu a 22h30. Service parfois lent quand c est plein : commander d entree le plat et le dessert pour partir sereinement a 21h40. Si c est complet en arrivant, demander a quelle heure une table se libere, ou se rabattre sur le Baraonda (centre, +238 596 61 96). Tel +238 997 47 61. PAIEMENT : carte acceptee, avec parfois un supplement d environ 3 % : prevoir des especes pour eviter les frais.",
               "meal"),
            ev("21h40", "Taxi vers le Bikini Beach Club",
               "Depart du Soul Kitchen a 21h40 : la table de la White Party est reservee a 22h00. Taxi reserve la veille pour l aller et le retour. Environ 10 minutes jusqu au Bikini Beach Club, plage d Algodoeiro. Repere : tarif officiel Santa Maria - hotels Melia 350 CVE le jour, 450 CVE la nuit (environ 4 EUR), en euros ou escudos, petites coupures. Plan B : le Soul Kitchen appelle un taxi, ou il y en a sur la place centrale, prix fixe avant de monter.",
               "transport", "~6 €/taxi"),
            ev("22h00", "White Party au Bikini Beach Club",
               "RESERVE au nom de Morieux : table de 4 en zone White Party, vendredi 20/11 de 22h00 a 01h30 (table gardee 3h30). Confirmation et messages sur la page de reservation bikinibeachclub.com, le club peut demander de reconfirmer avant la date. Le vendredi soir, le Bikini Beach Club organise sa White Party de 22h00 a 03h00 : tout le monde en blanc, un cocktail de bienvenue offert, DJ et fete au bord de l eau. Carte bancaire et Apple Pay acceptes.",
               "show", "Reserve"),
            ev("01h30", "Taxi retour au logement",
               "Le chauffeur de l aller nous attend devant l entree du club a 01h30. Plan B : demander un taxi a l accueil du Bikini Beach Club. Tarif officiel de nuit : 450 CVE (environ 4 EUR), prix fixe avant de monter, adresse : Rua 15 de Agosto 108, centre de Santa Maria. Pas plus tard : reveil a 07h00 et depart a 08h00. Ne pas rentrer a pied : 4 km de nuit, peu eclaire.",
               "transport", "~6 €/taxi"),
        ],
        "tip": "BUDGET PAR COUPLE (estimation genereuse, on se fait plaisir) : especes ~60 EUR (Sol Doce ~50 €, transats ~5 €, taxis ~4 €), carte ~215 EUR (Cam’s ~16 €, boissons à la plage ~20 €, Soul Kitchen ~100 €, White Party ~80 €). SOL DOCE : especes uniquement. Garder 500 CVE par couple pour le taxi de demain matin (Ady). Journee tranquille : piscine sur le toit, poisson au Sol Doce, plage du ponton ou Angulo, sieste. Derniere soiree : bon diner puis White Party au Bikini Beach Club, TOUT LE MONDE EN BLANC (a prevoir dans les valises). Valises bouclees avant de sortir, retour vers 01h30 au plus tard. Reveil 07h00 demain, rien ne doit etre fait le matin a part partir. Ce soir : taxi aller et retour, prix fixe avant de monter, et retour cale a l aller avec le chauffeur pour 01h30.",
        "note": "Demain : taxi a 08h00 devant le logement (reserve la veille), aeroport vers 08h30, vol a 11h40.",
    },
    {
        "id": 8, "chap": "sal", "dayNum": 8, "date": "SAM 21 NOV",
        "brief": ["💶 ~10 € / couple", "💳 ~70 € / couple", "🚕 Taxi à 8h00, réservé la veille"],
        "label": "SAM 21 NOV - RETOUR EN FRANCE",
        "location": "Santa Maria - Aeroport SID - Paris Orly",
        "hotel": "Vol TO3233",
        "events": [
            ev("07h00", "Reveil et derniers rangements",
               "Verifier chambres et salle de bains, vider le frigo, sortir les poubelles selon les consignes de l hote. Pas de petit-dejeuner au logement : on mange a l aeroport apres l enregistrement.",
               "hotel"),
            ev("08h00", "Check-out et route vers l aeroport",
               "Taxi reserve la veille, devant le logement a 08h00. Tarif officiel Santa Maria - aeroport : 1 000 CVE le jour (environ 9 EUR) par voiture, 2 taxis s il le faut avec les valises. Depart a 08h00 (check-out limite 11h00, mais le vol impose de partir tot). Cles selon les consignes de l hote. 18 km, 20 a 25 minutes. Especes uniquement.",
               "transport", "~15 €/taxi"),
            ev("08h30", "Arrivee aeroport de Sal - Enregistrement",
               "Arrivee a l aeroport de Sal vers 08h30, soit plus de 3h avant le vol (Transavia demande 2h30 minimum). Depot des bagages ferme 75 min avant le depart, soit 10h25. Petite aerogare, mais controle des passeports a la sortie du territoire.",
               "transport"),
            ev("09h15", "Petit-dejeuner et sandwich pour le vol",
               "Apres l enregistrement et la police : cafe et viennoiserie, et un sandwich par personne a emporter pour le vol, qui traverse l heure du dejeuner. Bon moment pour depenser les derniers escudos. Choix limite dans cette petite aerogare : ne pas attendre la derniere minute.",
               "meal"),
            ev("11h40", "Vol Transavia TO3233 Sal vers Orly",
               "Vol direct de 5h50 en Boeing 737-800. Arrivee a Orly a 19h30 heure de Paris. Ref compagnie K6UNPB. Billets PAYES. Rien n est inclus a bord : repas et boissons payants, d ou le sandwich achete a Sal.",
               "transport", "Paye"),
            ev("19h30", "Arrivee a Orly (heure de Paris)",
               "Arrivee a l aeroport d Orly a 19h30 heure de Paris. Terminal d arrivee a verifier sur les ecrans (Transavia arrive au T2 ou au T3). Compter une bonne heure pour la police, les bagages et le parking.",
               "transport"),
            ev("20h30", "Route retour vers Marck",
               "Environ 305 km, compter 3h de route plus la pause diner. Arrivee a Marck vers 00h15.",
               "transport"),
            ev("21h45", "Diner sur l aire d Assevillers",
               "Pause diner d environ 45 minutes sur l A1, a l aire d Assevillers (vers Peronne), a peu pres a mi-chemin : restauration et boutique, horaires du soir a verifier. Le conducteur souffle avant la deuxieme moitie de la route.",
               "meal"),
        ],
        "tip": "BUDGET PAR COUPLE (estimation genereuse, on se fait plaisir) : especes ~10 EUR (taxi ~8 €), carte ~70 EUR (petit-déjeuner et sandwichs à l’aéroport ~30 €, dîner sur l’autoroute ~40 €). Taxi : Ady, reserve la veille. Depenser ou changer les derniers escudos a l aeroport : ils ne se changent pas en France. Les horaires de la journee sont en heure du Cap-Vert jusqu au vol, puis en heure de Paris a partir de l arrivee a Orly.",
        "note": "",
    },
]

VOLS = [
    {"type": "ALLER", "route": "Paris Orly (ORY) T3 vers Sal Amilcar Cabral (SID)",
     "airline": "Transavia France TO3232 - Boeing 737-800 - direct 6h15 - economique",
     "schedule": "Sam. 14/11 - 06h30 (Paris) vers 10h45 (Sal)"},
    {"type": "RETOUR", "route": "Sal Amilcar Cabral (SID) vers Paris Orly (ORY)",
     "airline": "Transavia France TO3233 - Boeing 737-800 - direct 5h50 - economique",
     "schedule": "Sam. 21/11 - 11h40 (Sal) vers 19h30 (Paris)"},
]

RESAS = [
    {"date": "14 NOV", "name": "Vols Transavia TO3232 / TO3233", "detail": "PAYE - Ref K6UNPB - ref client 40-1068303696 - 2 426,00 EUR pour 4", "deadline": "PAYE", "color": "#2E6B3E"},
    {"date": "14 NOV", "name": AIRBNB, "detail": "PAYE 1 800,00 EUR - HMYTYQTCD3 - 14/11 15h00 au 21/11 11h00 - hote +351 961 976 139", "deadline": "PAYE", "color": "#2E6B3E"},
    {"date": "14 NOV", "name": "Diner Chez Pastis", "detail": "RESERVE par WhatsApp au nom de Morieux - 18h30 - 4 pers - table dans la cour - especes uniquement", "deadline": "RESERVE", "color": "#2E6B3E"},
    {"date": "15 NOV", "name": "Brunch Bikini Beach Club", "detail": "RESERVE (Resos) - 13h00-14h30 - 4 pers - paiement sur place", "deadline": "RESERVE", "color": "#2E6B3E"},
    {"date": "15 NOV", "name": "Diner Atlantic Piano Bar & Grill", "detail": "RESERVE (TableHelm) au nom de Morieux - 19h45 - 4 pers - table gardee 15 min - WhatsApp +238 975 51 53", "deadline": "RESERVE", "color": "#2E6B3E"},
    {"date": "16 NOV", "name": "Plongee Cabo Verde Diving", "detail": "PAYE - 226,72 EUR - Samuel et Cedric", "deadline": "PAYE", "color": "#2E6B3E"},
    {"date": "17 NOV", "name": "Diner Marea", "detail": "RESERVE par WhatsApp au nom de Morieux - 19h00 - 4 pers - ESPECES UNIQUEMENT (euros ou escudos)", "deadline": "RESERVE", "color": "#2E6B3E"},
    {"date": "18 NOV", "name": "Catamaran Cape Verde Sailing", "detail": "RESERVE (Viator) - ref 1460555133 - Samuel Morieux, 4 adultes - RDV 08h20 au Palm Beach Restaurant (5 min d attente max) - annulation gratuite jusqu au 17/11 08h30", "deadline": "RESERVE", "color": "#2E6B3E"},
    {"date": "18 NOV", "name": "Diner Il Gobbo", "detail": "RESERVE par WhatsApp au nom de Morieux - 19h30 - 4 pers - +238 952 41 29", "deadline": "RESERVE", "color": "#2E6B3E"},
    {"date": "16 NOV", "name": "Diner Ocean Cafe", "detail": "RESERVE par WhatsApp au nom de Morieux - 19h30 - 4 pers - terrasse demandee - carte", "deadline": "RESERVE", "color": "#2E6B3E"},
    {"date": "17 NOV", "name": "Dejeuner Gata Fish, Palmeira", "detail": "RESERVE par WhatsApp au nom de Morieux - 12h30 - 4 pers - carte acceptee", "deadline": "RESERVE", "color": "#2E6B3E"},
    {"date": "19 NOV", "name": "Diner Barracuda", "detail": "RESERVE par WhatsApp au nom de Morieux - 19h00 - 4 pers - table en bord de mer - especes uniquement", "deadline": "RESERVE", "color": "#2E6B3E"},
    {"date": "20 NOV", "name": "White Party Bikini Beach Club", "detail": "RESERVE au nom de Morieux - 4 pers - zone White Party - 22h00-01h30 (table 3h30) - tenue blanche", "deadline": "RESERVE", "color": "#2E6B3E"},
    {"date": "17 NOV", "name": "Chauffeur 4x4 tour du nord", "detail": "Ady ou Taxi Sal Island - mardi 10h00-17h30 - Buracona, Palmeira, Shark Bay, Pedra de Lume - prix a negocier (~80 a 120 EUR la voiture)", "deadline": "A organiser", "color": "#C8573F"},
    {"date": "21 NOV", "name": "Taxi logement - aeroport", "detail": "Ady ou Taxi Sal Island - samedi 08h00 - 4 pers. et 4 valises - 1 000 CVE tarif officiel", "deadline": "A reserver la veille", "color": "#C8573F"},
    {"date": "14 NOV", "name": "Parking Orly", "detail": "Voiture de Cedric - du 14/11 vers 03h30 au 21/11 vers 20h30", "deadline": "A reserver", "color": "#C8573F"},
    {"date": "9 NOV", "name": "Preenregistrement EASE x4", "detail": "ease.gov.cv - 3 400 CVE (~31 EUR) par personne", "deadline": "Au plus tard 5 jours avant", "color": "#C8573F"},
]

PHRASES = [
    {"jp": "Bom dia / Boa tarde", "fr": "Bonjour / Bon apres-midi"},
    {"jp": "Boa noite", "fr": "Bonsoir, bonne nuit"},
    {"jp": "Obrigado / Obrigada", "fr": "Merci (homme / femme)"},
    {"jp": "Por favor", "fr": "S il vous plait"},
    {"jp": "Desculpe", "fr": "Pardon, excusez-moi"},
    {"jp": "Quanto custa ?", "fr": "Combien ca coute ?"},
    {"jp": "A conta, por favor", "fr": "L addition, s il vous plait"},
    {"jp": "Agua sem gas / com gas", "fr": "Eau plate / gazeuse"},
    {"jp": "Sim / Nao", "fr": "Oui / Non"},
    {"jp": "Onde fica ... ?", "fr": "Ou se trouve ... ?"},
    {"jp": "No stress", "fr": "La devise de Sal : on prend son temps"},
]

ESSENTIALS = [
    {"label": "Passeport", "val": "Un par voyageur, en cours de validite. Verifier les 4 des maintenant."},
    {"label": "Recu EASE", "val": "Preenregistrement + taxe aeroport sur ease.gov.cv, au plus tard 5 jours avant (9/11). Capture d ecran du QR code de chacun."},
    {"label": "Chauffeur Ady", "val": "Chauffeur de taxi avec qui l hote Airbnb travaille habituellement : Ady, +238 952 97 19 (WhatsApp). A contacter pour l arrivee a l aeroport le 14/11, le tour du nord le mardi, la soiree du vendredi et le depart du 21/11. Il organise aussi des visites de l ile. Fixer les prix a l avance, paiement en especes."},
    {"label": "Hote Airbnb", "val": "Sal Sol & Mar : +351 961 976 139 (numero portugais), joignable par telephone et WhatsApp. Le prevenir de l heure d arrivee le samedi 14,"},
    {"label": "Taxis", "val": "Pas de location de voiture. Taxis sans compteur et ESPECES UNIQUEMENT (pas de carte) : prix fixe avant de monter, tarifs officiels de la mairie dans les fiches Infos. Petites coupures en escudos ou euros. Pas d Uber ni de Bolt sur Sal."},
    {"label": "Budget par couple", "val": "Sur chaque etape, une pastille dit comment payer : Carte, Especes ou Especes ? (especes probables). Estimation genereuse pour la semaine, depenses partagees en deux, restos et bars compris (on se fait plaisir) : especes environ 750 EUR par couple, carte environ 1 247 EUR par couple (hors vols, Airbnb, plongee et catamaran deja payes). Le detail jour par jour est en haut de chaque journee. Conseil : partir avec 200 EUR en euros par couple (petites coupures, pieces de 1 et 2 EUR) et retirer le reste en escudos au fil des jours (aeroport des l arrivee, puis Santa Maria et Espargos). Les restos sans mention especes uniquement dans les avis sont comptes en carte."},
    {"label": "Carte bancaire + especes", "val": "ESPECES UNIQUEMENT : taxis, chauffeurs, Barracuda, entrees de Buracona et Pedra de Lume, chaussures d eau. CARTE UNIQUEMENT : Bikini Beach Club. Budget especes pour la semaine a 4, estimation : taxis environ 50 EUR, chauffeurs mardi et vendredi 130 a 190 EUR, entrees et petits frais environ 60 EUR, diner Barracuda 160 a 240 EUR, pourboires 40 EUR, soit environ 450 a 600 EUR. Partir avec 150 a 200 EUR en euros (petites coupures, pieces de 1 et 2 EUR) et retirer le reste en escudos sur place, a l aeroport des l arrivee puis a Santa Maria. Prevenir la banque du voyage et verifier les frais de retrait hors zone euro."},
    {"label": "Creme solaire haute protection", "val": "Indice UV jusqu a 9 en novembre. Chapeau et lunettes."},
    {"label": "Chaussures d eau", "val": "Une paire par personne, indispensable mardi : lave coupante et glissante a Buracona, roches et oursins a Shark Bay, cristaux de sel coupants a Pedra de Lume."},
    {"label": "Vieux maillot", "val": "Pour le lac sale : le sel et le soufre abiment les tissus."},
    {"label": "Coupe-vent leger", "val": "Les alizes soufflent fort en novembre, surtout en fin de journee."},
    {"label": "Anti-moustiques", "val": "Utile le soir."},
    {"label": "Trousse pharmacie", "val": "Medicaments habituels avec ordonnance, antidiarrheique, pansements. Offre de soins limitee sur l ile."},
    {"label": "Prises electriques", "val": "Types C et F en 220 V, comme en France. Pas d adaptateur."},
]

DATA = {
    "CHAPTERS": CHAPTERS, "DAYS": DAYS, "TRAINS": [], "VOLS": VOLS,
    "RESAS": RESAS, "PHRASES": PHRASES, "ESSENTIALS": ESSENTIALS,
}

# ------------------------------------------------------------------ INFO_DATA
vol_logistique = [
    {"titre": "Vols (reserve et paye)", "lignes": [
        "ALLER - sam. 14/11 : Paris Orly T3 06h30 vers Sal (SID) 10h45 heure locale - Transavia France TO3232 - Boeing 737-800 - direct 6h15",
        "RETOUR - sam. 21/11 : Sal (SID) 11h40 vers Paris Orly 19h30 heure de Paris - Transavia France TO3233 - Boeing 737-800 - direct 5h50",
        "Classe economique - 4 passagers : Samuel, Francoise, Cedric, Virginie",
    ]},
    {"titre": "References", "lignes": [
        "Ref de reservation compagnie (PNR) : K6UNPB",
        "Reference client : 40-1068303696",
        "Montant PAYE : 2 426,00 EUR pour les 4 passagers, aller et retour",
        "Gestion en ligne : transavia.com, rubrique Ma reservation (PNR + nom)",
    ]},
    {"titre": "Horaires a ne pas rater", "lignes": [
        "Enregistrement en ligne : ouvre 30h avant (aller le 13/11 a 00h30, retour le 20/11 a 05h40 heure de Sal)",
        "Arrivee a l aeroport : Orly 04h00 (2h30 avant), Sal 08h45 (pres de 3h avant)",
        "Depot des bagages : ferme 75 min avant (Orly 05h15, Sal 10h25)",
    ]},
    {"titre": "Bagages", "lignes": [
        "Bagage cabine non inclus (indique sur les cartes d embarquement) : un petit sac sous le siege par personne, 40 x 30 x 20 cm maximum",
        "Valises en soute : verifier sur MyTransavia qu elles figurent bien sur la reservation",
        "Transavia est stricte sur les dimensions cabine : mesurer les sacs avant",
    ]},
]

INFO = {
    "Depart de Marck vers Orly": {
        "title": "Depart de nuit vers Orly",
        "intro": "Le vol part a 06h30 et Transavia demande 2h30 d avance pour un vol hors Schengen. Il faut donc etre au Terminal 3 a 04h00 au plus tard, ce qui impose un depart de Marck a 00h05 (3h15 de route, avec 10 minutes de marge).",
        "conseil": "Option plus reposante : une nuit dans un hotel pres d Orly le vendredi 13/11, depart a 03h30 a pied ou en navette. A arbitrer selon le prix et le parking.",
        "logistique": [
            {"titre": "Trajet", "lignes": ["Depart de Marck (62730) avec la voiture de Cedric", "Environ 305 km par l A26 puis l A1", "Environ 3h15 de nuit"]},
            {"titre": "A ne pas oublier", "lignes": ["Passeports des 4 voyageurs", "Recus EASE (QR codes)", "Cartes d embarquement telechargees"]},
            {"titre": "A confirmer", "lignes": ["Parking Orly pour la voiture de Cedric"]},
        ],
    },
    "Parking Orly - depot voiture": {
        "title": "Parking a Orly",
        "intro": "Parking pour la voiture de Cedric, non reserve a ce jour. Duree : du samedi 14/11 vers 03h30 au samedi 21/11 vers 20h30, soit 8 jours.",
        "conseil": "Reserver en ligne a l avance, c est nettement moins cher qu au guichet. Un parking proche du Terminal 3 evite la navette au milieu de la nuit.",
        "logistique": [{"titre": "Statut", "lignes": ["A RESERVER", "Ajouter ici la reference une fois reserve (onglet Infos, checklist)"]}],
    },
    "Arrivee aeroport Orly T3 - Depot bagages": {
        "title": "Orly Terminal 3 - Depart Transavia",
        "intro": "Transavia France part du Terminal 3 d Orly. Le vol pour Sal est hors Schengen : enregistrement des bagages, securite, puis police aux frontieres.",
        "conseil": "La regle a retenir : depot des bagages ferme a 05h15. Sans bagage en soute et avec la carte d embarquement sur le telephone, on peut aller directement au controle.",
        "logistique": [{"titre": "Deroule conseille", "lignes": [
            "04h00 : arrivee au Terminal 3, comptoirs Transavia",
            "05h15 : fermeture du depot des bagages",
            "04h45 a 05h30 : securite puis controle des passeports",
            "06h00 environ : embarquement (heure exacte sur la carte)",
            "06h30 : decollage TO3232",
        ]}],
    },
    "Vol Transavia TO3232 Orly vers Sal": {
        "title": "Vol aller Paris Orly vers Sal",
        "intro": "Vol direct Transavia France TO3232 en Boeing 737-800, 6h15 de vol. Depart 06h30 heure de Paris, arrivee 10h45 heure du Cap-Vert (2h de decalage).",
        "conseil": "Prevoir de quoi manger a bord ou avant l embarquement : les services a bord sont payants chez Transavia.",
        "logistique": vol_logistique,
    },
    "Atterrissage a Sal - Aeroport Amilcar Cabral": {
        "title": "Arrivee a l aeroport Amilcar Cabral (SID)",
        "intro": "Le principal aeroport international du Cap-Vert, au centre de l ile de Sal, pres d Espargos. Santa Maria est a environ 18 km au sud.",
        "conseil": "Sans preenregistrement EASE fait a l avance, il faut regulariser sur place avec une attente plus longue et des frais. Le faire avant le 9/11.",
        "logistique": [
            {"titre": "Formalites a l arrivee", "lignes": [
                "Pas de visa pour un sejour de moins de 30 jours (ressortissants francais)",
                "Preenregistrement EASE obligatoire, taxe 3 400 CVE (~31 EUR) par personne, sur ease.gov.cv uniquement",
                "Presenter passeport + recu EASE au controle",
            ]},
            {"titre": "En sortant", "lignes": [
                "Distributeurs pour retirer des escudos",
                "Taxis officiels devant la sortie : 1 000 CVE (~9 EUR) jusqu au centre de Santa Maria le jour, minivan pour 4 avec valises. Ou Ady, par WhatsApp des l atterrissage (+238 952 97 19)",
                "Taxis devant l aerogare : fixer le prix avant de monter",
            ]},
        ],
    },
    AIRBNB: {
        "title": AIRBNB,
        "image": "airbnb.jpg",
        "intro": "Appartement entier loue sur Airbnb a Santa Maria, au cœur de la ville, dans un immeuble recent face a la plage avec piscine sur le toit. Hote : Sal Sol & Mar. Notre base pour les 7 nuits du sejour.",
        "conseil": "Toutes les consignes (codes, cles, regles de la maison) sont dans l appli Airbnb, rubrique Procedure d arrivee et Reglement interieur. Les telecharger avant le depart en cas de reseau faible.",
        "logistique": [
            {"titre": "Reservation", "lignes": [
                "RESERVE sur Airbnb - code de confirmation HMYTYQTCD3",
                "PAYE : 1 800,00 EUR (recu dans l appli Airbnb), soit 900 EUR par couple",
                "Annulation gratuite avant le 31/10 a 15h00",
                "Remboursement partiel en cas d annulation avant le 7/11 a 15h00",
            ]},
            {"titre": "Hote", "lignes": ["Telephone et WhatsApp : +351 961 976 139 (numero portugais)", "Messagerie Airbnb aussi disponible dans l appli"]},
            {"titre": "Adresse", "lignes": [ADR_AIRBNB, "A environ 20-25 min de l aeroport en voiture"]},
            {"titre": "Sejour", "lignes": ["Arrivee samedi 14/11 a partir de 15h00", "Depart samedi 21/11 avant 11h00 (vous partez a 08h00)", "7 nuits - 4 voyageurs"]},
        ],
    },
    "Premiere balade - plage et ponton de Santa Maria": {
        "title": "Plage et ponton de Santa Maria",
        "image": "ponton-santa-maria.jpg",
        "intro": "Santa Maria est la station balneaire du sud de Sal : une longue plage de sable blanc, une eau turquoise et un ponton en bois ou les pecheurs debarquent leurs prises en fin de journee.",
        "voir": ["Le retour de peche au ponton et la decoupe du thon sur place", "La promenade du front de mer", "Le coucher de soleil vers 17h58"],
        "conseil": "Le vent est souvent soutenu en novembre : la partie de plage abritee pres du ponton est plus agreable pour la baignade.",
    },
    "Route vers le Bikini Beach Club": {
        "title": "Acces au Bikini Beach Club",
        "image": "bikini-beach.jpg",
        "intro": "Le club se trouve sur la plage d Algodoeiro, dans la zone touristique ZDTI, a cote des hotels du groupe Lagoon dont le Melia Llana. Environ 10 min de voiture depuis Santa Maria.",
        "conseil": "En taxi depuis Santa Maria : 350 CVE le jour (tarif officiel). Une source decrit un court transfert en bateau pour rejoindre le club : demander a l accueil des hotels voisins si besoin. Arriver vers 12h50 pour etre a table a 13h00.",
        "logistique": [TAXI_BLOC],
    },
    "Brunch au Bikini Beach Club": {
        "title": "Brunch au Bikini Beach Club",
        "image": "bikini-brunch.jpg",
        "intro": "Beach club en bord de mer, ambiance musicale et detendue la journee. Le dimanche, formule brunch de 12h00 a 20h00.",
        "horaires": ["Dimanche 15/11 : reservation 13h00 - 14h30", "Club ouvert le dimanche de 12h00 a 20h00", "Ferme le lundi"],
        "tarifs": ["Non prepaye : reglement sur place", "Carte bancaire ou Apple Pay uniquement, pas d especes"],
        "conseil": "La table est tenue 1h30. Acces piscine demande dans le message de reservation, sans reponse ecrite : faire confirmer avant ou a l arrivee.",
        "logistique": [
            {"titre": "Reservation", "lignes": [
                "Au nom de Morieux - 4 personnes - zone Restaurant",
                "Dimanche 15 novembre 2026, 13h00 a 14h30",
                "Reserve le 11/10 sur Resos (bikini-beach-club.resos.com), message : brunch + acces piscine",
            ]},
            {"titre": "Contact", "lignes": [
                "Bikini Beach, ZDTI, plage d Algodoeiro, Ilha do Sal",
                "mathias@bikinibeachclub.com - info@bikinibeachclub.com",
                "bikinibeachclub.com - Instagram @bikinibeachcv",
            ]},
        ],
    },
    "RDV Cabo Verde Diving - Porto Antigo 1": {
        "title": "Plongee avec Cabo Verde Diving",
        "intro": "Centre de plongee installe a Santa Maria, avec un centre principal (Aquarium) sur le front de mer et des antennes dans plusieurs hotels. Journee en deux temps : preparation le matin, plongee en mer l apres-midi.",
        "horaires": ["RDV 08h30 au Porto Antigo 1", "09h00 - 11h30 : briefing et entrainement", "14h00 - 16h30 : plongee en mer"],
        "tarifs": ["PAYE : 226,72 EUR pour 2 personnes (Samuel et Cedric)"],
        "conseil": "Apporter maillot, serviette, creme solaire, une bouteille d eau. Signaler au centre tout probleme de sante. Respecter 12h minimum entre la derniere plongee et un vol : aucun souci ici, retour le 21/11.",
        "logistique": [
            {"titre": "Contact", "lignes": [
                "Cabo Verde Diving - Santa Maria, Sal",
                "Tel et WhatsApp : +238 595 37 96",
                "caboverdediving.net",
            ]},
            {"titre": "Statut", "lignes": ["RESERVE ET PAYE", "Participants : Samuel et Cedric"]},
        ],
    },
    "Enregistrement en ligne vol retour": {
        "title": "Enregistrement en ligne du retour",
        "intro": "L enregistrement en ligne Transavia ouvre 30h avant le vol TO3233, soit le vendredi 20/11 a 05h40 heure du Cap-Vert.",
        "conseil": "Enregistrer les 4 passagers et garder les cartes d embarquement hors ligne sur les telephones.",
        "logistique": [{"titre": "Reference", "lignes": ["PNR K6UNPB", "transavia.com, rubrique Ma reservation"]}],
    },
    "Check-out et route vers l aeroport": {
        "title": "Depart de Santa Maria",
        "intro": "Taxi a 08h00 devant le logement, arrivee a l aeroport vers 08h30, plus de 3h avant le vol de 11h40. Le taxi est a reserver la veille.",
        "conseil": "Faire le tour du logement la veille au soir pour ne rien oublier : chargeurs dans les prises, affaires dans le coffre-fort, le frigo. Reserver le taxi la veille : minivan pour 4 avec valises.",
        "logistique": [TAXI_BLOC],
    },
    "Arrivee aeroport de Sal - Enregistrement": {
        "title": "Aeroport de Sal - depart",
        "intro": "Petite aerogare, mais un seul vol peut generer une file au comptoir. Depot des bagages ferme 75 min avant le depart, soit a 10h25.",
        "logistique": [{"titre": "Deroule conseille", "lignes": [
            "08h45 : arrivee a l aeroport, comptoir Transavia, depot des bagages",
            "10h25 : fermeture du depot des bagages",
            "Controle des passeports et securite",
            "11h40 : decollage TO3233",
        ]}],
    },
    "Vol Transavia TO3233 Sal vers Orly": {
        "title": "Vol retour Sal vers Paris Orly",
        "intro": "Vol direct Transavia France TO3233 en Boeing 737-800, 5h50 de vol. Depart 11h40 heure du Cap-Vert, arrivee 19h30 heure de Paris.",
        "conseil": "Les escudos ne se changent pas facilement en France : les depenser avant de partir ou les garder pour un prochain voyage.",
        "logistique": vol_logistique,
    },
}
INFO["Angulo Beach Bar - journee transat"] = INFO_ANGULO = {
    "title": "Angulo - beach bar de Santa Maria",
    "image": "angulo.jpg",
    "intro": "Beach bar et restaurant installe directement sur la plage, rattache a un club de windsurf, a l est du centre de Santa Maria. Terrasse, transats et parasols, musique live certains soirs. La bonne adresse pour une journee transat avec dejeuner sur place.",
    "horaires": ["Tous les jours de 8h00 a 22h00", "Service du midi jusque vers 15h00 (selon les avis)"],
    "tarifs": ["Transats gratuits si on consomme au bar, sinon environ 5 EUR (avis 2024, a verifier)", "Carte variee : poisson, pates, pizzas, burgers, salades, plats vegetariens"],
    "voir": ["Les transats face a la mer", "Les kitesurfeurs et windsurfeurs de la baie", "Un cocktail en fin d apres-midi"],
    "conseil": "Arriver en milieu de matinee pour choisir ses transats. Creme solaire et chapeau : le vent rafraichit mais le soleil tape fort.",
    "logistique": [
        {"titre": "Adresse", "lignes": ["Angulo Cabo Verde - Praia Antonio de Sousa, Santa Maria, Ilha do Sal 4111", "Tel : +238 970 11 71", "A l est du centre de Santa Maria, accessible a pied ou en quelques minutes de voiture"]},
    ],
}
INFO["Lac sale de Pedra de Lume"] = {
    "title": "Salines de Pedra de Lume",
    "image": "pedra-de-lume.jpg",
    "intro": "Un ancien cratere volcanique au bord de la cote est, ou la mer s infiltre et s evapore depuis des siecles. On y a exploite le sel jusqu au XXe siecle. On entre par un tunnel creuse dans la roche, puis on decouvre les bassins blancs et roses au fond du cratere. L eau est si salee qu on flotte sans le moindre effort, comme en mer Morte.",
    "horaires": ["Tous les jours de 9h00 a 17h45", "Les cars d excursions arrivent surtout entre 10h et 14h : programme a 16h00 pour eviter la foule"],
    "tarifs": [
        "Entree : 5 a 6 EUR par personne selon les sources (660 CVE), baignade comprise",
        "Douche d eau douce : 1 EUR en pieces, environ 30 secondes d eau",
        "Paiement en ESPECES : la carte passe mal. Euros ou escudos, petites coupures",
        "Petit pourboire possible pour le guide du tunnel (2 a 5 EUR au total)",
    ],
    "duree": "1h30 a 2h, ou 30 min de plus pour le sentier du bord du cratere",
    "voir": [
        "Le tunnel d entree creuse dans la roche",
        "La baignade en flottaison dans le bassin principal",
        "Les anciens bassins et les montagnes de sel",
        "La boue volcanique a se passer sur la peau (odeur de soufre, peau douce ensuite)",
        "Le petit village de Pedra de Lume et son port en contrebas",
    ],
    "conseil": "CHAUSSURES D EAU OBLIGATOIRES : les cristaux de sel coupent les pieds nus. Ne pas se raser le matin meme, l eau pique sur la moindre coupure. Garder la tete hors de l eau, ne pas eclabousser, et poser une bouteille d eau douce au bord pour se rincer les yeux en cas de projection. 20 a 30 min dans l eau suffisent. Prendre un vieux maillot : le sel et le soufre abiment les tissus. Laisser bijoux et montres dans la voiture.",
    "logistique": [
        {"titre": "A emporter", "lignes": ["Chaussures d eau (une paire par personne)", "Vieux maillot porte sous les vetements", "Serviette", "Bouteille d eau douce pour les yeux", "Especes : environ 25 EUR pour 4 + pieces de 1 EUR pour la douche"]},
        {"titre": "Acces", "lignes": ["Environ 30 min depuis Santa Maria par la route goudronnee", "Cote est de l ile, au nord-est d Espargos", "Cafe sur place pour une boisson fraiche"]},
    ],
}
INFO["Buracona et l Oeil Bleu"] = {
    "title": "Buracona et l Oeil Bleu (Olho Azul)",
    "image": "oeil-bleu.jpg",
    "intro": "Sur la cote nord-ouest, une plateforme de lave noire battue par l Atlantique. Deux attractions : une grande piscine naturelle ou l on peut se baigner quand la mer est calme, et une grotte, l Oeil Bleu, ou la lumiere du soleil entre par une ouverture sous-marine et rend l eau d un bleu electrique.",
    "horaires": ["Tous les jours de 9h00 a 18h00", "Oeil Bleu visible seulement entre 11h00 et 13h00 environ, quand le soleil est au plus haut", "Ciel couvert ou brume : effet faible ou absent"],
    "tarifs": ["Entree : environ 3 EUR par personne, en ESPECES (euros ou escudos)", "Le tarif peut changer : prevoir un peu de marge"],
    "duree": "45 min a 1h30",
    "voir": [
        "L Oeil Bleu : file d attente courte pour regarder dans la grotte, quelques minutes chacun",
        "La piscine naturelle dans la lave, baignade si la mer est calme",
        "Les vagues qui explosent contre la cote noire",
        "Le paysage lunaire de la piste d acces",
    ],
    "conseil": "Chaussures fermees ou chaussures d eau : le basalte est coupant, brulant au soleil et glissant pres de l eau. Baignade uniquement dans le bassin, quand les gardiens l autorisent et si les vagues n atteignent pas la plateforme. Interdiction absolue de se baigner ou de sauter dans la grotte. Ne jamais tourner le dos a la mer. Peu d ombre : chapeau, creme et eau.",
    "logistique": [
        {"titre": "Acces", "lignes": ["Environ 6 km au nord de Palmeira, suivre les panneaux Buracona", "Derniers kilometres sur piste de cailloux, presque sans signalisation", "Pas de taxi classique : chauffeur en 4x4 ou pick-up, beaucoup de taxis normaux refusent la piste", "Le chauffeur attend sur le parking pendant la visite"]},
        {"titre": "Sur place", "lignes": ["Accueil, cafe-restaurant, toilettes, souvenirs", "Vestiaires sommaires : maillot sous les vetements", "Vendeurs parfois insistants"]},
    ],
}
INFO["Dejeuner de poisson a Palmeira"] = {
    "title": "Palmeira, le port de la cote ouest",
    "image": "gata-fish.jpg",
    "mapsUrl": "https://www.google.com/maps/search/?api=1&query=Gata+Fish+%26+Yacht+Club+Palmeira+Sal+Cabo+Verde",
    "mapsLabel": "Gata Fish & Yacht Club sur Maps",
    "intro": "Le principal port de l ile apres l aeroport : bateaux de peche colores, petites maisons et quelques restaurants simples ou l on mange le poisson du jour. Ambiance de village, tres loin des resorts de Santa Maria.",
    "voir": ["Le port et les barques de peche", "Le poisson du jour grille, souvent thon, wahoo ou merou selon la peche", "La cachupa, le plat national (mais de haricots, mais et viande ou poisson)"],
    "conseil": "RESERVE par WhatsApp au nom de Morieux : mardi 17/11 vers 12h30, 4 personnes. Demander le prix du poisson du jour ou de la langouste avant de commander (un avis signale un ecart sur l addition). Service lent : compter 1h30, c est le rythme de l ile.",
    "logistique": [
        {"titre": "Reservation", "lignes": ["Au nom de Morieux - 4 personnes", "Mardi 17 novembre 2026 vers 12h30", "Reserve le 29/10 par WhatsApp, confirme par le restaurant le 30/10"]},
        {"titre": "Notre choix : Gata Fish & Yacht Club", "lignes": [
            "Sur le port de Palmeira",
            "4,4/5 sur Tripadvisor (120 avis), Travellers Choice 2026",
            "Specialites : langouste (lagosta suada), carpaccio de thon, buzios, lapas, cachupa",
            "Ouvert tous les jours de 9h00 a 17h00",
            "Tel et WhatsApp : +238 950 13 28",
            "Carte bancaire acceptee",
            "Budget : environ 25 a 40 EUR par personne",
            "Points faibles cites dans les avis : attente longue, peu d anglais parle",
        ]},
        {"titre": "Plan B", "lignes": ["Esplanada Rotterdam, aussi a Palmeira : 4,0/5 (89 avis), poisson frais et fruits de mer"]},
    ],
}
INFO["Balade a Espargos"] = {
    "title": "Espargos, la ville de l ile",
    "image": "espargos.jpg",
    "intro": "Capitale administrative de Sal, au centre de l ile, pres de l aeroport. Les Capverdiens y vivent et y travaillent : marche, petites boutiques, rues aux facades colorees. Un apercu de la vie locale en une heure.",
    "conseil": "Se garer pres de la place centrale et marcher. Bon endroit pour retirer des escudos et faire le plein avant de rentrer.",
}
INFO["Route vers Buracona"] = {
    "title": "Route vers Buracona",
    "intro": "D Espargos, traverser l ile vers Palmeira sur la cote ouest, puis prendre la piste vers le nord. Environ 25 min au total.",
    "conseil": "Arriver vers 11h00 permet d etre dans le creneau de l Oeil Bleu (11h-13h). Rouler doucement sur la piste et eviter les ornieres de sable.",
}
INFO["Diner en musique a l Ocean Cafe"] = {
    "title": "Ocean Cafe - place centrale",
    "image": "ocean-cafe.jpg",
    "intro": "Le rendez-vous anime du centre de Santa Maria, sur la place principale, a une rue de la plage. Musique live presque tous les soirs avec des guitaristes et chanteurs locaux, DJ le week-end, ambiance festive ou l on finit souvent par danser.",
    "horaires": ["Tous les jours de 7h00 a 1h00", "Musique live presque tous les soirs, sans programme fixe"],
    "voir": ["La terrasse sur la place pour profiter de la musique", "Plateau de poissons grilles, calamars, crevettes", "Pizzas fines, fish and chips, burgers", "Bieres locales et cocktails"],
    "conseil": "RESERVE par WhatsApp au nom de Morieux : lundi 16/11 a 19h30, 4 personnes. La terrasse pres des musiciens a ete demandee mais pas confirmee : la redemander en arrivant.",
    "logistique": [{"titre": "Reservation", "lignes": ["Au nom de Morieux - 4 personnes", "Lundi 16 novembre 2026 a 19h30", "Reserve le 29/10 par WhatsApp, confirme par le restaurant le 30/10"]}, {"titre": "Contact", "lignes": ["Praca Central, Santa Maria", "Tel et WhatsApp : +238 580 35 05"]}],
}
INFO["Verre et concert au Buddy Bar"] = {
    "title": "Buddy Bar - musique live",
    "image": "buddy-bar.jpg",
    "intro": "Classe numero 1 des concerts de Santa Maria sur Tripadvisor (4,5/5, 177 avis). Terrasse sur l axe principal, melange de touristes et de Capverdiens, groupe live presque tous les soirs (funana, reggae, musique capverdienne), puis DJ jusque tard.",
    "horaires": ["Tous les soirs a partir de 18h00, jusque tard (horaires du mardi a verifier)", "Musique live le plus souvent jusque vers 1h00"],
    "tarifs": ["Cocktails autour de 6 EUR (pinte de pina colada citee a 6 EUR)", "Bar uniquement : on y va apres le diner"],
    "conseil": "Plusieurs avis signalent des erreurs d addition et des frais pour paiement par carte : verifier l addition, payer en especes de preference, garder un oeil sur ses affaires et ignorer les rabatteurs de rue.",
}
INFO["Diner et karaoke a l Atlantic Piano Bar & Grill"] = {
    "title": "Atlantic Piano Bar & Grill",
    "image": "atlantic.jpg",
    "intro": "Bar-grill chic de Santa Maria, connu pour ses viandes premium et sa musique live toute la semaine, avec des artistes locaux et internationaux. Le dimanche, karaoke dans la rue : ambiance garantie.",
    "voir": ["Steaks premium : tomahawk, T-bone, faux-filet, entrecote", "Poulpe et carpaccio de boeuf", "Cocktails classiques et signatures"],
    "conseil": "La table n est gardee que 15 minutes apres 19h45 : partir a l heure de l Ola Brasil, ou prevenir sur WhatsApp en cas de retard.",
    "logistique": [
        {"titre": "Reservation", "lignes": [
            "Au nom de Morieux - 4 personnes",
            "Dimanche 15 novembre 2026 a 19h45",
            "Reserve sur TableHelm (date dans le mail de confirmation)",
            "Table gardee 15 minutes apres l heure de reservation",
            "Modifier ou annuler : lien Manage or cancel dans le mail de confirmation TableHelm",
            "Non prepaye : reglement sur place par carte bancaire",
        ]},
        {"titre": "Contact", "lignes": [
            "WhatsApp : +238 975 51 53 (retard, question)",
            "Instagram : atlanticpianobarcv",
        ]},
    ],
}
INFO["Croisiere en catamaran - Cape Verde Sailing"] = {
    "title": "Catamaran demi-journee - Cape Verde Sailing",
    "image": "catamaran-voile.jpg",
    "intro": "Sortie de trois heures en catamaran a voile au depart de Santa Maria, avec l equipe de Cape Verde Sailing. On longe la cote sud-ouest de Sal, on passe au large de Ponta do Sino, puis arret baignade et snorkeling dans une eau turquoise, selon la mer du jour. En-cas et boissons a volonte a bord.",
    "horaires": ["Mercredi 18/11 : depart a 08h30 (sortie du matin, mer plus calme)", "Rendez-vous a 08h20 au Palm Beach Restaurant (confirme par Cape Verde Sailing)", "Le chauffeur attend 5 minutes maximum", "Retour : depose au Palm Beach Restaurant"],
    "tarifs": ["Reserve et regle sur Viator (montant dans la confirmation Viator), environ 59 EUR par adulte", "Prise en charge et retour en bus compris", "Pourboire de l equipage non compris"],
    "voir": ["Le passage au large de Ponta do Sino et de son phare", "La baignade et le snorkeling", "Dauphins, tortues, poissons volants ou baleines si on a de la chance"],
    "conseil": "RENDEZ-VOUS CONFIRME : 08h20 au Palm Beach Restaurant, chauffeur 5 minutes d attente maximum. Viser 08h10 sur place. Pour ceux qui craignent le mal de mer, prendre un comprime avant d embarquer : la houle peut etre forte. Le vent peut raccourcir la sortie ou deplacer l arret baignade.",
    "logistique": [
        {"titre": "Reservation", "lignes": ["RESERVE sur Viator - reference 1460555133", "Au nom de Samuel Morieux - 4 adultes", "Mercredi 18 novembre 2026, depart a 08h30", "Catamaran demi-journee - guide en anglais", "Annulation gratuite jusqu au 17/11 a 08h30 (heure du Cap-Vert), ensuite non remboursable", "Aucune modification acceptee moins de 24h avant", "Billet (e-card) dans Apple Wallet sur l iPhone de Samuel, et dans l appli Viator", "Modifier ou annuler : viator.com/account/bookings", "Meteo defavorable : nouvelle date ou remboursement"]},
        {"titre": "Rendez-vous", "lignes": ["Mercredi 18/11 a 08h20 au Palm Beach Restaurant, Santa Maria", "Chauffeur de Cape Verde Sailing : 5 minutes d attente maximum", "Depart du bateau : l un de leurs deux points selon le vent (ponton de Santa Maria en travaux)", "Retour : depose au Palm Beach Restaurant", "Confirme par WhatsApp le 29/10"]},
        {"titre": "Contact", "lignes": ["Cape Verde Sailing : +238 933 95 10 (telephone et WhatsApp)", "Chat Viator dans l appli", "CapeVerdeSailing@gmail.com"]},
        {"titre": "A bord", "lignes": ["Compris : en-cas, biere, vin, sodas, eau, masques et tubas", "Pas de vrai repas : dejeuner prevu au LobStar au retour", "25 personnes maximum", "Telephone dans une pochette etanche"]},
    ],
}
INFO["Rendez-vous au Palm Beach Restaurant"] = INFO["Croisiere en catamaran - Cape Verde Sailing"]
INFO["Dejeuner au LobStar, au pied du ponton"] = {
    "title": "LobStar - au pied du ponton",
    "intro": "Cabane en pierre sur le front de mer de Santa Maria, au pied du ponton ou les pecheurs debarquent leur prise. La langouste y est la specialite, cuisinee de plusieurs facons.",
    "voir": ["La langouste grillee a la cap-verdienne", "Le risotto a la langouste", "Le poisson du jour"],
    "conseil": "Demander le prix de la langouste avant de commander, elle se vend souvent au poids. Prevoir des especes au cas ou.",
    "logistique": [{"titre": "Pratique", "lignes": ["Front de mer, au pied du ponton de Santa Maria", "Retour du catamaran au Palm Beach Restaurant, puis a pied le long du front de mer", "4,3/5 sur pres de 920 avis Tripadvisor"]}],
}
INFO["Diner chez Il Gobbo"] = {
    "title": "Il Gobbo - italien",
    "image": "il-gobbo.jpg",
    "intro": "Petit restaurant italien de la Rua 15 de Agosto, a quelques pas du logement, parmi les mieux notes de Santa Maria. Cuisine soignee, pates et produits de la mer, cadre intime.",
    "conseil": "RESERVE par WhatsApp au nom de Morieux : mercredi 18/11 a 19h30, 4 personnes. Specialite mise en avant par la maison : la langouste fraiche a la catalane. Prevoir des especes si la carte ne passe pas.",
    "logistique": [{"titre": "Reservation", "lignes": ["Au nom de Morieux - 4 personnes", "Mercredi 18 novembre 2026 a 19h30", "Reserve le 29/10 par WhatsApp, confirme par le restaurant"]}, {"titre": "Pratique", "lignes": ["Rua 15 de Agosto, Santa Maria", "Mercredi : 11h00-15h00 et 18h00-22h00, ferme le mardi", "Tel et WhatsApp : +238 952 41 29", "4,9/5 sur 233 avis Google"]}],
}
INFO["Transats a Angulo Beach Bar"] = dict(INFO_ANGULO, conseil="Journee farniente : prendre les transats le matin, les garder en allant dejeuner au Palm Beach si le bar l accepte, sinon les reprendre a 14h30. Consommer au bar suffit en general pour ne pas payer les transats. Creme solaire, chapeau, eau : le soleil tape fort meme en novembre.")
INFO["Apres-midi transats a Angulo"] = INFO["Transats a Angulo Beach Bar"]
INFO["Coucher de soleil a Ponta Preta"] = {
    "title": "Restaurant Ponta Preta - coucher de soleil",
    "image": "ponta-preta.jpg",
    "intro": "Restaurant de plage sur la cote ouest de l ile, au bord de la plage de Ponta Preta, celebre pour ses vagues de surf et ses couchers de soleil. Contrairement a la plage de Santa Maria, tournee vers le sud, Ponta Preta regarde plein ouest : le soleil plonge dans l Atlantique, sans terre ni batiment devant.",
    "voir": ["Le soleil qui disparait dans l ocean vers 17h57", "Les surfeurs et kitesurfeurs dans les rouleaux", "Un grogue ou un ponche, les alcools locaux, ou une caipirinha"],
    "conseil": "Arriver vers 17h30 pour avoir une table au premier rang : c est le spot coucher de soleil le plus connu de l ile. Pas besoin de conducteur sobre : on vient en taxi. Mais caler le retour a l aller avec le chauffeur, car peu de taxis passent ici a la nuit tombee.",
    "logistique": [
        {"titre": "Acces", "lignes": ["Plage de Ponta Preta, cote ouest, au nord-ouest de Santa Maria", "Environ 10 a 15 minutes en voiture depuis le centre de Santa Maria", "Trop loin a pied : environ 1 heure par la plage", "Taxi : 500 CVE le jour, 700 CVE la nuit (tarifs officiels)"]},
        TAXI_BLOC,
        {"titre": "Pratique", "lignes": ["4,1/5 sur Tripadvisor (382 avis)", "Tel : +238 991 86 13", "Ouvert la journee et apres le coucher du soleil (horaires non publies, appeler pour verifier)", "Prevoir des especes au cas ou la carte ne passe pas"]},
    ],
}
INFO["Retour de Ponta Preta"] = INFO["Coucher de soleil a Ponta Preta"]
INFO["Diner de fete au Soul Kitchen"] = {
    "title": "Soul Kitchen",
    "intro": "Restaurant de plage a Santa Maria, a l etage de La Villa Beach Lounge, avec une terrasse face a l ocean. Musique live tous les soirs a partir de 19h00 : le bon endroit pour un dernier diner qui lance la soiree avant la White Party.",
    "horaires": ["Tous les jours de 09h00 a 22h30", "Musique live des 19h00"],
    "voir": ["Les pates aux fruits de mer, le plat le plus cite", "Le poisson du jour", "Le menu vegetarien, rare sur l ile", "Le concert en terrasse au coucher du jour"],
    "tarifs": ["Environ 40 a 50 EUR par personne avec le vin", "Carte acceptee, supplement possible d environ 3 % : especes conseillees"],
    "conseil": "Sans reservation : arriver vers 19h00. Le service peut etre lent quand c est plein, alors commander plat et dessert d un coup et demander l addition vers 21h20 pour partir a 21h40 vers le Bikini Beach Club. Si c est complet, plan B : Baraonda, dans le centre (+238 596 61 96, 18h00-23h00).",
    "logistique": [
        {"titre": "Pratique", "lignes": ["Plage de Santa Maria, a l etage de La Villa Beach Lounge", "A pied depuis le logement par le front de mer", "Tel : +238 997 47 61", "4,6/5 sur Tripadvisor (816 avis)"]},
    ],
}
INFO["Kizomba au Pub Calema"] = {
    "title": "Pub Calema - kizomba",
    "intro": "Bar local du centre de Santa Maria, connu pour la kizomba. Pas de deco, des chaises sur le trottoir, mais une vraie piste ou habitants et voyageurs dansent ensemble. Le meilleur endroit pour finir le sejour dans l ambiance cap-verdienne.",
    "voir": ["La kizomba et le funana, les danses de l archipel", "Les danseurs locaux, souvent tres bons", "Un grogue, le rhum de canne local"],
    "conseil": "Se laisser inviter a danser : c est le principe. Garder un oeil sur ses affaires dans la foule et payer en especes, plus simple.",
    "logistique": [
        {"titre": "Pratique", "lignes": ["Rua 1 de Junho, centre de Santa Maria", "A pied depuis le front de mer (5 a 10 min) ou en taxi", "Ouvert tous les jours de 17h00 a 04h00", "Tel : +238 908 47 84"]},
    ],
}
INFO["Fin de soiree au Disco Pirata"] = {
    "title": "Disco Pirata",
    "intro": "La discotheque historique de Santa Maria, sous le Frankie s Bar, juste a cote du front de mer. Le vendredi est l une des deux soirees phares de la semaine, avec DJ et parfois des groupes.",
    "voir": ["Le melange hits internationaux et musique cap-verdienne", "La piste qui se remplit apres minuit"],
    "conseil": "Y aller pour une heure ou deux, pas plus : reveil a 07h00 et depart a 08h00. Entree parfois payante en especes a la porte. Retour a pied au logement, tout est dans le centre.",
    "logistique": [
        {"titre": "Pratique", "lignes": ["Sous le Frankie s Bar, zone de la plage, centre de Santa Maria", "Ouvert le week-end, de tard le soir jusqu au petit matin", "Prix moyens, cover en especes certains soirs", "Horaires variables selon la saison : verifier sur place dans la journee"]},
    ],
}
INFO["White Party au Bikini Beach Club"] = {
    "title": "White Party au Bikini Beach Club",
    "image": "white-party.jpg",
    "intro": "Chaque vendredi soir, le Bikini Beach Club, ou vous aurez brunche le dimanche, se transforme en club : dress code tout en blanc, DJ, cocktails, et la piscine et la mer en decor. La plus belle fete de la semaine sur l ile.",
    "horaires": ["Notre table : vendredi 20/11 de 22h00 a 01h30 (3h30)", "Soiree de 22h00 a 03h00 (club ouvert depuis 12h00)"],
    "tarifs": ["Un cocktail de bienvenue offert", "Autres prix non publies", "Carte bancaire et Apple Pay acceptes"],
    "voir": ["Tout le monde en blanc au bord de l eau", "Le DJ sur la terrasse face a l ocean"],
    "conseil": "Mettre une tenue blanche dans les valises des le depart de France. Table reservee : surveiller les mails, le club peut demander de reconfirmer la reservation avant la date. La table est rendue a 01h30 : c est aussi l heure du taxi retour. Plan B dans le centre de Santa Maria, a pied : Pub Calema pour la kizomba (Rua 1 de Junho, ouvert jusqu a 04h00), puis Disco Pirata, sous le Frankie s Bar.",
    "logistique": [
        {"titre": "Reservation", "lignes": ["RESERVE - confirme sur bikinibeachclub.com", "Au nom de Morieux - 4 personnes - zone White Party", "Vendredi 20 novembre 2026, 22h00 a 01h30 (table gardee 3h30)", "Reconfirmation possible demandee par le club avant la date", "Annuler ou ecrire au club : lien du mail de confirmation", "Mail du club : Info@bikinibeachclub.com"]},
        {"titre": "Acces", "lignes": ["Plage d Algodoeiro, zone touristique ZDTI, a cote du Melia Llana", "Environ 4 km du centre de Santa Maria : 10 minutes en taxi, 45 min a 1h a pied", "Pas de voiture ce soir : taxi aller et retour"]},
        {"titre": "Taxis : mode d emploi", "lignes": ["Pas d Uber ni de Bolt sur l ile : taxis classiques, licencies et controles par la police", "Pas de compteur : annoncer la destination et fixer le prix avant de monter", "Tarifs officiels : 150 CVE dans Santa Maria (200 la nuit)", "Bikini Beach (hotels Melia) : 350 CVE le jour, 450 CVE la nuit, soit environ 4 EUR la course", "Payer en euros ou escudos, petites coupures", "Aller : le Soul Kitchen appelle un taxi, ou taxis sur la place centrale", "Prendre le numero ou WhatsApp du chauffeur a l aller et caler le retour a 01h30", "Plan B retour : l accueil du club appelle un taxi", "Encore plus simple : demander dans la semaine un chauffeur de confiance a l hote Airbnb et reserver aller et retour"]},
    ],
}
INFO["Taxi vers le Bikini Beach Club"] = INFO["White Party au Bikini Beach Club"]
INFO["Taxi retour au logement"] = INFO["White Party au Bikini Beach Club"]
INFO["Dejeuner a Area Docas - Pedra de Lume"] = {
    "title": "Area Docas - Pedra de Lume",
    "image": "area-docas.jpg",
    "intro": "Restaurant de poisson sur le petit port de Pedra de Lume, sur la cote est, juste en face de l entree des salines. Terrasse face a l ocean, cuisine de la mer simple et fraiche, loin de l agitation de Santa Maria. Le bon arret pour dejeuner avant Shark Bay, a quelques minutes de route.",
    "voir": ["Le poisson du jour grille et le carpaccio de poisson", "La langouste, si on a le temps d attendre", "Le fromage de chevre a la confiture de papaye en dessert"],
    "conseil": "Arriver vers 12h50 pour avoir une table face a la mer. Si vous prenez la langouste, la commander des l arrivee : les avis signalent de l attente. Partir vers 15h00 pour etre a Shark Bay a maree montante. Les pizzas sont jugees moyennes : rester sur le poisson.",
    "logistique": [
        {"titre": "Pratique", "lignes": ["Port de Pedra de Lume, face a l entree des salines", "25 a 30 minutes en voiture depuis Santa Maria", "Shark Bay a environ 3 km au sud, 10 minutes de route", "Ouvert tous les jours de 10h00 a 22h00", "4,3/5 sur Google (295 avis), 4,1/5 sur Tripadvisor (35 avis)", "Prix raisonnables selon les avis, especes conseillees"]},
        {"titre": "Chauffeur de l apres-midi", "lignes": ["Reserve la veille (jeudi 19/11) : Ady, +238 952 97 19 (WhatsApp)", "Lui demander d appeler Area Docas la veille ou le matin pour garder une table de 4 vers 12h50", "12h20 logement, Pedra de Lume, Shark Bay, retour vers 17h30", "Forfait a negocier avec attente : environ 50 a 70 EUR la voiture (estimation)", "Repere officiel : Santa Maria - Pedra de Lume 1 400 CVE la course simple"]},
        TAXI_BLOC,
    ],
}
INFO["Route vers Pedra de Lume pour dejeuner"] = INFO["Dejeuner a Area Docas - Pedra de Lume"]
INFO["Petit-dejeuner chez Cam s"] = {
    "title": "Cam s Restaurante e Cafetaria",
    "intro": "Le cafe-restaurant cap-verdien du centre, dans la meme rue que le logement. Ouvert tot, petits prix, et l occasion de gouter le vrai petit-dejeuner de l archipel.",
    "voir": ["La cachupa guisada : la cachupa de la veille revenue a la poele, avec chorizo et oeuf au plat", "Les jus de fruits frais presses", "Un cafe cap-verdien, cultive sur l ile de Fogo"],
    "conseil": "Ferme le dimanche. Ouvre a 07h30 : pratique pour les matins ou l on part tot.",
    "logistique": [
        {"titre": "Pratique", "lignes": ["Rua 15 de Agosto, centre de Santa Maria", "Du lundi au samedi de 07h30 a 22h00, ferme le dimanche", "Tel : +238 954 53 76", "4,5/5 sur Google (1 080 avis), 4,3/5 sur Tripadvisor (495 avis)", "Cachupa guisada avec chorizo et oeuf : environ 4 EUR"]},
    ],
}
INFO["Petit-dejeuner chez Cam s avant la croisiere"] = INFO["Petit-dejeuner chez Cam s"]
INFO["Dernier petit-dejeuner chez Cam s"] = INFO["Petit-dejeuner chez Cam s"]
INFO["Petit-dejeuner au Cape Fruit"] = {
    "title": "Cape Fruit",
    "intro": "Le cafe-brunch le plus populaire de Santa Maria, dans la meme rue que le logement. Ambiance detendue, cuisine fraiche et coloree, ideal pour une matinee sans se presser.",
    "voir": ["Les pancakes et les crepes banane-chocolat", "Les bols de fruits tropicaux et les smoothies", "Les assiettes au saumon"],
    "conseil": "Souvent plein en milieu de matinee : arriver avant 10h00 pour avoir une table. Ferme a 16h00.",
    "logistique": [
        {"titre": "Pratique", "lignes": ["Rua 15 de Agosto, centre de Santa Maria", "Tous les jours de 08h00 a 16h00", "Tel : +238 982 22 05", "4,6/5 sur Tripadvisor (1 253 avis), 4,4/5 sur Google (1 035 avis)"]},
    ],
}
INFO["Petit-dejeuner tranquille au Cape Fruit"] = INFO["Petit-dejeuner au Cape Fruit"]
INFO["Petit-dejeuner au Papaya Cafe"] = {
    "title": "Papaya Cafe Cabo Verde",
    "image": "papaya.jpg",
    "intro": "Café coloré sur la rue pietonne principale de Santa Maria, a 5 minutes a pied du logement. Petits-dejeuners sucres et frais, jus presses et cafes de specialite, terrasse pour regarder passer le centre-ville.",
    "voir": ["Le bol d’açaí garni de fruits frais", "Les pancakes, le plat le plus cite dans les avis", "Les jus de fruits presses et les smoothies", "Cafes chauds et glaces"],
    "conseil": "Commander leger : le brunch du Bikini Beach Club est a 13h00. Le service peut etre lent aux heures de pointe, mais a 10h00 un dimanche ca passe.",
    "logistique": [
        {"titre": "Pratique", "lignes": ["Rue pietonne principale, centre de Santa Maria", "Tous les jours de 07h30 a 22h30", "Tel : +238 976 81 81", "Carte bancaire acceptee (Visa, Mastercard)", "4,2/5 sur Tripadvisor, 4,3/5 sur Google"]},
    ],
}
INFO["Piscine sur le toit de l immeuble"] = {
    "title": "Piscine sur le toit",
    "image": "airbnb.jpg",
    "intro": "La piscine sur le toit de notre immeuble, face a la plage de Santa Maria : une baignade au calme entre le petit-dejeuner et le Bikini Beach Club.",
    "conseil": "Prendre serviettes et creme solaire. Prevoir de redescendre vers 12h15 pour se changer : le taxi part a 12h35.",
}
INFO["Taxi de l aeroport vers le logement"] = {
    "title": "Taxi aeroport - Santa Maria",
    "intro": "Pas de voiture de location pour ce sejour. L hote Airbnb nous a donne le contact de son chauffeur habituel, Ady : le reserver pour l arrivee, il peut aussi organiser la visite de l ile. A defaut, la file des taxis officiels est juste devant l aerogare. Environ 20 minutes jusqu au logement.",
    "conseil": "Ecrire a Ady sur WhatsApp des l atterrissage, vers 11h00 (+238 952 97 19) : vol TO3232, 4 personnes et 4 valises. Inutile de le reserver a l avance, il y a toujours des taxis devant l aerogare. Plan B : Taxi Sal Island, +238 599 59 73 (WhatsApp). Fixer le prix a l avance. Avec un taxi de la file : minivan ou 2 taxis, prix fixe avant de charger les bagages.",
    "logistique": [TAXI_BLOC],
}
INFO["Taxi retour du Bikini Beach"] = {
    "title": "Taxi Bikini Beach - Santa Maria",
    "intro": "L accueil du club appelle un taxi, ou on en prend un devant le Melia Llana voisin. Environ 10 minutes jusqu au logement.",
    "logistique": [TAXI_BLOC],
}
INFO["Chauffeur de la journee - depart"] = {
    "title": "Un chauffeur pour la journee",
    "intro": "Sans voiture de location, le tour du nord se fait avec un chauffeur de taxi reserve pour la journee. Il attend a chaque arret et connait les pistes. C est courant sur l ile et souvent plus detendu que de conduire soi-meme.",
    "conseil": "Reserver la veille (lundi 16/11) avec Ady, le chauffeur de l hote Airbnb : +238 952 97 19 (WhatsApp). Il organise aussi les visites de l ile. Exiger un 4x4 ou un pick-up pour la piste de Buracona. Fixer a l avance le prix pour la journee complete, attente comprise, et le programme. Payer en especes a la fin. Lui offrir le dejeuner a Palmeira est apprecie.",
    "logistique": [
        {"titre": "Prix", "lignes": ["Pas de tarif officiel pour une journee : a negocier", "Ordre de grandeur : 80 a 120 EUR la voiture pour la journee (estimation, pas un prix publie)", "Repere officiel : une course simple Santa Maria - Palmeira coute deja 1 400 CVE (~13 EUR)", "Alternative cle en main : tour prive en 4x4 chez Cabomundo, 190 EUR la demi-journee ou 260 EUR la journee pour 3-4 personnes, dejeuner compris, entrees en plus (cabomundo.com)"]},
        {"titre": "Programme a donner au chauffeur", "lignes": ["10h00 depart du logement, Rua 15 Agosto 108", "Buracona (Olho Azul) vers 10h45", "12h30 dejeuner au Gata Fish & Yacht Club, Palmeira", "14h40 Shark Bay, pres de l epave (maree haute 14h01)", "16h00 salines de Pedra de Lume", "17h30 retour au logement"]},
        TAXI_BLOC,
    ],
}
INFO["Taxi vers Ponta Preta"] = INFO["Coucher de soleil a Ponta Preta"]
INFO["Dejeuner pieds dans le sable et transats a Angulo"] = dict(INFO_ANGULO, conseil="Arriver avant 14h00 pour etre servi au dejeuner (service du midi jusque vers 15h00). Demander des transats en commandant : gratuits si on consomme. Les valises sont deja deposees au logement. Plan B pieds dans le sable : Barracuda, sur la plage de Santa Maria pres du ponton (12h00-16h00 et 19h00-23h00, especes uniquement, +238 599 04 50).")
INFO["Diner homard grille au Barracuda"] = {
    "title": "Restaurante Barracuda - homard grille",
    "image": "barracuda.jpg",
    "intro": "Le restaurant les pieds dans le sable de la plage de Santa Maria, pres du ponton : les pecheurs debarquent leur prise juste devant. Specialites de la mer, homard et langouste grilles, poissons parfois rares que le personnel conseille volontiers, sauces maison.",
    "horaires": ["Tous les jours 12h00-16h00 et 19h00-23h00"],
    "tarifs": ["Homard et langouste : prix souvent au poids, a demander avant de commander", "Portions genereuses, souvent prevues pour deux", "ESPECES UNIQUEMENT"],
    "voir": ["Homard ou langouste grilles", "Poisson du jour grille", "Le coucher de soleil depuis les tables dans le sable"],
    "conseil": "RESERVE par WhatsApp au nom de Morieux : jeudi 19/11 a 19h00, 4 personnes, en bord de mer. Etre a l heure. Faire peser et chiffrer le homard avant cuisson. Avoir assez d especes sur soi.",
    "logistique": [{"titre": "Reservation", "lignes": ["Au nom de Morieux - 4 personnes", "Jeudi 19 novembre 2026 a 19h00", "Table en bord de mer", "Reserve le 29/10 par WhatsApp, confirme par le restaurant"]}, {"titre": "Contact", "lignes": ["Plage de Santa Maria, pres du ponton", "Tel (Google Maps, le plus a jour) : +238 599 04 50", "Fixe du site officiel : +238 242 80 10", "Mail : barracudagrupo10@gmail.com", "restaurantebarracuda.com", "4,1/5 sur Tripadvisor (1 844 avis), 4,3/5 sur Google"]},
                   {"titre": "Plan B langouste", "lignes": ["LobStar, sur la jetee de Santa Maria : 4,3/5 (921 avis), specialiste de la langouste mais plutot cuisinee (catalane, risotto) que grillee"]}],
}
INFO["Shark Bay - les requins citrons"] = {
    "title": "Shark Bay - les requins citrons",
    "image": "shark-bay.jpg",
    "intro": "Une cote rocheuse et peu profonde du milieu de la cote est de Sal, ou de jeunes requins citrons viennent tourner autour des visiteurs qui marchent dans l eau jusqu aux genoux. Spectaculaire et sans danger si on respecte les consignes.",
    "horaires": ["Acces libre", "Mardi 17/11 : maree haute 14h01, maree basse 19h28", "Visite prevue 14h40-15h40, juste apres la maree haute : eau assez profonde, requins proches du bord"],
    "tarifs": ["Pas de droit d entree officiel", "Location de chaussures d eau sur place : environ 3 EUR", "Toilettes : 1 EUR", "Guide facultatif : la plupart des sources conseillent de s en passer"],
    "voir": ["Les jeunes requins citrons, a 50-100 m du bord", "L epave du grand bateau echoue, point de repere", "La cote volcanique et le recif"],
    "conseil": "Rester immobile et laisser les requins venir, ne jamais les toucher ni les nourrir. Chaussures d eau indispensables : roches volcaniques, coraux et oursins. Pas d ombre : creme et chapeau. A maree tres basse, l eau est trop peu profonde et les requins s eloignent, d ou le creneau de l apres-midi. Requins plus ou moins presents selon les jours, aucune garantie.",
    "logistique": [{"titre": "Acces", "lignes": [
        "Avec le chauffeur du tour du nord, qui attend pendant la visite",
        "Depuis Palmeira : retour vers Espargos puis la cote est",
        "Puis piste de sable cote mer jusqu a l epave",
        "Environ 35 min, rouler doucement sur la piste",
        "Ensuite Pedra de Lume, a environ 3 km : 10 min",
    ]}],
}
INFO["Dejeuner au Palm Beach Restaurant"] = {
    "title": "Palm Beach Restaurant",
    "image": "palm-beach.jpg",
    "intro": "Restaurant du centre de Santa Maria, specialise dans le poisson frais et les pizzas, avec vue sur la mer. Ambiance decontractee et chaleureuse.",
    "horaires": ["Tous les jours a partir de 11h00"],
    "tarifs": ["Milieu de gamme : environ 25 EUR par personne"],
    "voir": ["Poisson local du jour", "Pizzas", "Desserts maison"],
    "conseil": "4,2/5 sur pres de 1 000 avis Google et 4,2/5 sur 1 103 avis Tripadvisor. Reservation conseillee en haute saison.",
}
INFO["Premier diner chez Chez Pastis"] = {
    "title": "Chez Pastis",
    "image": "chez-pastis.jpg",
    "intro": "Une petite adresse tres appreciee de Santa Maria, cachee dans une ruelle du centre : une cour sous un arbre, eclairee a la bougie, deco soignee avec des oeuvres d artistes locaux. Cuisine capverdienne et produits de la mer, avec des ingredients frais et locaux.",
    "horaires": ["Lundi au samedi : 18h30 - 23h00, ferme le dimanche", "Deux services : 18h30 et 20h45", "Samedi 14 : on vise le service de 18h30 pour se coucher tot"],
    "tarifs": ["Prix moderes a hauts selon les sources, bon rapport qualite-prix d apres les avis"],
    "voir": ["Steak de thon grille", "Filet de boeuf", "Poisson et fruits de mer du jour", "Desserts maison"],
    "conseil": "Table reservee dans la cour, sous l arbre : le meilleur coin. Prevoir les especes en escudos ou en euros, la carte n est pas acceptee.",
    "logistique": [{"titre": "Reservation", "lignes": ["Au nom de Morieux - 4 personnes", "Samedi 14 novembre 2026 a 18h30", "Reserve le 29/10 par WhatsApp", "Table dans la cour", "Paiement sur place en especes uniquement"]},
                   {"titre": "Adresse et contact", "lignes": ["Rua Amilcar Cabral 5, Santa Maria", "4,4/5 sur Google (365 avis)", "Tel et WhatsApp : +238 984 36 96"]}],
}
INFO["Apero caipirinha au Ola Brasil"] = {
    "title": "Beach Bar Ola Brasil",
    "image": "ola-brasil.jpg",
    "intro": "Bar de plage a l ambiance bresilienne, sur le sable de Santa Maria, face a l ocean. Calme la journee, plus anime au coucher du soleil. Repute pour ses caipirinhas.",
    "horaires": ["Tous les jours de 11h00 a 21h30, ferme le mercredi"],
    "tarifs": ["Happy hour sur les boissons"],
    "conseil": "4,8/5 sur 316 avis Google. Parfait pour l apero avant le diner : il ferme a 21h30.",
}
INFO["Diner gastronomique au Marea"] = {
    "title": "Marea - la meilleure table de Santa Maria",
    "image": "marea.jpg",
    "intro": "Le restaurant le mieux note de l ile : produits de la mer et cuisine italienne revisitee avec des techniques de cuisine moleculaire. Petite salle et veranda abritee, a l ecart du boulevard, ambiance intime.",
    "horaires": ["Lundi au samedi : 19h00 - 21h00", "Ferme le dimanche"],
    "voir": ["Tagliatelles au thon", "Vitello tonnato revisite", "Poisson du jour"],
    "conseil": "RESERVE pour 4 a 19h00. ESPECES UNIQUEMENT, euros ou escudos, aucune carte acceptee : retirer avant le mardi soir. 4,8/5 sur Tripadvisor (1 127 avis) et Google (299 avis). Ensuite, dernier verre en musique au Buddy Bar.",
    "logistique": [{"titre": "Reservation", "lignes": ["Au nom de Morieux - 4 personnes", "Mardi 17 novembre 2026 a 19h00", "Reserve le 29/10 par WhatsApp, confirme par Franca"]}, {"titre": "Paiement", "lignes": ["ESPECES UNIQUEMENT : euros ou escudos", "Pas de carte bancaire"]}, {"titre": "Contact", "lignes": ["Tel et WhatsApp : +238 982 21 65"]}],
}
INFO["Dernier verre au Buddy Bar"] = INFO["Verre et concert au Buddy Bar"]
INFO["Check-in " + AIRBNB] = INFO[AIRBNB]

# ------------------------------------------------------------------ CITY_INFO
CITY = {
    "sal": {
        "image": "ile-de-sal.jpg",
        "intro": "Sal est l ile la plus touristique du Cap-Vert : une ile plate et desertique de l Atlantique, a 600 km des cotes du Senegal, bordee de plages de sable blanc. Santa Maria, au sud, concentre la vie, les restaurants et la plage. En novembre, il fait autour de 28 C la journee et 22 C la nuit, la mer est a 26 C et il ne pleut presque jamais. Le vent des alizes souffle fort, ce qui fait le bonheur des kitesurfeurs.",
        "highlights": [
            "Samedi 14 - arrivee, dejeuner les pieds dans le sable et transats a Angulo, diner Chez Pastis.",
            "Dimanche 15 - grasse matinee, piscine sur le toit, brunch et piscine au Bikini Beach Club, apero au Ola Brasil, karaoke a l Atlantic.",
            "Lundi 16 - plongee pour Samuel et Cedric, journee transat a Angulo pour Francoise et Virginie, diner a l Ocean Cafe et coucher tot.",
            "Mardi 17 - tour du nord avec chauffeur : l Oeil Bleu de Buracona, poisson a Palmeira, requins citrons a Shark Bay, lac sale de Pedra de Lume, diner au Marea.",
            "Mercredi 18 - catamaran le matin avec Cape Verde Sailing, langouste au LobStar, sieste, coucher de soleil au Bar Marley, diner italien chez Il Gobbo.",
            "Jeudi 19 - farniente a Angulo, coucher de soleil a Ponta Preta, homard grille au Barracuda.",
            "Vendredi 20 - piscine sur le toit, poisson au Sol Doce, plage du ponton, puis diner et White Party au Bikini Beach.",
            "Samedi 21 - taxi a 08h00, vol de 11h40, Orly a 19h30.",
        ],
        "conseil": "No stress, c est la devise de l ile. Les services prennent leur temps, mieux vaut s y faire des le premier jour. Soleil tres fort (indice UV 9) meme quand le vent rafraichit : creme et chapeau en permanence.",
    },
}

# ------------------------------------------------------------------ Tables de puces
PLANE = ["Vol Transavia TO3232 Orly vers Sal", "Atterrissage a Sal - Aeroport Amilcar Cabral",
         "Vol Transavia TO3233 Sal vers Orly", "Arrivee a Orly (heure de Paris)"]
CAR = ["Depart de Marck vers Orly", "Parking Orly - depot voiture",
       "Prise de la voiture de location - Aeroport SID", "Route vers Santa Maria",
       "Route vers le Bikini Beach Club", "Check-out et route vers l aeroport",
       "Restitution de la voiture - Aeroport SID", "Route retour vers Marck",
       "Plein de carburant et bagages", "Route vers Pedra de Lume", "Route vers Buracona", "Retour a Santa Maria"]
WALK = ["Arrivee aeroport Orly T3 - Depot bagages", "Securite et controle des passeports",
        "Premiere balade - plage et ponton de Santa Maria"]
COPYDEST = {
    "Transats a Angulo Beach Bar": "Angulo, Praia Antonio de Sousa, Santa Maria, Ilha do Sal, Cabo Verde",
    "Route vers Shark Bay": "Shark Bay, Baia da Parda, Ilha do Sal, Cabo Verde",
    "Route vers Pedra de Lume": "Salinas de Pedra de Lume, Ilha do Sal, Cabo Verde",
    "Route vers Buracona": "Buracona, Olho Azul, Ilha do Sal, Cabo Verde",
    "Taxi de l aeroport vers le logement": "Rua 15 Agosto 108, Santa Maria, Sal 4111, Cabo Verde",
    "Check-in " + AIRBNB: "Rua 15 Agosto 108, Santa Maria, Sal 4111, Cabo Verde",
    "Route vers le Bikini Beach Club": "Bikini Beach, ZDTI, Praia de Algodoeiro, Santa Maria, Ilha do Sal, Cabo Verde",
    "Check-out et route vers l aeroport": "Aeroporto Internacional Amilcar Cabral, Espargos, Ilha do Sal, Cabo Verde",
    "Depart de Marck vers Orly": "Aeroport Paris-Orly, Terminal 3, 94390 Orly",
}

def q(s):
    import urllib.parse
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote_plus(s)

MAPS_URLS = {
    "Premier diner chez Chez Pastis": q("Chez Pastis Rua Amilcar Cabral 5 Santa Maria Sal Cabo Verde"),
    "Petit-dejeuner tranquille au Cape Fruit": q("Cape Fruit Santa Maria Sal Cabo Verde"),
    "Transats a Angulo Beach Bar": q("Angulo Cabo Verde Santa Maria Sal"),
    "Dejeuner au Palm Beach Restaurant": "https://maps.app.goo.gl/DgUBRztCTFQS8qGo8",
    "Apres-midi transats a Angulo": q("Angulo Cabo Verde Santa Maria Sal"),
    "Coucher de soleil a Ponta Preta": q("Restaurant Ponta Preta Ilha do Sal Cabo Verde"),
    "Retour de Ponta Preta": "https://maps.app.goo.gl/Dx5Vf6wRjakuiq9a6",
    "Diner de fete au Soul Kitchen": q("Soul Kitchen La Villa Santa Maria Sal Cabo Verde"),
    "Kizomba au Pub Calema": q("Pub Calema Rua 1 de Junho Santa Maria Sal"),
    "Fin de soiree au Disco Pirata": q("Disco Pirata Santa Maria Sal Cabo Verde"),
    "White Party au Bikini Beach Club": q("Bikini Beach Club Sal Cabo Verde"),
    "Taxi vers le Bikini Beach Club": q("Bikini Beach Club Sal Cabo Verde"),
    "Taxi retour au logement": "https://maps.app.goo.gl/Dx5Vf6wRjakuiq9a6",
    "Diner homard grille au Barracuda": q("Restaurante Barracuda Santa Maria Sal Cabo Verde"),
    "Dernier verre en musique": q("Ocean Cafe Santa Maria Sal Cabo Verde"),
    "Route vers Pedra de Lume pour dejeuner": q("Area Docas Pedra de Lume Sal Cabo Verde"),
    "Dejeuner a Area Docas - Pedra de Lume": q("Area Docas Pedra de Lume Sal Cabo Verde"),
    "Croisiere en catamaran - Cape Verde Sailing": "https://maps.app.goo.gl/DgUBRztCTFQS8qGo8",
    "Rendez-vous au Palm Beach Restaurant": "https://maps.app.goo.gl/DgUBRztCTFQS8qGo8",
    "Dejeuner au LobStar, au pied du ponton": q("LobStar Santa Maria Sal Cabo Verde"),
    "Diner chez Il Gobbo": q("Il Gobbo Santa Maria Sal Cabo Verde"),
    "Petit-dejeuner chez Cam s avant la croisiere": q("Cam's Restaurante e Cafetaria Santa Maria Sal"),
    "Dernier petit-dejeuner chez Cam s": q("Cam's Restaurante e Cafetaria Santa Maria Sal"),
    "Route vers Shark Bay": q("Shark Bay Sal Cabo Verde"),
    "Shark Bay - les requins citrons": q("Shark Bay Sal Cabo Verde"),
    "Diner en musique a l Ocean Cafe": q("Ocean Cafe Santa Maria Sal Cabo Verde"),
    "Verre et concert au Buddy Bar": q("Buddy Bar Santa Maria Sal Cabo Verde"),
    "Diner et karaoke a l Atlantic Piano Bar & Grill": q("The Atlantic Piano Bar Santa Maria Sal Cabo Verde"),
    "Apero caipirinha au Ola Brasil": q("Beach Bar Ola Brasil Santa Maria Sal Cabo Verde"),
    "Diner gastronomique au Marea": q("Marea restaurant Santa Maria Sal Cabo Verde"),
    "Dernier verre au Buddy Bar": q("Buddy Bar Santa Maria Sal Cabo Verde"),
    "Route vers Pedra de Lume": q("Salinas de Pedra de Lume Sal Cabo Verde"),
    "Lac sale de Pedra de Lume": q("Salinas de Pedra de Lume Sal Cabo Verde"),
    "Route vers Buracona": q("Buracona Olho Azul Sal Cabo Verde"),
    "Buracona et l Oeil Bleu": q("Buracona Olho Azul Sal Cabo Verde"),
    "Dejeuner de poisson a Palmeira": q("Gata Fish & Yacht Club Palmeira Sal Cabo Verde"),
    "Balade a Espargos": q("Espargos Sal Cabo Verde"),
    "Petit-dejeuner au Cape Fruit": q("Cape Fruit Santa Maria Sal Cabo Verde"),
    "Petit-dejeuner au Papaya Cafe": q("Papaya Cafe Cabo Verde Santa Maria Sal"),
    "Piscine sur le toit de l immeuble": "https://maps.app.goo.gl/Dx5Vf6wRjakuiq9a6",
    "Retour a Santa Maria": "https://maps.app.goo.gl/Dx5Vf6wRjakuiq9a6",
    "Depart de Marck vers Orly": q("Aeroport Paris-Orly Terminal 3"),
    "Arrivee aeroport Orly T3 - Depot bagages": q("Aeroport Paris-Orly Terminal 3"),
    "Atterrissage a Sal - Aeroport Amilcar Cabral": q("Aeroporto Internacional Amilcar Cabral Sal"),
    "Taxi de l aeroport vers le logement": "https://maps.app.goo.gl/Dx5Vf6wRjakuiq9a6",
    "Depot des bagages au logement": "https://maps.app.goo.gl/Dx5Vf6wRjakuiq9a6",
    "Taxi vers Ponta Preta": q("Restaurant Ponta Preta Ilha do Sal Cabo Verde"),
    "Taxi retour du Bikini Beach": "https://maps.app.goo.gl/Dx5Vf6wRjakuiq9a6",
    "Check-in " + AIRBNB: "https://maps.app.goo.gl/Dx5Vf6wRjakuiq9a6",
    "Premiere balade - plage et ponton de Santa Maria": q("Pontao de Santa Maria Sal Cabo Verde"),
    "Route vers le Bikini Beach Club": q("Bikini Beach Club Sal Cabo Verde"),
    "Brunch au Bikini Beach Club": q("Bikini Beach Club Sal Cabo Verde"),
    "Apres-midi piscine et plage": q("Bikini Beach Club Sal Cabo Verde"),
    "RDV Cabo Verde Diving - Porto Antigo 1": q("Porto Antigo 1 Santa Maria Sal Cabo Verde"),
    "Briefing et entrainement plongee": q("Cabo Verde Diving Aquarium Santa Maria Sal"),
    "Plongee en mer": q("Cabo Verde Diving Aquarium Santa Maria Sal"),
    "Check-out et route vers l aeroport": q("Aeroporto Internacional Amilcar Cabral Sal"),
    "Arrivee aeroport de Sal - Enregistrement": q("Aeroporto Internacional Amilcar Cabral Sal"),
    "Coucher de soleil": q("Praia de Santa Maria Sal Cabo Verde"),
    "Dejeuner pieds dans le sable et transats a Angulo": q("Angulo Cabo Verde Santa Maria Sal"),
    "Petit-dejeuner chez Cam s": q("Cam's Restaurante e Cafetaria Santa Maria Sal"),
    "Angulo Beach Bar - journee transat": q("Angulo Cabo Verde Santa Maria Sal"),
    "Pause dejeuner": q("restaurants Santa Maria Sal Cabo Verde"),
    "Reveil et derniers rangements": "https://maps.app.goo.gl/Dx5Vf6wRjakuiq9a6",
}
MAPS_ALWAYS = ["Rendez-vous au Palm Beach Restaurant", "Route vers Pedra de Lume pour dejeuner", "Route vers Shark Bay", "Route vers Pedra de Lume", "Route vers Buracona", "Retour a Santa Maria", "Depart de Marck vers Orly", "Arrivee aeroport Orly T3 - Depot bagages",
               "Atterrissage a Sal - Aeroport Amilcar Cabral", "Taxi de l aeroport vers le logement",
               "Route vers le Bikini Beach Club",
               "Check-out et route vers l aeroport",
               "Arrivee aeroport de Sal - Enregistrement"]

def ics(uid, title, start, end, desc, alarm):
    return {"id": uid, "title": title, "ics": "\n".join([
        "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Carnet Voyage Cap-Vert 2026//FR",
        "CALSCALE:GREGORIAN", "METHOD:PUBLISH", "BEGIN:VEVENT",
        "DTSTART:" + start, "DTEND:" + end, "SUMMARY:" + title,
        "DESCRIPTION:" + desc, "STATUS:CONFIRMED",
        "BEGIN:VALARM", "TRIGGER:-" + alarm, "ACTION:DISPLAY",
        "DESCRIPTION:Rappel - " + title, "END:VALARM",
        "END:VEVENT", "END:VCALENDAR"])}

CAL_EVENTS = [
    ics("depart_maison", "Depart de Marck vers Orly", "20261114T000500", "20261114T033000",
        "Etre a Orly T3 a 04h00. Depot bagages ferme a 05h15. Passeports + recus EASE.", "PT30M"),
    ics("vol_aller", "Vol Transavia TO3232 Orly - Sal", "20261114T063000", "20261114T084500",
        "Ref K6UNPB. Orly T3. Depot bagages ferme 05h15. Arrivee Sal 10h45 heure locale.", "PT3H"),
    ics("bikini", "Brunch Bikini Beach Club", "20261115T130000", "20261115T143000",
        "Reserve Resos au nom de Morieux - 4 pers - zone Restaurant. CB ou Apple Pay uniquement.", "PT45M"),
    ics("plongee", "Plongee Cabo Verde Diving - RDV Porto Antigo 1", "20261116T083000", "20261116T163000",
        "Samuel et Cedric. Paye 226,72 EUR. Briefing 09h00-11h30, mer 14h00-16h30. +238 595 37 96.", "PT1H"),
    ics("tour_nord", "Tour du nord : Buracona, Palmeira, Shark Bay, Pedra de Lume", "20261117T100000", "20261117T173000",
        "Depart 10h00. Chaussures d eau, maillot, serviette, especes (~50 EUR entrees). Oeil Bleu 10h45, dejeuner Palmeira 12h30, Shark Bay 14h40, Pedra de Lume 16h00.", "PT30M"),
    ics("checkin_retour", "Enregistrement en ligne Transavia TO3233", "20261120T090000", "20261120T091500",
        "Ouvert depuis 05h40. PNR K6UNPB. Telecharger les 4 cartes d embarquement.", "PT15M"),
    ics("depart_retour", "Depart vers l aeroport de Sal", "20261121T080000", "20261121T084500",
        "Check-out. Taxi reserve a 08h00. Aeroport vers 08h30. Bagages fermes a 10h25.", "PT30M"),
    ics("vol_retour", "Vol Transavia TO3233 Sal - Orly", "20261121T114000", "20261121T123000",
        "Ref K6UNPB. Depot bagages ferme 10h25. Arrivee Orly 19h30 heure de Paris.", "PT3H"),
]
CAL_MAP = {
    "Chauffeur de la journee - depart": "tour_nord",
    "Depart de Marck vers Orly": "depart_maison",
    "Vol Transavia TO3232 Orly vers Sal": "vol_aller",
    "Brunch au Bikini Beach Club": "bikini",
    "RDV Cabo Verde Diving - Porto Antigo 1": "plongee",
    "Enregistrement en ligne vol retour": "checkin_retour",
    "Check-out et route vers l aeroport": "depart_retour",
    "Vol Transavia TO3233 Sal vers Orly": "vol_retour",
}

# ------------------------------------------------------------------ Checklist reservations
CHK_ITEMS = [
    {"id": "vols", "name": "Vols Transavia TO3232 / TO3233", "date": "14 et 21 nov", "deadline": "PAYE", "color": "#2E6B3E"},
    {"id": "airbnb", "name": AIRBNB, "date": "14 au 21 nov", "deadline": "PAYE - 1 800 EUR", "color": "#2E6B3E"},
    {"id": "bikini", "name": "Brunch Bikini Beach Club", "date": "15 nov", "deadline": "RESERVE - paiement sur place", "color": "#2E6B3E"},
    {"id": "atlantic", "name": "Diner Atlantic Piano Bar (dimanche)", "date": "15 nov", "deadline": "RESERVE (TableHelm) - 19h45 - Morieux - paiement sur place", "color": "#2E6B3E"},
    {"id": "plongee", "name": "Plongee Cabo Verde Diving", "date": "16 nov", "deadline": "PAYE", "color": "#2E6B3E"},
    {"id": "pastis", "name": "Diner Chez Pastis (premier soir)", "date": "14 nov", "deadline": "RESERVE (WhatsApp) - 18h30 - Morieux - table dans la cour - especes", "color": "#2E6B3E"},
    {"id": "whiteparty", "name": "White Party Bikini Beach (vendredi)", "date": "20 nov", "deadline": "RESERVE - 22h00-01h30 - Morieux - tenue blanche", "color": "#2E6B3E"},
    {"id": "croisiere", "name": "Catamaran Cape Verde Sailing (mercredi matin)", "date": "18 nov", "deadline": "RESERVE (Viator) - ref 1460555133 - RDV 08h20 au Palm Beach Restaurant", "color": "#2E6B3E"},
    {"id": "oceancafe", "name": "Diner Ocean Cafe (lundi soir)", "date": "16 nov", "deadline": "RESERVE (WhatsApp) - 19h30 - Morieux - 4 pers", "color": "#2E6B3E"},
    {"id": "ilgobbo", "name": "Diner Il Gobbo (mercredi)", "date": "18 nov", "deadline": "RESERVE (WhatsApp) - 19h30 - Morieux - 4 pers", "color": "#2E6B3E"},
    {"id": "marea", "name": "Diner Marea (mardi)", "date": "17 nov", "deadline": "RESERVE (WhatsApp) - 19h00 - Morieux - 4 pers - ESPECES UNIQUEMENT (euros ou escudos)", "color": "#2E6B3E"},
    {"id": "barracuda", "name": "Diner Barracuda (jeudi)", "date": "19 nov", "deadline": "RESERVE (WhatsApp) - 19h00 - Morieux - 4 pers - bord de mer - especes", "color": "#2E6B3E"},
    {"id": "gata", "name": "Dejeuner Gata Fish, Palmeira (mardi)", "date": "17 nov", "deadline": "RESERVE (WhatsApp) - 12h30 - Morieux - 4 pers", "color": "#2E6B3E"},
    {"id": "parking", "name": "Parking Orly", "date": "14 au 21 nov", "deadline": "A reserver", "color": "#C8573F"},
]
# ------------------------------------------------------------------ A faire avant le depart (todo datee)
TODO_ITEMS = [
    {"id": "ease", "ico": "🛂", "due": "2026-11-09", "rt": "09:00", "evd": "2026-11-14", "color": "#C8573F",
     "name": "Preenregistrement EASE (x4)", "sub": "Sur ease.gov.cv, pour l arrivee du sam 14/11 (5 jours avant au plus tard)"},
    {"id": "morabeza", "ico": "🏖️", "due": "2026-11-10", "rt": "09:00", "evd": "2026-11-19", "color": "#C8573F",
     "name": "Vérifier la réouverture du Morabeza", "sub": "Sur Google Maps. Si oui : jeu 19/11 apres-midi a la place d Angulo"},
    {"id": "checkin", "ico": "✈️", "due": "2026-11-13", "rt": "09:00", "evd": "2026-11-14", "color": "#5B3A7E",
     "name": "Enregistrement en ligne aller", "sub": "Vol TO3232 du sam 14/11 a 06h30 - ouvre le 13/11 a 00h30 - ref K6UNPB"},
    {"id": "ady_aller", "group": "ady", "due": "2026-11-14", "rt": "11:15", "evd": "2026-11-14", "color": "#C8573F",
     "name": "Appeler un taxi a l aeroport", "sub": "Samedi 14 novembre vers 11h15, a la sortie des bagages : aeroport vers le logement, 4 personnes et 4 valises", "go": [1, "Appeler un taxi a l aeroport"]},
    {"id": "call_bikini", "group": "ady", "due": "2026-11-15", "rt": "12:05", "evd": "2026-11-15", "color": "#C8573F",
     "name": "Appeler un taxi pour le Bikini", "sub": "Dimanche 15 novembre, depart 12h35 du logement vers le Bikini Beach Club", "go": [2, "Appeler un taxi pour le Bikini"]},
    {"id": "call_bikini_ret", "group": "ady", "due": "2026-11-15", "rt": "17:00", "evd": "2026-11-15", "color": "#C8573F",
     "name": "Appeler un taxi pour rentrer du Bikini", "sub": "Dimanche 15 novembre, depart 17h30 du Bikini Beach Club vers le logement", "go": [2, "Appeler un taxi pour rentrer du Bikini"]},
    {"id": "ady_nord", "group": "ady", "due": "2026-11-16", "rt": "12:00", "evd": "2026-11-17", "color": "#C8573F",
     "name": "Reserver le chauffeur du tour du nord", "sub": "Lundi 16 novembre a la pause dejeuner, pour le mardi 10h00-17h30 en 4x4 : Buracona, Palmeira, Shark Bay, Pedra de Lume", "go": [3, "Reserver le chauffeur du tour du nord"]},
    {"id": "call_ponta", "group": "ady", "due": "2026-11-19", "rt": "16:45", "evd": "2026-11-19", "color": "#C8573F",
     "name": "Appeler un taxi pour Ponta Preta", "sub": "Jeudi 19 novembre, depart 17h15 d Angulo vers Ponta Preta, retour vers 18h20", "go": [6, "Appeler un taxi pour Ponta Preta"]},
    {"id": "ady_ven", "group": "ady", "due": "2026-11-19", "rt": "18:45", "evd": "2026-11-20", "color": "#C8573F",
     "name": "Reserver le taxi de la White Party", "sub": "Jeudi 19 novembre au soir, pour le vendredi : 21h40 Soul Kitchen vers White Party, retour a 01h30", "go": [6, "Reserver le taxi de la White Party"]},
    {"id": "ady_retour", "group": "ady", "due": "2026-11-20", "rt": "18:15", "evd": "2026-11-21", "color": "#C8573F",
     "name": "Reserver le taxi de l aeroport", "sub": "Vendredi 20 novembre au soir, pour le samedi 08h00 : logement vers aeroport, 4 personnes et 4 valises", "go": [7, "Reserver le taxi de l aeroport"]}
]
TODO_GROUPS = {"ady": {"ico": "🚕", "name": "Taxis", "sub": "Ady, Taxi Sal Island ou un autre - especes - prix a fixer avant", "pick": 1,
                       "foot": "Chaque case est la meme que la pastille A FAIRE de la carte verte du jour, ou le message WhatsApp est pret. Sinon : taxis officiels, prix fixe avant de monter."}}

RESA_DETAILS = {
    "vols": {"num": "K6UNPB", "site": "Transavia (ref client 40-1068303696)",
             "info": "PAYE 2 426,00 EUR pour 4 - TO3232 sam 14/11 Orly T3 06h30 > Sal 10h45 - TO3233 sam 21/11 Sal 11h40 > Orly 19h30 - eco"},
    "airbnb": {"num": "HMYTYQTCD3", "site": "Airbnb",
               "info": "PAYE 1 800,00 EUR - hote +351 961 976 139 (tel et WhatsApp) - Sal Sol & Mar - Rua 15 Agosto 108, Santa Maria - arrivee 14/11 15h00, depart 21/11 11h00 - annulation gratuite avant 31/10 15h00, partielle avant 7/11 15h00"},
    "bikini": {"num": "Resos - au nom de Morieux", "site": "Bikini Beach Club",
               "info": "RESERVE - dim 15/11 13h00-14h30 - 4 pers - zone Restaurant - paiement sur place CB ou Apple Pay - acces piscine a confirmer"},
    "plongee": {"num": "Cabo Verde Diving", "site": "caboverdediving.net",
                "info": "PAYE 226,72 EUR pour 2 (Samuel, Cedric) - lun 16/11 RDV 08h30 Porto Antigo 1 - 09h00-11h30 briefing, 14h00-16h30 mer - +238 595 37 96"},
}
LOCKED = ["vols", "airbnb", "pastis", "bikini", "plongee", "atlantic", "marea", "croisiere", "ilgobbo", "barracuda", "whiteparty", "gata", "oceancafe"]

HEBERGEMENTS = [
    {"dates": "14-21 NOV", "name": AIRBNB, "stars": "Airbnb - 7 nuits",
     "addr": ADR_AIRBNB, "ref": "Airbnb HMYTYQTCD3",
     "maps": "https://maps.app.goo.gl/Dx5Vf6wRjakuiq9a6"},
]


# ------------------------------------------------------------------ Moyen de deplacement de chaque etape
# (mode, precision) : le texte est ajoute en tete de la description de l etape.
DEPLACEMENT = {
    "Depart de Marck vers Orly": ("voiture", "En voiture (voiture de Cedric), environ 3h15"),
    "Parking Orly - depot voiture": ("voiture", "En voiture jusqu au parking, puis a pied ou navette du parking vers le Terminal 3"),
    "Arrivee aeroport Orly T3 - Depot bagages": ("pied", "A pied ou en navette depuis le parking"),
    "Securite et controle des passeports": ("pied", "A pied dans l aerogare"),
    "Embarquement": ("pied", "A pied jusqu a la porte"),
    "Vol Transavia TO3232 Orly vers Sal": ("avion", "En avion"),
    "Atterrissage a Sal - Aeroport Amilcar Cabral": ("avion", "En avion"),
    "Dejeuner pieds dans le sable et transats a Angulo": ("pied", "A pied depuis le logement, environ 400 m"),
    "Depot des bagages au logement": ("aucun", "Au logement, Rua 15 Agosto 108"),
    "Check-in " + AIRBNB: ("pied", "A pied depuis Angulo, environ 400 m : les valises sont deja au logement"),
    "Premiere balade - plage et ponton de Santa Maria": ("pied", "A pied depuis le logement"),
    "Coucher de soleil": ("pied", "A pied, sur la plage de Santa Maria"),
    "Route vers le Bikini Beach Club": ("voiture", "En taxi, environ 10 min, 350 CVE"),
    "Brunch au Bikini Beach Club": ("pied", "Sur place, depose par le taxi"),
    "Apres-midi piscine et plage": ("pied", "Sur place au club"),
    "Petit-dejeuner chez Cam s": ("pied", "A pied, dans la rue du logement"),
    "RDV Cabo Verde Diving - Porto Antigo 1": ("pied", "A pied depuis le logement, tout est dans le centre de Santa Maria (verifier la distance sur Maps)"),
    "Briefing et entrainement plongee": ("pied", "Sur place au centre de plongee"),
    "Angulo Beach Bar - journee transat": ("pied", "A pied par la plage ou le front de mer, 10 a 15 min vers l est du centre"),
    "Pause dejeuner": ("pied", "A pied, pres du centre de plongee"),
    "Plongee en mer": ("pied", "Depart avec le centre de plongee, qui organise la sortie en mer"),
    "Croisiere en catamaran - Cape Verde Sailing": ("voiture", "Transfert par le chauffeur de Cape Verde Sailing jusqu au point de depart du jour"),
    "Rendez-vous au Palm Beach Restaurant": ("pied", "A pied depuis Cam s, le Palm Beach est dans le centre de Santa Maria, en bord de mer"),
    "Dejeuner au LobStar, au pied du ponton": ("pied", "A pied depuis le Palm Beach Restaurant, ou le catamaran nous redepose"),
    "Sieste et plage": ("pied", "A pied, logement et plage du ponton"),
    "Diner chez Il Gobbo": ("pied", "A pied, dans la rue du logement"),
    "Petit-dejeuner tranquille au Cape Fruit": ("pied", "A pied, dans la rue du logement"),
    "Transats a Angulo Beach Bar": ("pied", "A pied depuis le logement, environ 10 minutes"),
    "Dejeuner au Palm Beach Restaurant": ("pied", "A pied depuis Angulo, environ 10 minutes vers l ouest jusqu au ponton"),
    "Apres-midi transats a Angulo": ("pied", "A pied depuis le Palm Beach, environ 10 minutes vers l est le long de la plage"),
    "Coucher de soleil a Ponta Preta": ("pied", "Depose par le taxi devant le restaurant"),
    "Retour de Ponta Preta": ("voiture", "En taxi, 10 a 15 minutes, avec le chauffeur de l aller"),
    "Diner de fete au Soul Kitchen": ("pied", "A pied par le front de mer, quelques minutes depuis le logement"),
    "Kizomba au Pub Calema": ("pied", "A pied depuis le front de mer, 5 a 10 minutes"),
    "Fin de soiree au Disco Pirata": ("pied", "A pied dans le centre, quelques minutes depuis le Calema"),
    "Taxi vers le Bikini Beach Club": ("voiture", "En taxi, environ 10 minutes"),
    "White Party au Bikini Beach Club": ("pied", "Sur place au club"),
    "Taxi retour au logement": ("voiture", "En taxi, environ 10 minutes jusqu au logement"),
    "Diner homard grille au Barracuda": ("pied", "A pied depuis le logement, sur la plage pres du ponton"),
    "Dernier verre en musique": ("pied", "A pied dans le centre"),
    "Route vers Pedra de Lume pour dejeuner": ("voiture", "Avec le chauffeur de l apres-midi, 25 a 30 min"),
    "Dejeuner a Area Docas - Pedra de Lume": ("aucun", "Le chauffeur attend ou revient a l heure convenue"),
    "Petit-dejeuner chez Cam s avant la croisiere": ("pied", "A pied, dans la rue du logement"),
    "Dernier petit-dejeuner chez Cam s": ("pied", "A pied, dans la rue du logement"),
    "Taxi de l aeroport vers le logement": ("voiture", "En taxi, 18 km, environ 20 min"),
    "Taxi retour du Bikini Beach": ("voiture", "En taxi, environ 10 min, 350 CVE"),
    "Chauffeur de la journee - depart": ("voiture", "Le chauffeur passe nous prendre au logement"),
    "Taxi vers Ponta Preta": ("voiture", "En taxi depuis Angulo, 10 a 15 minutes"),
    "Valises bouclees avant la soiree": ("aucun", "Au logement"),
    "Route vers Shark Bay": ("voiture", "Avec le chauffeur, depuis Palmeira, environ 35 min dont une fin en piste de sable"),
    "Shark Bay - les requins citrons": ("pied", "Le chauffeur attend pres de l epave, puis a pied dans l eau"),
    "Premier diner chez Chez Pastis": ("pied", "A pied depuis le logement, dans le centre de Santa Maria"),
    "Diner en musique a l Ocean Cafe": ("pied", "A pied depuis le logement, place centrale de Santa Maria"),
    "Verre et concert au Buddy Bar": ("pied", "A pied, sur l axe principal du centre, a quelques minutes de l Ocean Cafe"),
    "Diner et karaoke a l Atlantic Piano Bar & Grill": ("pied", "A pied dans Santa Maria (adresse exacte sur Maps)"),
    "Petit-dejeuner au Papaya Cafe": ("pied", "A pied, environ 5 minutes depuis le logement"),
    "Piscine sur le toit de l immeuble": ("pied", "Retour a pied au logement, environ 5 minutes"),
    "Apero caipirinha au Ola Brasil": ("pied", "A pied sur la plage de Santa Maria"),
    "Diner gastronomique au Marea": ("pied", "A pied dans Santa Maria, a l ecart du boulevard (adresse exacte sur Maps)"),
    "Dernier verre au Buddy Bar": ("pied", "A pied, sur l axe principal du centre"),
    "Petit-dejeuner au Cape Fruit": ("pied", "A pied, dans la rue du logement, le chauffeur passe nous prendre a 10h00"),
    "Route vers Pedra de Lume": ("voiture", "Avec le chauffeur, depuis Shark Bay, environ 10 min"),
    "Lac sale de Pedra de Lume": ("pied", "Le chauffeur attend au parking du site, puis a pied par le tunnel"),
    "Route vers Buracona": ("voiture", "Avec le chauffeur en 4x4, depuis Espargos, environ 25 min dont une fin en piste"),
    "Buracona et l Oeil Bleu": ("pied", "Le chauffeur attend au parking du site, puis a pied sur les passerelles et la lave"),
    "Dejeuner de poisson a Palmeira": ("voiture", "Avec le chauffeur, depuis Buracona, environ 6 km et 10 a 15 min, puis a pied sur le port"),
    "Balade a Espargos": ("voiture", "Avec le chauffeur, depuis Santa Maria, environ 25 min, puis a pied dans le centre"),
    "Retour a Santa Maria": ("voiture", "Avec le chauffeur, 25 a 30 min"),
    "Enregistrement en ligne vol retour": ("aucun", "Sur le telephone, depuis le logement"),
    "Reveil et derniers rangements": ("aucun", "Au logement"),
    "Check-out et route vers l aeroport": ("voiture", "En taxi reserve la veille, 20 a 25 min"),
    "Arrivee aeroport de Sal - Enregistrement": ("pied", "Depose par le taxi devant l aerogare"),
    "Vol Transavia TO3233 Sal vers Orly": ("avion", "En avion"),
    "Arrivee a Orly (heure de Paris)": ("pied", "A pied ou en navette jusqu au parking"),
    "Route retour vers Marck": ("voiture", "En voiture de Cedric, environ 3h"),
}
# ---- maj rythme : deplacements des nouvelles etapes
DEPLACEMENT["Dejeuner de poisson au Sol Doce"] = ("pied", "A pied depuis le logement, environ 5 minutes, pres du ponton")
DEPLACEMENT["Apres-midi plage, transats et baignade"] = ("pied", "A pied, plage du ponton ou 10 minutes vers l est jusqu a Angulo")
DEPLACEMENT["Sieste avant la derniere soiree"] = ("aucun", "Au logement")
DEPLACEMENT["Grasse matinee et cafe au logement"] = ("aucun", "Au logement")
DEPLACEMENT["Piscine sur le toit de l immeuble"] = ("pied", "Au logement, sur le toit")
DEPLACEMENT["Petit-dejeuner a Orly"] = ("pied", "A pied dans l aerogare, apres les controles")
DEPLACEMENT["Petit-dejeuner et sandwich pour le vol"] = ("pied", "A pied dans l aerogare, apres la police")
DEPLACEMENT["Diner sur l aire d Assevillers"] = ("voiture", "En voiture, environ 1h15 depuis Orly par l A1")
_titres = set()
for _d in DAYS:
    for _e in _d["events"]:
        _titres.add(_e["title"])
        if _e["title"] in DEPLACEMENT:
            _mode, _txt = DEPLACEMENT[_e["title"]]
            if not _e["body"].startswith("Deplacement :"):
                _e["body"] = "Deplacement : " + _txt + ". " + _e["body"]
_manquants = sorted(_titres - set(DEPLACEMENT))
assert not _manquants, "Etapes sans moyen de deplacement : %s" % _manquants
PLANE = [t for t, (m, _) in DEPLACEMENT.items() if m == "avion"]
CAR = [t for t, (m, _) in DEPLACEMENT.items() if m == "voiture"]
WALK = [t for t, (m, _) in DEPLACEMENT.items() if m == "pied"]


# ---------------------------------------------------------------- pastilles A RESERVER / Web / theme
# titre d evenement -> id de la checklist : pastille rouge A RESERVER tant que la case n est pas cochee
# titre -> numero WhatsApp : badge turquoise TAXI A APPELER (pas de reservation)
# titre -> message WhatsApp pre-rempli ({oi} = salutation selon le taxi)
CALL_TAXI = {"Taxi de l aeroport vers le logement": {
    "fr": "{oi}\nNous venons d atterrir a l aeroport de Sal (vol TO3232).\nNous sommes 4 personnes avec 4 valises.\nNous avons besoin d un taxi pour Santa Maria, Rua 15 de Agosto 108.\nEtes-vous disponible maintenant ?\nSi oui, quel est le prix ?\nMerci !\nSamuel",
    "en": "Hello!\nWe just landed at Sal airport (flight TO3232).\nWe are 4 people with 4 suitcases.\nWe need a taxi to Santa Maria, Rua 15 de Agosto 108.\nAre you available now?\nIf so, how much is it?\nThank you!\nSamuel"}}
# petites cartes vertes "Appeler un taxi" 30 min avant chaque taxi pris sur le moment
# titre de la carte -> (titre du taxi, heure, sous-titre, message fr, message en) ; {oi} = salutation
_SIGN = "\nMerci !\nSamuel"
_SIGN_EN = "\nThank you!\nSamuel"
CALL_CARDS = {
    "Appeler un taxi a l aeroport": ("Taxi de l aeroport vers le logement", "11h15", "Des la sortie des bagages, 4 personnes et 4 valises",
        CALL_TAXI["Taxi de l aeroport vers le logement"]["fr"], CALL_TAXI["Taxi de l aeroport vers le logement"]["en"]),
    "Appeler un taxi pour le Bikini": ("Route vers le Bikini Beach Club", "12h05", "Depart 12h35 du logement, 4 personnes",
        "{oi}\nNous sommes 4 personnes au logement, Rua 15 de Agosto 108 a Santa Maria.\nNous avons besoin d un taxi a 12h35 pour le Bikini Beach Club, a cote du Melia Llana (Algodoeiro).\nEtes-vous disponible ?\nSi oui, quel est le prix ?" + _SIGN,
        "Hello!\nWe are 4 people at Rua 15 de Agosto 108, Santa Maria.\nWe need a taxi at 12:35 to Bikini Beach Club, next to Melia Llana (Algodoeiro).\nAre you available?\nIf so, how much is it?" + _SIGN_EN),
    "Appeler un taxi pour rentrer du Bikini": ("Taxi retour du Bikini Beach", "17h00", "Depart 17h30 du Bikini Beach Club, 4 personnes",
        "{oi}\nNous sommes 4 personnes au Bikini Beach Club, a cote du Melia Llana (Algodoeiro).\nNous avons besoin d un taxi a 17h30 pour rentrer a Santa Maria, Rua 15 de Agosto 108.\nEtes-vous disponible ?\nSi oui, quel est le prix ?" + _SIGN,
        "Hello!\nWe are 4 people at Bikini Beach Club, next to Melia Llana (Algodoeiro).\nWe need a taxi at 17:30 back to Santa Maria, Rua 15 de Agosto 108.\nAre you available?\nIf so, how much is it?" + _SIGN_EN),
    "Appeler un taxi pour Ponta Preta": ("Taxi vers Ponta Preta", "16h45", "Depart 17h15 d Angulo, 4 personnes, retour vers 18h20",
        "{oi}\nNous sommes 4 personnes a l Angulo Beach Bar, plage Antonio de Sousa a Santa Maria.\nNous avons besoin d un taxi a 17h15 pour le restaurant Ponta Preta.\nPuis d un retour vers 18h20 a Santa Maria, Rua 15 de Agosto 108.\nEtes-vous disponible ?\nSi oui, quel est le prix pour l aller et le retour ?" + _SIGN,
        "Hello!\nWe are 4 people at Angulo Beach Bar, Antonio de Sousa beach, Santa Maria.\nWe need a taxi at 17:15 to Ponta Preta restaurant.\nThen a ride back around 18:20 to Santa Maria, Rua 15 de Agosto 108.\nAre you available?\nIf so, how much for both rides?" + _SIGN_EN),
    # la veille au soir : reserver les taxis du lendemain (carte inseree dans le jour indique)
    "Reserver le chauffeur du tour du nord": ("@3", "12h00", "Tour du nord demain mardi 17 novembre, 10h00 a 17h30, en 4x4",
        "{oi}\nNous sommes 4 personnes logees Rua 15 de Agosto 108 a Santa Maria.\nNous aimerions reserver un chauffeur en 4x4 ou pick-up pour demain, mardi 17 novembre, de 10h00 a 17h30 environ.\nProgramme : Buracona, Palmeira, Shark Bay et Pedra de Lume.\nEtes-vous disponible ?\nSi oui, quel est le prix pour la journee ?" + _SIGN,
        "Hello!\nWe are 4 people staying at Rua 15 de Agosto 108, Santa Maria.\nWe would like to book a driver with a 4x4 or pick-up for tomorrow, Tuesday 17 November, from 10:00 to about 17:30.\nPlan: Buracona, Palmeira, Shark Bay and Pedra de Lume.\nAre you available?\nIf so, how much for the day?" + _SIGN_EN),
    "Reserver le taxi de la White Party": ("@6", "18h45", "White Party demain vendredi 20 novembre : aller 21h40, retour 01h30",
        "{oi}\nNous sommes 4 personnes a Santa Maria.\nNous aimerions reserver un taxi pour demain soir, vendredi 20 novembre.\nAller a 21h40 : du restaurant Soul Kitchen (plage de Santa Maria, La Villa Beach Lounge) vers le Bikini Beach Club.\nRetour a 01h30 : du Bikini Beach Club vers Rua 15 de Agosto 108.\nEtes-vous disponible ?\nSi oui, quel est le prix pour l aller et le retour ?" + _SIGN,
        "Hello!\nWe are 4 people in Santa Maria.\nWe would like to book a taxi for tomorrow night, Friday 20 November.\nOut at 21:40: from Soul Kitchen restaurant (Santa Maria beach, La Villa Beach Lounge) to Bikini Beach Club.\nBack at 01:30: from Bikini Beach Club to Rua 15 de Agosto 108.\nAre you available?\nIf so, how much for both rides?" + _SIGN_EN),
    "Reserver le taxi de l aeroport": ("@7", "18h15", "Demain samedi 21 novembre a 08h00, 4 personnes et 4 valises",
        "{oi}\nNous sommes 4 personnes avec 4 valises, logees Rua 15 de Agosto 108 a Santa Maria.\nNous aimerions reserver un taxi pour demain, samedi 21 novembre, a 08h00, du logement a l aeroport de Sal.\nEtes-vous disponible ?\nSi oui, quel est le prix ?" + _SIGN,
        "Hello!\nWe are 4 people with 4 suitcases, staying at Rua 15 de Agosto 108, Santa Maria.\nWe would like to book a taxi for tomorrow, Saturday 21 November, at 08:00, to Sal airport.\nAre you available?\nIf so, how much is it?" + _SIGN_EN),
}
# carte -> id de la case A FAIRE (partagee avec les taches Taxis) et prix affiche
CALL_IDS = {"Appeler un taxi a l aeroport": "ady_aller", "Appeler un taxi pour le Bikini": "call_bikini",
            "Appeler un taxi pour rentrer du Bikini": "call_bikini_ret", "Appeler un taxi pour Ponta Preta": "call_ponta",
            "Reserver le chauffeur du tour du nord": "ady_nord", "Reserver le taxi de la White Party": "ady_ven", "Reserver le taxi de l aeroport": "ady_retour"}
CALL_PX = {"Reserver le chauffeur du tour du nord": "~50 €/couple", "Reserver le taxi de la White Party": "~6 €/taxi", "Reserver le taxi de l aeroport": "~15 €/taxi"}
# trajets en taxi : depart, arrivee, duree, carte verte d appel ou de reservation liee
_LOGT = "Logement, Rua 15 de Agosto 108"
TAXI_ROUTES = {
    "Taxi de l aeroport vers le logement": ("Aeroport de Sal, sortie de l aerogare", _LOGT, "18 km, environ 20 minutes", "Appeler un taxi a l aeroport"),
    "Route vers le Bikini Beach Club": (_LOGT, "Bikini Beach Club, plage d Algodoeiro", "Environ 10 minutes, 4 km", "Appeler un taxi pour le Bikini"),
    "Taxi retour du Bikini Beach": ("Bikini Beach Club, devant l entree", _LOGT, "Environ 10 minutes", "Appeler un taxi pour rentrer du Bikini"),
    "Chauffeur de la journee - depart": (_LOGT, "Buracona, Palmeira, Shark Bay, Pedra de Lume, retour au logement", "En 4x4 ou pick-up, de 10h00 a 17h30 environ", "Reserver le chauffeur du tour du nord"),
    "Taxi vers Ponta Preta": ("Angulo Beach Bar, plage Antonio de Sousa", "Restaurant Ponta Preta", "10 a 15 minutes", "Appeler un taxi pour Ponta Preta"),
    "Retour de Ponta Preta": ("Restaurant Ponta Preta", _LOGT, "10 a 15 minutes, meme chauffeur qu a l aller", "Appeler un taxi pour Ponta Preta"),
    "Taxi vers le Bikini Beach Club": ("Soul Kitchen, plage de Santa Maria", "Bikini Beach Club, plage d Algodoeiro", "Environ 10 minutes", "Reserver le taxi de la White Party"),
    "Taxi retour au logement": ("Bikini Beach Club, devant l entree", _LOGT, "Environ 10 minutes, meme chauffeur qu a l aller", "Reserver le taxi de la White Party"),
    "Check-out et route vers l aeroport": (_LOGT, "Aeroport de Sal", "18 km, 20 a 25 minutes", "Reserver le taxi de l aeroport"),
}
def _hk(h):
    _v = int(h[:2]) * 60 + int(h[3:])
    return _v + 1440 if _v < 300 else _v
for _ct, (_tt, _h, _sub, _mfr, _men) in CALL_CARDS.items():
    if _tt.startswith("@"):
        _d = [d for d in DAYS if d["id"] == int(_tt[1:])][0]
        _i = len([e for e in _d["events"] if _hk(e["time"]) <= _hk(_h)])
        _d["events"].insert(_i, ev(_h, _ct, _sub, "transport"))
        continue
    for _d in DAYS:
        _ix = [i for i, _e in enumerate(_d["events"]) if _e["title"] == _tt]
        if _ix:
            _d["events"].insert(_ix[0], ev(_h, _ct, _sub, "transport"))
            break
    else:
        raise SystemExit("taxi introuvable : " + _tt)

# taxis proposes par le badge TAXI A APPELER : nom, detail, numero WhatsApp
TAXI_LIST = [["Ady", "Chauffeur de l hote Airbnb", "2389529719", "+238 952 97 19", "Bonjour Ady !"], ["Taxi Sal Island", "Plan B, base a Santa Maria, 5/5 sur Google", "2385995973", "+238 599 59 73", "Bonjour !"]]

RESA_TODO = {
    "Parking Orly - depot voiture": "parking",
}

# titre -> "f" (farniente, plage, transat) ou "v" (visite, excursion)
THEME = {
    "Dejeuner pieds dans le sable et transats a Angulo": "f",
    "Coucher de soleil": "f",
    "Apres-midi piscine et plage": "f",
    "Piscine sur le toit de l immeuble": "f",
    "Angulo Beach Bar - journee transat": "f",
    "Transats a Angulo Beach Bar": "f",
    "Apres-midi transats a Angulo": "f",
    "Coucher de soleil a Ponta Preta": "f",
    "Premiere balade - plage et ponton de Santa Maria": "v",
    "Balade a Espargos": "v",
    "Buracona et l Oeil Bleu": "v",
    "Lac sale de Pedra de Lume": "v",
    "Croisiere en catamaran - Cape Verde Sailing": "v",
    "Sieste et plage": "f",
    "Shark Bay - les requins citrons": "v",
}

def _web(name, sub, tel=None, wa=False, links=()):
    return {"name": name, "sub": sub, "tel": tel, "wa": wa, "links": [list(x) for x in links]}
TA = "https://www.tripadvisor.com/Restaurant_Review-g482848-"
WEB = {
    "Dejeuner pieds dans le sable et transats a Angulo": _web("Angulo Beach Bar", "Praia Antonio de Sousa - tous les jours 8h00-22h00 - carte acceptee", "+2389701171", True, [("Site web Angulo", "https://www.angulocaboverde.com/")]),
    "Premier diner chez Chez Pastis": _web("Chez Pastis", "Rua Amilcar Cabral 5 - lun-sam 18h30-23h00 - especes uniquement", "+2389843696", True, [("Site web chezpastis.com", "https://chezpastis.com")]),
    "Brunch au Bikini Beach Club": _web("Bikini Beach Club", "Plage d Algodoeiro - brunch le dimanche 12h00-20h00 - carte uniquement", None, False, [("Site web", "https://bikinibeachclub.com/"), ("Programme de la semaine", "https://bikinibeachclub.com/whats-on/")]),
    "Diner et karaoke a l Atlantic Piano Bar & Grill": _web("The Atlantic Piano Bar & Grill", "Santa Maria - karaoke le dimanche soir - reserve le 15/11 a 19h45", "+2389755153", True, [("Instagram atlanticpianobarcv", "https://www.instagram.com/atlanticpianobarcv/")]),
    "Petit-dejeuner chez Cam s": _web("Cam s Restaurante e Cafetaria", "Rua 15 de Agosto - lun-sam des 07h30, ferme le dimanche", "+2389545376", True, [("Site web Cam s", "http://camsrestauracao.com/")]),
    "RDV Cabo Verde Diving - Porto Antigo 1": _web("Cabo Verde Diving", "Porto Antigo 1 - PAYE pour Samuel et Cedric", "+2385953796", True, [("Site web", "https://www.caboverdediving.net")]),
    "Diner en musique a l Ocean Cafe": _web("Ocean Cafe", "Place centrale de Santa Maria - reserve lun 16/11 19h30 au nom de Morieux", "+2385803505", True, [("Site web Ocean Cafe", "http://www.oceancaboverde.com/")]),
    "Petit-dejeuner au Papaya Cafe": _web("Papaya Cafe Cabo Verde", "Rue pietonne principale - tous les jours 07h30-22h30 - carte acceptee", "+2389768181", True, [("Site web Papaya", "https://www.papayacaboverde.com/")]),
    "Petit-dejeuner au Cape Fruit": _web("Cape Fruit", "Rua 15 de Agosto - tous les jours 08h00-16h00 - prevoir des especes", "+2389822205", True, [("Instagram Cape Fruit", "https://www.instagram.com/capefruitsal/")]),
    "Dejeuner de poisson a Palmeira": _web("Gata Fish & Yacht Club", "Port de Palmeira - reserve mar 17/11 12h30 au nom de Morieux - carte acceptee", "+2389501328", True, [("Google Maps (pas de site web)", "https://www.google.com/maps/search/?api=1&query=Gata+Fish+%26+Yacht+Club+Palmeira+Sal+Cabo+Verde")]),
    "Diner gastronomique au Marea": _web("Marea", "Santa Maria - RESERVE mardi 17/11 19h00 au nom de Morieux - ESPECES UNIQUEMENT (euros ou escudos)", "+2389822165", True, [("Google Maps (pas de site web)", "https://www.google.com/maps/search/?api=1&query=Marea+restaurant+Santa+Maria+Sal+Cabo+Verde")]),
    "Croisiere en catamaran - Cape Verde Sailing": _web("Cape Verde Sailing - catamaran", "Reserve sur Viator (ref. 1460555133) - mercredi 18/11 RDV 08h20 au Palm Beach Restaurant", "+2389339510", True, [("Reserver sur Viator (lien de Samuel)", "https://www.viator.com/fr-FR/search/133137P8?mcid=70066"), ("Site Cape Verde Sailing", "https://cvsailing.com/trips/catamaran-half-day-trip/"), ("Avis Tripadvisor", "https://www.tripadvisor.ca/AttractionProductReview-g482847-d23652011-Half_day_Catamaran_Sailing_Tour_in_Santa_Maria-Ilha_do_Sal.html")]),
    "Diner chez Il Gobbo": _web("Il Gobbo", "Rua 15 de Agosto - RESERVE mercredi 18/11 19h30 au nom de Morieux", "+2389524129", True, [("Google Maps (pas de site web)", "https://www.google.com/maps/search/?api=1&query=Il+Gobbo+Santa+Maria+Sal+Cabo+Verde")]),
    "Dejeuner au Palm Beach Restaurant": _web("Palm Beach Restaurant", "Plage de Santa Maria, au ponton - 11h00-22h00 - prevoir des especes", "+2382422643", False, [("Site web et reservation", "https://palmbeachsal.com/")]),
    "Coucher de soleil a Ponta Preta": _web("Restaurant Ponta Preta", "Plage de Ponta Preta, cote ouest - horaires non publies", "+2389918613", True, [("Google Maps (pas de site web)", "https://www.google.com/maps/search/?api=1&query=Restaurant+Ponta+Preta+Ilha+do+Sal+Cabo+Verde")]),
    "Diner homard grille au Barracuda": _web("Restaurante Barracuda", "Plage de Santa Maria - RESERVE jeudi 19/11 19h00 au nom de Morieux - especes uniquement", "+2385990450", True, [("Site web Barracuda", "http://www.restaurantebarracuda.com/")]),
    "Dejeuner a Area Docas - Pedra de Lume": _web("Area Docas", "Port de Pedra de Lume - tous les jours 10h00-22h00 - pas de reservation en ligne : table a faire garder par Ady", None, False, [("Google Maps (pas de site web)", "https://www.google.com/maps/search/?api=1&query=Area+Docas+Pedra+de+Lume+Sal+Cabo+Verde")]),
    "Diner de fete au Soul Kitchen": _web("Soul Kitchen", "Plage de Santa Maria (La Villa) - 09h00-22h30 - musique live des 19h00 - sans reservation", "+2389974761", True, [("Site Soul Kitchen", "http://www.soulkitchencaboverde.com/"), ("Tripadvisor", "https://www.tripadvisor.co.uk/Restaurant_Review-g482848-d13294464-Reviews-Soul_Kitchen_Restaurant-Santa_Maria_Ilha_do_Sal.html")]),
    "White Party au Bikini Beach Club": _web("White Party - Bikini Beach Club", "Reserve vendredi 20/11 22h00-01h30 - tenue blanche - carte acceptee", None, False, [("Reserver en ligne", "https://bikinibeachclub.com/booking"), ("Programme de la semaine", "https://bikinibeachclub.com/whats-on/")]),
}
for _t in ["Angulo Beach Bar - journee transat", "Transats a Angulo Beach Bar", "Apres-midi transats a Angulo"]:
    WEB[_t] = WEB["Dejeuner pieds dans le sable et transats a Angulo"]
for _t in ["Petit-dejeuner chez Cam s avant la croisiere", "Dernier petit-dejeuner chez Cam s"]:
    WEB[_t] = WEB["Petit-dejeuner chez Cam s"]
WEB["Petit-dejeuner tranquille au Cape Fruit"] = WEB["Petit-dejeuner au Cape Fruit"]
WEB["Rendez-vous au Palm Beach Restaurant"] = WEB["Croisiere en catamaran - Cape Verde Sailing"]


# ---------------------------------------------------------------- icone discrete devant le titre (remplace THEME + pastilles voiture et copier)
_ICO = {"f": "\U0001F3D6\uFE0F", "v": "\U0001F9ED"}
THEME["Coucher de soleil a Ponta Preta"] = "a"
ICON = {}
for _d in DAYS:
    for _e in _d["events"]:
        _t = _e["title"]
        _m = DEPLACEMENT.get(_t, ("", ""))[0]
        if THEME.get(_t) in ("f", "v"):
            ICON[_t] = _ICO[THEME[_t]]
        elif THEME.get(_t) == "a" or _e["type"] == "show":
            ICON[_t] = "\U0001F379"          # bar, apero
        elif _e["type"] == "meal":
            ICON[_t] = "\u2615" if (_t.startswith("Petit-dejeuner") or _t.startswith("Dernier petit-dejeuner") or "Cape Fruit" in _t) else "\U0001F37D\uFE0F"
        elif _e["type"] == "transport" and _m == "voiture":
            ICON[_t] = "\U0001F697" if _d["chap"] == "fr" or "Marck" in _t else "\U0001F695"
CAR = []          # plus de pastille Voiture : l icone taxi suffit
COPYDEST = {}     # plus de pastille Copier

WEB["Check-in " + AIRBNB] = _web("Hote Airbnb - Sal Sol & Mar", "Rua 15 Agosto 108, Santa Maria - arrivee a partir de 15h00", "+351961976139", True, [("Ouvrir l appli Airbnb", "https://www.airbnb.fr/trips")])

# Ady, chauffeur donne par l hote Airbnb
for _k in ['Taxi de l aeroport vers le logement', 'Chauffeur de la journee - depart', 'Route vers Pedra de Lume pour dejeuner', 'Check-out et route vers l aeroport', 'Taxi vers le Bikini Beach Club', 'Taxi retour au logement', 'Taxi vers Ponta Preta', 'Route vers le Bikini Beach Club', 'Taxi retour du Bikini Beach']:
    WEB[_k] = _web("Ady, chauffeur de taxi", "Chauffeur habituel de l hote Airbnb - transferts et visites de l ile - especes", "+2389529719", True, [])
    WEB[_k].update({"telLabel": "Appeler Ady", "telPretty": "+238 952 97 19"})

WEB["Check-in " + AIRBNB].update({"telLabel": "Appeler l hote", "telPretty": "+351 961 976 139"})


# ---------------------------------------------------------------- moyen de paiement (pastille sur la carte)
# carte / especes / plutot (especes probables) / les2 / verifier (inconnu : prevoir des especes)
PAY = {
    "Depart de Marck vers Orly": "carte",
    "Taxi de l aeroport vers le logement": "especes", "Dejeuner pieds dans le sable et transats a Angulo": "carte",
    "Premier diner chez Chez Pastis": "especes",
    "Petit-dejeuner au Papaya Cafe": "carte",
    "Route vers le Bikini Beach Club": "especes", "Brunch au Bikini Beach Club": "carte", "Apres-midi piscine et plage": "carte",
    "Taxi retour du Bikini Beach": "especes", "Apero caipirinha au Ola Brasil": "carte", "Diner et karaoke a l Atlantic Piano Bar & Grill": "carte",
    "Petit-dejeuner chez Cam s": "carte", "Angulo Beach Bar - journee transat": "carte", "Pause dejeuner": "carte",
    "Diner en musique a l Ocean Cafe": "carte", "Verre et concert au Buddy Bar": "carte",
    "Petit-dejeuner au Cape Fruit": "plutot", "Chauffeur de la journee - depart": "especes", "Buracona et l Oeil Bleu": "especes",
    "Dejeuner de poisson a Palmeira": "carte", "Lac sale de Pedra de Lume": "especes", "Diner gastronomique au Marea": "especes",
    "Dernier verre au Buddy Bar": "carte",
    "Petit-dejeuner chez Cam s avant la croisiere": "carte", "Croisiere en catamaran - Cape Verde Sailing": "carte", "Rendez-vous au Palm Beach Restaurant": "carte",
    "Dejeuner au LobStar, au pied du ponton": "carte", "Diner chez Il Gobbo": "carte",
    "Petit-dejeuner tranquille au Cape Fruit": "plutot", "Transats a Angulo Beach Bar": "carte", "Dejeuner au Palm Beach Restaurant": "plutot",
    "Apres-midi transats a Angulo": "carte", "Taxi vers Ponta Preta": "especes", "Coucher de soleil a Ponta Preta": "carte",
    "Retour de Ponta Preta": "especes", "Diner homard grille au Barracuda": "especes", "Dernier verre en musique": "carte",
    "Dernier petit-dejeuner chez Cam s": "carte", "Route vers Pedra de Lume pour dejeuner": "especes",
    "Dejeuner a Area Docas - Pedra de Lume": "plutot", "Shark Bay - les requins citrons": "especes",
    "Diner de fete au Soul Kitchen": "carte", "Taxi vers le Bikini Beach Club": "especes", "White Party au Bikini Beach Club": "carte",
    "Taxi retour au logement": "especes", "Check-out et route vers l aeroport": "especes",
}

WEB["Dejeuner au LobStar, au pied du ponton"] = _web("LobStar", "Front de mer, au pied du ponton de Santa Maria", None, False, [("Site web LobStar", "https://www.lobstar.site/")])

# ---------------------------------------------------------------- budget par couple (accordeon de l onglet Infos)
BUDGET = {
    "title": "Budget sur place par couple",
    "intro": "Budget de depenses sur place PAR COUPLE (les depenses communes sont partagees en deux) : taxis et chauffeurs, visites et entrees, restaurants, bars et beach club. Estimation volontairement genereuse, boissons et vin compris : on se fait plaisir. Les vols, l Airbnb, la plongee et le catamaran, déjà payés, ne sont pas comptés. Les lieux sans mention espèces uniquement dans les avis sont comptés en carte.",
    "days": [
        ["Sam 14", 110, 90, "Taxis, Chez Pastis (especes), petit-dejeuner a Orly, Angulo (carte)"],
        ["Dim 15", 5, 280, "Taxis (especes), brunch et piscine au Bikini, Ola Brasil et Atlantic (carte)"],
        ["Lun 16", 10, 160, "Pourboires (especes), Cam s, dejeuner, Ocean Cafe, Angulo (carte)"],
        ["Mar 17", 240, 130, "Chauffeur Ady, entrees, Shark Bay, Cape Fruit, Marea (especes), Gata Fish et Buddy Bar (carte)"],
        ["Mer 18", 15, 207, "Pourboire (especes), Cam s, LobStar, Il Gobbo (carte) - catamaran deja paye sur Viator"],
        ["Jeu 19", 250, 110, "Cape Fruit, Palm Beach, taxis, Barracuda (especes), Angulo, Ponta Preta, dernier verre (carte)"],
        ["Ven 20", 60, 215, "Sol Doce, transats, taxis (especes), Cam s, boissons, diner et White Party (carte)"],
        ["Sam 21", 10, 70, "Taxi Ady (especes), aeroport de Sal et diner sur l autoroute (carte)"],
    ],
    "note": "Prevoir les especes au fil des jours (distributeurs a l aeroport, Santa Maria et Espargos).",
}

# ---------------------------------------------------------------- Mes notes : notes pre-remplies par jour (id du jour), modifiables sur le telephone
DEFAULT_DAY_NOTES = {
    5: "CATAMARAN : rendez-vous confirme a 08h20 au Palm Beach Restaurant, retour au meme endroit. Chauffeur 5 minutes d attente maximum.\n",
}


# ------------------------------------------------------------------ Vue synthetique des restaurants (Infos)
# titre d evenement -> nom court affiche dans l accordeon Restaurants
RESTO_SHORT = {
    "Dejeuner pieds dans le sable et transats a Angulo": "Angulo Beach Bar",
    "Premier diner chez Chez Pastis": "Chez Pastis",
    "Petit-dejeuner au Papaya Cafe": "Papaya Café",
    "Brunch au Bikini Beach Club": "Bikini Beach Club (brunch)",
    "Diner et karaoke a l Atlantic Piano Bar & Grill": "Atlantic Piano Bar",
    "Petit-dejeuner chez Cam s": "Cam’s",
    "Pause dejeuner": "Pause déjeuner libre",
    "Diner en musique a l Ocean Cafe": "Ocean Café",
    "Petit-dejeuner au Cape Fruit": "Cape Fruit",
    "Dejeuner de poisson a Palmeira": "Gata Fish, Palmeira",
    "Diner gastronomique au Marea": "Marea",
    "Petit-dejeuner chez Cam s avant la croisiere": "Cam’s",
    "Dejeuner au LobStar, au pied du ponton": "LobStar",
    "Diner chez Il Gobbo": "Il Gobbo",
    "Petit-dejeuner tranquille au Cape Fruit": "Cape Fruit",
    "Dejeuner au Palm Beach Restaurant": "Palm Beach",
    "Diner homard grille au Barracuda": "Barracuda",
    "Dernier petit-dejeuner chez Cam s": "Cam’s",
    "Dejeuner a Area Docas - Pedra de Lume": "Area Docas, Pedra de Lume",
    "Diner de fete au Soul Kitchen": "Soul Kitchen",
}


# ---- vendredi libre (maj rythme)
for _d in (INFO, WEB, MAPS_URLS, PAY, DEPLACEMENT, THEME, RESTO_SHORT):
    if "Dejeuner pieds dans le sable et transats a Angulo" in _d:
        _d["Dernier dejeuner et transats a Angulo"] = _d["Dejeuner pieds dans le sable et transats a Angulo"]
RESTO_SHORT["Dernier dejeuner et transats a Angulo"] = "Angulo Beach Bar"
THEME["Sieste avant la derniere soiree"] = "f"
MAPS_URLS["Sieste avant la derniere soiree"] = "https://maps.app.goo.gl/Dx5Vf6wRjakuiq9a6"
# dimanche
THEME["Grasse matinee et cafe au logement"] = "f"
MAPS_URLS["Grasse matinee et cafe au logement"] = "https://maps.app.goo.gl/Dx5Vf6wRjakuiq9a6"
# repas ajoutes
PAY["Petit-dejeuner a Orly"] = "carte"
RESTO_SHORT["Petit-dejeuner a Orly"] = "Orly (aéroport)"
PAY["Petit-dejeuner et sandwich pour le vol"] = "verifier"
RESTO_SHORT["Petit-dejeuner et sandwich pour le vol"] = "Aéroport de Sal"
PAY["Diner sur l aire d Assevillers"] = "carte"
RESTO_SHORT["Diner sur l aire d Assevillers"] = "Aire d’Assevillers (A1)"
MAPS_URLS["Diner sur l aire d Assevillers"] = "https://www.google.com/maps/search/?api=1&query=Aire+d+Assevillers+A1"

INFO["Dernier dejeuner et transats a Angulo"] = INFO_ANGULO

# ---- vue "billets" des reservations (textes deja accentues, ne pas passer dans fr)
RESA_VIEW = {
    "parking": {"k": "0", "when": "Avant le départ", "j": "dès que possible", "ico": "🅿️", "t": "Parking Orly", "sub": "Voiture de Cédric, du 14/11 vers 03h30 au 21/11 vers 20h30"},
    "oceancafe": {"k": "1116b", "dw": "LUN", "dn": "16", "m": "NOV", "ico": "🎶", "t": "Ocean Café", "line": "19h30 · musique live · terrasse demandée", "ref": "Morieux", "st": "Réservé"},
    "gata": {"k": "1117", "dw": "MAR", "dn": "17", "m": "NOV", "ico": "🍽️", "t": "Gata Fish, Palmeira", "line": "12h30 · port de Palmeira · tour du nord", "ref": "Morieux", "st": "Réservé"},
    "vols": {"k": "1114a", "dw": "SAM", "dn": "14", "m": "NOV", "ico": "✈️", "t": "Vols Transavia", "line": "Aller 06h30 Orly · retour 21/11 11h40", "ref": "K6UNPB", "st": "Payé"},
    "airbnb": {"k": "1114b", "dw": "SAM", "dn": "14", "m": "NOV", "ico": "🏠", "t": "Airbnb Sal Sol & Mar", "line": "7 nuits · arrivée 15h00 · départ 21/11 11h00", "ref": "HMYTYQTCD3", "st": "Payé"},
    "pastis": {"k": "1114c", "dw": "SAM", "dn": "14", "m": "NOV", "ico": "🍽️", "t": "Chez Pastis", "line": "18h30 · table dans la cour", "ref": "Morieux", "st": "Réservé", "cash": True},
    "bikini": {"k": "1115a", "dw": "DIM", "dn": "15", "m": "NOV", "ico": "🥂", "t": "Brunch Bikini Beach Club", "line": "13h00 · zone Restaurant", "ref": "Resos", "st": "Réservé"},
    "atlantic": {"k": "1115b", "dw": "DIM", "dn": "15", "m": "NOV", "ico": "🎤", "t": "Atlantic Piano Bar", "line": "19h45 · karaoké", "ref": "TableHelm", "st": "Réservé"},
    "plongee": {"k": "1116a", "dw": "LUN", "dn": "16", "m": "NOV", "ico": "🤿", "t": "Plongée Cabo Verde Diving", "line": "08h30 Porto Antigo 1 · Samuel, Cédric", "ref": "226,72 €", "st": "Payé"},
    "marea": {"k": "1117a", "dw": "MAR", "dn": "17", "m": "NOV", "ico": "🍽️", "t": "Marea", "line": "19h00", "ref": "Morieux", "st": "Réservé", "cash": True},
    "croisiere": {"k": "1118a", "dw": "MER", "dn": "18", "m": "NOV", "ico": "⛵", "t": "Catamaran Cape Verde Sailing", "line": "RDV 08h20 au Palm Beach", "ref": "1460555133", "st": "Réservé"},
    "ilgobbo": {"k": "1118b", "dw": "MER", "dn": "18", "m": "NOV", "ico": "🍽️", "t": "Il Gobbo", "line": "19h30", "ref": "Morieux", "st": "Réservé"},
    "barracuda": {"k": "1119a", "dw": "JEU", "dn": "19", "m": "NOV", "ico": "🍽️", "t": "Barracuda", "line": "19h00 · bord de mer", "ref": "Morieux", "st": "Réservé", "cash": True},
    "whiteparty": {"k": "1120a", "dw": "VEN", "dn": "20", "m": "NOV", "ico": "🎉", "t": "White Party Bikini Beach", "line": "22h00 - 01h30 · tenue blanche", "ref": "Morieux", "st": "Réservé"},
}

# ---- vendredi midi : Sol Doce + apres-midi plage
INFO["Dejeuner de poisson au Sol Doce"] = {
    "title": "Restaurante Sol Doce",
    "intro": "Petit restaurant de poisson au bord de la plage de Santa Maria, pres du ponton. On y choisit son poisson du jour, cuisine sans chichis et cuit devant soi. L adresse de poisson la mieux notee du centre pour le dejeuner.",
    "horaires": ["Tous les jours de 10h00 a 18h00, ferme le mercredi", "Dejeuner uniquement : pas de service le soir"],
    "voir": ["Le poisson du jour grille (pargo, thon, wahoo selon la peche)", "Tataki et tartare de thon", "Lapas (patelles) et frites maison", "Le retour des pecheurs au ponton vers 12h30"],
    "tarifs": ["Petits prix : environ 2 000 a 2 500 CVE par personne", "ESPECES UNIQUEMENT, pas de carte"],
    "conseil": "Sans reservation : y aller directement vers 12h30. Si c est complet, patienter un peu ou faire un tour sur la plage et revenir. Le service est en general rapide, mais un avis d aout signale une longue attente : verifier que la commande est bien partie en cuisine.",
    "logistique": [{"titre": "Pratique", "lignes": ["Plage de Santa Maria, pres du ponton (Casa Viana)", "Tel et WhatsApp : +238 994 65 62", "4,6/5 sur Tripadvisor (412 avis), Travellers Choice 2026", "Palissades de chantier autour du ponton en ce moment"]}],
}
INFO["Apres-midi plage, transats et baignade"] = {
    "title": "Plage du ponton ou Angulo",
    "intro": "Pour le dernier apres-midi, deux plages a 10 minutes l une de l autre. La plage du ponton est la partie la plus abritee de la baie de Santa Maria : sable fin, peu de vagues, ideale pour se baigner. Angulo, a l est, a des transats assures mais une mer plus agitee.",
    "conseil": "Plan A : plage du ponton, demander sur place s il y a des transats a louer. Plan B : Angulo, transats gratuits avec une consommation (sinon environ 5 EUR), baignade pres du bord, a l ecart des kitesurfeurs. Creme et chapeau : le soleil tape fort meme avec le vent.",
}
WEB["Dejeuner de poisson au Sol Doce"] = _web("Restaurante Sol Doce", "Pres du ponton - 10h00-18h00, ferme le mercredi - especes uniquement", "+2389946562", True, [("Tripadvisor", "https://www.tripadvisor.co.uk/Restaurant_Review-g482848-d5414889-Reviews-Restaurante_Sol_Doce-Santa_Maria_Ilha_do_Sal.html")])
WEB["Dejeuner de poisson au Sol Doce"].update({"telLabel": "WhatsApp Sol Doce", "telPretty": "+238 994 65 62"})
WEB["Apres-midi plage, transats et baignade"] = WEB["Dejeuner pieds dans le sable et transats a Angulo"]
PAY["Dejeuner de poisson au Sol Doce"] = "especes"
PAY["Apres-midi plage, transats et baignade"] = "verifier"
MAPS_URLS["Dejeuner de poisson au Sol Doce"] = q("Restaurante Sol Doce Santa Maria Sal Cabo Verde")
MAPS_URLS["Apres-midi plage, transats et baignade"] = q("Pontao de Santa Maria Sal Cabo Verde")
RESTO_SHORT["Dejeuner de poisson au Sol Doce"] = "Sol Doce"
THEME["Apres-midi plage, transats et baignade"] = "f"

# ---- liens Tripadvisor directs (ajoutes apres le site web / Instagram, avant Google Maps)
_TAF = "https://www.tripadvisor.fr/Restaurant_Review-g482848-"
_TAS = "https://www.tripadvisor.fr/Search?q="
_TRIPA = {
    "Angulo": _TAF + "d4019885-Reviews-Angulo_Cabo_Verde-Santa_Maria_Ilha_do_Sal.html",
    "Chez Pastis": _TAF + "d2024191-Reviews-Chez_Pastis-Santa_Maria_Ilha_do_Sal.html",
    "Atlantic": _TAF + "d32829929-Reviews-The_Atlantic_Piano_Bar_and_Grill-Santa_Maria_Ilha_do_Sal.html",
    "Cams": _TAF + "d12171327-Reviews-Cam_s_Restaurante_E_Cafetaria-Santa_Maria_Ilha_do_Sal.html",
    "Ocean": _TAF + "d2646933-Reviews-Ocean_Cafe-Santa_Maria_Ilha_do_Sal.html",
    "Cape Fruit": _TAF + "d4799033-Reviews-Cape_Fruit-Santa_Maria_Ilha_do_Sal.html",
    "Marea": _TAF + "d6154118-Reviews-Marea_Italian_Restauran-Santa_Maria_Ilha_do_Sal.html",
    "Il Gobbo": _TAF + "d34084604-Reviews-Il_Gobbo_ilha_do_Sal-Santa_Maria_Ilha_do_Sal.html",
    "Palm Beach": _TAF + "d4731725-Reviews-Palm_Beach_Restaurant-Santa_Maria_Ilha_do_Sal.html",
    "Barracuda": _TAF + "d2658934-Reviews-Restaurante_Barracuda-Santa_Maria_Ilha_do_Sal.html",
    "LobStar": _TAF + "d15092634-Reviews-LobStar_Enjoyable_Seafood_Restaurant-Santa_Maria_Ilha_do_Sal.html",
    "Sol Doce": _TAF + "d5414889-Reviews-Restaurante_Sol_Doce-Santa_Maria_Ilha_do_Sal.html",
    "Soul Kitchen": "https://www.tripadvisor.fr/Restaurant_Review-g482848-d13294464-Reviews-Soul_Kitchen_Restaurant-Santa_Maria_Ilha_do_Sal.html",
    "Gata": _TAS + "Gata+Fish+Yacht+Club+Palmeira+Sal",
    "Area Docas": _TAS + "Area+Docas+Pedra+de+Lume",
    "Ponta Preta": "https://www.tripadvisor.fr/Restaurant_Review-g482847-d5494544-Reviews-Restaurant_Ponta_Preta-Ilha_do_Sal.html",
    "Buddy Bar": "https://www.tripadvisor.fr/Attraction_Review-g482848-d8816287-Reviews-Buddy_Bar-Santa_Maria_Ilha_do_Sal.html",
    "Ola Brasil": "https://www.tripadvisor.fr/Restaurant_Review-g482848-d28666532-Reviews-Beach_Bar_Ola_Brasil_Santa_Maria_Sal-Santa_Maria_Ilha_do_Sal.html",
    "Bikini": "https://www.tripadvisor.fr/Restaurant_Review-g482847-d12927337-Reviews-Bikini_Beach_Club-Ilha_do_Sal.html",
    "Papaya": _TAS + "Papaya+Cafe+Santa+Maria+Sal",
}
_TRIPA_EV = {
    "Dejeuner pieds dans le sable et transats a Angulo": "Angulo", "Angulo Beach Bar - journee transat": "Angulo",
    "Transats a Angulo Beach Bar": "Angulo", "Apres-midi transats a Angulo": "Angulo", "Dernier dejeuner et transats a Angulo": "Angulo",
    "Premier diner chez Chez Pastis": "Chez Pastis", "Diner et karaoke a l Atlantic Piano Bar & Grill": "Atlantic",
    "Petit-dejeuner chez Cam s": "Cams", "Petit-dejeuner chez Cam s avant la croisiere": "Cams", "Dernier petit-dejeuner chez Cam s": "Cams",
    "Diner en musique a l Ocean Cafe": "Ocean", "Petit-dejeuner au Cape Fruit": "Cape Fruit", "Petit-dejeuner tranquille au Cape Fruit": "Cape Fruit",
    "Diner gastronomique au Marea": "Marea", "Diner chez Il Gobbo": "Il Gobbo", "Dejeuner au Palm Beach Restaurant": "Palm Beach",
    "Diner homard grille au Barracuda": "Barracuda", "Dejeuner au LobStar, au pied du ponton": "LobStar",
    "Dejeuner de poisson au Sol Doce": "Sol Doce", "Diner de fete au Soul Kitchen": "Soul Kitchen",
    "Dejeuner de poisson a Palmeira": "Gata", "Dejeuner a Area Docas - Pedra de Lume": "Area Docas",
    "Coucher de soleil a Ponta Preta": "Ponta Preta", "Brunch au Bikini Beach Club": "Bikini", "White Party au Bikini Beach Club": "Bikini",
    "Petit-dejeuner au Papaya Cafe": "Papaya", "Apero caipirinha au Ola Brasil": "Ola Brasil",
    "Dernier verre au Buddy Bar": "Buddy Bar",
}
_TRIPA_NOTE = {"Angulo": "4,3", "Chez Pastis": "4,5", "Atlantic": "4,4", "Cams": "4,3", "Ocean": "4,6", "Cape Fruit": "4,6",
    "Marea": "4,8", "Il Gobbo": "4,9", "Palm Beach": "4,2", "Barracuda": "4,1", "LobStar": "4,3", "Sol Doce": "4,6",
    "Soul Kitchen": "4,6", "Gata": "4,4", "Area Docas": "4,1", "Ponta Preta": "4,1", "Bikini": "4,2", "Ola Brasil": "4,7", "Buddy Bar": "4,5", "Papaya": "4,2"}
# pastille verte sur l etape : note + lien direct ; on retire Tripadvisor de la fenetre Web pour ne pas doubler
TA_EVENTS = {_t: [_TRIPA[_k], _TRIPA_NOTE[_k]] for _t, _k in _TRIPA_EV.items()}
for _t in TA_EVENTS:
    if _t in WEB:
        WEB[_t]["links"] = [l for l in WEB[_t]["links"] if "tripadvisor" not in l[1]]

# ---- videos TikTok (lien, pas de lecture hors ligne)
for _k, _v in INFO.items():
    if _v.get("title", "").startswith("Angulo - beach bar"):
        _v["video"] = "https://vm.tiktok.com/ZN8Up4qjw/"
# Bikini Beach Club : vue aerienne (photo de Samuel) + video TikTok
INFO["Route vers le Bikini Beach Club"]["image"] = "bikini-beach-club.jpg"
INFO["Brunch au Bikini Beach Club"]["image"] = "bikini-beach-club.jpg"
for _k in ("Route vers le Bikini Beach Club", "Brunch au Bikini Beach Club", "White Party au Bikini Beach Club"):
    INFO[_k]["video"] = "https://vm.tiktok.com/ZN8UputtH/"
INFO["Apero caipirinha au Ola Brasil"]["video"] = "https://vm.tiktok.com/ZN8UpHegv/"
INFO["Diner et karaoke a l Atlantic Piano Bar & Grill"]["image"] = "atlantic-enseigne.jpg"
INFO["Diner et karaoke a l Atlantic Piano Bar & Grill"]["video"] = "https://vm.tiktok.com/ZN8UpX9LW/"
INFO["Diner en musique a l Ocean Cafe"]["video"] = "https://vm.tiktok.com/ZN8UpV24K/"
INFO["Dernier verre au Buddy Bar"]["image"] = "buddy-bar-cocktails.jpg"
INFO["Dernier verre au Buddy Bar"]["video"] = "https://vm.tiktok.com/ZN8UpKrcL/"
INFO["Dejeuner au LobStar, au pied du ponton"]["image"] = "lobstar.jpg"
INFO["Dejeuner au LobStar, au pied du ponton"]["video"] = "https://vm.tiktok.com/ZN8UsJkUs/"
INFO["Dejeuner au Palm Beach Restaurant"]["image"] = "palm-beach-plat.jpg"
INFO["Dejeuner au Palm Beach Restaurant"]["video"] = "https://vm.tiktok.com/ZN8UpEXFE/"
INFO["Diner homard grille au Barracuda"]["video"] = "https://vm.tiktok.com/ZN8UsjkKQ/"
INFO["Dejeuner de poisson au Sol Doce"]["video"] = "https://vm.tiktok.com/ZN8UsR8jj/"
INFO["Diner de fete au Soul Kitchen"]["image"] = "soul-kitchen.jpg"


# ---------------------------------------------------------------- balades du matin (au choix : balade ou grasse matinee)
def _gm(lat, lng):
    return "https://www.google.com/maps/search/?api=1&query=%s,%s" % (lat, lng)
def _gps(pts):
    return ("https://www.google.com/maps/dir/?api=1&origin=16.59736%2C-22.90267&destination=16.59753%2C-22.90336&waypoints="
            + "%7C".join("%s%%2C%s" % p for p in pts) + "&travelmode=walking")
_P = {"ponton": (16.59675, -22.90754), "phare": (16.58605, -22.92319), "pp": (16.59846, -22.92751),
      "salines": (16.61102, -22.90237), "kite": (16.61460, -22.89722), "angulo": (16.59629, -22.89897),
      "eglise": (16.59853, -22.90635), "conchas": (16.59523, -22.89472)}
WALK_T1 = "Balade du matin : phare et plage de Ponta Preta"
WALK_T2 = "Balade du matin : salines et Kite Beach"
WALK_T3 = "Balade du matin : Santa Maria au reveil"
WALKS = {
    WALK_T1: {"km": "8,5 km", "dur": "2h15", "gps": _gps([_P["ponton"], _P["phare"], _P["pp"]]),
              "eau": "1 litre par personne minimum. Aucune ombre et aucun point d eau sur le parcours : les bars de Ponta Preta n ouvrent qu a 10h00. Casquette, creme solaire et lunettes.",
              "stops": [
                  ["balade-ponton.jpg", "Le ponton", "Bateaux de peche colores et eau turquoise. Le ponton est abime depuis la tempete de 2024 : on le regarde depuis la plage.", _gm(*_P["ponton"])],
                  ["balade-phare.jpg", "Phare de Ponta do Sino", "Le petit phare blanc de la pointe sud de l ile, posé sur des kilometres de sable.", _gm(*_P["phare"])],
                  ["balade-ponta-preta.jpg", "Plage de Ponta Preta", "Eau turquoise, rouleaux et surfeurs. Presque personne le matin : la plus belle plage de Sal.", _gm(*_P["pp"])],
                  ["balade-dunes.jpg", "Retour par les dunes", "Sable ride par le vent et touffes vertes, entre Ponta Preta et Santa Maria.", ""],
              ]},
    WALK_T2: {"km": "6 km", "dur": "1h50", "gps": _gps([_P["salines"], _P["kite"], _P["conchas"], _P["angulo"]]),
              "eau": "1 litre par personne minimum. Pas d ombre ni de point d eau aux salines. Le cafe de Kite Beach peut depanner s il est ouvert. Casquette et creme solaire.",
              "stops": [
                  ["balade-salines.jpg", "Salines de Santa Maria", "Bassins de sel au milieu des dunes. On peut rapporter un morceau de sel : laisser une piece aux ouvriers.", _gm(*_P["salines"])],
                  ["balade-kite-beach.jpg", "Kite Beach", "Les voiles de kitesurf dans l alize, cote est. Cafe sur place.", _gm(*_P["kite"])],
                  ["balade-conchas.jpg", "Praia das Conchas", "Le cimetiere des coquillages : les pecheurs y deposent les coquilles vides depuis des annees. Belle vue sur Santa Maria.", _gm(*_P["conchas"])],
                  ["balade-angulo.jpg", "Retour par Angulo", "Le long de la plage jusqu a Angulo, puis Cape Fruit pour le petit-dejeuner.", _gm(*_P["angulo"])],
              ]},
    WALK_T3: {"km": "3,6 km", "dur": "1h10", "gps": _gps([_P["eglise"], _P["ponton"], (16.59504, -22.91282), _P["angulo"]]),
              "eau": "Une bouteille d eau par personne : le soleil tape deja fort a 9h00. Casquette et creme solaire.",
              "stops": [
                  ["balade-eglise.jpg", "Eglise Nossa Senhora das Dores", "La petite eglise du centre, Rua 1 de Junho.", _gm(*_P["eglise"])],
                  ["balade-peche.jpg", "Retour de peche au ponton", "Les pecheurs debarquent et decoupent le poisson sur place.", _gm(*_P["ponton"])],
                  ["balade-praia-santa-maria.jpg", "Praia de Santa Maria", "La grande plage a l ouest du ponton, au calme avant l arrivee des transats. Demi-tour ici.", "https://maps.app.goo.gl/Qhwmw2LdU4DWm9Mw8"],
                  ["balade-angulo.jpg", "Toute la baie jusqu a Angulo", "Retour le long de l eau, on repasse devant le ponton et on file vers l est jusqu a Angulo.", _gm(*_P["angulo"])],
                  ["balade-rue-pietonne-2.jpg", "Rue pietonne", "Facades colorees et cafes qui ouvrent, jusqu a Cam s.", "https://www.google.com/maps/search/?api=1&query=Rua+1+de+Junho+Santa+Maria+Sal+Cabo+Verde"],
              ]},
}
_WB = {
    WALK_T1: "AU CHOIX : balade ou grasse matinee, le reste de la journee ne change pas. Boucle de 8,5 km, environ 2h15 avec les pauses photo, depart 08h00 du logement. On descend au ponton, puis on longe la plage vers l ouest jusqu au phare de Ponta do Sino, la pointe sud de l ile. On continue sur le sable jusqu a Ponta Preta, puis retour par l interieur, entre les dunes. Marcher sur le sable mouillé au bord de l eau : il est plus dur, on avance mieux. Retour au logement vers 10h15.",
    WALK_T2: "AU CHOIX : balade ou grasse matinee, le reste de la journee ne change pas. Boucle d environ 6 km, 1h50, depart 07h30 du logement. On monte vers le nord jusqu aux salines de Santa Maria, au milieu des dunes, puis Kite Beach sur la cote est. Retour vers le sud par la plage et la Praia das Conchas, le cimetiere des coquillages, jusqu a Angulo. Petit-dejeuner chez Cape Fruit a 09h30.",
    WALK_T3: "AU CHOIX : balade ou grasse matinee, le reste de la journee ne change pas. Petite boucle de 3,6 km, environ 1h10, depart 08h45 apres l enregistrement en ligne. L eglise, puis le ponton a l heure du retour de peche. On longe la plage vers l ouest jusqu a la Praia de Santa Maria, puis demi-tour et toute la baie vers l est jusqu a Angulo. Retour par la rue pietonne jusqu a Cam s pour 10h00.",
}
for _d in DAYS:
    for _e in _d["events"]:
        if _d["date"] == "DIM 15 NOV" and _e["title"] == "Grasse matinee et cafe au logement":
            _e["time"] = "10h15"
            _e["body"] = "Au retour de la balade, ou apres une grasse matinee. " + _e["body"]
        if _d["date"] == "VEN 20 NOV" and _e["title"] == "Enregistrement en ligne vol retour":
            _e["time"] = "08h30"
            _e["body"] += " A faire avant la balade du matin."
def _ins(date, ev_obj):
    d = next(x for x in DAYS if x["date"] == date)
    i = next(n for n, e in enumerate(d["events"]) if "05h00" <= e["time"] and e["time"] > ev_obj["time"])
    d["events"].insert(i, ev_obj)
for _dt, _tt, _h in (("DIM 15 NOV", WALK_T1, "08h00"), ("JEU 19 NOV", WALK_T2, "07h30"), ("VEN 20 NOV", WALK_T3, "08h45")):
    _ins(_dt, ev(_h, _tt, _WB[_tt], "activity", "OPTION"))
    MAPS_ALWAYS.append(_tt)
    MAPS_URLS[_tt] = WALKS[_tt]["gps"]
    ICON[_tt] = "\U0001F97E"
WALK_IMGS = sorted({s[0] for w in WALKS.values() for s in w["stops"] if s[0]})
for _d in DAYS:
    for _e in _d["events"]:
        if _d["date"] == "JEU 19 NOV" and _e["title"] == "Petit-dejeuner tranquille au Cape Fruit":
            _e["body"] = _e["body"].replace("Grasse matinee, puis petit-dejeuner sans se presser.", "Au retour de la balade, ou apres une grasse matinee : petit-dejeuner sans se presser.", 1)
# liens des vignettes : fiche Google du lieu (nom + identifiant), plus parlant qu un point GPS
_PID = {"Le ponton": ("The Pier of Santa Maria", "ChIJMRh3xApcSwkRImvgx7tVk90"),
        "Retour de peche au ponton": ("The Pier of Santa Maria", "ChIJMRh3xApcSwkRImvgx7tVk90"),
        "Phare de Ponta do Sino": ("Farol Ponta do Sino", "ChIJBxBQp31dSwkRH6qLeHlBdUM"),
        "Plage de Ponta Preta": ("Ponta Preta beach", "ChIJL_mXeABdSwkRdEZHk9vC05g"),
        "Salines de Santa Maria": ("Salina Santa Maria", "ChIJY8AJEEJbSwkRASoBaIxwHk8"),
        "Kite Beach": ("Kite Beach Schildkrote Sal", "ChIJca6MfPxbSwkR3EwFmlNWREY"),
        "Praia das Conchas": ("Shell Cemetery Beach", "ChIJlRxl07NbSwkRLMoHVYydCjo"),
        "Retour par Angulo": ("Angulo Beach Bar & Restaurant", "ChIJMzr0pIxbSwkRUnMEg1yLWec"),
        "Toute la baie jusqu a Angulo": ("Angulo Beach Bar & Restaurant", "ChIJMzr0pIxbSwkRUnMEg1yLWec"),
        "Eglise Nossa Senhora das Dores": ("Catholic Church of Our Lady of Sorrows", "ChIJg02ShApcSwkR-_8Vnpl8-F8")}
import urllib.parse as _up
for _w in WALKS.values():
    for _s in _w["stops"]:
        if _s[1] in _PID:
            _n, _id = _PID[_s[1]]
            _s[3] = "https://www.google.com/maps/search/?api=1&query=" + _up.quote_plus(_n) + "&query_place_id=" + _id
# lien Maps de l eglise fourni par Samuel
for _w in WALKS.values():
    for _s in _w["stops"]:
        if _s[1] == "Eglise Nossa Senhora das Dores":
            _s[3] = "https://maps.app.goo.gl/TTtJohj36fqUjNpWA"
# lien Maps du ponton (retour de peche) fourni par Samuel
for _w in WALKS.values():
    for _s in _w["stops"]:
        if _s[1] == "Retour de peche au ponton":
            _s[3] = "https://maps.app.goo.gl/MRwY8JrJ57ikTiUW9"

# ---- parking Orly reserve (confirmation Paris Aeroport recue par Cedric, sortie corrigee le 06/11)
for _d in DAYS:
    for _e in _d["events"]:
        if _e["title"] == "Parking Orly - depot voiture":
            _e["body"] = ("Parking P3 Orly, RESERVE ET PAYE (confirmation Paris Aeroport dans le mail de Cedric). "
                          "Entree possible des 03h00, sortie jusqu au samedi 21/11 a 21h59. La barriere lit la plaque DA-242-MH ; "
                          "si elle ne la reconnait pas, taper sur la borne d entree le code d acces 594521.")
INFO["Parking Orly - depot voiture"] = {
    "title": "Parking P3 Orly",
    "intro": "Parking P3 de l aeroport d Orly, reserve et paye en ligne sur Paris Aeroport (mail de confirmation recu par Cedric). Entree le samedi 14/11 a partir de 03h00, sortie le samedi 21/11 avant 21h59.",
    "conseil": "Plaque enregistree : DA-242-MH, la barriere s ouvre seule a l entree comme a la sortie. Si la camera ne lit pas la plaque, taper le code d acces 594521 sur la borne d entree.",
    "logistique": [{"titre": "Reservation", "lignes": [
        "Parking : P3 Orly",
        "Entree : samedi 14/11 a partir de 03h00",
        "Sortie : samedi 21/11 avant 21h59 (atterrissage a 19h30)",
        "Plaque : DA-242-MH (voiture de Cedric)",
        "Code d acces de secours (borne d entree) : 594521",
        "Une question : 3950 (Paris Aeroport)"]}],
}
RESA_VIEW["parking"] = {"k": "1114", "dw": "SAM", "dn": "14", "m": "NOV", "ico": "🅿️", "t": "Parking P3 Orly",
                        "line": "Entrée dès 03h00 · sortie 21/11 avant 21h59", "ref": "DA-242-MH", "st": "Payé"}
if "parking" not in LOCKED:
    LOCKED.append("parking")
for _r in RESAS:
    if _r.get("name") == "Parking Orly":
        _r["detail"] = "PAYE - Parking P3 Orly (Paris Aeroport) - plaque DA-242-MH - entree 14/11 des 03h00 - sortie 21/11 avant 21h59 - code d acces 594521"
        _r["deadline"] = "PAYE"
        _r["color"] = "#2E6B3E"
for _r in CHK_ITEMS:
    if _r.get("id") == "parking":
        _r["deadline"] = "PAYE - P3 Orly - plaque DA-242-MH - sortie 21/11 avant 21h59"
        _r["color"] = "#2E6B3E"
RESA_DETAILS["parking"] = {"num": "Plaque DA-242-MH", "site": "Paris Aeroport - Parking P3 Orly",
    "info": "PAYE - entree sam 14/11 des 03h00 - sortie sam 21/11 avant 21h59 - code d acces de secours 594521 - question : 3950"}
RESA_TODO.pop("Parking Orly - depot voiture", None)
for _d in DAYS:
    for _e in _d["events"]:
        if _e["title"] == "Parking Orly - depot voiture":
            _e["cost"] = "Payé"

# ---- EASE : preenregistrement et taxe aeroport payes le 08/11 pour les 4 (recus a garder dans Infos > Vos billets)
RESA_VIEW["ease"] = {"k": "1113", "dw": "SAM", "dn": "14", "m": "NOV", "ico": "🛂", "t": "EASE Cap-Vert",
                     "line": "Préenregistrement et taxe aéroport · 4 voyageurs", "ref": "4 reçus", "st": "Payé"}
RESA_DETAILS["ease"] = {"num": "4 recus EASE", "site": "ease.gov.cv",
    "info": "PAYE le 08/11 - 30,83 EUR (3 400 CVE) par personne, 123,32 EUR pour 4 - vol TO3232, entree par Sal, arrivee 14/11, retour 21/11 - recus : Samuel 12055869, Francoise 12055903, Cedric 12055739, Virginie 12055812 - photos des recus dans Infos > Vos billets"}
if "ease" not in LOCKED:
    LOCKED.append("ease")
for _r in CHK_ITEMS:
    if _r.get("id") == "ease":
        _r["deadline"] = "PAYE le 08/11 - 4 recus (Infos > Vos billets)"
        _r["color"] = "#2E6B3E"
for _r in RESAS:
    if _r.get("name") == "Preenregistrement EASE x4":
        _r["detail"] = "PAYE le 08/11 - 30,83 EUR par personne (123,32 EUR pour 4) - recus dans Infos > Vos billets"
        _r["deadline"] = "PAYE"
        _r["color"] = "#2E6B3E"
for _r in ESSENTIALS if "ESSENTIALS" in globals() else []:
    if _r.get("label") == "Recu EASE":
        _r["val"] = "Paye le 08/11 pour les 4. Ajouter les photos des recus dans Infos > Vos billets : elles restent dans le telephone, disponibles hors connexion."
# EASE fait le 08/11 et Morabeza abandonne (beach club pas rouvert) : retires des a faire
TODO_ITEMS[:] = [t for t in TODO_ITEMS if t.get("id") not in ("ease", "morabeza")]
for _d in DAYS:
    for _e in _d["events"]:
        if "OPTION MORABEZA" in _e["body"]:
            _e["body"] = _e["body"].split(" OPTION MORABEZA")[0]
INFO["Atterrissage a Sal - Aeroport Amilcar Cabral"]["conseil"] = "Preenregistrement EASE fait et paye le 08/11 pour les 4 : au controle, presenter le passeport et le recu de chacun (photos dans Infos > Vos billets)."
if not any(_r.get("id") == "ease" for _r in CHK_ITEMS):
    CHK_ITEMS.insert(0, {"id": "ease", "name": "Preenregistrement EASE x4", "date": "14 nov", "deadline": "PAYE le 08/11 - 4 recus (Infos > Vos billets)", "color": "#2E6B3E"})
# fiche depart de nuit : rapprochement avec le parking reserve et les recus EASE
_fd = INFO["Depart de Marck vers Orly"]
_fd["conseil"] = "Parking reserve et paye (P3 Orly) : on va directement au parking, la barriere lit la plaque DA-242-MH (code de secours 594521). Puis navette ou marche jusqu au Terminal 3 pour 04h00."
_fd["logistique"] = [
    {"titre": "Trajet", "lignes": ["Depart de Marck (62730) avec la voiture de Cedric", "Environ 305 km par l A26 puis l A1", "Environ 3h15 de nuit"]},
    {"titre": "Parking (reserve et paye)", "lignes": ["P3 Orly, reserve et paye sur Paris Aeroport", "Entree a partir de 03h00 le 14/11", "Plaque DA-242-MH reconnue a la barriere", "Code de secours a la borne d entree : 594521", "Sortie le 21/11 avant 21h59"]},
    {"titre": "A ne pas oublier", "lignes": ["Un passeport pour chacun des 4", "Recus EASE (payes le 08/11, photos dans Infos > Vos billets)", "Cartes d embarquement telechargees"]},
]
for _d in DAYS:
    for _e in _d["events"]:
        if _e["title"] == "Depart de Marck vers Orly":
            _e["body"] = _e["body"].replace("Arrivee a l aeroport d Orly vers 03h30 (parking)", "Arrivee a l aeroport d Orly vers 03h30, directement au parking P3 reserve")
# parking : P3 Orly 3, heure d entree en tete, lien Maps sur le parking
_P3 = "https://www.google.com/maps/search/?api=1&query=Parking+P3+Orly+3&query_place_id=ChIJ80NzJtF15kcR4N0RTvqjJBI"
MAPS_URLS["Parking Orly - depot voiture"] = _P3
if "Parking Orly - depot voiture" not in MAPS_ALWAYS:
    MAPS_ALWAYS.append("Parking Orly - depot voiture")
for _d in DAYS:
    for _e in _d["events"]:
        if _e["title"] == "Parking Orly - depot voiture":
            _e["body"] = ("Parking P3 Orly, a cote d Orly 3 : ENTREE RESERVEE A PARTIR DE 03h00. RESERVE ET PAYE (confirmation Paris Aeroport dans le mail de Cedric). "
                          "La barriere lit la plaque DA-242-MH ; si elle ne la reconnait pas, taper sur la borne d entree le code d acces 594521. "
                          "Ensuite a pied jusqu au Terminal 3. Sortie jusqu au samedi 21/11 a 21h59.")
INFO["Parking Orly - depot voiture"]["title"] = "Parking P3 Orly (Orly 3)"
INFO["Parking Orly - depot voiture"]["intro"] = "Parking officiel P3 d Orly, a cote du Terminal 3, reserve et paye en ligne sur Paris Aeroport (mail de confirmation recu par Cedric). Entree le samedi 14/11 a partir de 03h00, sortie le samedi 21/11 avant 21h59."
INFO["Depart de Marck vers Orly"]["conseil"] = "Parking reserve et paye (P3 Orly, entree des 03h00) : on va directement au parking, la barriere lit la plaque DA-242-MH (code de secours 594521). Puis a pied jusqu au Terminal 3 pour 04h00."
_P3 = "https://maps.app.goo.gl/C5fw5Mg8sP6ZA9a86"
MAPS_URLS["Parking Orly - depot voiture"] = _P3
INFO["Parking Orly - depot voiture"]["mapsUrl"] = _P3
INFO["Parking Orly - depot voiture"]["mapsLabel"] = "Parking P3 Orly sur Maps"
# Terminal 3 d Orly : lien Maps fourni par Samuel (le trajet de nuit pointe sur le parking P3)
_T3 = "https://maps.app.goo.gl/7C9UsQcrsn3Zq7qi8"
for _t in ("Arrivee aeroport Orly T3 - Depot bagages", "Petit-dejeuner a Orly", "Arrivee a Orly (heure de Paris)", "Vol Transavia TO3232 Orly vers Sal"):
    MAPS_URLS[_t] = _T3
    if _t not in MAPS_ALWAYS:
        MAPS_ALWAYS.append(_t)
    if _t in INFO:
        INFO[_t]["mapsUrl"] = _T3
        INFO[_t]["mapsLabel"] = "Orly Terminal 3 sur Maps"
MAPS_URLS["Depart de Marck vers Orly"] = _P3
INFO["Depart de Marck vers Orly"]["mapsUrl"] = _P3
INFO["Depart de Marck vers Orly"]["mapsLabel"] = "Parking P3 Orly sur Maps"
# P3 -> Terminal 3 a pied : le P3 est en face d Orly 3, environ 5 minutes (10 avec les valises et l ascenseur)
for _d in DAYS:
    for _e in _d["events"]:
        if _e["title"] == "Parking Orly - depot voiture":
            _e["body"] = _e["body"].replace("Ensuite a pied jusqu au Terminal 3.", "Ensuite a pied jusqu a l enregistrement du Terminal 3 : le P3 est juste en face, environ 5 minutes, compter 10 minutes avec les valises.")
INFO["Parking Orly - depot voiture"]["logistique"][0]["lignes"].insert(1, "A pied jusqu au Terminal 3 (en face) : environ 5 minutes, 10 avec les valises")
INFO["Depart de Marck vers Orly"]["conseil"] = INFO["Depart de Marck vers Orly"]["conseil"].replace("Puis a pied jusqu au Terminal 3 pour 04h00.", "Puis a pied jusqu a l enregistrement du Terminal 3 (en face du P3) : environ 5 minutes, 10 avec les valises, pour y etre a 04h00.")
# a bord du Boeing 737-800 Transavia (sources : transavia.com, seatmaps.com, flight-report)
_B738 = {"titre": "À bord du Boeing 737-800", "lignes": [
    "189 sieges, une seule classe, 3 + 3 de chaque cote de l allee",
    "Espace pour les jambes d environ 76 cm : les sieges avec plus d espace (issues de secours, premier rang) sont payants a la reservation ou sur MyTransavia",
    "Pas d ecran ni de films a bord : telecharger films, series et musique avant de partir",
    "Prises USB-A et USB-C : installation progressive, pas sur tous les avions et parfois coupees, donc prendre une batterie chargee",
    "Boissons et repas payants a bord : prevoir de quoi manger pour plus de 6 heures",
    "La cabine est souvent fraiche : un pull ou une veste dans le bagage a main"]}
for _t in ("Vol Transavia TO3232 Orly vers Sal", "Vol Transavia TO3233 Sal vers Orly"):
    if _t in INFO and _B738 not in INFO[_t].setdefault("logistique", []):
        INFO[_t]["logistique"].append(_B738)
# duree de vol et decalage horaire (Cap-Vert UTC-1, Paris UTC+1 en novembre : 2 heures de moins a Sal)
_VOLT = {"Vol Transavia TO3232 Orly vers Sal": ["Duree du vol : 6h15 sans escale",
            "Depart 06h30 heure de Paris, arrivee 10h45 heure de Sal (12h45 a Paris)",
            "Decalage horaire : MOINS 2 HEURES a Sal. On recule sa montre de 2 heures en arrivant : quand il est midi a Paris, il est 10h00 a Sal",
            "Les telephones se mettent a l heure seuls a l atterrissage ; penser a la montre"],
         "Vol Transavia TO3233 Sal vers Orly": ["Duree du vol : 5h50 sans escale (les vents portent au retour)",
            "Depart 11h40 heure de Sal (13h40 a Paris), arrivee 19h30 heure de Paris",
            "Decalage horaire : PLUS 2 HEURES en rentrant. On avance sa montre de 2 heures : quand il est 10h00 a Sal, il est midi a Paris"]}
for _t, _l in _VOLT.items():
    if _t in INFO:
        _lg = INFO[_t].setdefault("logistique", [])
        if not any(b.get("titre") == "Duree et decalage horaire" for b in _lg):
            _lg.insert(0, {"titre": "Duree et decalage horaire", "lignes": _l})
# le vol retour avait la meme fiche que l aller : fiche propre au retour pour la duree et le decalage
import copy as _copy
if INFO.get("Vol Transavia TO3233 Sal vers Orly") is INFO.get("Vol Transavia TO3232 Orly vers Sal"):
    INFO["Vol Transavia TO3233 Sal vers Orly"] = _copy.deepcopy(INFO["Vol Transavia TO3232 Orly vers Sal"])
for _b in INFO["Vol Transavia TO3233 Sal vers Orly"]["logistique"]:
    if _b.get("titre") == "Duree et decalage horaire":
        _b["lignes"] = _VOLT["Vol Transavia TO3233 Sal vers Orly"]
for _t in ("Vol Transavia TO3232 Orly vers Sal", "Vol Transavia TO3233 Sal vers Orly"):
    INFO[_t] = _copy.deepcopy(INFO[_t])
    for _b in INFO[_t]["logistique"]:
        if _b.get("titre") == "Duree et decalage horaire":
            _b["lignes"] = list(_VOLT[_t])
# jour du depart (France) : peage aller environ 25 EUR partage entre les 2 couples, par carte
if DAYS[0]["brief"][0].startswith("💳") is False:
    DAYS[0]["brief"].insert(0, "💳 ~13 € / couple")

# ---- Bar Marley : mercredi 18, de 16h00 a 19h05, entre la sieste et Il Gobbo (valide par Samuel le 09/11)
_MD = next(d for d in DAYS if d["date"] == "MER 18 NOV")
_MK = "https://www.google.com/maps/search/?api=1&query=Bar+Marley+Santa+Maria+Sal&query_place_id=ChIJs-lF4MBdSwkRoXC349BeoDo"
_W1, _W2, _W3, _WC = "Taxi vers le Bar Marley", "Coucher de soleil au Bar Marley", "Retour du Bar Marley vers Il Gobbo", "Appeler un taxi pour le Bar Marley"
_new = [
    ev("15h30", _WC, "Mercredi 18 novembre, depart 16h00 du logement vers le Bar Marley, retour a 19h05 vers Il Gobbo", "transport"),
    ev("16h00", _W1, "Le taxi passe nous prendre au logement. Annoncer Bar Marley, sur la plage devant l hotel Melia Tortuga, au nord de Ponta Preta. Environ 10 minutes. Le retour de 19h05 est demande dans le meme message : le reconfirmer au chauffeur en descendant. Especes uniquement.", "transport", "~7 €/taxi"),
    ev("16h15", _W2, "Bar de plage reggae sur la cote ouest, devant le Melia Tortuga : DJ, cocktails, poulet jerk au barbecue, et le coucher de soleil dans l océan vers 17h55. Le mercredi soir, il y a un spectacle de feu et beaucoup de monde : en arrivant a 16h15, on a le temps de prendre une bonne table en bord de plage. Juste des verres, le diner est chez Il Gobbo. Cocktails assez chers pour Sal (autour de 14 EUR l Aperol Spritz d apres un avis). Ouvert de 12h00 a minuit, ferme le dimanche.", "show"),
    ev("19h05", _W3, "Le meme chauffeur revient nous chercher a 19h05, comme convenu a l aller, et nous depose directement chez Il Gobbo, Rua 15 de Agosto, dans la rue du logement, pour 19h30. Tarif de nuit, especes uniquement. Plan B : le bar appelle un taxi.", "transport", "~7 €/taxi"),
]
for _e in reversed(_new):
    _i = next(n for n, x in enumerate(_MD["events"]) if x["title"] == "Diner chez Il Gobbo")
    _MD["events"].insert(_i, _e)
CALL_CARDS[_WC] = (_W1, "15h30", "Depart 16h00 du logement, 4 personnes, retour a 19h05 vers Il Gobbo",
    "{oi}\nNous sommes 4 personnes au logement, Rua 15 de Agosto 108 a Santa Maria.\nNous avons besoin d un taxi a 16h00 pour le Bar Marley, sur la plage devant l hotel Melia Tortuga.\nPuis d un retour a 19h05 vers le restaurant Il Gobbo, Rua 15 de Agosto a Santa Maria.\nEtes-vous disponible ?\nSi oui, quel est le prix pour l aller et le retour ?" + _SIGN,
    "Hello!\nWe are 4 people at Rua 15 de Agosto 108, Santa Maria.\nWe need a taxi at 16:00 to Bar Marley, on the beach in front of Melia Tortuga hotel.\nThen a ride back at 19:05 to Il Gobbo restaurant, Rua 15 de Agosto, Santa Maria.\nAre you available?\nIf so, how much for both rides?" + _SIGN_EN)
CALL_IDS[_WC] = "call_marley"
TAXI_ROUTES[_W1] = (_LOGT, "Bar Marley, plage devant le Melia Tortuga", "Environ 10 minutes", _WC)
TAXI_ROUTES[_W3] = ("Bar Marley, plage devant le Melia Tortuga", "Restaurant Il Gobbo, Rua 15 de Agosto", "Environ 10 minutes, meme chauffeur qu a l aller", _WC)
_ix = next(n for n, t in enumerate(TODO_ITEMS) if t["id"] == "call_ponta")
TODO_ITEMS.insert(_ix, {"id": "call_marley", "group": "ady", "due": "2026-11-18", "rt": "15:30", "evd": "2026-11-18", "color": "#C8573F",
    "name": _WC, "sub": "Mercredi 18 novembre, depart 16h00 du logement vers le Bar Marley, retour a 19h05 vers Il Gobbo", "go": [_MD["id"], _WC]})
INFO[_W2] = {"title": "Bar Marley - coucher de soleil",
    "intro": "Bar de plage reggae sur la cote ouest, devant l hotel Melia Tortuga, au nord de Ponta Preta. DJ, cocktails, poulet jerk au barbecue, vue sur le coucher de soleil dans l océan. 4,1/5 sur pres de 300 avis Google.",
    "conseil": "Le mercredi soir, spectacle de feu et beaucoup de monde : arriver tot pour avoir une table en bord de plage. Cocktails assez chers pour Sal. Moyen de paiement non precise dans les avis : prendre des especes en plus de la carte.",
    "logistique": [{"titre": "Pratique", "lignes": ["Plage devant le Melia Tortuga, au nord de Ponta Preta", "Ouvert de 12h00 a minuit, ferme le dimanche", "Coucher de soleil vers 17h55", "Environ 10 minutes de taxi depuis le logement"]}],
    "mapsUrl": _MK, "mapsLabel": "Bar Marley sur Maps"}
INFO[_W1] = INFO[_W2]; INFO[_W3] = INFO[_W2]
for _t in (_W1, _W2):
    MAPS_URLS[_t] = _MK
    if _t not in MAPS_ALWAYS: MAPS_ALWAYS.append(_t)
MAPS_URLS[_W3] = q("Il Gobbo Santa Maria Sal Cabo Verde")
PAY.update({_W1: "especes", _W2: "verifier", _W3: "especes"})
DEPLACEMENT.update({_W1: ("voiture", "En taxi depuis le logement, environ 10 minutes"), _W2: ("pied", "Depose par le taxi devant le bar"),
                    _W3: ("voiture", "En taxi, environ 10 minutes, avec le chauffeur de l aller")})
ICON[_W2] = "\U0001F379"
for _e in _MD["events"]:
    if _e["title"] == "Sieste et plage":
        _e["body"] = _e["body"].replace("Apres-midi sans programme : sieste au logement", "Sieste au logement")
        _e["body"] += " Depart pour le Bar Marley a 16h00."
_MD["brief"] = ["💶 ~25 € / couple", "💳 ~250 € / couple"] + _MD["brief"][2:]
_MD["tip"] = _MD["tip"].replace("especes ~15 EUR (pourboire equipage), carte ~207 EUR (catamaran déjà payé sur Viator, Cam’s ~16 €, LobStar ~90 €, Il Gobbo ~100 €)",
    "especes ~25 EUR (pourboire equipage, taxis du Bar Marley), carte ~250 EUR (catamaran déjà payé sur Viator, Cam’s ~16 €, LobStar ~90 €, verres au Bar Marley ~40 €, Il Gobbo ~100 €)")
for _r in BUDGET["days"]:
    if _r[0] == "Mer 18":
        _r[1], _r[2], _r[3] = 25, 250, "Pourboire et taxis du Bar Marley (especes), Cam s, LobStar, verres au Bar Marley, Il Gobbo (carte) - catamaran deja paye sur Viator"
_TD = next(d for d in DAYS if d["date"] == "MAR 17 NOV")
_TD["note"] = _TD["note"].replace("Diner reserve chez Il Gobbo a 19h30.", "Apres la sieste, coucher de soleil au Bar Marley de 16h00 a 19h05, puis diner reserve chez Il Gobbo a 19h30.")
_MD["events"].sort(key=lambda e: _hk(e["time"]))
# Bar Marley : photo de Samuel + video TikTok
INFO[_W2]["image"] = "bar-marley.jpg"
INFO[_W2]["video"] = "https://vm.tiktok.com/ZN8fTqR8L/"

# ---- logement : immeuble LUX, pres du Columbus (info de l hote, 12/11)
_A0 = "Rua 15 de Agosto 108"
_AFR = "Rua 15 de Agosto 108, immeuble LUX (pres du Columbus)"
_AEN = "Rua 15 de Agosto 108, LUX building (near Columbus)"
def _fix(o):
    if isinstance(o, str):
        return o.replace(_A0, _AFR) if _A0 in o and "LUX" not in o else o
    if isinstance(o, list):
        return [_fix(x) for x in o]
    if isinstance(o, tuple):
        return tuple(_fix(x) for x in o)
    if isinstance(o, dict):
        return {k: _fix(v) for k, v in o.items()}
    return o
for _d in DAYS:
    for _k in list(_d.keys()):
        if _k != "events":
            _d[_k] = _fix(_d[_k])
    for _e in _d["events"]:
        _e["body"] = _fix(_e["body"])
for _k in list(INFO.keys()):
    INFO[_k] = _fix(INFO[_k])
for _k in list(CALL_CARDS.keys()):
    _t, _h, _s, _fr, _en = CALL_CARDS[_k]
    CALL_CARDS[_k] = (_t, _h, _fix(_s), _fr.replace(_A0, _AFR), _en.replace(_A0, _AEN))
for _k in list(TAXI_ROUTES.keys()):
    TAXI_ROUTES[_k] = _fix(TAXI_ROUTES[_k])
    TAXI_ROUTES[_k] = tuple(x.replace("Logement, Rua 15 de Agosto", "Logement, immeuble LUX, Rua 15 de Agosto") if isinstance(x, str) and "LUX" not in x else x for x in TAXI_ROUTES[_k])
RESAS[:] = _fix(RESAS); CHK_ITEMS[:] = _fix(CHK_ITEMS); ESSENTIALS[:] = _fix(ESSENTIALS)
for _k in list(RESA_DETAILS.keys()):
    RESA_DETAILS[_k] = _fix(RESA_DETAILS[_k])
for _k in ("Airbnb Sal Sol & Mar", "Check-in Airbnb Sal Sol & Mar"):
    if _k in INFO and "LUX" not in INFO[_k]["intro"]:
        INFO[_k] = dict(INFO[_k])
        INFO[_k]["intro"] = INFO[_k]["intro"].replace("dans un immeuble recent", "dans l immeuble LUX, recent,") + " Pour le chauffeur : immeuble LUX, Rua 15 de Agosto, tout pres du Columbus."

# ---- bagages : a laisser a la réception de l immeuble LUX (consigne du proprietaire, 12/11)
_BAG_OLD = [
    ("L hote est d accord pour garder les bagages au logement a 12h15, avant le check-in. On pose les valises et on part dejeuner les mains libres.",
     "Consigne de Sol & Mar, le propriétaire : les bagages se laissent à la réception de l immeuble LUX, a 12h15, avant le check-in. On pose les valises a l accueil et on part dejeuner les mains libres."),
    ("Bagages deja deposes a 12h15 avec l accord de l hote.", "Bagages déjà laissés à la réception de l immeuble a 12h15."),
    ("Les valises sont deposees au logement a 12h15", "Les valises sont laissées à la réception de l immeuble LUX a 12h15"),
    ("Les valises sont deja deposees au logement.", "Les valises sont déjà à la réception de l immeuble."),
    ("les valises sont deja au logement", "les valises attendent à la réception de l immeuble"),
]
def _bag(o):
    if isinstance(o, str):
        for a, b in _BAG_OLD:
            o = o.replace(a, b)
        return o
    if isinstance(o, list): return [_bag(x) for x in o]
    if isinstance(o, tuple): return tuple(_bag(x) for x in o)
    if isinstance(o, dict): return {k: _bag(v) for k, v in o.items()}
    return o
for _d in DAYS:
    for _k in list(_d.keys()):
        if _k != "events": _d[_k] = _bag(_d[_k])
    for _e in _d["events"]: _e["body"] = _bag(_e["body"])
for _k in list(INFO.keys()): INFO[_k] = _bag(INFO[_k])
for _k in list(DEPLACEMENT.keys()): DEPLACEMENT[_k] = _bag(DEPLACEMENT[_k])
DEPLACEMENT["Depot des bagages au logement"] = ("aucun", "Réception de l immeuble LUX, Rua 15 de Agosto 108")

# ---- cartes d embarquement aller (enregistrement fait le 13/11)
_SIEGES = "Cedric 9A, Virginie 9B, Samuel 10A, Francoise 10B"
for _d in DAYS:
    for _e in _d["events"]:
        if _e["title"] == "Embarquement" and _e["time"] == "06h00":
            _e["time"] = "05h45"
            _e["body"] = ("Embarquement a 05h45, zone 3. La porte est fermée à 06h10 : après, plus personne ne monte. "
                          "La porte n est pas encore indiquee sur les cartes : la lire sur les ecrans en sortant du controle des passeports. "
                          "Sieges : " + _SIEGES + " (hublot pour Cedric et Samuel). Cartes d embarquement sur les telephones, ref K6UNPB.")
        if _e["title"] == "Vol Transavia TO3232 Orly vers Sal":
            _e["body"] = _e["body"].replace("Ref compagnie K6UNPB.", "Ref compagnie K6UNPB, enregistrement fait le 13/11. Sieges : " + _SIEGES + ".")
    if "Enregistrement en ligne Transavia ouvert 30h avant le vol, soit le vendredi 13/11 a 00h30." in _d.get("tip", ""):
        _d["tip"] = _d["tip"].replace("Enregistrement en ligne Transavia ouvert 30h avant le vol, soit le vendredi 13/11 a 00h30.",
            "Enregistrement fait le 13/11 : embarquement 05h45, porte fermee a 06h10, sieges " + _SIEGES + ".")
    _d["events"].sort(key=lambda e: _hk(e["time"]))
_T3I = INFO["Arrivee aeroport Orly T3 - Depot bagages"]
_T3I["logistique"][0]["lignes"] = [l for l in _T3I["logistique"][0]["lignes"] if not l.startswith("06h00 environ")]
_i = [k for k, l in enumerate(_T3I["logistique"][0]["lignes"]) if l.startswith("06h30")][0]
_T3I["logistique"][0]["lignes"][_i:_i] = ["05h45 : embarquement, zone 3 (porte sur les ecrans)", "06h10 : fermeture de la porte"]
TODO_ITEMS[:] = [t for t in TODO_ITEMS if t.get("id") != "checkin"]
RESA_VIEW["vols"]["line"] = "Aller 06h30 Orly · embarquement 05h45 · retour 21/11 11h40"
RESA_VIEW["vols"]["st"] = "Enregistré"
RESA_DETAILS["vols"]["info"] += " - ALLER ENREGISTRE le 13/11 : embarquement 05h45, porte fermee 06h10, zone 3 - sieges " + _SIEGES + " - bagage cabine non inclus (petit sac sous le siege seulement)"
INFO["Vol Transavia TO3232 Orly vers Sal"].setdefault("logistique", []).insert(0, {"titre": "Cartes d embarquement", "lignes": [
    "Enregistrement fait le 13/11, ref K6UNPB",
    "Embarquement 05h45, zone 3, porte fermee a 06h10",
    "Cedric 9A et Virginie 9B, Samuel 10A et Francoise 10B",
    "Bagage cabine non inclus : un petit sac sous le siege par personne (40 x 30 x 20 cm)",
]})
