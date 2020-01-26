import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
from ipywidgets import interact, IntSlider, FloatSlider

resolution = 200
x = np.linspace(-3, 3, resolution)


def plot(size, alpha, effect):
    sigma = np.sqrt(1 / size)

    null_distribution = stats.norm(0, sigma)
    sample_distribution = stats.norm(effect, sigma)
    threshold = null_distribution.isf(alpha)
    xx = np.linspace(threshold, x.max(), resolution)
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.plot(x, null_distribution.pdf(x), label='帰無分布')
    ax.plot(x, sample_distribution.pdf(x), label='標本分布')
    ax.fill_between(xx, 0, sample_distribution.pdf(xx), color='red')
    ax.legend()
    ax.set(
        title=f'検定力 = {sample_distribution.sf(threshold):.2f}',
        xlim=(x.min(), x.max()),
        ylim=(0, 3))
    plt.show()


def show():
    style = dict(description_width='7em')
    size = IntSlider(
        value=10,
        min=10,
        max=50,
        step=10,
        description='サンプルサイズ',
        continuous_update=False,
        style=style)
    alpha = FloatSlider(
        value=0.05,
        min=0.01,
        max=0.1,
        step=0.01,
        description='有意水準',
        continuous_update=False,
        style=style)
    effect = FloatSlider(
        value=0.5,
        min=0.1,
        max=1,
        step=0.1,
        description='効果量',
        continuous_update=False,
        style=style)
    interact(plot, size=size, alpha=alpha, effect=effect)
