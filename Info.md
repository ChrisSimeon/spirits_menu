# Aufbau der App

- Die einzelnen Produkte werden nach auswählbaren Kategorien und unterkategorien unterteilt
- Die Kategorien sind wie folgt: Gin, Whisky /Whiskey (unterkategorien: American, Scotch, Andere), Likör (Bitter / Sweet), Shots, Rum, Brände / Heimisches, fort. Weine (unterkat: portwein, wermut, Sherry)
- Das Aroma der einzelnen Spirituosen wird mit Aroma und Geschmackstags beschrieben. Wenn jemand nach Banane sucht, wird als erstes der Geschmack also Likör gefunden, danach Spirituosen, in denen das Aroma angelegt ist.
- Es gibt eine Suchmöglichkeit
- Es gibt das Klassiche Burger Menü, hier lassen sich die einzelnen Spirituosen aussuchen.
- Das Layout ist Mobile-First

## Eigenschaften des Produkt Objekts

- Name
- Kategorie / Unterkategorie
- dict -> Mengenoption1 (2cl / 100ml): Preis
- dict -> Mengenoption2 (4cl / 200ml): Preis
- dict -> Mengenoption3 (Flasche): Preis
- Verfügbarkeit: Verfügbar / gerade aus / nicht mehr gelistet
- Beschreibung
- Tags
-

# Weitere zu etablierende Features

- Auslesen einer CSV mit allen wichtigen Daten
- Admin Bereich zum abändern des jeweiligen Porduktes
- ein Warenkorb für größere Bestellungen, die dann vom Service per QR ausgelesen werden kann.
- Weitere Möglichkeiten für Kombination mit Longdrink / Im Cocktail...
- Suche in einer Kategorie: Suche nach Gin zitrisch

# Models

- Es muss eine Klasse für die Einzelnen Produkte geben
  - die einzelnen Produkte haben einen Foreign Key zu einer Kategorie oder zu einer Subkategorie
- Es muss eine Klasse für die Kategorien geben
  - Kategorien werden von Subkategorien und von Produkten Referiert.
- Es muss eine Klasse für die Subkategorien geben
  - Subkategorien haben einen Foreign Key zu den Kategorien und Sie werden von den Produkten referenziert
