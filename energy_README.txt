----------------------------------------
SVENSK VERSION
----------------------------------------

energi.py — Användning och indata­beskrivning

Syfte
- Skapar ett stapeldiagram (PNG) som visar energivärden: "Före", "Efter" och "Besparing".
- Skriptet läser in en CSV-fil och skriver ut energy.png.

Krav
- Python 3
- pandas
- matplotlib
Installation: pip install pandas matplotlib

CSV-struktur (energy.csv)
- Kommaavgränsad fil med rubrikrad och en datarad.
- Obligatoriska kolumner (i denna ordning): Category, Före, Efter, Besparing
- Exempel:
  Category,Före,Efter,Besparing
  Energianvändning,3.25,2.25,1.0

Funktion
- Skriptet läser den första dataraden och förväntar sig minst tre numeriska kolumner efter Category.
- Diagrammet visar:
  - "Före" och "Efter" som två staplar (vänster y-axel).
  - "Besparing" som en tredje stapel (ritad med sekundär y-axel).
- Skriptet lägger till numeriska etiketter ovanpå staplarna.
- Rubriken är fast: "Årlig CO₂e-besparing vid energiminskning (t CO₂e/år)".
- Resultatet sparas som energy.png i samma mapp.

Körning (Windows)
- Från projektmappen:
  python energi.py energi.csv

Utdata
- Filer: energy.png sparas i aktuell mapp.

Noteringar och begränsningar
- Skriptet är avsett för en enda datarad med tre värden. För flera rader eller annan kolumnstruktur behöver koden anpassas.
- Om CSV-filen innehåller färre än tre datakolumner uppstår ett ValueError.
- Kontrollera att rubriknamn inte innehåller extra mellanslag (t.ex. använd "Före", inte " Före").



----------------------------------------
ENGLISH VERSION
----------------------------------------

Purpose
- Generate a bar chart (PNG) that visualizes energy values: "Före", "Efter" and "Besparing".
- The script reads a CSV and writes energy.png.

Requirements
- Python 3
- pandas
- matplotlib
Install: pip install pandas matplotlib

CSV structure (energy.csv)
- Comma-separated file with header and one data row.
- Required columns (in this order): Category, Före, Efter, Besparing
- Example:
  Category,Före,Efter,Besparing
  Energianvändning,3.25,2.25,1.0

Behavior
- The script reads the first data row and expects at least three numeric columns after the Category.
- Plots:
  - "Före" and "Efter" as two bars (left axis).
  - "Besparing" as a third bar (plotted using a secondary y-axis).
- Adds numeric annotations on top of bars.
- Sets a fixed title: "Årlig CO₂e-besparing vid energiminskning (t CO₂e/år)".
- Saves the result as energy.png in the same folder.

How to run (Windows)
- From the repository folder:
  python energi.py energi.csv

Output
- energy.png saved to the current folder.

Notes and limitations
- The script is intended for a single data row with three values. For multiple rows or different column layouts the code must be adapted.
- If the CSV has fewer than 3 data columns, the program raises a ValueError.
- Ensure header names have no extra spaces (e.g. use "Före", not " Före").
