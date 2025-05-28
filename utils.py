#utils
import matplotlib.pyplot as plt
import numpy as np




min_plot_time, max_plot_time = -0.2, 25















min_plot_voltage, max_plot_voltage = -0.05, 1.25
original_time = np.array([min_plot_time, 0, 0.15, 0.5, 1, 2, 5, 10, 20, max_plot_time])
transformed_time = np.linspace(0, 4.5, len(original_time))
transform_time = lambda t: np.interp(t, original_time, transformed_time)


def setup_plot(lvrt_points, hvrt_points):
    fig, ax = plt.subplots(figsize=(10, 6))
    return fig,  ax
def get_transformed_curve(points):
    t, v = points[:, 0], points[:, 1]
    return transform_time(t), v

def use_transformed_curve(lv, hv):
    lvrt_x, lvrt_y = get_transformed_curve(lv)
    hvrt_x, hvrt_y = get_transformed_curve(hv)
    return lvrt_x,lvrt_y,hvrt_x, hvrt_y

def fill_between_curves(ax, x, y1, y2, color, label=None, alpha=0.1, text_offset=(0, 0)):
    ax.fill_between(x, y1, y2, color=color, alpha=alpha, zorder=1)
    if label:
        x_center = (x[0] + x[-1]) / 2 + text_offset[0]
        y_center = (np.min([y1, y2]) + np.max([y1, y2])) / 2 + text_offset[1]
        ax.text(
            x_center, y_center,
            label, color='black', fontsize=12, fontweight='bold',
            ha='center', va='center', zorder=2
        )
    
def plottingfunc(ax, lvrt_x,lvrt_y,hvrt_x, hvrt_y):
    for x, y in [(lvrt_x, lvrt_y), (hvrt_x, hvrt_y)]:
        ax.plot(x, y, color='black', linewidth=2.5, zorder=5)
        return ax


def draw_guidelines(ax, xs, ys):
    for x, y in zip(xs, ys):
        ax.axhline(y=y, xmin=0, xmax=x / transformed_time[-1],
                   linestyle='--', color='gray', linewidth=1.0, alpha=0.7)
        ax.axvline(x=x, ymin=0, ymax=y / max_plot_voltage,
                   linestyle='--', color='gray', linewidth=1.0, alpha=0.7)
        
def guidelinesfunc(ax, lvrt_x,lvrt_y,hvrt_x, hvrt_y):
    draw_guidelines(ax, np.concatenate([lvrt_x[1:-1], hvrt_x[1:-1]]),
                   np.concatenate([lvrt_y[1:-1], hvrt_y[1:-1]]))
    return ax



def addAreaA(ax, min, max):
    ax.axhspan(min, max, color='teal', alpha=0.2, zorder=0)
    ax.text(
        transform_time([min_plot_time, max_plot_time]).mean(), (min+max)/2,
        "Continuous Operating Range\nArea A",
        color='black', fontsize=12, fontweight='bold',
        ha='center', va='center', zorder=1
    )
    return ax

def addSideArrowLabel(ax, min, max):
    center = (min + max)/2

    label = f"{min} < Un < {max}"
    ax.text(5, center, label, color='black', fontsize=12, fontweight='bold',
            ha='center', va='center', zorder=2)
    ax.annotate(
        '',
        xy=(transform_time(max_plot_time), max),
        xytext=(4.9, center+0.03),
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
        xy=(transform_time(max_plot_time), min),
        xytext=(4.9, center - 0.03),
        arrowprops=dict(
            arrowstyle='->',
            color='black',
            lw=2,
            shrinkA=0,
            shrinkB=0
        ),
        zorder=10
    )
    return ax

def clean(ax):
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_linewidth(1.0)
    return ax
