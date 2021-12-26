# Luke 23 - Sabotasje!
```
Alvene i sledegarasjen rapporterer om at noen har tuklet med julegaveruta som er lagt inn i slede-GPSen. Det er kritisk fordi det ikke er mulig å overstyre sledens GPS-kurs under flyturen. Det har visst blitt lagt til et stopp på Antarktis, rett utenfor SPST sitt hovedkvarter, og jeg (Julenissen) er redd for at SPST planlegger å rappe alle gavene fra sleden på selveste julaften.

I slede-GPS-loggen er det lagt igjen en kort beskjed: "Ikke god jul, hilsen M".

Det er derfor høy prioritet å finne ut hvem "M" er, før "M" klarer å utrette mer ugagn. Mellomleder har skrytt av din innsats denne førjulstiden, så jeg vil derfor betro denne viktige oppgaven til nettopp deg. Jeg personlig har ikke tid, for jeg skal først på gløggsmaking og så skal jeg se Grevinnen og Hovmesteren. Du blir gitt tilgang til kontoret mitt i kveld for å lete gjennom papirer og se om du klarer å finne ut hvem rakkeren er. Navnet rapporteres tilbake til meg (du må selv pakke navnet inn i formatet pst{}).

Dette oppdraget er gradert "Temmelig Hemmelig", så ikke fortell om dine funn til noen andre enn meg personlig.

 📎 Julenissens_kontor.png

Hoho, Julenissen
```

![julenissens kontor](.\Julenissens_kontor%20%E2%80%93%20Kopi.png)

---

## Løsning

Den medfølgende bilde filen er uvanelig stor, og mistanken blir bekreftet av å inspisere bildet nærmere. Det skjuler seg en komprimert mappe i bildet. Ved å endre filtypen til `.zip` kan det skjulte innholdet vises. Der ligger det en [beskjed](./julenissens_kontor/note_to_elf.txt).

```
En alvebetjent kom innom kontoret nettopp, og delte sin hypotese om hvem
som kan stå bak de uheldige hendelsene denne førjulstiden. Jeg skriver det ned
slik at jeg husker det til senere, for nå må jeg straks løpe for å rekke
lunsjgrøten. Alvebetjenten tror at den skyldige har et navn på M, fordi
vedkommende kaller seg for "M". Videre mente alvebetjenten at den skyldige må
være ansatt i NPST, av flere grunner. Først og fremst fordi vedkommende lekket
konfidensiell informasjon om pakkefordelingsruta tidlig i desember. Men også
fordi vedkommende kommuniserte med SPST fra vår stue.

Spørsmålet er da hvorfor en NPST-ansatt vil snu ryggen til julen og samarbeide
med SPST. Alle NPST-ansatte er "snille", og ikke "slemme". Hvis en alv skulle
hoppe over til "slem"-listen, så mister alven umiddelbart alvtorisasjonen og
dermed også jobben. Så hva kan være grunnen til at en "snill" alvebetjent ønsker
å sabotere årets julegavedistribusjon?
Det klarte ingen av oss å svare på.
```

Den inneholder også en PDF med liste over hvem som har fått presanger. Jeg kopierte innholdet til VSCode, og med et raskt søk fant jeg en NPST ansatt som ikke hadde mottatt julegave, vi har vårt motiv. 

```
Navn         Snill   Mottatt gave   Ansatt i NPST
...
Maximilian   Ja      Nei            Ja
...
```
Flagg: `pst{Maximilian}`
