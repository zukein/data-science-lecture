#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import string
import numpy as np
from scipy.stats import norm
import pandas as pd
from IPython.display import display
pd.set_option('max_rows', 5)

#%%
n_sample = 1000
n_features = 5
np.random.seed(1234)
sample = pd.DataFrame(
    np.random.normal(size=(n_sample, n_features)),
    columns=[string.ascii_uppercase[i] for i in range(n_features)])
for i, rate in enumerate(np.linspace(0, 0.5, n_features)):
    missing = np.random.choice(n_sample,
                               size=int(n_sample * rate),
                               replace=False)
    sample.iloc[missing, i] = np.nan

print('sample')
display(sample)

#%% [markdown]
# ###### 練習問題
#
# 正規分布で$\pm 3\sigma$範囲に含まれる値の割合を求める。

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# 中央絶対偏差を求める以下の関数 mad を完成させる。


#%%1
def mad(x):
    return


#%%2
def mad(x):
    return


#%%3
def mad(x):
    return


#%%4
def mad(x):
    return


#%%5
def mad(x):
    return


#%%
mad(sample['A'])

#%% [markdown]
# ###### 練習問題
#
# 標準正規分布の $75\%$ 点を求め、 $0.6744897501960817$ と比較する。
# $1$ を標準正規分布の $75\%$ 点で割り、 $1.4826$ と比較する。

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# Hampel 判別法に基づいて外れ値かどうかを判定する (外れ値でない場合に True 、外れ値の場合に False を返す) 以下の関数 Hampel を完成させる。


#%%1
def hampel(ndarray):
    return


#%%2
def hampel(ndarray):
    return


#%%3
def hampel(ndarray):
    return


#%%4
def hampel(ndarray):
    return


#%%5
def hampel(ndarray):
    return


#%%
sample.loc[hampel(sample['A'])]

#%% [markdown]
# ###### 練習問題
#
# 箱ひげ図における外れ値かどうかを判定する (外れ値でない場合に True 、外れ値の場合に False を返す) 以下の関数 isin_box を完成させる。


#%%1
def isin_box(ndarray):
    return


#%%2
def isin_box(ndarray):
    return


#%%3
def isin_box(ndarray):
    return


#%%4
def isin_box(ndarray):
    return


#%%5
def isin_box(ndarray):
    return


#%%
sample.loc[isin_box(sample['A'])]
