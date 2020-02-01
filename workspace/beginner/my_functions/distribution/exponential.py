import numpy as np
from scipy import stats
from ipywidgets import interact, FloatLogSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def plot(lambda_):
    x = np.linspace(0, 9, 100)
    y = stats.expon.pdf(x, scale=1 / lambda_)
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.plot(x, y)
    ax.set(
        title='指数分布',
        xlabel=r'取りうる値 $\left( 0\sim \infty \right)$',
        xlim=(0, x.max()),
        ylim=(0, 1))
    ax.set_ylabel('確率密度', rotation=0, horizontalalignment='right')
    plt.show()


def show():
    style = dict(description_width='initial')
    interact(
        plot,
        lambda_=FloatLogSlider(
            value=0.5,
            base=10,
            min=-1,
            max=1,
            step=0.25,
            description='単位時間あたり平均回数：',
            continuous_update=False,
            readout_format='.1f',
            style=style))
