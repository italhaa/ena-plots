#fig2.py

import matplotlib.pyplot as plt

# Create figure (wider than tall for 2:1 aspect)
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the given line
x_points = [-0.8, -0.1, 0.1, 0.3]
y_points = [-1, 0, 0, 1]
ax.plot(x_points, y_points, color='black')

# Set axis limits
xlim = (-1.0, 1.0)
ylim = (-1.5, 1.5)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

# Set ticks
x_ticks = [-1.0, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0]
y_ticks = [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
ax.grid(True)

# Move spines to origin
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# Show left and bottom spine, hide top/right
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['left', 'bottom']:
    ax.spines[spine].set_linewidth(1.0)
    ax.spines[spine].set_visible(True)

# Set custom aspect ratio: 1 x-unit = 2 y-units
ax.set_aspect(1/2)

# Hide default x and y tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# Draw only the x-tick labels below the x-axis spine (no tick marks)
for xtick in x_ticks:
    ax.text(
        xtick, ylim[0] - 0.1,
        f"{xtick:.1f}",
        ha='center',
        va='top',
        fontsize=10
    )

# Draw only the y-tick labels left of y-axis spine (no tick marks)
for ytick in y_ticks:
    ax.text(
        xlim[0] - 0.08, ytick,
        f"{ytick:.1f}",
        ha='right',
        va='center',
        fontsize=10
    )

# Manually add x-axis label below the x tick labels
ax.text(
    0, ylim[0] - 0.3,
    'dU [p.u.]',
    ha='center',
    va='top',
    fontsize=12
)

# Manually add y-axis label to the left of y tick labels, rotated vertical
ax.text(
    xlim[0] - 0.25, 0,
    'dIq [p.u.]',
    ha='center',
    va='center',
    rotation='vertical',
    fontsize=12
)

# Area labels
ax.text(0.4, 0.2, 'Area D', fontsize=12)
ax.text(-0.4, -0.8, 'Area B', fontsize=12)
ax.text(0.15, 0.55, 'k1', fontsize=8)
ax.text(-0.5, -0.45, 'k2', fontsize=8)

# Set a visible rectangle frame around the entire figure (including labels)
fig.patch.set_linewidth(2)
fig.patch.set_edgecolor('black')

plt.savefig("../plots/fig2.png", dpi=800, bbox_inches='tight')
