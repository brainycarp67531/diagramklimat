livslangd.py — Visualisering av livslängd och besparing

Detta Python-skript används för att skapa ett linjediagram (PNG) som visualiserar livslängd för pumpar:  
Ny Pump, Renoverad Pump och Besparing — exempelvis vid jämförelse mellan en ny pump och en renoverad pump.

---

Syfte

- Läsa in livslängdsdata från en CSV-fil.  
- Skapa ett linjediagram som visar livslängd och besparing i ton CO₂e per år.  
- Pumpar (Ny och Renoverad) visas på vänster Y-axel.  
- Besparing visas på höger Y-axel för tydligare jämförelse.  
- Flytta den bearbetade CSV-filen till en arkivmapp.  

---

Struktur

projektmapp/
│
├── livslangd.py
├── config.json
├── data/
│   └── livslangd/
│       ├── indata/
│       │   └── exempel.csv
│       ├── utdata/
│       │   └── (skapade diagram sparas här)
│       └── arkiv/
│           └── (bearbetade CSV-filer flyttas hit)

---

Krav

Programvara
- Python 3.9 eller senare  
- Följande Python-paket:
  pip install pandas matplotlib

(Du kan också installera via en requirements.txt om du vill.)

---

Konfigurationsfil (config.json)

Alla sökvägar styrs via filen config.json:

{
    "livslangd": {
        "indata": "data/livslangd/indata",
        "utdata": "data/livslangd/utdata",
        "arkiv": "data/livslangd/arkiv"
    }
}

- indata: mapp där CSV-filer hämtas från  
- arkiv: mapp dit bearbetade filer flyttas  
- utdata: mapp där PNG-diagram sparas  

---

CSV-struktur

CSV-filen ska innehålla minst tre kolumner som representerar:
1. Ny Pump  
2. Renoverad Pump  
3. Besparing

Exempel (data/livslangd/indata/pumpjamforelse.csv):

Ny Pump, Renoverad Pump, Besparing
150, 120, 30
155, 118, 37
160, 115, 45
165, 110, 55

Obs: Flera datapunkter kan användas för att visa en tidsserie eller jämförelse över tid.

---

Körning

Från terminalen, kör:
python livslangd.py 123456

Skriptet kommer då att:
1. Läsa in data/livslangd/indata/123456.csv
2. Skapa linjediagrammet data/livslangd/utdata/123456_livslangd.png
3. Flytta 123456.csv till data/livslangd/arkiv/

---

Resultat

- Bildfilen (.png) visar tre linjer:
  - Ny Pump – värden för ny pump (vänster Y-axel, mörkgrön färg)  
  - Renoverad Pump – värden för renoverad pump (vänster Y-axel, mörkare grön färg)  
  - Besparing – skillnaden i t CO₂e/år (höger Y-axel, ljusgrön färg)  

Diagrammet använder dubbla Y-axlar för att tydligt visa både pumpvärden och besparing.
Diagrammet sparas automatiskt i den mapp som anges i config.json.

---

Diagraminformation

- Titel: "Livslängd – Ny Pump, Renoverad Pump, Besparing"
- Bredd: 32 cm (omvandlas till inches för Matplotlib)
- Höjd: 8 cm (omvandlas till inches för Matplotlib)
- Linjebredd: 2 pixlar
- Färgschema:
  - Ny Pump: #6F895F (mörkgrön)
  - Renoverad Pump: #4E5E40 (mörkare grön)
  - Besparing: #C4D2C9 (ljusgrön)

---

Felhantering

- Om config.json saknas → visas ett tydligt felmeddelande.  
- Om CSV-filen inte hittas → skriptet avbryts med varning.  
- Om CSV:n saknar någon av de tre obligatoriska kolumnerna → kastas ett ValueError.  

---

Jämförelse med andra skript

- energi.py/charts.py energi – visar energibesparing med stapeldiagram
- material.py/charts.py material – visar materialbesparing med stapeldiagram
- livslangd.py – visar livslängdsjämförelse med linjediagram över tid

Alla skript följer samma grundstruktur men genererar olika typer av diagram.

---
