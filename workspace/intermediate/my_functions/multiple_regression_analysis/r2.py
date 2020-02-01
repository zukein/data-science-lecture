import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
import statsmodels.api as sm
from ipywidgets import interact, IntSlider
from IPython.display import display

n_samples = 1000
X, y = make_regression(n_samples=n_samples,
                       n_features=2,
                       n_informative=2,
                       noise=20.0,
                       random_state=1234)


def r2(k):
    if k > 2:
        np.random.seed(1234)
        X_large = np.hstack((X, np.random.normal(size=(n_samples, k - 2))))
    else:
        X_large = X
    df = pd.DataFrame(X_large, columns=[f'X{i+1}' for i in range(k)])
    result = sm.OLS(endog=y, exog=df).fit()
    print(f'決定係数 (R^2)\n{result.rsquared:.3f}')
    print(f'自由度調整済み決定係数 (Adjusted R^2)\n{result.rsquared_adj:.3f}')
    print('意味のある変数は2つだけで残りは乱数')
    display(df)


def show():
    k = IntSlider(value=2,
                  min=2,
                  max=100,
                  continuous_update=False,
                  description='変数の数')
    interact(r2, k=k)
