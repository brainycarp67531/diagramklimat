# Diagramklimat — CO₂e Visualiseringsverktyg

## Översikt

Detta Python-program används för att skapa diagram från CSV-filer som innehåller jämförelser och besparingar i CO₂e-utsläpp. Programmet stödjer tre typer av diagram:

- **energi** — stapeldiagram för besparing kopplad till energiförbrukning
- **material** — stapeldiagram för besparing kopplad till materialval (ny pump vs renoverad pump)
- **livslangd** — linjediagram för livslängdsjämförelse mellan ny och renoverad pump över tid

Programmet läser in CSV-filer, skapar diagram (PNG) och flyttar därefter de bearbetade filerna till en arkivmapp. Alla sökvägar hämtas från en gemensam **`config.json`**-fil.

---

## Beroenden

Installera nödvändiga Python-paket:

```bash
pip install pandas matplotlib
```

**Krav:**
- Python 3.9 eller senare
- pandas
- matplotlib

---

## Användning

### Kommandon

Programmet kan köras via huvudfilen `main.py` eller direkt via de specifika skripten:

```bash
# Via main.py (rekommenderat)
python main.py energi <filnamn>
python main.py material <filnamn>
python main.py livslangd <filnamn>

# Direkt via skript
python charts.py energi <filnamn>
python charts.py material <filnamn>
python livslangd.py <filnamn>
```

### Exempel

```bash
python main.py energi 123456
python main.py material pumpdata
python main.py livslangd pumpjamforelse
```

Detta kommer att:
1. Läsa in `<filnamn>.csv` från indata-mappen som anges i `config.json`
2. Skapa ett diagram i utdata-mappen
3. Flytta CSV-filen till arkiv-mappen

---

## Konfiguration

### Struktur för `config.json`

Alla sökvägar styrs via filen `config.json`:

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
  },
  "livslangd": {
    "indata": "data/livslangd/indata",
    "utdata": "data/livslangd/utdata",
    "arkiv": "data/livslangd/arkiv"
  }
}
```

**Obs:** Skapa mapparna enligt denna struktur innan du kör programmet.

---

## CSV-struktur

### För `energi`

Programmet förväntar sig **en rad med minst tre kolumner**:

| Före | Efter | Besparing |
|------|--------|------------|
| 100  | 70     | 30         |

Exempel: `data/energi/indata/eldata.csv`

### För `material`

Programmet förväntar sig **en rad med minst tre kolumner**:

| Ny Pump | Renoverad Pump | Besparing |
|----------|----------------|------------|
| 200      | 150            | 50         |

Exempel: `data/material/indata/pumpdata.csv`

### För `livslangd`

CSV-filen ska innehålla minst tre kolumner:

```csv
Ny Pump, Renoverad Pump, Besparing
150, 120, 30
155, 118, 37
160, 115, 45
165, 110, 55
```

**Obs:** Flera datapunkter kan användas för att visa en tidsserie eller jämförelse över tid.

Exempel: `data/livslangd/indata/pumpjamforelse.csv`

---

## Resultat

Efter körning skapas ett diagram (PNG-bild) i den angivna utdata-mappen och den ursprungliga CSV-filen flyttas till arkivmappen.

### Mappstruktur efter körning

```
data/
├── energi/
│   ├── indata/
│   ├── utdata/
│   │   └── 123456_energi.png
│   └── arkiv/
│       └── 123456.csv
├── material/
│   ├── indata/
│   ├── utdata/
│   │   └── pumpdata_material.png
│   └── arkiv/
│       └── pumpdata.csv
└── livslangd/
    ├── indata/
    ├── utdata/
    │   └── pumpjamforelse_livslangd.png
    └── arkiv/
        └── pumpjamforelse.csv
```

---

## Diagraminformation

### Energi (stapeldiagram)

- **Titel:** Årlig CO₂e-besparing vid energiminskning (t CO₂e/år)
- **Staplar:** *Före*, *Efter*, *Besparing*
- **Färger:** 
  - Mörkgrön (#6F895F) för jämförda värden
  - Ljusgrön (#C4D2C9) för besparing
- **Dimensioner:** 16 cm × 8 cm

### Material (stapeldiagram)

- **Titel:** Materialrelaterad CO₂e-besparing (t CO₂e/år)
- **Staplar:** *Ny Pump*, *Renoverad Pump*, *Besparing*
- **Färger:** 
  - Mörkgrön (#6F895F) för jämförda värden
  - Ljusgrön (#C4D2C9) för besparing
- **Dimensioner:** 16 cm × 8 cm

### Livslängd (linjediagram)

- **Titel:** Livslängd – Ny Pump, Renoverad Pump, Besparing
- **Linjer:**
  - *Ny Pump* — värden för ny pump (vänster Y-axel, mörkgrön #6F895F)
  - *Renoverad Pump* — värden för renoverad pump (vänster Y-axel, mörkare grön #4E5E40)
  - *Besparing* — skillnaden i t CO₂e/år (höger Y-axel, ljusgrön #C4D2C9)
- **Dimensioner:** 32 cm × 8 cm
- **Linjebredd:** 2 pixlar
- **Specialfunktion:** Använder dubbla Y-axlar för att tydligt visa både pumpvärden och besparing

---

## Felhantering

Programmet hanterar vanliga fel som:

- Saknad `config.json`
- Fel i JSON-formatet
- Saknad CSV-fil
- För få kolumner i CSV-filen
- Saknade obligatoriska kolumner i CSV-filen (för livslängd)

I dessa fall skrivs ett tydligt felmeddelande ut i terminalen.

---

## Projektstruktur

```
diagramklimat/
├── main.py              # Huvudingång för programmet
├── charts.py            # Genererar energi- och materialdiagram
├── livslangd.py         # Genererar livslängdsdiagram
├── config.json          # Konfigurationsfil med mappsökvägar
├── README.md            # Denna fil
├── README.txt           # Original README för energi/material
├── livslangd_README.txt # Original README för livslängd
└── data/                # Datamappar enligt config.json
    ├── energi/
    ├── material/
    └── livslangd/
```

---

## Jämförelse mellan diagramtyper

| Diagramtyp | Skript | Diagramformat | Användning |
|------------|--------|---------------|------------|
| **energi** | charts.py | Stapeldiagram | Energibesparing (före/efter jämförelse) |
| **material** | charts.py | Stapeldiagram | Materialbesparing (ny vs renoverad pump) |
| **livslangd** | livslangd.py | Linjediagram | Livslängdsjämförelse över tid |

Alla skript följer samma grundstruktur:
1. Läs konfiguration från `config.json`
2. Läs data från CSV-fil i indata-mappen
3. Generera diagram och spara i utdata-mappen
4. Flytta CSV-filen till arkiv-mappen

---

## Licens och användning

Fritt att använda och anpassa inom ditt projekt. Förbättringar kan enkelt göras genom att justera färger, titlar eller layout i koden.
