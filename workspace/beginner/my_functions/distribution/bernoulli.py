from scipy import stats
from ipywidgets import interact, FloatSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def plot(p):
    x = [0, 1]
    y = stats.bernoulli.pmf(x, p)

    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.vlines(x, 0, y)
    ax.set(title='ベルヌーイ分布', xlabel='取りうる値', ylim=(0, 1.1), xticks=x)
    ax.set_ylabel('確率', rotation=0, horizontalalignment='right')
    plt.show()


def show():
    interact(
        plot,
        p=FloatSlider(
            value=0.5,
            min=0.0,
            max=1.0,
            step=0.1,
            description='成功確率：',
            continuous_update=False,
            readout_format='.1f'))
