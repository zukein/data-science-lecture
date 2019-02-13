import numpy as np
from scipy import stats
from ipywidgets import interact, IntSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

xlim = (0, 15)
x = np.linspace(xlim[0], xlim[1], 100)


def plot(df):
    chi2 = stats.chi2.pdf(x, df=df)
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.plot(x, chi2, label=r'自由度 ${df}$ の $\chi^2$ 分布'.format(df=df))
    ax.legend()
    ax.set(title=r'$\chi^2$ 分布', xlim=xlim, ylim=(0, 0.3))
    plt.show()


def show():
    df = IntSlider(
        value=1, min=1, max=10, description='自由度', continuous_update=False)
    interact(plot, df=df)
