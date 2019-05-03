import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
from ipywidgets import interact, FloatSlider


def hist(scale):
    x = np.random.normal(size=1000000, scale=scale)
    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.hist(x, range=(-6, 6), bins=200, density=True)
    ax.set(xlim=(-6, 6), ylim=(0, 1))
    plt.show()


def show():
    style = dict(description_width='initial')
    interact(
        hist,
        scale=FloatSlider(
            value=1.0,
            min=0.5,
            max=2,
            step=0.1,
            description='データの散らばり具合：',
            continuous_update=False,
            style=style))
