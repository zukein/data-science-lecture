from collections import OrderedDict
import numpy as np
from scipy.stats import beta
from sklearn.metrics import precision_recall_curve
from ipywidgets import interact, FloatSlider, SelectionSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
from matplotlib.patches import Rectangle


def plot(performance, threshold):
    # a : b = p : 1 - p
    # a + b = 2, 4, 8, 16...
    def f(x):
        return x * 4**(performance * 5 - 2)

    a = f(performance)
    b = f(1 - performance)

    _, (ax1, ax2) = plt.subplots(1, 2, figsize=figaspect(1 / 2))

    point_t = np.linspace(0, 1, 20)
    point_f = np.linspace(0, 1, 80)
    x_t = beta.ppf(point_t, a, b)
    x_f = 1 - beta.ppf(point_f, a, b)
    colors = {'真陽性': 'yellow', '偽陰性': 'orange', '偽陽性': 'pink', '真陰性': 'brown'}
    ax1.scatter(x_t, np.ones_like(x_t), color='black', marker='.', s=2)
    ax1.scatter(x_f, np.zeros_like(x_f), color='black', marker='.', s=2)
    xlim, ylim = ax1.get_xlim(), ax1.get_ylim()
    height = 0.5 - ylim[1]
    for truth in [True, False]:
        y = ylim[1] if truth else 0.5
        for pred in [True, False]:
            x = threshold if pred else xlim[0]
            width = xlim[1] - threshold if pred else threshold - xlim[0]
            label = '真' if truth == pred else '偽'
            label += '陽性' if pred else '陰性'
            ax1.add_patch(
                Rectangle((x, y),
                          width=width,
                          height=height,
                          facecolor=colors[label],
                          alpha=0.3,
                          label=label))
    ax1.axvline(threshold, linestyle='--', linewidth=1, alpha=0.3)
    ax1.legend(loc='center')
    ax1.set(title='混同行列 (左が陰性・右が陽性)',
            xlabel='予測',
            ylabel='正解',
            xlim=(0, 1),
            ylim=ylim,
            yticks=(0, 1),
            yticklabels=('False', 'True'))

    tt = beta.ppf(np.linspace(0, 1, 1000), a, b)
    ff = 1 - beta.ppf(np.linspace(0, 1, 4000), a, b)
    yy = np.hstack([np.ones_like(tt), np.zeros_like(ff)])
    yy_pred = np.hstack([tt, ff])
    pre, rec, _ = precision_recall_curve(yy, yy_pred)
    ax2.plot(rec, pre, color='black', linewidth=0.5)
    tp = beta.sf(threshold, a, b)
    fp = beta.cdf(1 - threshold, a, b) * 4
    ax2.scatter(beta.sf(threshold, a, b), tp / (tp + fp))
    ax2.set(title='PR曲線', xlabel='再現率', ylabel='適合率', xlim=(0, 1), ylim=(0, 1))

    plt.show()


def show():
    p = SelectionSlider(options=OrderedDict([('ランダム', 0.5), ('悪い', 0.6),
                                             ('そこそこ', 0.7), ('良い', 0.8)]),
                        value=0.5,
                        description='性能',
                        continuous_update=False)
    t = FloatSlider(value=0.5,
                    min=0.01,
                    max=0.99,
                    step=0.01,
                    description='閾値',
                    readout_format='.2f',
                    continuous_update=False)
    interact(plot, performance=p, threshold=t)
