import numpy as np
from scipy.stats import beta
from sklearn.metrics import precision_recall_curve, roc_curve
from ipywidgets import interactive_output, IntSlider, Play, jslink
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
from matplotlib.patches import Rectangle
from IPython.display import display

n_threshold = 100

# a : b = p : 1 - p
# a + b = 2, 4, 8, 16...
p = 0.65


def f(x):
    return x * 4**(p * 5 - 2)


a = f(p)
b = f(1 - p)

point_t = np.linspace(0, 1, 20)
point_f = np.linspace(0, 1, 80)
x_t = beta.ppf(point_t, a, b)
x_f = 1 - beta.ppf(point_f, a, b)
tt = beta.ppf(np.linspace(0, 1, 1000), a, b)
ff = 1 - beta.ppf(np.linspace(0, 1, 4000), a, b)
yy = np.hstack([np.ones_like(tt), np.zeros_like(ff)])
yy_pred = np.hstack([tt, ff])
pre, rec, pr_t = precision_recall_curve(yy, yy_pred)
fpr, tpr, roc_t = roc_curve(yy, yy_pred)


def plot(i):
    threshold = i / n_threshold

    _, axes = plt.subplots(1, 3, figsize=figaspect(1 / 3))

    ax = axes[0]
    colors = {'真陽性': 'yellow', '偽陰性': 'orange', '偽陽性': 'pink', '真陰性': 'brown'}
    scatter_prop = dict(color='black', marker='.', s=2)
    ax.scatter(x_t, np.ones_like(x_t), **scatter_prop)
    ax.scatter(x_f, np.zeros_like(x_f), **scatter_prop)
    xlim, ylim = ax.get_xlim(), ax.get_ylim()
    height = 0.5 - ylim[1]
    for truth in [True, False]:
        y = ylim[1] if truth else 0.5
        for pred in [True, False]:
            x = threshold if pred else xlim[0]
            width = xlim[1] - threshold if pred else threshold - xlim[0]
            label = '真' if truth == pred else '偽'
            label += '陽性' if pred else '陰性'
            ax.add_patch(
                Rectangle((x, y),
                          width=width,
                          height=height,
                          facecolor=colors[label],
                          alpha=0.3,
                          label=label))
    ax.axvline(threshold, linestyle='--', linewidth=1, alpha=0.3)
    ax.legend(loc='center')
    ax.set(title='混同行列 (左が陰性・右が陽性)',
           xlabel='予測',
           ylabel='正解',
           xlim=(0, 1),
           ylim=ylim,
           yticks=(0, 1),
           yticklabels=('False', 'True'))

    auc_prop = dict(color='blue', alpha=0.3)
    curve_prop = dict(color='black', linewidth=0.5)
    ax = axes[1]
    x = beta.sf(threshold, a, b)
    tp = beta.sf(threshold, a, b)
    fp = beta.cdf(1 - threshold, a, b) * 4
    y = tp / (tp + fp)
    cond = rec >= x
    xx = rec[cond]
    yy = pre[cond]
    ax.fill_between(xx, 0, yy, **auc_prop)
    ax.plot(rec, pre, **curve_prop)
    ax.scatter(x, y)
    ax.set(title='PR曲線', xlabel='再現率', ylabel='適合率', xlim=(0, 1), ylim=(0, 1))

    ax = axes[2]
    x = beta.cdf(1 - threshold, a, b)
    y = beta.sf(threshold, a, b)
    cond = fpr >= x
    xx = fpr[cond]
    yy = tpr[cond]
    ax.fill_between(xx, 0, yy, **auc_prop)
    ax.plot(fpr, tpr, **curve_prop)
    ax.scatter(x, y)
    ax.set(title='ROC曲線',
           xlabel='偽陽性率',
           ylabel='真陽性率',
           xlim=(0, 1),
           ylim=(0, 1))

    plt.show()


def show():
    margin = 1
    i = IntSlider(value=1,
                  min=margin,
                  max=n_threshold - margin,
                  step=1,
                  continuous_update=False)
    play = Play(interval=100,
                value=1,
                min=margin,
                max=n_threshold - margin,
                step=1)
    jslink((play, 'value'), (i, 'value'))
    output = interactive_output(plot, dict(i=i))
    display(play, output)
