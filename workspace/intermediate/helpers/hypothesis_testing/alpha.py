import numpy as np
from scipy import stats
from ipywidgets import interact, FloatSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

x_min, x_max = -6, 6
resolution = 100
x = np.linspace(x_min, x_max, 100)
edge_color = 'black'
true_color = 'blue'
false_color = 'red'
transparency = 0.1


def plot(diff, alpha):
    hypothesis = diff == 0
    sample_dist = stats.norm()
    null_dist = stats.norm(loc=diff)
    range_min, range_max = null_dist.interval(1 - alpha)
    left = np.linspace(x_min, range_min, resolution)
    center = np.linspace(range_min, range_max, resolution)
    right = np.linspace(range_max, x_max, resolution)
    plt.figure(figsize=figaspect(1 / 2))
    ax = plt.axes()
    ax.plot(
        x,
        sample_dist.pdf(x),
        color=edge_color,
        alpha=transparency,
        linestyle='dotted',
        label='標本分布')
    ax.plot(x, null_dist.pdf(x), color=edge_color, label='帰無分布')
    kwargs = dict(facecolor='white', edgecolor=edge_color)
    ax.fill_between(
        center, 0, null_dist.pdf(center), hatch='/', label='採択域', **kwargs)
    for i, side in enumerate([left, right]):
        if i is 1:
            kwargs['label'] = '棄却域'
        ax.fill_between(side, 0, null_dist.pdf(side), hatch='.', **kwargs)
    kwargs = dict(alpha=transparency)
    for i, side in enumerate([left, right]):
        kwargs['color'] = false_color if hypothesis else true_color
        if i is 1:
            kwargs['label'] = '第一種の誤り (の確率)' if hypothesis \
                else '正しい棄却 (の確率)'
        ax.fill_between(side, 0, sample_dist.pdf(side), **kwargs)
    if hypothesis:
        kwargs['color'] = true_color
        kwargs['label'] = '正しい採択 (の確率)'
    else:
        kwargs['color'] = false_color
        kwargs['label'] = '第二種の誤り (の確率)'
    ax.fill_between(center, 0, sample_dist.pdf(center), **kwargs)
    ax.legend()
    title = '帰無仮説 $H_{0}$ が'
    title += '正しい' if hypothesis else '誤り'
    ax.set(
        title=title, xlim=(x_min, x_max), ylim=(0, 0.45), xticks=(), yticks=())
    plt.show()


def show():
    style = {'description_width': '10em'}
    diff = FloatSlider(
        value=0,
        min=-3,
        max=3,
        step=0.5,
        description='母平均と標本平均の差',
        continuous_update=False,
        readout_format='.1f',
        style=style)
    alpha = FloatSlider(
        value=0.05,
        min=0.01,
        max=0.3,
        step=0.01,
        description='有意水準',
        continuous_update=False,
        readout_format='.2f',
        style=style)
    interact(plot, diff=diff, alpha=alpha)
