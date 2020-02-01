import numpy as np
from sklearn.datasets import make_regression
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
from ipywidgets import interact, ToggleButtons, IntSlider

resolution = 50

X, y, coef = make_regression(n_samples=100,
                             n_features=2,
                             n_informative=2,
                             noise=20.0,
                             coef=True,
                             random_state=1)
margin = np.absolute(coef).max()
coef1, coef2 = coef
w1 = np.linspace(min(coef1 - margin, -margin), max(coef1 + margin, margin),
                 resolution)
w2 = np.linspace(min(coef2 - margin, -margin), max(coef2 + margin, margin),
                 resolution)
xx, yy = np.meshgrid(w1, w2)
W = np.c_[xx.ravel(), yy.ravel()]

y_hat = W.dot(X.T)
mse = ((y.reshape((1, -1)) - y_hat)**2).mean(axis=1).reshape(xx.shape)
norm = np.absolute(W).sum(axis=1).reshape(xx.shape)

alphamin = 0
alphamax = 100
offset = -max(mse.max(), W.max()) * 0.3
xlim = (xx.min(), xx.max())
ylim = (yy.min(), yy.max())
zlim = (offset, (mse + alphamax * np.absolute(norm)).max())

plt.figure(figsize=figaspect(1))
ax = plt.axes(projection='3d')


def plot(mode, alpha):
    cost = np.zeros_like(xx)
    title = []
    if mode % 2 is 1:
        cost += mse
        title.append(
            r'\frac{1}{2n}\sum ^{n}_{i=1}\left( y_{i} -\hat{y}_{i}\right)^{2}')
    if mode > 1:
        cost += alpha * norm
        title.append(r'\alpha \sum ^{k}_{i=1} |w_{i}|')
    optim = np.unravel_index(np.argmin(cost), cost.shape)

    ax.clear()
    ax.plot_surface(xx, yy, cost, alpha=0.7)
    ax.contour(xx, yy, cost, zdir='z', offset=offset)
    ax.grid(False)
    zeros = np.zeros(2)
    kwargs = dict(zs=offset, color='black', linewidth=1, alpha=0.3)
    ax.plot(zeros, ylim, **kwargs)
    ax.plot(xlim, zeros, **kwargs)
    ax.scatter(xx[optim],
               yy[optim], (cost[optim], offset),
               marker='x',
               color='red')
    ax.set(title='損失関数 $L={}$'.format('+'.join(title)),
           xlabel='$w_{1}$',
           ylabel='$w_{2}$',
           zlabel='コスト',
           zlim=zlim)
    plt.show()


def show():
    mode = ToggleButtons(options=[('MSE', 1), ('L1', 2), ('MSE+L1', 3)],
                         value=1,
                         description='損失関数')
    alpha = IntSlider(value=1,
                      min=alphamin,
                      max=alphamax,
                      step=10,
                      description=r'$\alpha$',
                      continuous_update=False)
    interact(plot, mode=mode, alpha=alpha)
