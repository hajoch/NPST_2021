# Luke 15 - Kameraopptak gir klarhet

```
Etter gårsdagens reinsdyrflukt bestemmer alvebetjent M. Nist seg for å sjekke kameraloggen. Dessverre ser det ut som om det bare eR blått og grØnt støy Der... Klarer du å finne ut noe mer fra opptaket?

Mvh Mellomleder

📎 opptak.gif
```

---

## Løsning

Teksten hinter til "RØD", og om vi bryker Python til å trekke ut kun den røde kanalen i gifen, ser vi det følgende:
![Rød kanal](./red_channel.gif)

Det gjemmer seg åpenbart noe oppe i venstre hjørne.

Skriver en til liten snutt i Python for å klippe ut de første 30x30 pixelene i hver keyframe. Og setter dem sammen så får vi en tall serie. Som minner veldig om tekst i Decimal form:

![Sammensatt bilde](./mosaic.jpg)

Litt vanskelig å se med formatet på bildet med følgende tall blir synlig.

>80 83 84 123 72 101 114 86 97 114 68 101 116 73 107 107 101 77 121 101 197 83 101 71 105 116 116 46 46 46 125

En til enkel pyhton snutt så åpenbarer flagget seg.

Flagg: `PST{HerVarDetIkkeMyeÅSeGitt...}`
