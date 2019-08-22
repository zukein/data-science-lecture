#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace/beginner'))
    print(os.getcwd())
except:
    pass

#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
pd.set_option('max_rows', 5)

#%%
tips = sns.load_dataset('tips')
print('tips')
display(tips)

#%% [markdown]
# ###### 練習問題
#
# tipsデータセットの`time`列でグループ分けし、`day`ごとのデータ数を層別棒グラフで表示する。

#%%
print('tips')
display(tips)

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# tipsデータセットの`sex`列でグループ分けし、`day`ごとのデータ数を積み上げ棒グラフで表示する。

#%%
print('tips')
display(tips)

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# tipsデータセットの`smoker`列でグループ分けし、`day`ごとのデータ数を100%積み上げ棒グラフで表示する。

#%%
print('tips')
display(tips)

#%%1

#%%2

#%%3

#%%4

#%%5

#%%
iris = sns.load_dataset('iris')
print('iris')
display(iris)

iris.boxplot('sepal_length', by='species')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# irisデータセットの`species`列でグループ分けし、`petal_length`列の箱ひげ図を表示する。

#%%
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
# irisデータセットの`species`列でグループ分けし、 x 軸を`petal_length`、 y 軸を`petal_width`にして散布図を表示する。

#%%
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
# economicsデータセットの`psavert`列と`uempmed`列を折れ線グラフで表示する。

#%%
economics = pd.read_csv('data/economics.csv', parse_dates=[0])
print('economics')
display(economics)

#%%1

#%%2

#%%3

#%%4

#%%5
