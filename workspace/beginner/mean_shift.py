#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import pandas as pd
from sklearn.cluster import MeanShift
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('max_rows', 5)

#%% [markdown]
# ###### 練習問題
#
# mpg データセットの任意の変数 (複数) を元に Mean Shift クラスタリングを実行する。その後、得られたクラスタに何らかの意味づけができそうか考える。

#%%
mpg = sns.load_dataset('mpg')
print('mpg')
display(mpg)

#%%1

#%%2

#%%3

#%%4

#%%5
