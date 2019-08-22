#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic
pd.set_option('max_rows', 5)

#%% [markdown]
# ###### 練習問題
#
# irisデータセットの`petal_length`を x 軸、`petal_width`を y 軸にとった散布図を表示してみる。

#%%
iris = sns.load_dataset('iris')
print('iris')
display(iris)

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# tipsデータセットの`day`列と`smoker`列を用いて、モザイク図を表示してみる。

#%%
tips = sns.load_dataset('tips')
print('tips')
display(tips)

#%%1

#%%2

#%%3

#%%4

#%%5
