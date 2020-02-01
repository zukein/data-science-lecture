import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, Lasso
from ipywidgets import interact, FloatLogSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

n = 10
degree = 10
n_valid_feature = 3
margin = 0.1
size = 5

np.random.seed(1234)

poly = PolynomialFeatures(degree=degree, include_bias=False)
poly.fit(np.zeros(n).reshape((-1, 1)))
scaler = StandardScaler()


def get_multinomial(x):
    return poly.transform(x.reshape((-1, 1)))


x = np.linspace(-1, 1, n)
X = get_multinomial(x)
X = scaler.fit_transform(X)
all_features = np.arange(X.shape[1])
np.random.shuffle(all_features)
valid_features = all_features[:n_valid_feature]
coef = np.random.uniform(-0.1, 0.1, (n_valid_feature, 1))
noise = np.random.normal(0, 0.01, (n))
y = X[:, valid_features].dot(coef).ravel() + noise

x_min, x_max = x.min() - margin, x.max() + margin
y_min, y_max = y.min() - margin, y.max() + margin
xx = np.linspace(x_min, x_max, 150)
XX = scaler.transform(get_multinomial(xx))

linear = LinearRegression().fit(X, y)


def plot(alpha):
    lasso = Lasso(alpha=alpha, max_iter=100000).fit(X, y)

    _, axes = plt.subplots(1, 2, figsize=figaspect(1 / 2))

    for ax, title, model in zip(axes, ['多項式回帰 (正則化なし)', 'ラッソ回帰 (正則化あり)'],
                                [linear, lasso]):
        ax.scatter(x, y)
        ax.plot(xx, model.predict(XX))
        ax.set(title=title,
               xlim=(x_min, x_max),
               ylim=(y_min, y_max),
               xticks=(),
               yticks=())

    plt.show()


def show():
    alpha = FloatLogSlider(value=0,
                           base=10,
                           min=-5,
                           max=-1,
                           step=0.5,
                           description=r'正則化の強さ $\alpha$',
                           continuous_update=False,
                           style={'description_width': 'initial'})
    interact(plot, alpha=alpha)
