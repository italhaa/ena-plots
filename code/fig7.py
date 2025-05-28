# fig7.py
import matplotlib.pyplot as plt
import numpy as np
from vrt_utils import *

lower_range = 0.85

# === LVRT & HVRT Points ===
lvrt_points = np.array([
    [min_plot_time, lower_range], [0, lower_range], [0, 0.3], [0.15, 0.3], [0.15, 0.5],
    [2, lower_range-0.05], [20, lower_range-0.05], [20, lower_range], [max_plot_time, lower_range]
])
hvrt_points = np.array([
    [min_plot_time, 1.1], [0, 1.1], [0, 1.2], [2, 1.2],
    [2, 1.1], [max_plot_time, 1.1]
])

# === Setup Plot ===
fig, ax = setup_plot(lvrt_points, hvrt_points)
lvrt_x, lvrt_y, hvrt_x, hvrt_y = use_transformed_curve(lvrt_points, hvrt_points)

# === Area A: Normal Operation Band ===
addAreaA(ax, lower_range, 1.1)

# === Plot VRT Curves ===
plottingfunc(ax, lvrt_x, lvrt_y, hvrt_x, hvrt_y)

# === Drop Lines ===
guidelinesfunc(ax, lvrt_x, lvrt_y, hvrt_x, hvrt_y)

# === Area D: Above HVRT ===
lvrt_y_interp = np.interp(hvrt_x, lvrt_x, lvrt_y)
mask_d = hvrt_y > 1.1
if np.any(mask_d):
    fill_between_curves(ax, hvrt_x[mask_d], np.maximum(lvrt_y_interp[mask_d], 1.1),
                        hvrt_y[mask_d], color='red', label='Area D')

# === Area B: Below LVRT ===
hvrt_y_interp = np.interp(lvrt_x, hvrt_x, hvrt_y)
mask_b = lvrt_y < lower_range
if np.any(mask_b):
    fill_between_curves(ax, lvrt_x[mask_b], lvrt_y[mask_b],
                        np.minimum(hvrt_y_interp[mask_b], lower_range),
                        color='blue', label='Area B', text_offset=(-1, 0.125))

# === Manual Labels ===
ax.text(3, 0.7, "Area C", color='black', fontsize=12, fontweight='bold',
        ha='center', va='center', zorder=2)


# === Side Arrows ===
addSideArrowLabel(ax, lower_range, 1.1)

# === Final Axes Setup ===
ax.set_xlabel('Time [sec]', fontsize=12)
ax.set_ylabel('Voltage (U) at Generator Terminal [p.u.]', fontsize=12)
ax.set_xlim(transform_time([min_plot_time, max_plot_time]))
ax.set_ylim(min_plot_voltage, max_plot_voltage)
ax.grid(axis='x')

# === Ticks ===
x_tick_times = np.array([0, 0.15, 1, 2, 10, 20])
ax.set_xticks(transform_time(x_tick_times))
ax.set_xticklabels([f"{t:g}" for t in x_tick_times])

y_tick_values = np.sort(np.append(np.arange(0, 1.21, 0.1), 0.85))
ax.set_yticks(y_tick_values)
ax.set_yticklabels([f"{v:.2g}" for v in y_tick_values])

# === Cleanup ===
clean(ax)

plt.tight_layout()
plt.savefig(f"../plots/fig7_0{int(lower_range * 100)}_110.png", dpi=800, bbox_inches='tight')
