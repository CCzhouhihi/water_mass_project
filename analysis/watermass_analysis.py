
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr

def build_watermass_dataframe(T, S, water_masses, group_round=100):
    
    # Flatten the temperature and salinity values
    T_vals = T.values.flatten()
    S_vals = S.values.flatten()
    # Extract coordinates
    depth_vals = T['depth'].values
    lat_vals = T['lat'].values
    lon_vals = T['lon'].values
    # Broadcast 3D grids
    D, La, Lo = T['depth'], T['lat'], T['lon']
    D3, La3, Lo3 = xr.broadcast(D, La, Lo)
    D_flat = D3.values.flatten()
    # Create a mask for non-NaN T and S to get valid data points
    mask = (~pd.isnull(T_vals)) & (~pd.isnull(S_vals))
    # Build DataFrame
    df = pd.DataFrame({
        'Temperature': T_vals[mask],
        'Salinity': S_vals[mask],
        'Depth': D_flat[mask]
    })
    # Classify each point into a water mass
    def classify(row):
        for name, wm in water_masses.items():
            if wm['Tmin'] <= row['Temperature'] <= wm['Tmax'] and wm['Smin'] <= row['Salinity'] <= wm['Smax']:
                return name
        return 'Other' # If no match
    # Group depth values (round to nearest)
    df['WaterMass'] = df.apply(classify, axis=1)
    df['DepthGroup'] = (df['Depth'] // group_round * group_round).astype(int)
    return df

def plot_watermass_pie_by_depth(df, water_masses, selected_groups=None):
    # Get the list of depth groups to include in the plot
    if selected_groups is None:
        depth_groups = sorted(df['DepthGroup'].unique())
    else:
        # Only include selected groups that actually exist in the DataFrame
        depth_groups = sorted([g for g in selected_groups if g in df['DepthGroup'].unique()])
    
    n = len(depth_groups)
    ncols = 3
    nrows = (n + ncols - 1) // ncols
    # Create subplots
    fig, axes = plt.subplots(nrows, ncols, figsize=(4 * ncols, 4 * nrows))
    axes = axes.flatten()
    # Plot a pie chart for each depth group
    for i, group in enumerate(depth_groups):
        ax = axes[i]
        subset = df[df['DepthGroup'] == group]
        counts = subset['WaterMass'].value_counts()
        colors = [water_masses.get(k, {'color': 'gray'})['color'] for k in counts.index]

        ax.pie(counts, labels=counts.index, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 8})
        ax.set_title(f"{group} m")

    for j in range(i + 1, len(axes)):  # Turn off unused subplots
        axes[j].axis('off')

    plt.suptitle("Water Mass Composition by Depth Layer", fontsize=16)
    plt.tight_layout()
    plt.show()
