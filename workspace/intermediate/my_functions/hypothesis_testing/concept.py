import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

p = 0.15
lower = p / 2
upper = 1 - p / 2
x_min, x_max = -4, 4
y_max = 0.45
resolution = 50
line_color = 'black'
in_color = 'blue'
out_color = 'red'
transparency = 0.5
line_style = 'dotted'
line_width = 5
font_size = 10
distribution = stats.t(df=30)
range_min, range_max = distribution.interval(1 - p)
left = np.linspace(x_min, range_min, resolution)
center = np.linspace(range_min, range_max, resolution)
right = np.linspace(range_max, x_max, resolution)
range_list = [left, center, right]
center_list = [left.mean(), center.mean(), right.mean()]
color_list = [out_color, in_color, out_color]
text_list = ['疑わしい', 'あり得なくはない', '疑わしい']


def show():
    _, (ax1, ax2) = plt.subplots(2, 1, figsize=figaspect(2 / 1), sharex=True)

    for xx, color in zip(range_list, color_list):
        ax1.fill_between(xx, 0, distribution.pdf(xx), color=color)
    ax1.vlines((range_min, range_max),
               0,
               y_max,
               color=line_color,
               alpha=transparency,
               linestyles=line_style)
    for x, text, color in zip(center_list, text_list,
                              [out_color, 'white', out_color]):
        ax1.text(
            x,
            0.2,
            text,
            color=color,
            size=font_size,
            horizontalalignment='center',
            verticalalignment='top')
    ax1.set(xlim=(x_min, x_max), ylim=(0, y_max), xticks=(), yticks=())

    for xx, color in zip(range_list, color_list):
        ax2.plot(xx, distribution.cdf(xx), color=color)
    kwargs = dict(color=line_color, alpha=transparency, linestyles=line_style)
    ax2.hlines((lower, upper), x_min, (left.max(), right.min()), **kwargs)
    ax2.vlines((left.max(), right.min()), 0, 1, **kwargs)
    for y_lower, y_upper, color in zip([0, lower, upper], [lower, upper, 1],
                                       color_list):
        ax2.vlines(x_min, y_lower, y_upper, color=color, linewidths=line_width)
    for x, y, text, color in zip(center_list, [lower / 2, 0.5, 1 - lower / 2],
                                 text_list, color_list):
        ax2.text(
            x,
            y,
            text,
            color=color,
            size=font_size,
            horizontalalignment='center',
            verticalalignment='center')
    ax2.set(
        ylim=(0, 1),
        yticks=(lower, upper),
        yticklabels=(r'$\frac{\alpha }{2} $', r'$1-\frac{\alpha }{2}$'))

    plt.subplots_adjust(hspace=0)
    plt.show()
