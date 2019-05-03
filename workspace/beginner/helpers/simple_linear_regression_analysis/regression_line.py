from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    x, y = make_regression(
        n_samples=8, n_features=1, bias=50, noise=10, random_state=1234)
    x = StandardScaler().fit_transform(x)
    model = LinearRegression().fit(x, y)
    a = model.coef_
    b = model.intercept_
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.axhline(0, linewidth=1, color='gray')
    ax.axvline(0, linewidth=1, color='gray')
    ax.scatter(x, y, color='black', label='データ')
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    xlim = (min(xlim[0], -3), max(xlim[1], 3))
    ylim = (min(ylim[0], -3 * a + b), max(ylim[1], 3 * a + b))
    ax.plot(xlim, a * xlim + b, label='回帰直線 $y=ax+b$')
    ax.hlines((a + b, b), (1, xlim[0]), (2, 0),
              color='gray',
              linestyle='dashed')
    ax.vlines(2, a + b, 2 * a + b, color='gray', linestyle='dashed')
    ax.text(1.5, (a + b) * 0.9, 1, verticalalignment='top')
    ax.text(2 * 1.05, 1.5 * a + b, '$a$', horizontalalignment='left')
    ax.legend()
    ax.set(
        xlabel='$x$',
        xlim=xlim,
        ylim=ylim,
        xticks=(0, ),
        yticks=(b, ),
        yticklabels=('$b$', ))
    ax.set_ylabel('$y$', rotation='horizontal')
    plt.show()
