import numpy as np
from ipywidgets import interact, FloatSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

resolution = 100
x_ones = np.linspace(0.6, 1, 5)
x_zeros = -x_ones
x = np.stack((x_ones, x_zeros))
y_ones = np.ones_like(x_ones)
y_zeros = np.zeros_like(x_ones)
y = np.stack((y_ones, y_zeros))


def get_z(a, b, x):
    return a + b * x


def logistic(z):
    return 1 / (1 + np.exp(-z))


def plot(a, b):
    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.scatter(x, y, color='black', linewidths=0.1)
    x_min, x_max = ax.get_xlim()
    ax.hlines((0, 1), x_min, x_max, linewidth=1, alpha=0.3)
    z_zeros = get_z(a, b, x_zeros)
    z_ones = get_z(a, b, x_ones)
    y_hat_zeros = logistic(z_zeros)
    y_hat_ones = logistic(z_ones)
    ax.vlines(x_zeros, 1, y_hat_zeros, colors='red', label='尤度$(y=0)$')
    ax.vlines(x_ones, 0, y_hat_ones, colors='blue', label='尤度$(y=1)$')
    xx = np.linspace(x_min, x_max, resolution)
    zz = get_z(a, b, xx)
    yy = logistic(zz)
    ax.plot(xx, yy, color='black', alpha=0.5, label=r'$\hat{y}$')
    ax.legend()
    log_likelihood = np.log(1 - y_hat_zeros).sum() + np.log(y_hat_ones).sum()
    ax.set(title=f'対数尤度={log_likelihood:.3f}',
           xlim=(x_min, x_max),
           xticks=(),
           xlabel='$x$',
           ylabel='$y$')


def show():
    a = FloatSlider(value=0,
                    min=-10,
                    max=10,
                    step=0.1,
                    description='$a$',
                    continuous_update=False)
    b = FloatSlider(value=5,
                    min=-10,
                    max=10,
                    step=0.1,
                    description='$b$',
                    continuous_update=False)
    interact(plot, a=a, b=b)
