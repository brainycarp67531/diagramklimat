# energi.py — Visualisering av energibesparing

Detta Python-skript används för att skapa ett **stapeldiagram (PNG)** som visualiserar energivärden:  
**Före**, **Efter** och **Besparing** — exempelvis vid jämförelse mellan en gammal och en ny pump.

---

## Syfte

- Läsa in energidata från en CSV-fil.  
- Skapa ett stapeldiagram som visar energiförändring och besparing i ton CO₂e per år.  
- Flytta den bearbetade CSV-filen till en arkivmapp.  

---

## Struktur

```
projektmapp/
│
├── energi.py
├── config.json
├── indata/
│   └── exempel.csv
├── utdata/
│   └── (skapade diagram sparas här)
└── arkiv/
    └── (bearbetade CSV-filer flyttas hit)
```

---

## Krav

### Programvara
- **Python 3.9** eller senare  
- Följande Python-paket:
  ```bash
  pip install pandas matplotlib
  ```

*(Du kan också installera via en `requirements.txt` om du vill.)*

---

## Konfigurationsfil (`config.json`)

Alla sökvägar styrs via filen `config.json`:

```json
{
    "energi": {
        "indata": "indata/",
        "arkiv": "arkiv/",
        "utdata": "utdata/"
    }
}
```

- **indata**: mapp där CSV-filer hämtas från  
- **arkiv**: mapp dit bearbetade filer flyttas  
- **utdata**: mapp där PNG-diagram sparas  

---

## CSV-struktur

CSV-filen ska innehålla **minst tre kolumner** som representerar:
1. **Före**  
2. **Efter**  
3. **Besparing**

Exempel (`indata/energibesparing.csv`):

```csv
, Före, Efter, Besparing
Energivärden, 150, 100, 50
```

> **Obs:** Endast första raden används för beräkningen.

---

## Körning

Från terminalen, kör:
```bash
python energi.py energibesparing
```

Skriptet kommer då att:
1. Läsa in `indata/energibesparing.csv`
2. Skapa stapeldiagrammet `utdata/energibesparing_energi.png`
3. Flytta `energibesparing.csv` till `arkiv/`

---

## Resultat

- Bildfilen (`.png`) visar tre staplar:
  - **Före** – ursprungligt värde  
  - **Efter** – nytt värde  
  - **Besparing** – skillnaden i t CO₂e/år  

Diagrammet sparas automatiskt i den mapp som anges i `config.json`.

---

## Felhantering

- Om `config.json` saknas → visas ett tydligt felmeddelande.  
- Om CSV-filen inte hittas → skriptet avbryts med varning.  
- Om CSV:n har färre än tre kolumner → kastas ett `ValueError`.  

---

## Tips

- Använd `Path` från `pathlib` för att enkelt ändra sökvägar.
- Anpassa färger och titel i funktionen `generate_bar_chart()` om du vill ändra utseendet.
- Du kan skapa flera diagram genom att lägga in flera CSV-filer i `indata/` och köra kommandot flera gånger.

---

## Licens

Fri att använda och modifiera. Ange gärna källa om du delar vidare.

---
