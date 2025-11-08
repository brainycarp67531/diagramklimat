# Diagramgenerator för energi- och materialdata

## Översikt

Detta Python-program används för att skapa stapeldiagram från CSV-filer som innehåller jämförelser och besparingar i CO₂e-utsläpp.  
Programmet kan generera två typer av diagram:

- **energi** – visar besparing kopplad till energiförbrukning  
- **material** – visar besparing kopplad till materialval (ny pump vs renoverad pump)

Programmet läser in en CSV-fil, skapar ett diagram (PNG) och flyttar därefter den bearbetade filen till en arkivmapp.

Alla sökvägar hämtas från en gemensam **`config.json`**-fil.

---

## Användning

### Kommandon

```bash
python charts.py energi filnamn
python charts.py material filnamn
```

### Exempel

```bash
python charts.py energi eldata
python charts.py material pumpdata
```

Detta kommer att:
1. Läsa in `eldata.csv` (eller `pumpdata.csv`) från mappen som anges i `config.json`
2. Skapa ett stapeldiagram i utdata-mappen
3. Flytta CSV-filen till arkiv-mappen

---

## Struktur för `config.json`

```json
{
  "energi": {
    "indata": "data/energi/indata",
    "utdata": "data/energi/utdata",
    "arkiv": "data/energi/arkiv"
  },
  "material": {
    "indata": "data/material/indata",
    "utdata": "data/material/utdata",
    "arkiv": "data/material/arkiv"
  }
}
```

Skapa mapparna enligt denna struktur innan du kör programmet.

---

## Struktur på CSV-filer

Programmet förväntar sig **en rad med minst tre kolumner**.

### För `energi`
| Före | Efter | Besparing |
|------|--------|------------|
| 100  | 70     | 30         |

### För `material`
| Ny Pump | Renoverad Pump | Besparing |
|----------|----------------|------------|
| 200      | 150            | 50         |

Filen ska sparas som till exempel:  
`data/energi/indata/eldataprojekt.csv`

---

## Resultat

Efter körning skapas ett diagram (PNG-bild) i den angivna utdata-mappen och den ursprungliga CSV-filen flyttas till arkivmappen.

Exempel:

```
data/
├── energi/
│   ├── indata/
│   ├── utdata/
│   │   └── eldata_energi.png
│   └── arkiv/
│       └── eldata.csv
└── material/
    ├── indata/
    ├── utdata/
    │   └── pumpdata_material.png
    └── arkiv/
        └── pumpdata.csv
```

---

## Diagraminformation

### Energi
- Titel: **Årlig CO₂e-besparing vid energiminskning (t CO₂e/år)**
- Staplar: *Före*, *Efter*, *Besparing*
- Färg: Mörkgrön för jämförda värden, ljusgrön för besparing

### Material
- Titel: **Materialrelaterad CO₂e-besparing (t CO₂e/år)**
- Staplar: *Ny Pump*, *Renoverad Pump*, *Besparing*
- Färg: Mörkgrön för jämförda värden, ljusgrön för besparing

---

## Beroenden

Installera nödvändiga Python-paket:

```bash
pip install pandas matplotlib
```

---

## Felhantering

Programmet hanterar vanliga fel som:
- Saknad `config.json`
- Fel i JSON-formatet
- Saknad CSV-fil
- För få kolumner i CSV-filen

I dessa fall skrivs ett tydligt felmeddelande ut i terminalen.

---

## Licens och användning

Fritt att använda och anpassa inom ditt projekt.  
Förbättringar kan enkelt göras genom att justera färger, titlar eller layout i koden.
