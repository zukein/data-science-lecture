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
from matplotlib.figure import figaspect
import seaborn as sns
pd.set_option('max_rows', 5)

#%% [markdown]
# ## Mean Shift
# ---
# 特徴空間で、指定した距離内の密度に基づいてクラスタ数を求める手法。

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
from helpers.mean_shift import visualization
visualization.show(iris[['sepal_length', 'sepal_width']])

#%% [markdown]
# ## PythonでのMean Shiftクラスタリング実行方法
# ---
# `sklearn.clusterMeanShift`を用いる。 bandwidth は指定しなければ、自動的にアルゴリズムから決める。

#%%
help(MeanShift)

#%%
ms = MeanShift(n_jobs=-1)
data = iris[['petal_length', 'petal_width']].values
ms.fit(data)
pred = ms.predict(data)
print(pred)

#%%
plt.scatter(data[:, 0], data[:, 1], c=pred)
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# mpg データセットに k-means クラスタリングを適用し、得られたクラスタに何らかの意味づけができそうか考える。

#%%
mpg = sns.load_dataset('mpg')
print('mpg')
display(mpg)
