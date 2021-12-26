# Luke 14 - Reinsdyr på villspor
```
Fire av Julenissens favorittreinsdyr ble sluppet løs fra basen på Svalbard i går. Heldigvis er det sporing på reinsdyrene, så en av alvene i NPST har funnet en datamaskin og lastet ned sporingsdataen. Han klarer dessverre ikke å finne ut hvordan man får tak i GPS-filene.

Kan du hjelpe han?

Nb: Hvis du skulle finne noe mistenkelig i dataen, så rapporter tilbake med hva du fant, omkranset av PST{ og }.

Mvh Mellomleder

📎 sporing.zip
```

---

## Løsning

Med litt kreativ editering av Rudolf-tegningen, med mye justering av exposure, hue og saturation så åpenbarer det seg noen tall og bokstaver. Dette er nøkkelen for å pakke ut zip-filen med GPS data.

Denne GPS dataen laster lastet opp i [Google My Maps](mymaps.google.com). Da får vi opp ruten til reinsdyrene, men banen ser litt merkelig ut. Det er noen tagger/hopp i ruten. Dette viser seg å være morse kode, som kan dekodes.

![Skjermbilde](./skjermbilde.png)
![Skjermbilde](./skjermbilde_2.png)

Flagg: `pst{runforestrun}`