#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import numpy as np
from scipy import stats
import pandas as pd

#%% [markdown]
# ###### 練習問題
#
# 平均を算出する関数`mean`を完成させる。 (NumPyは使わない)

#%%
np.random.seed(1234)
x = np.random.randint(1, 100, 20)
print(f'x = {x}')


#%%1
def mean(x):
    return


#%%2
def mean(x):
    return


#%%3
def mean(x):
    return


#%%4
def mean(x):
    return


#%%5
def mean(x):
    return


#%%
print(f'結果: {mean(x)}')
print(f'正解: {x.mean()}')

#%% [markdown]
# ###### 練習問題
#
# 中央値を算出する関数`median`を完成させる。 (NumPyは使わない)

#%%
np.random.seed(1234)
x = np.random.randint(1, 100, 20)
print(f'x = {x}')


#%%1
def median(x):
    return


#%%2
def median(x):
    return


#%%3
def median(x):
    return


#%%4
def median(x):
    return


#%%5
def median(x):
    return


#%%
print(f'結果: {median(x)}')
print(f'正解: {np.median(x)}')

#%% [markdown]
# ###### 練習問題
#
# 最頻値を算出する関数`mode`を完成させる。 (SciPyは使わない)

#%%
np.random.seed(1234)
x = np.random.randint(1, 10, 15)


#%%1
def mode(x):
    return


#%%2
def mode(x):
    return


#%%3
def mode(x):
    return


#%%4
def mode(x):
    return


#%%5
def mode(x):
    return


#%%
mode(x)

#%% [markdown]
# ###### 練習問題
#
# 分散を算出する関数`variance`を完成させる。 (平均の算出以外にNumPyの関数は使わない)

#%%
np.random.seed(1234)
x = np.random.normal(size=100)


#%%1
def variance(x):
    return


#%%2
def variance(x):
    return


#%%3
def variance(x):
    return


#%%4
def variance(x):
    return


#%%5
def variance(x):
    return


#%%
print(f'結果: {variance(x):.3f}')
print('正解' if np.isclose(variance(x), x.var()) else '不正解')

#%% [markdown]
# ###### 練習問題
#
# 標準偏差を算出する関数`standard_deviation`を完成させる。 (NumPyの標準偏差を算出する関数は使わない)

#%%
np.random.seed(1234)
x = np.random.normal(size=100)


#%%1
def standard_deviation(x):
    return


#%%2
def standard_deviation(x):
    return


#%%3
def standard_deviation(x):
    return


#%%4
def standard_deviation(x):
    return


#%%5
def standard_deviation(x):
    return


#%%
print(f'結果: {standard_deviation(x):.3f}')
print('正解' if np.isclose(standard_deviation(x), x.std()) else '不正解')

#%% [markdown]
# ###### 練習問題
#
# 四分位点を算出する関数`quartile`を完成させる。結果は`[25%点, 50%点, 75%点]`の配列で返す。配列`x`の長さは奇数に限定してもよい。 (NumPyの四分位点を算出する関数は使わない)

#%%
np.random.seed(1234)
x = np.random.choice(np.arange(1, 100), size=9, replace=False)


#%%1
def quartile(x):
    return


#%%2
def quartile(x):
    return


#%%3
def quartile(x):
    return


#%%4
def quartile(x):
    return


#%%5
def quartile(x):
    return


#%%
print(f'結果: {quartile(x)}')
print(f'正解: {np.percentile(x, (25, 50, 75))}')
