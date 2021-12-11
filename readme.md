# En dashboard för alla lovsånger som vi har i ProPresenter

Just nu så finns det inget sätt att se vilka lovsånger vi har i Propresenter
Även om en fillista är en bra början, så hade det varit trevligt att ha en "dashboard" för allt detta.

Huvudsaklig användare kommer bli lovsångsledare.

## DATAKÄLLOR

- pro6-filer: ger själva lovsångstexten. Bra början
- Playlists ifrån Macen. Eftersom vi inte tar bort gamla körscheman så har vi ju tillgång till dessa

## Filformat

[pro6 är redan reverse-engineerat till plain text här](https://github.com/alexhenrie/pro6-to-txt)

Men det är fortfarande inte konsumerbart... vi behöver fixa med autocomplete o sånt mög.
Och få grejerna till något mer konsumerbart än txt-filer

Kanske något sånt här hade varit trevligt...

```json
[
    {
        "title": "O store Gud",
        "text": "O store Gud, när jag den värld beskådar\n",
    }
]
```

Så kan man tanka ner hela skiten i JS...
Bygg en Vue-js som itererar den json-filen och ha någon enkel sökalgoritm.

Så nu gäller det ju bara att generera statisk HTML för dashboarden.
Sorteringen får komma senare.


```
===========================================
| LOVSÅNGSBANKEN                          |
| Här är en lista på lovsånger som finns! |
===========================================

[  Sök  ]

O store Gud [x]
    O store Gud, när jag den värld beskådar...
```

Sökningen ska highlighta strängen i varje dokument.

# Prioriteringar

Gör interfacet så enkelt som möjligt (för att macen ska slippa göra grejer). Helst ska man bara behöva ladda upp en .tar.gz och sen så sköts allting av pipelinen därifrån.

Input: songs.tgz
Output: songs.json

```
[Gruppera efter söndag]

Söndag V41
===========
Tusen skäl | Jag vill alltid prisa dig |

[Gamla favoriter]

Här är en lista med lovsånger som inte sjungits på ett tag
Men som tidigare har varit populära

Låt oss få se LIVE	2020-05-24 12:41:54+00:00	7

[Alla Lovsånger, sorterade på datum reverse]

playlist_date	songs
song		
Bara Jesus	2019-11-24 09:53:11+00:00	1
Kom med din Ande (Basse)	2019-11-24 09:53:11+00:00	1
Vi dansar	2019-11-24 09:53:11+00:00	1
Hosianna (Hanna) välsignad vare han EJ KOMPLETT	2019-12-01 11:08:07+00:00	1
Hosianna Davids son	2019-12-01 11:08:07+00:00	1
Fader vår (kärlekens väg)	2019-12-01 11:08:07+00:00	1
Det hände sig (Ära vare Gud i höjd)	2019-12-08 14:29:33+00:00	1
Vi tänder ett ljus i advent	2019-12-08 14:29:33+00:00	2
Stilla Natt	2019-12-15 11:29:28+00:00	2
Kärlek vid som oceaner	2019-12-15 11:29:28+00:00	1

```

# Hur mergar vi de två datakällorna

För att kunna göra "dessa spelades i söndags" så använder vi playlists.json:

```json
[
    {
        "playlist_name": "sön 24 nov",
        "playlist_date": "2019-11-24T10:53:11+01:00",
        "songs": ["Herre vi vill ge dig ära"]
    }
]
```

När webbappen itererar sångerna så skriver den ut titeln, och gör en lookup i songs.json efter rätt sång. Det blir mycket snabbare om formen på songs.json är

```json
{
    "herre vi vill ge dig ära": "\n\n Du den högste, du den störste\nDu regerar över jord och himmel\n\nDu som öppnar våra ögon\nSå vi ser den nåd som du vill ge oss\n\n Ingen annan är som du\n\n Herre vi vill ge dig ära\nGe dig all vår lovsång\n\n Älska dig som älskat oss först\n\n Vi vill lyfta våra händer\nFyllda av beundran\n\n Älska dig som älskar oss\n\nDu är sanning, du är livet\nDu är kärleken som övervinner\n\nDu som räddar och befriar\nDu som ger oss hopp för nya dagar\n\n Ingen annan är som du\n\nIngen annan\n\n Bara du är värd vår ära\nBara du är värd vår sång\n\nVi ger Dig all ära"
}
```

typ. Det gör det mindre dynamiskt om man vill utöka songs.json senare dock
Kolla först hur segt det blir

