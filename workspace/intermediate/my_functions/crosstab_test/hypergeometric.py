import numpy as np
from scipy import stats
from ipywidgets import interact, IntSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def plot(total, n_objects, n_drawn):
    x = np.arange(0, n_drawn + 1)
    distribution = stats.hypergeom(total, n_objects, n_drawn)
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.vlines(x, 0, distribution.pmf(x))
    ax.set(title='超幾何分布', xlabel='対象の個数', ylim=(0, 1), xticks=x)
    ax.set_ylabel('確率', rotation=0, horizontalalignment='right')
    plt.show()


def show():
    total = IntSlider(
        value=10, min=2, max=15, description='総数', continuous_update=False)
    n_objects = IntSlider(
        value=3, min=1, description='対象の総数', continuous_update=False)
    n_drawn = IntSlider(
        value=5, min=1, description='抽出回数', continuous_update=False)

    def update(*args):
        n_objects.max = total.value
        n_drawn.max = total.value

    total.observe(update, 'value')
    n_objects.observe(update, 'value')
    n_drawn.observe(update, 'value')

    interact(plot, total=total, n_objects=n_objects, n_drawn=n_drawn)
