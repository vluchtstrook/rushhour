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

## Vooraf
Dit programma is geschreven in Python en bevat een aantal packages die allereerst geinstalleerd moeten worden op de computer om de code te kunnen runnen. Welke packages er nodig zijn staan beschreven in **requirements.txt** en zijn als volgt te installeren:

```
pip3 install -r requirements.txt
```

Het programma wordt vanuit de **main.py** gedraaid. Vanuit hier wordt het csv bestand ingeladen en worden de gegevens in de juiste vormen opgeslagen. Daarnaast worden hier de algoritmes aangestuurd wanneer deze uit de comments zijn gehaald. Voor de werking van de algoritmes hoeft alleen het algoritme uit de comments gehaald te worden in de main.py en de rest regelt het programma zelf. 

Voor het runnen van een specifieke puzzel moet je in de terminal aangeven de naam van de puzzel die je wilt runnen, dit doe je als volgt:

```
python3 main.py Rushhour6x6_2.csv
```
Wanneer je de naam van het csv bestand weglaat zal het programma automatisch de eerste puzzel pakken. 

In de terminal zie je welk algoritme er is gebruikt, wat de lengte van het pad is om naar de oplossing te komen, vervolgens zie je hoeveel states er hierbij zijn afgegaan en hoeveel daarvan uniek zijn. Daarnaast wordt er een csv file gegenereerd waarbij de verplaatsing van de voertuigen ten opzichte van het beginbord staan weergegeven.  

## De algoritmes

### Het random algoritme - code/algorithms/randomise.py
Als eerste hebben we een random algoritme geimplementeerd die fungeert als baseline voor de oplossing. 
Dit random algoritme werkt volledig random doordat het een random auto uitkiest die bewogen moet worden en daarbij een random move.
Hierbij wordt er nergens rekening mee gehouden om het zo random mogelijk te maken. 
Vervolgens wordt er gecheckt of deze actie mogelijk is, kan auto C wel 1 plek naar rechts bewegen bijvoorbeeld?
Als deze actie mogelijk is, dan wordt dit ook uitgevoerd en wordt er vanaf deze nieuwe staat verdergegaan en het random algoritme herhaaldelijk toegepast.
Zodra de actie niet mogelijk is, bijvoorbeeld wanneer het voertuig door de move van het bord af zou bewegen of tegen een andere auto ingaan, dan wordt er niks veranderd en wordt het random algoritme weer toegepast op dezelfde staat.
Dit gaat net zo lang door totdat er een oplossing is waarbij de rode auto op de plek staat van de uitgang. 

### Het breadth first algoritme - code/algorithms/breadth_first.py
Ons tweede algoritme is het breadth first algoritme. 
Bij dit algoritme wordt er in een boom structuur gekeken naar de verschillende states totdat er een oplossing is gevonden. 
Bij deze aanpak wordt er per state gekeken hoeveel mogelijke child-states er mogelijk zijn (hierbij is een child-state steeds een andere state waarbij er 1 voertuig is veranderd ten opzichte van de huidige state (parent state).
Alle staten die hiermee wordt gecreeerd worden opgeslagen in een dictionary, genaamd path_memory.
Dit herhaalt zich net zo lang er een state komt waarbij de rode auto op de eindpositie staat en er een oplossing is gevonden. 
Dan wordt het pad herleidt door te kijken van welke parent state de 'winning' child state afkomstig is.
Dit wordt net zo lang gedaan totdat er geen parent state meer van een child state te vinden is en dit geeft aan dat die state de beginsituatie is. 

### Het depth first algoritme - code/algorithms/depth_frist.py
Ook hebben we het depth first algoritme gebruikt. Deze verschilt qua code niet zo veel met de breadth first algoritme, maar geeft wel een hele andere uitkomst wat interessant kan zijn. Het depth first algoritme wordt ook gestructureerd aan de hand van vertakkingen, maar hierbij wordt er eerst naar de uiterste vertakking gekeken en als daar een oplossing uitkomt is dat ook gelijk de oplossing die depth first geeft.
Dit algoritme zal dus met de begin state beginnen en vanaf hier steeds 1 nieuwe state aanmaken en doorgaan op gelijk deze state tot de winning state is bereikt.

### Het A* algoritme - code/algorithms/astar.py
Daarnaast hebben we het A* algoritme toegepast die in zekere zin lijkt op het breadth first algoritme, maar met een admissable heiristiek.
Het heuristiek is admissable doordat er nooit een overschatting is want het geeft altijd de minimale aantal stappen dat nog gezet moeten worden vanaf een bepaalde staat tot de winning state. Hierbij wordt er per staat berekent wat de 'kosten' zijn voor die staat om tot de winning state te komen. Deze kosten worden bepaald door het aantal auto's dat tussen de rode auto en de uitgang zitten + de afstand van de rode auto tot de uitgang + aantal voorgaande states. Hierbij is het belangrijk dat de queue de childs op volgorde rangschikt waarbij de child met de laagste kosten als eerste uit de queue wordt gehaald.  

### Het best first algoritme - code/algorithms/best_first.py
Als laatste het best first algoritme die ook op de A* lijkt, maar met net een andere berekening voor de zogenoemde kosten en een extra heuristiek. Deze heuristiek is gebaseerd op de afwijking dat een staat heeft ten opzichte van de gemiddelde winning state (die is berekent).
Voor die berekening wordt er een X aatal keer het random algoritme gedraaid met een winning state. Van deze X keren wordt het gemiddelde winning state bord gecreeerd (welke plek welke auto het meeste voorkwam). Voor de afwijking van een bepaalde state ten opzichte van het gemiddelde winning state worden kosten gerekend. 
Deze is erg snel, maar geeft geen garantie op het vinden van het beste antwoord, doordat het geen rekening houdt met de lengte van het pad en dus een overschatting kan maken. 

## De resultaten
