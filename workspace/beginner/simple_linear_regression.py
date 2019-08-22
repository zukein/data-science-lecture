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
# ###### 練習問題
#
# $b=0$ として、$a$ を横軸、 $\displaystyle \sum ^{n}_{i=1}\left( y-\hat{y}\right)^{2}$ の値を縦軸にとり、 $a$ の値を変化させたときのグラフを表示する。

#%%
x, y = make_regression(n_features=1, random_state=1234)
reg = pd.DataFrame(dict(x=x.ravel(), y=y))
print('reg')
display(reg)

#%%1

#%%2

#%%3

#%%4

#%%5

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

#%%1

#%%2

#%%3

#%%4

#%%5
