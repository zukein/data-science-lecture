#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
import seaborn as sns
from IPython.display import display
pd.set_option('max_rows', 5)

#%% [markdown]
# ## ケーススタディ
# ---
# マーケティング担当者として施策を考えるにあたり、累積購入金額に基づき顧客が 3 つのグループに分けられるのではないかと思っている。どのような方法が考えられるか。
#%% [markdown]
# ## k 平均法 (k-means)
# ---
# クラスタ数 k を指定して、データを分割する手法。

#%%
iris = sns.load_dataset('iris')
print('iris')
display(iris)
plt.figure(figsize=figaspect(1))
ax = plt.axes()
iris.plot.scatter('sepal_length', 'sepal_width', c='black', ax=ax)
ax.set(xticks=(), yticks=())
plt.show()

#%%
from helpers.kmeans import visualization
visualization.show(iris[['sepal_length', 'sepal_width']])

#%% [markdown]
# ## Pythonでのk-meansクラスタリング実行方法
# ---
# `sklearn.cluster.KMeans`を用いる。

#%%
help(KMeans)

#%%
km = KMeans(n_clusters=3, random_state=1234, n_jobs=-1)
data = iris[['petal_length', 'petal_width']].values
km.fit(data)
pred = km.predict(data)
print(pred)

#%%
plt.scatter(data[:, 0], data[:, 1], c=pred)
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# mpg データセットの任意の変数 (複数) を元にいくつのクラスタに分けられそうか考え、 k-means クラスタリングを実行する。その後、意図した通りにクラスタリングできているか確認する。

#%%
mpg = sns.load_dataset('mpg')
print('mpg')
display(mpg)
