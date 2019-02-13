import numpy as np
from scipy import stats
from ipywidgets import interact, SelectionSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

xlim = (-3, 3)
x = np.linspace(xlim[0], xlim[1], 100)
n = stats.norm.pdf(x)
ylim = (0, n.max() * 1.1)


def plot(df):
    t = stats.t.pdf(x, df=df)
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.plot(x, n, label='標準正規分布')
    ax.plot(x, t, label=f'自由度 ${df}$ の $t$ 分布')
    ax.legend()
    ax.set(title='標準正規分布と $t$ 分布', xlim=xlim, ylim=ylim)
    plt.show()


def show():
    df = SelectionSlider(
        options=[1, 3, 10, 30, 100],
        description='自由度',
        continuous_update=False)
    interact(plot, df=df)
