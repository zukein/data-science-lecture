#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
pd.set_option('max_rows', 5)

#%% [markdown]
# ###### 練習問題
#
# economicsデータセットの`psavert`列を折れ線グラフで表示する。

#%%
economics = pd.read_csv('data/economics.csv', parse_dates=[0])
print('economics')
display(economics)

#%%1

#%%2

#%%3

#%%4

#%%5
