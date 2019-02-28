#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from IPython.display import display
import matplotlib.pyplot as plt
pd.set_option('max_rows', 5)

#%% [markdown]
# ## 単回帰分析 (simple linear regression analysis)
# ---
# ある変数 $x$ によって別の変数 $y$ を $y=ax+b$ という形で説明・予測しようとする手法。
# データ中に存在する変数 $x$ の係数 $a$ を回帰係数 (coefficient) 、 $b$ を切片項 (intercept) という。 ( $b$ を含めて回帰係数と呼ぶこともある)

#%%
from helpers.simple_linear_regression_analysis import regression_line
regression_line.show()

#%% [markdown]
# ## 最小二乗法 (ordinary least squares)
# ---
# データから回帰直線 $y=ax+b$ を求めるにあたって、データ中の正解 $y$ と予測値 $\hat{y}$ の差が小さくなるように $a,b$ を決めたい。このとき、正解と予測の差の二乗 $(y-\hat{y})^{2}$ が最小になるように $a,b$ を決めるのが最小二乗法。

#%%
from helpers.simple_linear_regression_analysis import ols
ols.show()

#%% [markdown]
# ###### 練習問題
#
# $b=0$ として、$a$ を横軸、 $\displaystyle \sum ^{n}_{i=1}\left( y-\hat{y}\right)^{2}$ の値を縦軸にとり、 $a$ の値を変化させたときのグラフを表示する。

#%%
x, y = make_regression(n_features=1, random_state=1234)
reg = pd.DataFrame(dict(x=x.ravel(), y=y))
print('reg')
display(reg)

#%%
x = reg['x'].values.reshape((1, -1))
y = reg['y'].values
a = np.linspace(-500, 500, 20).reshape((-1, 1))
e = ((y - a * x)**2).sum(axis=1)
plt.plot(a, e)
plt.xlabel('a')
plt.show()

#%% [markdown]
# ## 回帰係数の標準誤差
# ---
# 回帰直線はサンプリングされたデータを元に求めるので、サンプリングを繰り返すと毎回異なる回帰直線が得られる。つまり、回帰係数も何らかの確率分布に従う確率変数である。その分布の標準偏差 (の推定量) を回帰係数の標準誤差という。

#%%
from helpers.simple_linear_regression_analysis import standard_error
standard_error.show()

#%% [markdown]
# ## Pythonでの回帰直線の求め方
# ---
# `sklearn.linear_model.LinearRegression`を用いる。

#%%
print('reg')
display(reg)

#%%
help(LinearRegression)

#%%
# 最初にインスタンスを作成
model = LinearRegression()
# fitメソッドで回帰直線を求める
# xはサイズが(サンプル数 × 変数の数)の行列でなければならない
x = reg['x'].values.reshape((-1, 1))
y = reg['y']
model.fit(x, y)
# 回帰係数はcoef_に格納
print('回帰係数', model.coef_)
# 切片はintercept_に格納
print('切片', model.intercept_)

#%% [markdown]
# ###### 練習問題
#
# 同一の母集団からサンプリングを行う関数`sampling`を用いて、 30 個のサンプルを取得して回帰直線を求める操作を 10,000 回繰り返し、得られた回帰係数から標準誤差を推定する。


#%%
def sampling(size):
    x = np.random.normal(size=size)
    y = 2 * x + np.random.normal(scale=0.3, size=size)
    return pd.DataFrame(dict(x=x, y=y))


print('samplingの使用例')
print('sampling(30)')
np.random.seed(1234)
display(sampling(30))

#%%
coef = np.zeros(10000)
for i in range(10000):
    data = sampling(30)
    model = LinearRegression().fit(data['x'].values.reshape((-1, 1)),
                                   data['y'])
    coef[i] = model.coef_
print(f'標準誤差 : {np.std(coef, ddof=1):.3f}')
