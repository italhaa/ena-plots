import matplotlib.pyplot as plt
import numpy as np
from vrt_utils import *

lvrt_points = np.array([
    [min_plot_time, 0.85], [0, 0.85], [0, 0.6], [0.15, 0.6],
    [0.15, 0.8], [0.6, 0.8], [0.6, 0.85], [max_plot_time, 0.85]
])
hvrt_points = np.array([
    [min_plot_time, 1.1], [max_plot_time, 1.1]
])

fig, ax = setup_plot(lvrt_points, hvrt_points)
lvrt_x, lvrt_y, hvrt_x, hvrt_y = use_transformed_curve(lvrt_points, hvrt_points)

ax.axhspan(0.85, 1.1, color='teal', alpha=0.2, zorder=0)
ax.text(transform_time([min_plot_time, max_plot_time]).mean(), 0.975,
        "Continuous Operating Range\nArea A",
        color='black', fontsize=12, fontweight='bold', ha='center', va='center', zorder=1)

plottingfunc(ax, lvrt_x, lvrt_y, hvrt_x, hvrt_y)
guidelinesfunc(ax, lvrt_x, lvrt_y, hvrt_x, hvrt_y)

hvrt_y_interp = np.interp(lvrt_x, hvrt_x, hvrt_y)
mask_b = lvrt_y < 0.85
if np.any(mask_b):
    fill_between_curves(ax, lvrt_x[mask_b], lvrt_y[mask_b],
                        np.minimum(hvrt_y_interp[mask_b], 0.85),
                        color='blue', label='Area B', text_offset=(-0.3, -0.05))

ax.text(3, 0.5, "Area C", color='black', fontsize=12, fontweight='bold',
        ha='center', va='center', zorder=2)

addSideArrowLabel(ax, 0.85, 1.1)

ax.set_xlabel('Time [sec]', fontsize=12)
ax.set_ylabel('Voltage (U) at Generator Terminal [p.u.]', fontsize=12)
ax.set_xlim(transform_time([min_plot_time, max_plot_time]))
ax.set_ylim(min_plot_voltage, max_plot_voltage)
ax.grid(axis='x')

x_tick_times = np.array([0, 0.15, 0.6, 1, 2, 10, 20])
ax.set_xticks(transform_time(x_tick_times))
ax.set_xticklabels([f"{t:g}" for t in x_tick_times])

y_tick_values = np.sort(np.append(np.arange(0, 1.21, 0.1), 0.85))
ax.set_yticks(y_tick_values)
ax.set_yticklabels([f"{v:.2g}" for v in y_tick_values])

clean(ax)
fig.patch.set_linewidth(2)
fig.patch.set_edgecolor('black')
plt.tight_layout()
plt.savefig("../plots/fig5.png", dpi=800, bbox_inches='tight')
