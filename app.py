import streamlit as st

st.set_page_config(page_title="WH40k Rules", layout="wide")
st.title("⚔️ Warhammer 40k - Assistant Règles")
st.markdown("**Tout le contenu est copié mot pour mot**")

regles = {
    "commandement": """Phase de Commandement
1. Début de la phase

* Résolvez toutes les règles qui se déclenchent au début de la phase de Commandement.

2. Gain des Points de Commandement (PC)

* Chaque joueur gagne 1 PC.

3. Jets d'Ébranlement
Le joueur actif effectue un jet d'ébranlement pour chaque unité qui :

* est déjà ébranlée, ou

* est à demi-effectif ou moins.

Résultat :

* Si une unité était ébranlée et réussit son jet, elle n'est plus ébranlée.

* Sinon, appliquez les effets normaux de l'ébranlement.

4. Aptitudes et règles de Commandement

* Résolvez toutes les autres règles qui se déclenchent pendant la phase de Commandement.

* N'incluez pas :

  * les règles du début de phase ;

  * les règles de fin de phase ;

  * le gain des PC ;

  * les jets d'ébranlement.

5. Fin de la phase
Résolvez les règles de fin de phase dans cet ordre :

1. Toutes les règles de fin de phase hors mission.

2. Les règles liées aux missions, si leurs conditions sont remplies.""",

    "mouvement": """Phase de Mouvement
1. Début de la phase

* Résolvez toutes les règles qui se déclenchent au début de la phase de Mouvement.

2. Déplacer les unités
Déplacez vos unités une par une jusqu'à ce que toutes aient été choisies.
Pour chaque unité :
Étape A : Choisir une unité
Vous pouvez choisir une unité :

* sur le champ de bataille ;

* en réserve stratégique ;

* embarquée dans un transport.

Étape B : Choisir un type de mouvement
Choisissez un mouvement autorisé :
Type
Condition principale
Rester immobile
Toujours possible
Mouvement normal
Unité non engagée
Avance
Unité non engagée
Retraite
Unité engagée
Débarquement
Depuis un transport
Arrivée
Depuis les réserves
Types de mouvement
Rester immobile
Distance : 0"
✅ Toutes les unités
Effets :

* Aucune figurine ne bouge.

* Ne déclenche pas les règles liées au début ou à la fin d'un mouvement.

Mouvement normal
Distance maximale : M
✅ Unité sur le champ de bataille et non engagée.
Effets :

* Déplacement normal selon les règles de mouvement.

* À la fin du mouvement, l'unité doit rester non engagée.

Mouvement d'Avance
Distance maximale : M + D6
✅ Unité sur le champ de bataille et non engagée.
Avant le mouvement :

* Lancez 1D6 pour déterminer la distance d'Avance.

Après le mouvement :

* L'unité doit être non engagée.

* Jusqu'à la fin du tour :

  * ❌ ne peut pas déclarer de charge ;

  * ❌ ne peut pas effectuer d'action ;

  * sauf règle spéciale contraire.

Mouvement de Retraite
Distance maximale : M
✅ Unité engagée.
Choisir le mode de retraite
Retraite en Bon Ordre
Conditions :

* l'unité n'est pas ébranlée.

Fuite Désespérée
Obligatoire si :

* l'unité est ébranlée.

Avant de bouger :

* Effectuez un jet de risque pour chaque figurine.

Pendant le mouvement :

* Les figurines peuvent traverser les figurines ennemies.

Après le mouvement :

* L'unité doit être non engagée.

* Jusqu'à la fin du tour :

  * ❌ ne peut pas tirer ;

  * ❌ ne peut pas charger ;

  * ❌ ne peut pas effectuer d'action.

Fuite Désespérée :

* Si l'unité n'est plus ébranlée après sa retraite, effectuez un jet d'ébranlement.""",

    "tir": """Phase de Tir
1. Début de la phase

* Résolvez toutes les règles qui se déclenchent au début de la phase de Tir.

2. Tirer avec les unités
Une unité est éligible pour tirer si :

* elle est sur le champ de bataille ;

* elle n'a pas déjà tiré durant cette phase.

Pour chaque unité :
Étape A : Choisir une unité
Sélectionnez une unité éligible.
Étape B : Choisir un type de tir
Choisissez l'un des types suivants :
Type de tir
Conditions
Tir normal
Non engagée, n'a pas avancé
Tir d'assaut
Non engagée, a avancé, possède une arme [ASSAUT]
Tir en combat rapproché
Engagée, n'a pas avancé
Tir indirect
Non engagée, n'a pas avancé, possède une arme [TIR INDIRECT]
Types de tir
Tir normal
Conditions
✅ Unité non engagée
✅ N'a pas effectué d'Avance ce tour
Effet

* Tire normalement selon les règles d'attaque.

Après avoir tiré

* ❌ Ne peut plus entreprendre d'action ce tour.

Tir d'Assaut
Conditions
✅ Unité non engagée
✅ A effectué une Avance ce tour
✅ Possède au moins une arme [ASSAUT]
Effet

* Tire normalement.

Restrictions

* Seules les armes [ASSAUT] peuvent être utilisées.

Après avoir tiré

* ❌ Ne peut plus entreprendre d'action ce tour.

Tir en Combat Rapproché
Conditions
✅ Unité engagée
✅ N'a pas effectué d'Avance ce tour
✅ Possède une arme [COMBAT RAPPROCHÉ] ou est un MONSTRE/VÉHICULE
Effet

* Peut tirer sur les unités avec lesquelles elle est engagée.

Cas des figurines ordinaires

* Utilisent uniquement des armes [COMBAT RAPPROCHÉ].

* Peuvent uniquement viser les ennemis engagés avec elles.

Cas des MONSTRES/VÉHICULES

* Peuvent utiliser leurs autres armes.

* Subissent -1 pour toucher sauf si :

  * l'arme est [COMBAT RAPPROCHÉ] ;

  * et vise une unité engagée.

⚠️ Les armes [DÉFLAGRATION] ne peuvent jamais cibler une unité engagée avec le tireur.
Après avoir tiré

* ❌ Ne peut plus entreprendre d'action ce tour.

Tir Indirect
Conditions
✅ Unité non engagée
✅ N'a pas effectué d'Avance ce tour
✅ Possède une arme [TIR INDIRECT]
Effet

* Peut tirer sur des cibles non visibles.

Restrictions des armes [TIR INDIRECT]
La cible :

* bénéficie toujours du couvert.

Le tireur :

* ❌ ne peut pas relancer ses jets de touche.

Jets pour toucher
Cas normal

* Seuls les résultats non modifiés de 6 touchent.

* Les résultats de 1 à 5 échouent automatiquement.

Si :

* l'unité est restée immobile ce tour ;

* ET la cible est visible par au moins une unité amie ;

alors :

* les résultats de 4 à 6 touchent normalement ;

* seuls les résultats de 1 à 3 échouent automatiquement.

Après avoir tiré

* ❌ Ne peut plus entreprendre d'action ce tour.

3. Fin de la phase

* Résolvez toutes les règles qui se déclenchent à la fin de la phase de Tir.""",

    "charge": """Phase de Charge
1. Début de la phase

* Résolvez toutes les règles qui se déclenchent au début de la phase de Charge.

2. Charger avec les unités
Résolvez les charges une unité à la fois.
Étape A : Déclarer une charge
Choisissez une unité éligible.
Une unité peut déclarer une charge si elle :
✅ est sur le champ de bataille ;
et notamment :
✅ a au moins une unité ennemie à 12" ou moins ;
❌ n'est pas engagée ;
❌ n'a pas effectué d'Avance ce tour ;
❌ n'a pas effectué de Retraite ce tour.
Étape B : Effectuer le jet de charge

* Lancez 2D6.

* Le résultat correspond à la distance maximale de charge.

Étape C : Tenter la charge
Si un mouvement de charge est possible :

* effectuez le mouvement de charge.

Sinon :

* la charge échoue ;

* l'unité ne se déplace pas.

Dans les deux cas, la charge est considérée comme résolue.
Mouvement de Charge
Distance maximale
2D6 (résultat du jet de charge)
Avant le mouvement
Choisissez une ou plusieurs unités ennemies :

* à 12" ou moins ;

* atteignables avec votre distance de charge.

Ces unités deviennent les cibles de charge.
Pendant le mouvement
Chaque figurine doit respecter les priorités suivantes :

1. Finir plus près d'au moins une cible de charge.

2. Si possible, finir à 1" ou moins d'une cible de charge.

3. Si possible, finir engagée avec une cible de charge.

Après le mouvement
L'unité doit :
✅ être engagée avec toutes les cibles de charge déclarées ;
✅ ne pas être engagée avec une unité qui n'était pas une cible de charge.
Bonus de la charge
Jusqu'à la fin du tour :
⚔️ Toutes les figurines de l'unité gagnent Combat en Premier.
3. Fin de la phase

* Résolvez toutes les règles qui se déclenchent à la fin de la phase de Charge.""",

    "combat": """Phase de Combat
1. Début de la phase

* Résolvez toutes les règles qui se déclenchent au début de la phase de Combat.

2. Insertion (Pile In)
Avant de combattre, les deux joueurs peuvent effectuer des mouvements d'insertion.
Ordre

1. Joueur actif.

2. Puis son adversaire.

Distance
? Jusqu'à 3"
Unité éligible si :

* elle est engagée ;

* ou elle a chargé ce tour ;

* ou elle effectuera un combat de débordement.

Mouvement d'insertion
Si l'unité est engagée

* Les cibles sont toutes les unités ennemies avec lesquelles elle est engagée.

Si elle n'est pas engagée

* Choisissez une ou plusieurs unités ennemies à 5" ou moins.

Restrictions

* Les figurines déjà en contact socle à socle ne bougent pas.

* Chaque figurine déplacée doit finir :

  * plus proche de la cible la plus proche ;

  * engagée avec elle si possible.

Après le mouvement

* L'unité doit être engagée.

* Une figurine déjà engagée avec un ennemi doit le rester.

3. Combattre
Une unité est éligible si :
✅ elle est engagée (ou l'était au début de cette étape)
OU
✅ elle a chargé ce tour.
Ordre des combats
Étape A : unités avec Combat en Premier
Le joueur actif commence.
Les joueurs alternent ensuite :

1. Choisir une unité avec Combat en Premier.

2. Résoudre son combat.

Quand il n'y a plus d'unités avec Combat en Premier :
➡️ Passez aux combats normaux.
Étape B : combats restants
Le joueur qui a fait la transition commence.
Les joueurs alternent :

1. Choisir une unité éligible.

2. Résoudre son combat.

Si une nouvelle unité gagne Combat en Premier, retour immédiat à l'étape précédente.
Types de combat
Combat normal
Condition
✅ Unité engagée.
Effet

* Combat normalement selon les règles d'attaque.

Combat de débordement
Condition
✅ Unité non engagée
OU
✅ Était non engagée au début de l'étape mais est devenue engagée pendant la phase.
Effet

1. Effectue une insertion supplémentaire de 3".

2. Combat normalement.

4. Consolidation
Après tous les combats :
Ordre

1. Joueur actif.

2. Puis adversaire.

Distance
? Jusqu'à 3"
Éligible si

* l'unité était éligible pour combattre durant cette phase.

Modes de consolidation
A. Consolidation Continue
Utilisée si

* l'unité est encore engagée.

Effet

* Les figurines en contact socle à socle ne bougent pas.

* Les autres se rapprochent au maximum de l'ennemi le plus proche.

Après le mouvement

* Toute figurine engagée avec un ennemi doit le rester.

B. Consolidation d'Engagement
Utilisée si

* l'unité n'est plus engagée ;

* mais est à 3" ou moins d'un ennemi.

Effet

* Chaque figurine doit se rapprocher de l'ennemi choisi.

* Si possible, finir engagée.

Après le mouvement

* L'unité doit être engagée avec toutes les cibles choisies.

⚠️ Si vous engagez une unité ennemie qui n'a pas encore combattu :

* votre adversaire doit immédiatement la choisir pour combattre.

C. Consolidation sur Objectif
Utilisée si

* aucun ennemi à portée ;

* mais un objectif est à 3" ou moins.

Effet

* Se rapprocher de l'objectif choisi.

* Finir à portée si possible.

Après le mouvement

* L'unité doit être à portée de cet objectif.

5. Fin de la phase

* Résolvez toutes les règles qui se déclenchent à la fin de la phase de Combat.""",

    "terrain": """Terrain & Objectifs

1. Les catégories de terrain
Terrain Exposé
Exemples :

* Cratères

* Barbelés

* Débris

Effets :

* Peu de protection.

* Aucune gêne au déplacement.

Terrain Léger
Exemples :

* Barricades

* Murs bas

* Statues

Effets :

* Peut fournir du couvert.

* Ne bloque pas significativement les mouvements.

Terrain Dense
Exemples :

* Ruines

* Bâtiments

* Bois

* Conteneurs

Effets :

* Bloque davantage les mouvements.

* Affecte fortement la visibilité.

* Possède la règle Plein.

2. Déplacement dans le terrain
Terrain Exposé ou Léger
✅ Toutes les figurines peuvent traverser librement.
Terrain Dense
INFANTERIE / BÊTES / NUÉES / MOBILE
✅ Peuvent traverser horizontalement.
INFANTERIE / BÊTES / NUÉES
✅ Peuvent aussi traverser verticalement.
Autres unités (véhicules, etc.)

* Peuvent traverser seulement si la section traversée fait 2" ou moins de haut.

* Sinon :

  * doivent monter puis redescendre normalement ;

  * ne peuvent pas traverser planchers ou plafonds ;

  * ne peuvent pas terminer leur mouvement sur un étage.

3. Mouvement vertical
Lorsqu'une figurine monte ou descend :

* Elle doit rester à ½" horizontalement du décor.

* Toute montée et descente compte dans la distance parcourue.

Exemple
Monter 3" + avancer 4" + descendre 3"
➡️ Mouvement total = 10"

4. Finir un mouvement sur un décor
Toujours autorisé
✅ Niveau du sol.
Autorisé sur un étage si :

* INFANTERIE

* BÊTE

* NUÉE

* VOL

* MONSTRE

ET

* le socle est entièrement stable ;

* aucune partie du socle ne dépasse.

5. Visibilité et couvert
Bénéfice du Couvert
Une unité obtient le couvert si :
Cas 1
Toutes ses figurines sont :

* INFANTERIE/BÊTES/NUÉES

* ET dans une zone de terrain.

Cas 2
Les figurines ne sont pas entièrement visibles à cause :

* d'un élément de terrain ;

* ou d'une zone occultante.

Effet
? L'attaquant subit :
CT -1
Caché
Une figurine est cachée si :
✅ INFANTERIE/BÊTE/NUÉE
ET
✅ Dans une zone contenant du terrain dense
ET
✅ N'a pas tiré ce tour ni au tour précédent.
Effet
Elle n'est visible qu'à :
? 15" ou moins
(c'est sa portée de détection)
Terrain Occultant
Les zones contenant :

* du terrain léger

* ou dense

sont occultantes.
Effet
Si toutes les lignes de vue passent par une ou plusieurs zones occultantes intermédiaires :
? Les figurines ne se voient pas.
Exception :

* la zone dans laquelle se trouve le tireur ;

* la zone dans laquelle se trouve la cible.

Règle Plein
Tous les terrains denses sont Pleins.
Effet
? Impossible de voir à travers :

* portes ;

* fenêtres ;

* ouvertures ;

situées à 3" ou moins du sol.
6. Objectifs
Portée d'un objectif
Une figurine est à portée d'un objectif si :
✅ elle est dans la zone de terrain de cet objectif.
Niveau de Contrôle (CO)
À chaque fin de phase et fin de tour :
Additionnez les caractéristiques CO de toutes vos figurines à portée.
Résultat

* Plus haut total = contrôle l'objectif.

* Égalité = personne ne contrôle.

Contrôler un objectif
Une unité contrôle un objectif si :

* elle est à portée ;

* elle contient au moins une figurine avec CO ≥ 1 ;

* son joueur contrôle cet objectif.

7. Objectifs sécurisés
Certaines règles permettent de sécuriser un objectif.
Effet
Vous continuez à contrôler l'objectif même sans figurine dessus.
Vous ne le perdez que si :
➡️ à la fin d'une phase,
le niveau de contrôle adverse devient supérieur au vôtre.""",

    "stratagemes": """Stratagèmes
Règles générales
Les stratagèmes coûtent des Points de Commandement (PC) et peuvent être utilisés pendant la bataille.
Chaque stratagème précise :

* ? Cible

* ⏰ Quand

* ⚙️ Effet

* ? Restrictions

* ? Coût en PC

Limites d'utilisation
Même stratagème
❌ Pas plus d'une fois par phase et par joueur.
Même unité
❌ Une unité ne peut généralement recevoir qu'un seul stratagème par phase.
(Sauf indication contraire.)
Séquence d'utilisation

1. Choisir la cible.

2. Dépenser les PC.

3. Résoudre les effets.

Si vous n'avez pas assez de PC :
➡️ impossible d'utiliser le stratagème.
Les Stratagèmes de Base
? Relance de Commandement (1PC)
Quand ?
Après avoir effectué :

* Avance

* Charge

* Dégâts

* Risque

* Touche

* Blessure

* Sauvegarde

* Nombre d'attaques

Effet
Relancez :

* un seul dé du jet ;

ou

* tout le jet de charge (2D6).

À retenir
? Le stratagème le plus universel du jeu.
? Courage Insensé (1PC)
Quand ?
Pendant l'étape d'Ébranlement.
Effet
Le jet d'ébranlement est automatiquement réussi.
Restriction
⚠️ Une seule fois par bataille.
À retenir
? Sauve une unité clé au moment critique.
? Explosifs / Grenades (1PC)
Quand ?
Votre phase de Tir.
Conditions

* Unité non engagée.

* Pas d'Avance.

* Mot-clé EXPLOSIFS ou GRENADES.

Effet

1. Choisir une figurine.

2. Choisir une cible visible à 8".

3. Lancer 6D6.

Chaque 4+ :
? 1 Blessure Mortelle.
Potentiel
Moyenne : environ 3 BM.
? Impact Écrasant (1PC)
Quand ?
Après une charge d'un MONSTRE ou VÉHICULE.
Effet
Lancez un nombre de D6 égal à l'Endurance de la figurine.
Pour chaque :

* 1 → votre unité subit 1 BM.

* 5+ → l'ennemi subit 1 BM.

Maximum :
? 6 BM infligées.
À retenir
? Très fort sur les grosses Endurances.
? Arrivée Précipitée (1PC)
Quand ?
Fin de la phase de Mouvement adverse.
Cible
Une unité en Réserve Stratégique.
Effet
Elle arrive immédiatement sur le champ de bataille.
Restriction
❌ Impossible au round 1.
À retenir
? Permet de surprendre l'adversaire.
? Tir en État d'Alerte (1PC)
Quand ?
Fin de la phase de Mouvement adverse.
Cible
Une unité non engagée.
Effet
Effectue un Tir au Jugé.
Tir au Jugé

* Portée : 24"

* Une seule cible visible

* Les touches réussissent uniquement sur des 6 naturels

* Aucune relance de touche

À retenir
? Excellent contre une unité qui s'approche pour charger.
? Écran de Fumée (1PC)
Quand ?
Début de la phase de Tir adverse.
Cible
Une unité avec le mot-clé FUMÉE.
Effet
Jusqu'à la fin de la phase :

* l'unité bénéficie du couvert ;

* les unités protégées par son écran de fumée également.

À retenir
? Outil défensif très rentable.
⚔️ Défi Épique (1PC)
Quand ?
Après avoir choisi un PERSONNAGE pour combattre.
Effet
Une figurine PERSONNAGE gagne :
? [PRÉCISION]
jusqu'à la fin de la phase.
À retenir
? Permet d'aller chercher les personnages ennemis.
? Intervention Héroïque (1PC)
Quand ?
Fin de la phase de Charge adverse.
Conditions

* Unité non engagée.

* À 12" ou moins d'un ennemi.

Effet
Effectue immédiatement une charge.
Modes
Bondir pour Défendre

* Ne peut charger que des unités ayant chargé ce tour.

Dans la Mêlée

* Distance maximale de charge limitée à 6".

* Peut charger n'importe quel ennemi à 6".

À retenir
? Permet de punir un mauvais placement adverse.
⚡ Contre-Offensive (2PC)
Quand ?
Pendant la phase de Combat adverse.
Après qu'une unité ennemie ait terminé ses attaques.
Cible
Une unité amie éligible pour combattre.
Effet

* Gagne Combat en Premier.

* Doit être la prochaine unité à combattre.""",

    "actions": """Actions
Qu'est-ce qu'une action ?
Certaines missions, règles ou capacités demandent à une unité d'effectuer une Action.
Chaque action indique :

* ⏰ Quand elle peut être entreprise

* ? Quelles unités peuvent la faire

* ? Combien de fois elle peut être utilisée

* ✅ Quand elle est accomplie

* ⚙️ Son effet

Conditions pour entreprendre une action
Une unité peut effectuer une action si elle remplit toutes les conditions suivantes :
✅ Sur le champ de bataille
✅ N'est pas ébranlée
✅ A une caractéristique CO ≥ 1
✅ N'est pas engagée(sauf unité TITANESQUE)
✅ N'a pas fait d'Avance ce tour
✅ N'a pas fait de Retraite ce tour
✅ N'a pas déjà effectué une autre action ce tour
Unités qui ne peuvent jamais effectuer d'actions
❌ AÉRODYNES
❌ FORTIFICATIONS
❌ Unités avec CO 0 ou "-"
Conséquences d'une action
Dès qu'une unité entreprend une action :
Jusqu'à la fin du tour :
❌ Ne peut pas tirer
(sauf TITANESQUE)
❌ Ne peut pas déclarer de charge
Comment réussir une action ?
Une fois l'action commencée :
L'action échoue si l'unité :
❌ Effectue un mouvement

* Mouvement normal

* Avance

* Retraite

* Charge

* Débarquement

* Arrivée

❌ Quitte le champ de bataille
L'action continue si l'unité effectue seulement :
✅ Mouvement d'insertion (Pile In)
✅ Mouvement de consolidation
Accomplir une action
Si l'unité est toujours éligible au moment indiqué par l'action :
✅ L'action est accomplie.
➡️ Appliquez alors l'effet décrit par l'action.""",

    "transports": """Transports
1. Capacité de Transport
Chaque TRANSPORT possède une capacité de transport indiquée sur sa fiche.
Cette capacité précise :

* quelles unités peuvent embarquer ;

* combien de figurines peuvent être transportées.

Important
✅ Plusieurs unités peuvent embarquer dans le même transport.
✅ Une unité peut commencer la partie embarquée.
⚠️ Le transport doit avoir assez de places pour toute l'unité.
2. Embarquer
Une unité peut embarquer après :

* un Mouvement Normal ;

* une Avance ;

* une Retraite.

Conditions
✅ Toutes les figurines sont à 3" ou moins du transport.
✅ L'unité n'a pas été placée sur le champ de bataille ce tour.
✅ Le transport peut accueillir cette unité.
✅ Il reste assez de capacité.
Effet

* Retirez l'unité du champ de bataille.

* Placez-la de côté.

* Elle est désormais embarquée.

3. Débarquer
Pendant votre phase de Mouvement, une unité embarquée peut débarquer.
Les 3 types de débarquement
Type
Distance
Risque
Charge possible ?
Rapide
3"
Non
❌
Tactique
3"
Non
✅
Combat
6"
Oui
❌
? Débarquement Rapide
Obligatoire si :
Le transport a effectué :

* un Mouvement Normal ;

* ou une Arrivée.

Placement
Chaque figurine est placée à 3" ou moins.
Après
❌ Pas de charge ce tour.
? Débarquement Tactique
Obligatoire si :
Le transport :

* est resté immobile ;

* ou n'a pas encore été activé.

Placement
Chaque figurine est placée à 3" ou moins.
Bonus
Après le débarquement :
✅ l'unité effectue immédiatement :

* un Mouvement Normal

ou

* une Avance.

? Débarquement de Combat
Utilisé lorsque :
Ni Rapide ni Tactique ne sont possibles.
Avant
Effectuez un jet de risque pour chaque figurine.
Placement
Chaque figurine est placée à 6" ou moins.
Les figurines peuvent être placées engagées avec des ennemis déjà engagés avec le transport.
Après
⚠️ L'unité devient Ébranlée.
❌ Pas de charge ce tour.
4. Transport détruit
Lorsqu'un transport est détruit :
Toutes les unités embarquées doivent effectuer un :
Débarquement d'Urgence
Avant
Effectuez un jet de risque pour chaque figurine.
Placement
Placez chaque figurine :

* à 6" ou moins du transport ;

* aussi près que possible.

Toute figurine impossible à placer :
? est détruite.
Après
⚠️ L'unité devient Ébranlée.
❌ Ne peut pas charger ce tour.""",

    "attachees": """Unités Attachées (Meneurs & Appuis)
1. Qu'est-ce qu'une unité attachée ?
Certaines unités possèdent les aptitudes :

* ? Meneur

* ? Appui

Avant la bataille, elles peuvent rejoindre une unité de Gardes du Corps.
L'ensemble forme une :
Unité Attachée
➡️ Elle est considérée comme une seule unité pour presque toutes les règles du jeu.
2. Formation d'une unité attachée
Lors de la création de l'armée :
Meneur
Peut rejoindre une unité de gardes du corps autorisée.
Appui
Peut également rejoindre une unité de gardes du corps autorisée.
Limite habituelle
Une unité de gardes du corps peut recevoir :
✅ 1 Meneur
✅ 1 Appui
Maximum.
(Sauf règle spéciale.)
Exemple
Escouade d'Intercessors :

* 5 Gardes du Corps

* 1 Capitaine (Meneur)

* 1 Apothicaire (Appui)

➡️ Les 7 figurines forment une seule Unité Attachée.
3. Quand l'unité est attaquée
Endurance utilisée
Tant qu'il reste au moins un garde du corps :
? utilisez toujours l'Endurance (E) des Gardes du Corps.
Même si le Meneur est plus résistant.
Exemple
Escouade :

* Gardes du Corps E4

* Capitaine E5

Tant qu'un garde du corps est vivant :
➡️ les attaques blessent sur E4.
Quand tous les gardes du corps sont morts :
➡️ on utilise alors E5.
4. Quand l'unité est détruite
Une unité attachée n'est considérée comme détruite que lorsque :
? la dernière figurine ayant commencé la partie dans cette unité est détruite.
5. Mots-clés
Une unité attachée possède :
Tous les mots-clés de toutes ses composantes
Exemple
Gardes du Corps :

* INFANTERIE

Meneur :

* INFANTERIE

* PERSONNAGE

L'unité attachée devient :
✅ INFANTERIE
✅ PERSONNAGE
Important
Les figurines ne gagnent pas individuellement les mots-clés.
Seule l'unité les possède.
6. Aptitudes dans une unité attachée
Aptitudes du Meneur ou de l'Appui
Elles affectent toute l'unité attachée.
Elles restent actives jusqu'à ce que :
? la dernière figurine du Meneur/Appui soit détruite.
Aptitudes des Gardes du Corps
Elles fonctionnent tant qu'il reste au moins un garde du corps.
Lorsque le dernier garde du corps meurt :
➡️ ces aptitudes disparaissent.
Aptitudes liées à une figurine précise
Exemples :

* Optimisation

* Relique

* Équipement spécial

Elles restent actives jusqu'à la destruction de cette figurine.
Cas particulier : mort pendant une attaque
Si une figurine qui fournit une aptitude est détruite au milieu d'une séquence d'attaques :
⚠️ son aptitude continue de s'appliquer jusqu'à la fin de toutes les attaques de l'unité attaquante.
Puis elle disparaît.""",

    "reserves": """Réserves & mouvements spéciaux
1. Réserve stratégique
Avant la bataille
Vous pouvez mettre des unités en réserve stratégique :

* au lieu de les déployer ;

* en les mettant de côté.

Limite
❌ Maximum : 50% des points de l’armée
(inclut les unités dans des transports en réserve)
Exceptions

* ❌ Fortifications ne peuvent pas être mises en réserve.

Important
Une unité en réserve :
➡️ n’est pas sur le champ de bataille
➡️ arrive plus tard
2. Unités repositionnées
Certaines règles permettent de :

* retirer une unité du champ de bataille

* la remettre en réserve

Règles importantes

* Une unité peut être retirée même après avoir bougé (si autorisé).

* Elle conserve les effets déjà appliqués.

Attention
Si elle avait déjà :

* avancé

* reculé

* débarqué

➡️ ces effets comptent toujours.
3. Arrivée des réserves
Les unités en réserve arrivent via un :
Mouvement d’arrivée
Conditions générales

* À partir du tour 2 (sauf exception)

* Unité en réserve stratégique

Placement
? Jusqu’à 6" du bord de table
ET
❌ à plus de 8" des unités ennemies
Restrictions
Avant le tour 3 :
❌ pas dans la zone de déploiement adverse
Après arrivée
❌ pas d'autres mouvements jusqu’à la prochaine phase de charge
Fin de partie
À la fin du tour 3 :
? toute unité en réserve non arrivée est détruite
(sauf exceptions : transports ou unités repositionnées)
4. Mouvement d'élan
Conditions
Une unité peut faire un mouvement d'élan si :

* une règle le permet

* elle n'est pas ébranlée

* elle n'est pas engagée

* elle ne s'est pas déjà déplacée à cette phase

Effet

* Se déplace vers la cible d'élan la plus proche

* Doit essayer de finir engagée avec elle

Restrictions après mouvement
❌ ne peut pas être engagée avec d'autres unités
❌ ne peut plus bouger ce tour
5. Figurines VOLANTES
Les unités avec le mot-clé VOL peuvent voler.
Lors d’un mouvement (normal, avance, retraite, charge)
Le joueur peut choisir de :
? Décoller
Effets du vol

* Distance de mouvement : -2"

* Ignore totalement la verticale

* Peut traverser :

  * figurines ennemies

  * véhicules

  * monstres

* Peut traverser tous les terrains (horizontal + vertical)""",

    "aerodynes": """AÉRODYNES
1. Déploiement
Obligation
Au début de la partie :
✈️ Toutes les unités AÉRODYNE doivent être placées en :
➡️ Réserve stratégique
2. Mouvement
Restrictions majeures
❌ Les AÉRODYNES ne peuvent pas :

* faire de mouvement normal

* avancer

* retraiter

* charger

✔️ Elles ne peuvent faire que :
➡️ Mouvement d’arrivée
Sortie du champ de bataille
À la fin du tour adverse :
✈️ Toute unité AÉRODYNE sur la table retourne en réserve stratégique
Interaction avec les autres unités
Traversée
✔️ Toutes les unités peuvent se déplacer à travers les AÉRODYNES.
Insertion / consolidation / élan

* Les AÉRODYNES sont ignorées pour :

  * choisir la cible la plus proche

  * déterminer les ennemis

⚠️ sauf si l’unité peut VOLER.
Engagement
Être engagé uniquement avec des AÉRODYNES :
➡️ n’empêche pas de bouger normalement
3. Tir
Règle spéciale
? La règle Tir plongeant n’a aucun effet sur :

* les AÉRODYNES qui tirent

* ou qui sont ciblées

4. Charge et combat
Restrictions générales
❌ Les AÉRODYNES ne peuvent pas déclarer de charge.
Qui peut les cibler ?
Pour charger
✔️ Seules les unités VOLANTES peuvent charger des AÉRODYNES.
Au corps à corps
✔️ Seules les unités VOLANTES peuvent :

* leur infliger des attaques de mêlée

* les cibler au combat"""
}

# ====================== APP ======================
phase = st.selectbox("Choisis une phase :", list(regles.keys()))

if phase:
    st.header(phase.capitalize())
    st.markdown(regles[phase])

st.caption("Assistant complet Warhammer 40k - Prêt pour mobile")
