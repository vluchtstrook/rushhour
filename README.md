README
Voor de README kijken we o.a. naar:

De case waar de studenten mee bezig geweest zijn is duidelijk geïntroduceerd in de README.
De aanpak van de verschillende algoritmen is duidelijk beschreven in de README.
Het is na lezen van de README duidelijk hoe de resultaten te reproduceren zijn, via een interface (command line), argumenten die meegegeven kunnen worden voor de verschillende functionaliteiten/algoritmen, of bijvoorbeeld een duidelijke uitleg welke file te runnen om welk resultaat te krijgen.

# Rush Hour
##### Anisha Sloeserwij, Julius Kempen en Tjarda Leppers

### De case: Rush Hour
Rush Hour is een spelletje waarbij het doel is om de rode auto van een bepaalde beginpositie op het speelbord naar de uitgang van het bord te verplaatsen.
Dit kun je doen door stap voor stap de voertuigen die in de weg staan om de rode auto te bewegen aan de kant te schuiven waar dit mogelijk is. 
Hierbij staan er een x aantal auto's op het bord en een x aantal vrachtwagens. Hierbij nemen de auto's 2 plekken van het bord in beslag en de vrachtwagens 3.
Het is belangrijk dat de voertuigen alleen zich mogen verplaatsen in de richting dat zij staan gepositioneerd en dat de auto's niet over elkaar heen kunnen staan.

Het oplossen van zo'n puzzel is erg ingewikkeld, doordat er veel mogelijkheden zijn om het bord te verplaatsen.
De grootte van dit probleem hebben we berekend aan de hand van de mogelijke state spaces die er zijn. 
Met behulp van algoritmes proberen we een oplossing te vinden voor elke puzzel. 
Welk algoritme hiervoor het beste is hangt af van verschillende aspecten en zullen in het kopje over de algoritmes toegelicht worden. 

### De algoritmes
#### Het random algoritme
Als eerste hebben we een random algoritme geimplementeerd die fungeert als baseline voor de oplossing. 
Dit random algoritme werkt volledig random doordat het een random auto uitkiest die bewogen moet worden en daarbij een random move.
Hierbij wordt er met niks rekening gehouden om het zo random mogelijk te maken. 
Vervolgens wordt er gecheckt of deze actie mogelijk is, kan auto C wel 1 plek naar rechts bewegen bijvoorbeeld?
Als deze actie mogelijk is, dan wordt dit ook uitgevoerd en wordt er vanaf deze nieuwe staat verdergegaan en het random algoritme herhaaldelijk toegepast.
Zodra de actie niet mogelijk is, bijvoorbeeld wanneer het voertuig door de move van het bord af zou bewegen of tegen een andere auto ingaan, dan wordt er niks veranderd en wordt het random algoritme weer toegepast op dezelfde staat.
Dit gaat net zo lang door totdat er een oplossing is waarbij de rode auto op de plek staat van de uitgang. 

##### Voordelen
Het voordeel van het random algoritme is dat het voor elke puzzel (die op te lossen is) een willekeurige oplossing vindt.
Daarnaast kan het een puzzel in een relatief korte tijd oplossen.

##### Nadelen
De oplossing kan uit wel 80.000 verschillende states bestaan. Dat wil zeggen dat het 80.000 stappen kost om tot een oplossing te komen. 
Het kan zo zijn dat een bepaalde state (positionering van de voertuigen op het bord) heel vaak voorkomt om tot een oplossing te komen, waardoor het bord herhaaldelijk dezelfde stappen zou kunnen nemen. Dit werkt heel onefficient voor de snelste weg naar de uitgang.

#### Het breadth first algoritme


## Code

### Algorithms
- init.py
- Random algorithm
- Algorithm 1
- Algorithm 2

### Classes
- init.py
- Grid (with class Grid)
- Vehicle (with class Vehicle)
- Loader
- Rushhour (with class Rushhour)

### Visualisation
- init.py
- visualise

## Data
- Rushhour6x6_1
- Rushhour6x6_2
- etc

## gitignore

## README

## mainfile
