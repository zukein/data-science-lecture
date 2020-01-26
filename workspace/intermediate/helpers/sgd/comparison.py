import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
from ipywidgets import interactive_output, Play, IntSlider, jslink, HBox
from IPython.display import display
import sys
import os
sys.path.append(os.path.dirname(__file__))
from gradient_descent import get_data, get_costs, train

lim = 1
resolution = 30

X, y, coef = get_data(100, 2)
min_lim, max_lim = coef - lim, coef + lim
grid1 = np.linspace(min_lim[0], max_lim[0], resolution)
grid2 = np.linspace(min_lim[1], max_lim[1], resolution)
w1, w2 = np.meshgrid(grid1, grid2)
weights = np.c_[w1.ravel(), w2.ravel()]
costs = get_costs(weights, X, y)
z = costs.reshape(w1.shape)

lr = 0.05
batch_size = 5
w_gd, c_gd = train(coef, X, y, lr=lr)
w_sgd, c_sgd = train(coef, X, y, lr=lr, batch_size=batch_size)

ws1 = [w_sgd[:, 0], w_gd[:, 0]]
ws2 = [w_sgd[:, 1], w_gd[:, 1]]
colors = ['red', 'blue']
labels = ['確率的勾配降下法', '最急降下法']


def plot(step):
    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()

    ax.contour(w1, w2, z)
    for xx, yy, color, label in zip(ws1, ws2, colors, labels):
        i = step if label == '確率的勾配降下法' else int(step // (y.size / batch_size))
        ax.scatter(xx[i], yy[i], marker='x', color=color, label=label)
        if i > 0:
            ax.scatter(xx[:i], yy[:i], marker='x', color=color, alpha=0.3)
    ax.legend()
    ax.set(xlim=(coef[0] - lim, coef[0] + lim),
           ylim=(coef[1] - lim, coef[1] + lim),
           xlabel='$w$',
           ylabel='コスト',
           xticks=(),
           yticks=())

    plt.show()


def show():
    step = IntSlider()
    play = Play(interval=100,
                value=0,
                min=0,
                max=c_sgd.size,
                description='経過時間')
    jslink((play, 'value'), (step, 'value'))
    controller = HBox([play, step])
    graph = interactive_output(plot, {'step': step})
    display(controller, graph)
