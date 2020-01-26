import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
from ipywidgets import interact, FloatLogSlider

n = 10
degree = 20
margin = 0.1

np.random.seed(1234)

poly = PolynomialFeatures(degree=degree, include_bias=False)
poly.fit(np.zeros(n).reshape((-1, 1)))
scaler = StandardScaler()


def get_multinomial(x):
    return poly.transform(x.reshape((-1, 1)))


x = np.linspace(-1, 1, n)
X = scaler.fit_transform(get_multinomial(x))
coef = np.random.uniform(-0.1, 0.1, (X.shape[1], 1))
noise = np.random.normal(0, 0.1, (n))
y = X.dot(coef).ravel() + noise

x_min, x_max = x.min() - margin, x.max() + margin
y_min, y_max = y.min() - margin, y.max() + margin
xx = np.linspace(x_min, x_max, 200)
XX = scaler.transform(get_multinomial(xx))

linear = LinearRegression().fit(X, y)


def plot(alpha):
    ridge = Ridge(alpha=alpha, normalize=True).fit(X, y)

    _, axes = plt.subplots(1, 2, figsize=figaspect(1 / 2))
    for ax, title, model in zip(axes, ['多項式回帰 (正則化なし)', 'リッジ回帰 (正則化あり)'],
                                [linear, ridge]):
        ax.scatter(x, y)
        ax.plot(xx, model.predict(XX))
        ax.set(title=title,
               xlim=(x_min, x_max),
               ylim=(y_min, y_max),
               xticks=(),
               yticks=())

    plt.show()


def show():
    style = dict(description_width='initial')
    alpha = FloatLogSlider(value=0,
                           base=10,
                           min=-7,
                           max=4,
                           step=1,
                           description=r'正則化の強さ $\alpha$',
                           continuous_update=False,
                           style=style)
    interact(plot, alpha=alpha)
