De aanpak van de verschillende algoritmen is duidelijk beschreven in de README.
Het is na lezen van de README duidelijk hoe de resultaten te reproduceren zijn, via een interface (command line), argumenten die meegegeven kunnen worden voor de verschillende functionaliteiten/algoritmen, of bijvoorbeeld een duidelijke uitleg welke file te runnen om welk resultaat te krijgen.

# Rush Hour
##### Anisha Sloeserwij, Julius Kempen en Tjarda Leppers

## De case: Rush Hour
Rush Hour is een spelletje waarbij het doel is om de rode auto van een bepaalde beginpositie op het speelbord naar de uitgang van het bord te verplaatsen.
Dit kun je doen door stap voor stap de voertuigen die in de weg staan om de rode auto te bewegen aan de kant te schuiven waar dit mogelijk is. 
Hierbij staan er een x aantal auto's op het bord en een x aantal vrachtwagens. Hierbij nemen de auto's 2 plekken van het bord in beslag en de vrachtwagens 3.
Het is belangrijk dat de voertuigen alleen zich mogen verplaatsen in de richting dat zij staan gepositioneerd en dat de auto's niet over elkaar heen kunnen staan.

Het oplossen van zo'n puzzel is erg ingewikkeld, doordat er veel mogelijkheden zijn om het bord te verplaatsen.
De grootte van dit probleem hebben we berekend aan de hand van de mogelijke state spaces die er zijn. 
Met behulp van algoritmes en heuristieken proberen we een oplossing te vinden voor elke puzzel. 
Welk algoritme hiervoor het beste is hangt af van verschillende aspecten en zullen in het kopje over de algoritmes toegelicht worden. 

## De algoritmes
In de main.py staan alle algoritmes die zijn geimplementeerd (uitgecommented). Verder staan alle files voor de algoritmes onder het kopje code/algorithms/"naam_algoritme". Voor de werking van de algoritmes hoeft alleen het algoritme uit de comments gehaald te worden en de rest regelt het programma zelf. In de terminal zie je welk algoritme er is gebruikt, wat de lengte van het pad is om naar de oplossing te komen, vervolgens zie je hoeveel states er hierbij zijn afgegaan en hoeveel daarvan uniek zijn. Daarnaast wordt er een csv file gegenereerd waarbij de verplaatsing van de voertuigen ten opzichte van het beginbord staan weergegeven.  

### Het random algoritme - code/algorithms/randomise.py
Als eerste hebben we een random algoritme geimplementeerd die fungeert als baseline voor de oplossing. 
Dit random algoritme werkt volledig random doordat het een random auto uitkiest die bewogen moet worden en daarbij een random move.
Hierbij wordt er nergens rekening mee gehouden om het zo random mogelijk te maken. 
Vervolgens wordt er gecheckt of deze actie mogelijk is, kan auto C wel 1 plek naar rechts bewegen bijvoorbeeld?
Als deze actie mogelijk is, dan wordt dit ook uitgevoerd en wordt er vanaf deze nieuwe staat verdergegaan en het random algoritme herhaaldelijk toegepast.
Zodra de actie niet mogelijk is, bijvoorbeeld wanneer het voertuig door de move van het bord af zou bewegen of tegen een andere auto ingaan, dan wordt er niks veranderd en wordt het random algoritme weer toegepast op dezelfde staat.
Dit gaat net zo lang door totdat er een oplossing is waarbij de rode auto op de plek staat van de uitgang. 

#### Voordelen
Het voordeel van het random algoritme is dat het voor elke puzzel (die op te lossen is) een willekeurige oplossing vindt.
Daarnaast kan het een puzzel in een relatief korte tijd oplossen.

#### Nadelen
De oplossing kan uit wel 80.000 verschillende states bestaan. Dat wil zeggen dat het 80.000 stappen kost om tot een oplossing te komen. 
Het kan zo zijn dat een bepaalde state (positionering van de voertuigen op het bord) heel vaak voorkomt om tot een oplossing te komen, waardoor het bord herhaaldelijk dezelfde stappen zou kunnen nemen. Dit werkt heel onefficient voor de snelste weg naar de uitgang.

### Het breadth first algoritme - code/algorithms/breadth_first.py
Ons tweede algoritme is het breadth first algoritme. 
Bij dit algoritme wordt er in een boom structuur gekeken naar de verschillende states totdat er een oplossing is gevonden. 
Bij deze aanpak wordt er per state gekeken hoeveel mogelijke child-states er mogelijk zijn (hierbij is een child-state steeds een andere state waarbij er 1 voertuig is veranderd ten opzichte van de huidige state (parent state).
Alle staten die hiermee wordt gecreeerd worden opgeslagen in een dictionary, genaamd path_memory.
Dit herhaalt zich net zo lang er een state komt waarbij de rode auto op de eindpositie staat en er een oplossing is gevonden. 
Dan wordt het pad herleidt door te kijken van welke parent state de 'winning' child state afkomstig is.
Dit wordt net zo lang gedaan totdat er geen parent state meer van een child state te vinden is en dit geeft aan dat die state de beginsituatie is. 

#### Voordelen
Het belangrijkste voordeel is dat er altijd de kortste weg naar de uitgang van het bord gevonden wordt als er een oplossing wordt gegeven.
Doordat het per laag in de boomstructuur kijkt naar de mogelijke volgende staten zal de eerste uitkomst ook de snelste route zijn. 

#### Nadelen

### Het depth first algoritme - code/algorithms/depth_frist.py
Ook hebben we het depth first algoritme gebruikt. Deze verschilt qua code niet zo veel met de breadth first algoritme, maar geeft wel een hele andere uitkomst wat interessant kan zijn. Het depth first algoritme wordt ook gestructureerd aan de hand van vertakkingen, maar hierbij wordt er eerst naar de uiterste vertakking gekeken en als daar een oplossing uitkomt is dat ook gelijk de oplossing die depth first geeft.
Dit algoritme zal dus met de begin state beginnen en vanaf hier steeds 1 nieuwe state aanmaken en doorgaan op gelijk deze state tot de winning state is bereikt.

#### Voordelen
Dit algoritme probeert gelijk zo diep mogelijk te graven naar een oplossing zonder alle mogelijkheden eerste per laag te bekijken. 

### Het A* algoritme - code/algorithms/astar.py


### Het best first algoritme - code/algorithms/best_first.py



