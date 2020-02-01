import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib.figure import figaspect
import matplotlib.pyplot as plt
from ipywidgets import interactive_output, jslink, IntSlider, Play, HBox
from IPython.display import display

reputation = 20
sample_size = 10
noise = 0.3


def plot(random_state):
    np.random.seed(1234 + random_state)
    x = np.random.random(sample_size)
    y = x + np.random.normal(scale=noise, size=sample_size)
    model = LinearRegression(n_jobs=-1).fit(x.reshape((-1, 1)), y)
    a = model.coef_
    b = model.intercept_
    xlim = np.array((-0.05, 1.05))
    ylim = xlim + (-noise * 3, noise * 3)
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.scatter(x, y, color='black')
    ax.plot(xlim, a * xlim + b)
    ax.set(xlim=xlim, ylim=ylim, xticks=(), yticks=())
    plt.show()


def show():
    value = 1
    value_min = 1
    value_max = reputation
    random_state = IntSlider(
        value=value, min=value_min, max=value_max, continuous_update=False)
    play = Play(interval=1000, value=value, min=value_min, max=value_max)
    jslink((play, 'value'), (random_state, 'value'))
    controller = HBox([play, random_state])
    output = interactive_output(plot, dict(random_state=random_state))
    display(controller, output)
