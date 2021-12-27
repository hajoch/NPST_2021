# Luke 21 - Mulig Lekkasje

```
NPST's sikkerhetssystemer er satt til øverste beredskap nå som jula nærmer seg, og den ene alvebetjenten oppdaget en melding som noen prøver å skjule. Kan du ta en nærmere titt på denne?

Mvh Mellomleder

📎 brev.txt
```
Link: [brev](.\brev.txt)

---

## Løsning

Når man trykker seg rundt i tekst filen oppdager man fort at her er det tegn som ikke er synlige. Litt inspeksjon viser at det er snakk om `zero width joiner` og `zero width non-joiner`. 

Siden det kun var to "skjulte" tegn som var spredt rundt i dokumentet var det nærliggende å tenke at dette skulle leses som binært.

Dette ble løst i [python](./decoder.py)

```
PS C:\~\NPST 2021\luke21> py .\decoder.py
output file written .. 
_____ DECODED MESSAGE _____ 
Jeg har planen klar!
De har nettopp delt ut oversikt over hvor nissen må stoppe og mate reinsdyrene underveis på ruta.

Her er det muligheter for å ødelegge!
Jeg holder dere oppdatert

-M
PST{ReadingBetweenTheLetters}
```
Flagg: `PST{ReadingBetweenTheLetters}`