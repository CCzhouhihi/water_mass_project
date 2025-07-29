
# region_defs.py
# Define ocean regions for analysis
# Add new regions by inputting the lat-lon information

regions = {
    'NorthAtlantic_Subpolar': {
        'name': 'Subpolar North Atlantic',
        'lat_range': (40, 65),
        'lon_range': (-60, -10)
    },
    'NorthPacific_Subpolar': {
        'name': 'Subpolar North Pacific',
        'lat_range': (40, 60),
        'lon_range': (140, 180)
    },
    'NorthAtlantic_Subtropical': {
        'name': 'Subtropical North Atlantic',
        'lat_range': (20, 35),
        'lon_range': (-80, -30)
    },
    'SouthAtlantic': {
        'name': 'South Atlantic',
        'lat_range': (-40, -10),
        'lon_range': (-40, 10)
    }
}
