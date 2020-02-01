import numpy as np
from sklearn.datasets import make_regression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    n = 10
    degree = 10
    n_valid_feature = 3
    resolution = 30

    np.random.seed(1234)

    poly = PolynomialFeatures(degree=degree, include_bias=False)
    poly.fit(np.zeros(n).reshape((-1, 1)))
    scaler = StandardScaler()

    x = np.linspace(-1, 1, n)
    X = poly.transform(x.reshape((-1, 1)))
    X = scaler.fit_transform(X)
    n_features = X.shape[1]
    all_features = np.arange(n_features)
    np.random.shuffle(all_features)
    valid_features = all_features[:n_valid_feature]
    coef = np.random.uniform(-0.1, 0.1, (n_valid_feature, 1))
    noise = np.random.normal(0, 0.01, (n))
    y = X[:, valid_features].dot(coef).ravel() + noise

    param = np.linspace(0.01, 0.1, resolution)
    history = np.zeros((n_features, resolution))

    for i, a in enumerate(param):
        history[:, i] = Lasso(alpha=a).fit(X, y).coef_

    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()

    for w in history:
        ax.plot(param, w)

    ax.set(xlabel=r'$\alpha$',
           ylabel='$w_{1} \sim w_{k}$',
           xlim=(param.min(), param.max()),
           yticks=())

    plt.show()
