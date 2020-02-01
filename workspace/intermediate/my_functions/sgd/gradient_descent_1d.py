import numpy as np
from ipywidgets import interactive_output
from ipywidgets.widgets import IntSlider, Play, jslink, HBox
from IPython.display import display
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
import sys
import os
sys.path.append(os.path.dirname(__file__))
from gradient_descent import get_data, get_costs, train

n = 100
epochs = 5
lim = 1
resolution = 30

X, y, coef = get_data(n, 1)

weights = np.linspace(coef - lim, coef + lim, resolution).reshape(-1, 1)
costs = get_costs(weights, X, y)
w, c = train(coef, X, y, epochs=epochs, init_w=lim * 0.9)

origin_x = w[:-1]
origin_y = c[:-1]
vec_x = w[1:] - w[:-1]
vec_y = c[1:] - c[:-1]


def plot(step):
    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.plot(weights, costs, color='blue')

    kwargs = dict(angles='xy', scale_units='xy', scale=1, color='red')
    if step > 0:
        ax.quiver(origin_x[step - 1:step], origin_y[step - 1:step],
                  vec_x[step - 1:step], vec_y[step - 1:step], **kwargs)
    if step > 1:
        ax.quiver(origin_x[:step - 1],
                  origin_y[:step - 1],
                  vec_x[:step - 1],
                  vec_y[:step - 1],
                  alpha=0.3,
                  **kwargs)

    ax.set(title='特徴が1つ(単回帰)',
           xlim=(coef - lim, coef + lim),
           ylim=(-costs.max() * 0.05, costs.max()),
           xlabel='$w$',
           ylabel='コスト')
    plt.show()


def show():
    play = Play(interval=500, value=0, min=0, max=epochs, step=1)
    step = IntSlider(value=0, min=0, max=epochs, description='ステップ')
    jslink((play, 'value'), (step, 'value'))
    controller = HBox([play, step])
    graph = interactive_output(plot, dict(step=step))
    display(controller, graph)
