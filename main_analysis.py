
from analysis.ts_plotting import plot_ts_diagrams_by_depth
from analysis.watermass_analysis import build_watermass_dataframe, plot_watermass_pie_by_depth
from analysis.region_defs import regions
from analysis.watermass_defs import water_masses

import xarray as xr

# ========== 1. Choose region ==========
region = regions['NorthAtlantic_Subpolar']  # Change this key to select a different region

# ========== 2. Load data ==========
temp_path = 'data/woa23_B5C2_t00_04.nc'
sali_path = 'data/woa23_B5C2_s00_04.nc'

ds_temp = xr.open_dataset(temp_path, decode_times=False)
ds_sali = xr.open_dataset(sali_path, decode_times=False)

T = ds_temp['t_an'].sel(lat=slice(*region['lat_range']), lon=slice(*region['lon_range']))
S = ds_sali['s_an'].sel(lat=slice(*region['lat_range']), lon=slice(*region['lon_range']))

# ========== 3. Plot T-S diagrams ==========
depths_to_plot = [0, 200, 700, 1000, 1500, 2000]
plot_ts_diagrams_by_depth(T, S, depths_to_plot, water_masses)

# ========== 4. Build data and plot pie charts ==========
df_all = build_watermass_dataframe(T, S, water_masses, group_round=100)
plot_watermass_pie_by_depth(df_all, water_masses, selected_groups=depths_to_plot)

