import numpy as np
from scipy import stats
from ipywidgets import interact, FloatSlider, FloatLogSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def plot(mu, sigma):
    xlim = (-4, 4)
    x = np.linspace(xlim[0], xlim[1], 100)
    y = stats.norm.pdf(x, loc=mu, scale=sigma)
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.plot(x, y)
    ax.set(
        title='正規分布',
        xlabel=r'取りうる値 $\left( -\infty \sim \infty \right)$',
        xlim=xlim,
        ylim=(0, 1))
    ax.set_ylabel('確率密度', rotation=0, horizontalalignment='right')
    plt.show()


def show():
    interact(
        plot,
        mu=FloatSlider(
            value=0,
            min=-1,
            max=1,
            step=0.5,
            description='平均：',
            continuous_update=False,
            readout_format='.1f'),
        sigma=FloatLogSlider(
            value=1,
            base=10,
            min=-0.25,
            max=0.25,
            step=0.125,
            description='標準偏差：',
            continuous_update=False,
            readout_format='.1f'))
