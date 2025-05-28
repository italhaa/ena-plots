#fig7.py
import matplotlib.pyplot as plt
import numpy as np
from utils import *

lvrt_x = ()


lvrt_points = np.array([
    [min_plot_time, 0.9], [0, 0.9], [0, 0.3], [0.15, 0.3], [0.15, 0.5],
    [2, 0.85], [20, 0.85], [20, 0.9], [max_plot_time, 0.9]
])
hvrt_points = np.array([
    [min_plot_time, 1.1], [0, 1.1], [0, 1.2], [2, 1.2],
    [2, 1.1], [max_plot_time, 1.1]
])





# === Plot Setup ===
fig, ax = plt.subplots(figsize=(10, 6))
lvrt_x, lvrt_y = get_transformed_curve(lvrt_points)
hvrt_x, hvrt_y = get_transformed_curve(hvrt_points)

# === Area A: Normal Operation Band ===
ax.axhspan(0.9, 1.1, color='teal', alpha=0.2, zorder=0)
ax.text(
    transform_time([min_plot_time, max_plot_time]).mean(), 1.0,
    "Continuous Operating Range\nArea A",
    color='black', fontsize=12, fontweight='bold',
    ha='center', va='center', zorder=1
)

# === Plot Curves ===
for x, y in [(lvrt_x, lvrt_y), (hvrt_x, hvrt_y)]:
    ax.plot(x, y, color='black', linewidth=2.5, zorder=5)

# === Drop Lines ===
draw_guidelines(ax, np.concatenate([lvrt_x[1:-1], hvrt_x[1:-1]]),
                   np.concatenate([lvrt_y[1:-1], hvrt_y[1:-1]]))

# === Area D: Above HVRT ===
lvrt_y_interp = np.interp(hvrt_x, lvrt_x, lvrt_y)
mask_d = hvrt_y > 1.1
if np.any(mask_d):
    fill_between_curves(
        ax,
        hvrt_x[mask_d],
        np.maximum(lvrt_y_interp[mask_d], 1.1),
        hvrt_y[mask_d],
        color='red',
        label='Area D'
    )

# === Area B: Below LVRT ===
hvrt_y_interp = np.interp(lvrt_x, hvrt_x, hvrt_y)
mask_b = lvrt_y < 0.9
if np.any(mask_b):
    fill_between_curves(
        ax,
        lvrt_x[mask_b],
        lvrt_y[mask_b],
        np.minimum(hvrt_y_interp[mask_b], 0.9),
        color='blue',
        label='Area B',
        text_offset=(-1, 0.125)
    )

# === Manual Labels ===
ax.text(3, 0.7, "Area C", color='black', fontsize=12, fontweight='bold',
        ha='center', va='center', zorder=2)
ax.text(5, 1, "0.9 < Un < 1.1", color='black', fontsize=12, fontweight='bold',
        ha='center', va='center', zorder=2)



ax.annotate(
    '',
    xy=(transform_time(25), 1.1),
    xytext=(4.9, 1.03),
    arrowprops=dict(
        arrowstyle='->',
        color='black',
        lw=2,
        shrinkA=0,
        shrinkB=0
    ),
    zorder=10
)

ax.annotate(
    '',
    xy=(transform_time(25), 0.9),
    xytext=(4.9, 0.97),
    arrowprops=dict(
        arrowstyle='->',
        color='black',
        lw=2,
        shrinkA=0,
        shrinkB=0
    ),
    zorder=10
)

# === Axes Setup ===
ax.set_xlabel('Time [sec]', fontsize=12)
ax.set_ylabel('Voltage (U) at Generator Terminal [p.u.]', fontsize=12)
ax.set_xlim(transform_time([min_plot_time, max_plot_time]))
ax.set_ylim(min_plot_voltage, max_plot_voltage)
ax.grid(axis='x')

# X Ticks
x_tick_times = np.array([0, 0.15, 1, 2, 10, 20])
ax.set_xticks(transform_time(x_tick_times))
ax.set_xticklabels([f"{t:g}" for t in x_tick_times])

# Y Ticks
y_tick_values = np.sort(np.append(np.arange(0, 1.21, 0.1), 0.85))
ax.set_yticks(y_tick_values)    
ax.set_yticklabels([f"{v:.2g}" f    or v in y_tick_values])



# Aesthetic Cleanup
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['left', 'bottom']:
    ax.spines[spine].set_linewidth(1.0)

fig.patch.set_linewidth(2)
fig.patch.set_edgecolor('black')



plt.tight_layout()

plt.savefig("fig7.png", dpi=800, bbox_inches='tight')
