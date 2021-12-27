# Luke 18 - Grønne Firkanter

```
Hei,

Alvdelingen for nettverksoperasjoner har utført en hemmelig nettverksoperasjon mot SPST. De har snublet over et "git repository", men de synes det er noe merksnodig med det. Alv en eller annen grunn så mener Alvdelingen for tekniske undersøkelser at det kan ha noe med "grønne firkanter" å gjøre, hva nå enn det betyr.

Kan du sjekke det ut?

📎groenne-firkanter.zip

Om du trenger hjelp så kunne du kanskje spurt alvdelingen for åpne kilder - de tar sikkert en titt på Github profilen til personen som "comitter" i repoet, kanskje det ligger et hint der.

Mvh

Mellomleder
```

---

## Løsning

Hintet om å ta en titt på github profilen, samt at oppgaven heter "Grønne Firkanter" pekte til at det var aktivitets kalenderen på github oppgaven handlet om.

Løsningsordet vil altså åpenbare seg om vi simulerer en aktivitets-kalender for github brukeren som har commitet the det lokale repo'et som følger med oppgaven.

Decoderen i python leser inn log filen for master branchen, og tegner et bilde av en kalender tilsvarende det som fins på github.

```
PS C:\~\NPST 2021\luke18> py .\decoder.py
image painted. opening image
````
![Løsning](.\output.png)

Flagg: `pst{get_clean_go_green}`
