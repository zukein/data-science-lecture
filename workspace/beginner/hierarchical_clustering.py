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
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import AgglomerativeClustering
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('max_rows', 5)

#%% [markdown]
# ## 階層的クラスタリング (hierarchical clustering)
# ---
# データを構造的に分割する手法。

#%%
arrests = pd.read_csv('data/USArrests.csv', index_col=0)
print('arrests')
display(arrests)

#%%
from helpers.hierarchical_clustering import visualization
visualization.show(arrests, arrests.index)

#%% [markdown]
# ## Pythonでの階層的クラスタリング実行方法
# ---
# `scipy.cluster.hierarchy.linkage`や`sklearn.cluster.AgglomerativeClustering`を、可視化には`scipy.cluster.hierarchy.dendrogram`を用いる。
# よほど特殊な事情がなければ`scipy`を使ったほうがよい。

#%%
iris = sns.load_dataset('iris').sample(n=40, random_state=1234).sort_index()
print('iris')
display(iris)

#%%
help(linkage)

#%%
help(dendrogram)

#%%
Z = linkage(iris.loc[:, 'sepal_length':'petal_width'].values, 'ward')
dendrogram(
    Z,
    labels=iris['species'].values,
    leaf_rotation='vertical',
    leaf_font_size=11)
plt.show()

#%%
help(AgglomerativeClustering)

#%%
model = AgglomerativeClustering(linkage='ward')
model.fit(iris.loc[:, 'sepal_length':'petal_width'].values)
children = model.children_
distance = np.arange(children.shape[0])
no_of_observations = np.arange(2, children.shape[0] + 2)
Z = np.column_stack([children, distance, no_of_observations]).astype(float)
dendrogram(
    Z,
    labels=iris['species'].values,
    leaf_rotation='vertical',
    leaf_font_size=11)
plt.show()

#%% [markdown]
# ###### 練習問題
#
# mpg データセットの任意の変数 (複数) を元に階層的クラスタリングを実行する。その後、得られたクラスタに何らかの意味づけができそうか考える。

#%%
mpg = sns.load_dataset('mpg')
print('mpg')
display(mpg)
