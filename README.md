
# Subpolar North Atlantic Water Mass Analysis

This project analyzes water masses in the subpolar North Atlantic using WOA23 data. It includes:

- T-S diagrams for selected depth layers
- Highlighted known water masses (e.g., LSW, NADW)
- Pie charts showing water mass composition at each depth

## Project Structure

water_mass_project/
│
├── data/                   # Input NetCDF data files (.nc)
│   └── woa23_B5C2_t00_04.nc  # Temperature
│   └── woa23_B5C2_s00_04.nc  # Salinity
│
├── analysis/               # Reusable Python modules
│   ├── __init__.py
│   ├── ts_plotting.py           # Functions to create T-S diagrams
│   ├── watermass_analysis.py   # Classification, statistics, pie plotting
│   ├── region_defs.py           # Lat/lon ranges for ocean regions
│   └── watermass_defs.py        # T/S boundaries for water masses
│
├── main_analysis.py        # Main file to run anything
└── README.md               # Project description 


## How to Run

1. Put NetCDF files in `data/`
2. Adjust paths in `main_analysis.py`
3. Run the script

```
python main_analysis.py
```
