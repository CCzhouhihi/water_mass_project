
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr

def build_watermass_dataframe(T, S, water_masses, group_round=100):
    T_vals = T.values.flatten()
    S_vals = S.values.flatten()

    depth_vals = T['depth'].values
    lat_vals = T['lat'].values
    lon_vals = T['lon'].values
    D, La, Lo = T['depth'], T['lat'], T['lon']
    D3, La3, Lo3 = xr.broadcast(D, La, Lo)
    D_flat = D3.values.flatten()

    mask = (~pd.isnull(T_vals)) & (~pd.isnull(S_vals))

    df = pd.DataFrame({
        'Temperature': T_vals[mask],
        'Salinity': S_vals[mask],
        'Depth': D_flat[mask]
    })

    def classify(row):
        for name, wm in water_masses.items():
            if wm['Tmin'] <= row['Temperature'] <= wm['Tmax'] and wm['Smin'] <= row['Salinity'] <= wm['Smax']:
                return name
        return 'Other'

    df['WaterMass'] = df.apply(classify, axis=1)
    df['DepthGroup'] = (df['Depth'] // group_round * group_round).astype(int)
    return df

def plot_watermass_pie_by_depth(df, water_masses, selected_groups=None):
    if selected_groups is None:
        depth_groups = sorted(df['DepthGroup'].unique())
    else:
        depth_groups = sorted([g for g in selected_groups if g in df['DepthGroup'].unique()])
    
    n = len(depth_groups)
    ncols = 3
    nrows = (n + ncols - 1) // ncols

    fig, axes = plt.subplots(nrows, ncols, figsize=(4 * ncols, 4 * nrows))
    axes = axes.flatten()

    for i, group in enumerate(depth_groups):
        ax = axes[i]
        subset = df[df['DepthGroup'] == group]
        counts = subset['WaterMass'].value_counts()
        colors = [water_masses.get(k, {'color': 'gray'})['color'] for k in counts.index]

        ax.pie(counts, labels=counts.index, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 8})
        ax.set_title(f"{group} m")

    for j in range(i + 1, len(axes)):
        axes[j].axis('off')

    plt.suptitle("Water Mass Composition by Depth Layer", fontsize=16)
    plt.tight_layout()
    plt.show()
