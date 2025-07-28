
# Subpolar North Atlantic Water Mass Analysis

This project analyzes water masses in the subpolar North Atlantic using WOA23 data. It includes:

- T-S diagrams for selected depth layers
- Highlighted known water masses (e.g., LSW, NADW)
- Pie charts showing water mass composition at each depth

## Project Structure

- **`data/`** — Input NetCDF data files (.nc)
  - `woa23_B5C2_t00_04.nc` — Temperature data
  - `woa23_B5C2_s00_04.nc` — Salinity data

- **`analysis/`** — Reusable Python modules
  - `__init__.py` — Module initializer
  - `ts_plotting.py` — Functions for creating temperature-salinity diagrams
  - `watermass_analysis.py` — Water mass classification, statistics, pie chart plotting
  - `region_defs.py` — Latitude/longitude definitions for ocean regions
  - `watermass_defs.py` — Temperature/salinity boundaries for water mass definitions

- **`main_analysis.py`** — Main script to run the full analysis workflow

- **`README.md`** — Project description and usage instructions

## How to Run

1. Put NetCDF files in `data/`
2. Adjust paths in `main_analysis.py`
3. Run the script

```
python main_analysis.py
```
