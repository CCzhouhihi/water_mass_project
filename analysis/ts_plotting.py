
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as patches
import pandas as pd
import numpy as np

def plot_ts_diagrams_by_depth(T, S, depths, water_masses):
    # Get all available depth levels from the data
    depth_vals = T['depth'].values
    # Find the closest index in the depth for each requested depth
    indices = [np.abs(depth_vals - d).argmin() for d in depths]
    matched_depths = [depth_vals[i] for i in indices]
    # Create subplots
    fig, axes = plt.subplots(2, 3, figsize=(15, 8), sharey=True, constrained_layout=True)
    axes = axes.flatten()
    # Function to draw rectangular boxes for water mass boundaries
    def add_water_mass_boxes(ax, with_label=False):
        for name, wm in water_masses.items():
            rect = patches.Rectangle(
                (wm['Smin'], wm['Tmin']),
                wm['Smax'] - wm['Smin'],
                wm['Tmax'] - wm['Tmin'],
                linewidth=1.2,
                edgecolor=wm['color'],
                facecolor='none',
                label=name if with_label else None   # Only label on first subplot
            )
            ax.add_patch(rect)
    # Loop over each subplot and corresponding depth index
    for i, (ax, idx, depth) in enumerate(zip(axes, indices, matched_depths)):
        T_layer = T.isel(depth=idx)   # Extract 2D data slice at that depth
        S_layer = S.isel(depth=idx)

        T_vals = T_layer.values.flatten()  # Convert data to 1D and remove NaNs
        S_vals = S_layer.values.flatten()
        mask = (~np.isnan(T_vals)) & (~np.isnan(S_vals))
        
        # Create a DataFrame for Seaborn plotting
        df = pd.DataFrame({
            'Temperature': T_vals[mask],
            'Salinity': S_vals[mask]
        })
        
        # Scatter plot of salinity vs temperature
        sns.scatterplot(data=df, x='Salinity', y='Temperature', s=5, alpha=0.5, ax=ax)
            
        ax.set_title(f"{int(depth)} m")
        ax.set_xlim(34.5, 36)
        ax.set_ylim(14, 0)
        ax.invert_yaxis()
        ax.set_xlabel('Salinity')
        if i % 3 == 0:    # Only show ylabel on first column
            ax.set_ylabel('Temperature')
        else:
            ax.set_ylabel('')

        add_water_mass_boxes(ax, with_label=(i == 0))

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.12, 0.95))
    plt.suptitle("T-S Diagrams at Selected Depths", fontsize=16)
    plt.show()
