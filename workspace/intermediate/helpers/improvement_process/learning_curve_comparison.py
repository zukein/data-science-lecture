import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    titles = ['高バイアス', '最適', '高バリアンス']
    labels = ['要求水準', 'トレーニングデータの結果', 'テストデータの結果']

    x_min, x_max = 1, 10
    x = np.linspace(x_min, x_max, 50)
    expected = .8
    train = np.array([[
        np.exp(-x * .9) * 1.5 + expected / 2 + .01,
        np.exp(-x * .6) * .35 + expected + .01,
        np.exp(-x * .3) * .25 + expected + .01
    ],
                      [
                          -np.exp(-x * .6) * 1.1 + .59,
                          -np.exp(-x * .6) * .35 + .19,
                          -np.exp(-x * .6) * .35 + .19
                      ]])
    validation = np.array([[
        -np.exp(-x * .9) + expected / 2 - .01,
        -np.exp(-x * .6) * 1.5 + expected - .01,
        -np.exp(-x * .2) * .95 + expected - .01
    ],
                           [
                               np.exp(-x * .6) * .75 + .61,
                               np.exp(-x * .6) * 1.45 + .21,
                               np.exp(-x * .2) * .95 + .21,
                           ]])

    _, axes = plt.subplots(2, 3, figsize=figaspect(2 / 3) * 2)

    for (row, col), ax in np.ndenumerate(axes):
        ax.plot(x, train[row, col], color='green', label=labels[1])
        ax.plot(x, validation[row, col], color='red', label=labels[2])

        ax.set(xlim=(x_min, x_max), ylim=(0, 1), xticklabels=())

        if row == 0:
            ax.axhline(expected, color='blue', label=labels[0])
            ax.set(title=titles[col])

            if col == 0:
                ax.legend(loc='lower right')
                ax.set(ylabel='正解率')

        else:
            ax.set(xlabel='トレーニングサンプル数',
                   xticks=np.arange(x_min, x_max + 1),
                   xticklabels=(['$1$'] + [''] * 8 + ['$n$']))

            if col == 0:
                ax.set(ylabel='損失')

        if row + col > 0:
            ax.set(yticklabels=())

    plt.show()
