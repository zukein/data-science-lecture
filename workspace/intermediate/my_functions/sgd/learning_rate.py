import numpy as np
from ipywidgets import interact, FloatLogSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
import sys
import os
sys.path.append(os.path.dirname(__file__))
from gradient_descent import get_data, get_costs, train

lim = 1
resolution = 30

X, y, coef = get_data(100, 1)

weights = np.linspace(coef - lim, coef + lim, resolution).reshape(-1, 1)
costs = get_costs(weights, X, y)


def plot(lr):
    w, c = train(coef, X, y, lr)

    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.plot(weights, costs, color='blue')
    ax.quiver(w[:-1],
              c[:-1],
              w[1:] - w[:-1],
              c[1:] - c[:-1],
              angles='xy',
              scale_units='xy',
              scale=1,
              color='red')
    ax.set(title='学習率 = {:.2f}'.format(lr),
           xlim=(coef - lim, coef + lim),
           ylim=(-costs.max() * 0.05, costs.max()),
           xlabel='$w$',
           ylabel='コスト',
           xticks=(),
           yticks=())
    plt.show()


def show():
    lr = FloatLogSlider(value=-1,
                        base=10,
                        min=-2,
                        max=0.5,
                        step=0.25,
                        description='学習率',
                        continuous_update=False)
    interact(plot, lr=lr)
