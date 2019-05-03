import numpy as np
from scipy import stats
from scipy.linalg import eigh
from ipywidgets import interact, FloatSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def plot(r):
    n = 100
    np.random.seed(1234)
    mat = np.array([
        [1.0, r],
        [r, 1.0]
    ])
    a = np.random.normal(size=(2, n))
    evals, evecs = eigh(mat)
    c = evecs.dot(np.diag(np.sqrt(evals)))
    x, y = c.dot(a)

    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.scatter(x, y, marker='.')
    ax.set(title=f'相関係数 $r_{{xy}}={stats.pearsonr(x, y)[0]:.2f}$',
           xlabel='$x$', ylabel='$y$', xticks=(), yticks=())

    plt.show()


def show():
    style = dict(description_width='initial')
    r = FloatSlider(value=0, min=-1, max=1, step=0.1,
                    description='相関係数 (目安)', continuous_update=False,
                    readout_format='.1f', style=style)
    interact(plot, r=r)
