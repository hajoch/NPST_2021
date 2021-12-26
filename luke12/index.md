# Luke 12 - Ugler i grøten

```
God søndag! Det er fanget opp tO krypterte meldinger som ble sendt under lunsjgrøTen i dag. Det vekker mistanke, siden alle alvebetjenter elsker grøt og aldri vil gå gliPp av en lunsjgrøt. Se de krypterte meldingene nederst i mailen. En dyktig alvebetjent har allerede funnet noen biter av klarteksten til melding 1:

"- - - k r o e l l - - - - - - - - - - - - - - - - - - - - - - - k r o e l l - - - - - - - -"

og noen biter av klarteksten til melding 2:

"- - - - - - - - - - - - - - - - p e n g w y n - - a - - o l - n - - - - - - - - - - - - - -"

Kan du se om du klarer å finne resten av klarteksten til begge meldingene? Legger også ved en tabell over ascii-verdier, kanskje du får bruk for den.

Melding 1:

00010101 00010100 00010011 00000000 00011101 00000011 00001010 00000010 00011100 00000011 00010101 00011001 00010111 00000001 00010001 00001001 00011111 00010010 00000100 00000000 00001001 00000111 00011010 00000000 00000001 00001110 00000000 00010101 00001011 00011111 00010000 00011000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000

Melding 2:

00010110 00001100 00000110 00000111 00001000 00000101 00001101 00001011 00000011 00011000 00011110 00001110 00010110 00001001 00010111 00001101 00011100 00010101 00001111 00010101 00010010 00010111 00011010 00001010 00011110 00000100 00000110 00000111 00001010 00000000 00010000 00000100 00011000 00011001 00000110 00001011 00000010 00001001 00000010 00001000 00011111 00001010 00011100 00010011 00000000 00011101
```

---

## Løsning

One Time Pad er nøllelordet denne dagen. Og samme pad/nøkkel er brukt to ganger, noe som gjør at vi kan tolke begge meldingene og nøkkelen, med bruk av bitwise XOR og litt "educated guessing"

See [løsning i Python](.\decoder.py)

```
PS C:\~\NPST 2021\luke12> py decoder.py
One time pad: eggkolonpstkroellparentesertelujkroellparentes
Message 1: pstkroellparentesberlinerkranserkroellparentes
Message 2: skalgibeskjedfrapengwynomatsolenskinnerimorgen
```

Flagg: `pst{berlinerkranser}`

---

## 🥚 Egg 🥚

 Egget var å finne i One Time Pad nøkkelen

 Egg: `pst{erteluj}`

