import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    resolution = 30
    n_samples = 20
    n_features = 10
    n_informative = 8
    effective_rank = 2

    X, y = make_regression(n_samples=n_samples,
                           n_features=n_features,
                           n_informative=n_informative,
                           effective_rank=effective_rank,
                           random_state=1234)

    param = np.logspace(-2, 2, num=resolution)
    history = np.zeros((n_features, resolution))

    for i, a in enumerate(param):
        history[:, i] = Ridge(alpha=a).fit(X, y).coef_

    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()

    for w in history:
        ax.plot(param, w)

    ax.set(xlabel=r'$\alpha$',
           ylabel='$w_{1} \sim w_{k}$',
           xlim=(param.min(), param.max()),
           xscale='log',
           yticks=())

    plt.show()
