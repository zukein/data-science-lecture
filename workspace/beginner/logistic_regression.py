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
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from IPython.display import display
pd.set_option('max_rows', 5)

#%% [markdown]
# ###### 練習問題
#
# ロジスティック分布の累積分布関数のグラフを表示する。

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# ロジスティック分布の確率密度関数のグラフを表示する。確率密度関数 $f'( x)$ は累積分布関数を $f( x)$ とすると、以下で表される。
#
# $\displaystyle f'( x) =f( x) \times ( 1-f( x))$

#%%1

#%%2

#%%3

#%%4

#%%5

#%%
x, y = make_classification(n_features=1,
                           n_informative=1,
                           n_redundant=0,
                           n_clusters_per_class=1,
                           random_state=1234)
clf = pd.DataFrame(dict(x=x.ravel(), y=y))
print('clf')
display(clf)

#%% [markdown]
# ###### 練習問題
#
# clfデータセットの散布図とclfデータセットから学習したロジスティック回帰の予測曲線 (累積分布関数) を表示する。

#%%1

#%%2

#%%3

#%%4

#%%5
