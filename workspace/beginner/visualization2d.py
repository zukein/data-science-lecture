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
# ## 考えてみる
# ---
# 2変数のデータ間の関係を視覚的に表現する手法で知っているものを挙げる。
#%% [markdown]
# ## GUIで実行してみる
#%% [markdown]
# ### 分布の確認
# ---
# RStudio のコンソールに`library(Rcmdr)`と入力して、 R Commander を起動。
#
# - `データ` -> `データのインポート` -> `テキストファイルまたはクリップボード, URLから`
#
# として、`フィールドの区切り記号`を`カンマ`にし、`OK`をクリック。`workspace/data/whiteside.csv`を読み込む。`データセットを表示`をクリックし、内容を確認。
#
# - `グラフ` -> `散布図`
#
# として、`x変数`に`Gas`、`y変数`に`Temp`を選択して、`OK`をクリック。散布図を確認。
#%% [markdown]
# ### グループ間比較
# ---
# RStudio のコンソールに`library(Rcmdr)`と入力して、 R Commander を起動。
#
# - `データ` -> `データのインポート` -> `テキストファイルまたはクリップボード, URLから`
#
# として、`フィールドの区切り記号`を`カンマ`にし、`OK`をクリック。`workspace/data/whiteside.csv`を読み込む。`データセットを表示`をクリックし、内容を確認。
#
# - `グラフ` -> `散布図`
#
# として、`x変数`に`Gas`、`y変数`に`Temp`、`層別のプロット`で`Insul`を選択して、`OK`をクリック。層別散布図を確認。
#%% [markdown]
# ## 散布図 (scattergram, scatter plot)
# ---
# 2変数間の関係を視覚的に表すグラフ。

#%%
mpg = sns.load_dataset('mpg')
sns.scatterplot('mpg', 'acceleration', data=mpg)
plt.title('燃費と加速力の関係')
plt.show()

#%% [markdown]
# ### Pythonでの散布図表示
# ---
# `seaborn.scatterplot`、`pandas.DataFrame.plot.scatter`、`matplotlib.pyplot.scatter`などを用いる。

#%%
print('mpg')
display(mpg)

#%%
help(sns.scatterplot)

#%%
sns.scatterplot('horsepower', 'mpg', data=mpg)
plt.title('馬力と燃費の関係')
plt.show()

#%%
help(pd.DataFrame.plot.scatter)

#%%
mpg.plot.scatter('weight', 'mpg')
plt.title('重量と燃費の関係')
plt.show()

#%%
help(plt.scatter)

#%%
plt.scatter('weight', 'horsepower', data=mpg)
plt.title('重量と馬力の関係')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# irisデータセットの`petal_length`を x 軸、`petal_width`を y 軸にとった散布図を表示してみる。

#%%
iris = sns.load_dataset('iris')
print('iris')
display(iris)

#%%

#%%
iris.plot.scatter('petal_length', 'petal_width')
plt.show()

#%% [markdown]
# ## モザイク図 (mosaic plot)
# ---
# クロス集計表の視覚化などに利用する。数値の大きさを面積で表す。
#
# `statsmodels.graphics.mosaicplot.mosaic`を用いる。

#%%
titanic = pd.read_csv('data/Titanic.csv')
print('titanic')
display(titanic)

#%%
help(mosaic)

#%%
mosaic(titanic, ['Class', 'Survived'])
plt.show()

#%% [markdown]
# ###### 練習問題
#
# tipsデータセットの`day`列と`smoker`列を用いて、モザイク図を表示してみる。

#%%
tips = sns.load_dataset('tips')
print('tips')
display(tips)

#%%

#%%
mosaic(tips, ['day', 'smoker'])
plt.show()
