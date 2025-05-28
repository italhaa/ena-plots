#fig3.py

import matplotlib.pyplot as plt
drop = 51

# === Create the figure and axis ===
fig, ax = plt.subplots(figsize=(8, 5))

# === Data points ===
x_points = [49, drop, 52, 52, 52.5]
y_points = [100, 100, 25, 0, 0]
ax.plot(x_points, y_points, color='black', linewidth=2)

# === Axis limits ===
ax.set_xlim(48.5, 53)
ax.set_ylim(0, 120)

# === Labels and title ===
ax.set_xlabel("System Frequency [Hz]", fontsize=12)
ax.set_ylabel(f"% of Power Output when f > {drop} Hz", fontsize=12)
ax.set_title("Power Curtailment during Over-Frequency", fontsize=14, fontweight='bold')

# === Grid: Horizontal lines only ===
ax.yaxis.grid(True)
ax.xaxis.grid(False)

# === Ticks ===
ax.set_xticks([48.5, 49, 49.5, 50, 50.5, 51, 51.5, 52, 52.5, 53])
ax.set_yticks(range(0, 121, 20))

# === Hide top and right spines ===
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# === Style left and bottom spines ===
for spine in ['left', 'bottom']:
    ax.spines[spine].set_linewidth(1.0)



# === Save the figure ===
plt.tight_layout()
plt.savefig(f"../plots/fig3_{int(drop*10)}.png", dpi=800, bbox_inches='tight')
