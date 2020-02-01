import numpy as np
from ipywidgets import interactive_output
from ipywidgets.widgets import IntSlider, Play, jslink, HBox
from IPython.display import display
from mpl_toolkits.mplot3d import Axes3D
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

X, y, coef = get_data(n, 2)
min_lim, max_lim = coef - lim, coef + lim
grid1 = np.linspace(min_lim[0], max_lim[0], resolution)
grid2 = np.linspace(min_lim[1], max_lim[1], resolution)
w1, w2 = np.meshgrid(grid1, grid2)
weights = np.c_[w1.ravel(), w2.ravel()]
costs = get_costs(weights, X, y)
w, c = train(coef, X, y, epochs=epochs, init_w=lim * 0.9)
offset = -c.max() * 0.1

origin_x = w[:-1, 0]
origin_y = w[:-1, 1]
origin_z = c[:-1]
vec_x = w[1:, 0] - w[:-1, 0]
vec_y = w[1:, 1] - w[:-1, 1]
vec_z = c[1:] - c[:-1]
history = np.vstack([origin_x, origin_y, origin_z, vec_x, vec_y, vec_z])

plt.figure(figsize=figaspect(1))
ax = plt.axes(projection='3d')


def plot(step):
    plt.cla()
    kwargs = dict(X=w1, Y=w2, Z=costs.reshape(w1.shape))
    ax.plot_surface(color='blue', alpha=0.3, **kwargs)
    ax.contour(zdir='z', offset=offset, **kwargs)

    if step > 0:
        args = list(history[:, step - 1])
        kwargs = dict(color='red')
        ax.quiver(*args, **kwargs)
        args[2] = offset
        args[5] = 0
        ax.quiver(*args, **kwargs)
    if step > 1:
        args = history[:, :step - 1].copy()
        kwargs = dict(color='red', alpha=0.2)
        ax.quiver(*args, **kwargs)
        args[2] = offset
        args[5] = 0
        ax.quiver(*args, **kwargs)
    zlim = ax.get_zlim()
    ax.set(title='特徴が2つ',
           xlabel='$w_{1}$',
           ylabel='$w_{2}$',
           zlabel='コスト',
           zlim=(offset, zlim[1]))

    plt.show()


def show():
    play = Play(interval=500, value=0, min=0, max=epochs, step=1)
    step = IntSlider(value=0, min=0, max=epochs, description='ステップ')
    jslink((play, 'value'), (step, 'value'))
    controller = HBox([play, step])
    graph = interactive_output(plot, dict(step=step))
    display(controller, graph)
