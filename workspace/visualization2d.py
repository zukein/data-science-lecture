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

#%% [markdown]
# ## 層別グラフ
# ---
# ある特徴 (通常はカテゴリカル変数の値) によって、いくつかのグループに分けられたグラフ。
# グループごとに傾向の差があるのか比較するのに用いる。
#%% [markdown]
# ### 層別棒グラフ

#%%
va = pd.read_csv('data/VADeaths.csv', index_col=0)
print('va')
display(va)

va.plot.bar()
plt.show()

#%% [markdown]
# #### Pythonでの層別棒グラフ表示
# ---
# `seaborn.countplot`、`pandas.DataFrame.plot.bar`などを用いる。

#%%
help(sns.countplot)

#%%
sns.countplot('day', hue='sex', data=tips)
plt.title('性別でグループ分けした曜日ごとのデータ数')
plt.show()

#%%
pd.crosstab(
    tips['day'], tips['smoker'], values=tips['total_bill'],
    aggfunc=sum).plot.bar()
plt.title('喫煙者かどうかでグループ分けした曜日ごとの売り上げ')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# tipsデータセットの`time`列でグループ分けし、`day`ごとのデータ数を層別棒グラフで表示する。

#%%
print('tips')
display(tips)

#%%

#%% [markdown]
# ### 積み上げ棒グラフ
# ---
# カテゴリ別の値を縦に積み上げた棒グラフ。全体の変化や割合の変化を見るために用いる。

#%%
print('va')
display(va)
va.plot.bar(stacked=True)
plt.show()

#%% [markdown]
# #### Pythonでの積み上げ棒グラフ表示
# ---
# `pandas.DataFrame.plot.bar`を用いる。

#%%
help(pd.DataFrame.plot.bar)

#%%
pd.crosstab(
    tips['day'], tips['smoker'], values=tips['total_bill'],
    aggfunc=sum).plot.bar(stacked=True)
plt.title('喫煙者かどうかでグループ分けした曜日ごとの売り上げ')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# tipsデータセットの`sex`列でグループ分けし、`day`ごとのデータ数を積み上げ棒グラフで表示する。

#%%
print('tips')
display(tips)

#%%

#%% [markdown]
# ### 100%積み上げ棒グラフ
# ---
# 積み上げ棒グラフの高さを揃えたグラフ。割合の変化を見るのに用いる。

#%%
print('va')
display(va)
va.apply(lambda x: x / va.sum(axis=1), axis=0).plot.bar(stacked=True)
plt.show()

#%% [markdown]
# #### Pythonでの100%積み上げ棒グラフ表示
# ---
# データセットの数値を割合に計算し直してから、`pandas.DataFrame.plot.bar`を用いる。

#%%
pd.crosstab(
    tips['day'],
    tips['smoker'],
    values=tips['total_bill'],
    aggfunc=sum,
    normalize='index').plot.bar(stacked=True)
plt.title('喫煙者かどうかでグループ分けした曜日ごとの売り上げ')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# tipsデータセットの`smoker`列でグループ分けし、`day`ごとのデータ数を100%積み上げ棒グラフで表示する。

#%%
print('tips')
display(tips)

#%%

#%% [markdown]
# ### 層別箱ひげ図

#%%
print('iris')
display(iris)

iris.boxplot('sepal_length', by='species')
plt.show()

#%% [markdown]
# #### Pythonでの層別箱ひげ図表示
# ---
# `seaborn.boxplot`、`pandas.DataFrame.boxplot`などを用いる。

#%%
print('tips')
display(tips)

#%%
help(sns.boxplot)

#%%
sns.boxplot('day', 'total_bill', hue='smoker', data=tips)
plt.title('喫煙家どうかでグループ分けされた、曜日別支払額の箱ひげ図')
plt.show()

#%%
help(pd.DataFrame.boxplot)

#%%
tips.boxplot('tip', by='day')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# irisデータセットの`species`列でグループ分けし、`petal_length`列の箱ひげ図を表示する。

#%%
print('iris')
display(iris)

#%%

#%% [markdown]
# ### 層別散布図

#%%
whiteside = pd.read_csv('data/whiteside.csv')
print('whiteside')
display(whiteside)

whiteside.plot.scatter(
    x='Temp',
    y='Gas',
    c=whiteside['Insul'].astype('category').cat.rename_categories(
        ['blue', 'red']))
plt.show()

#%% [markdown]
# #### Pythonでの層別散布図表示
# ---
# `seaborn.scatterplot`、`pandas.DataFrame.plot.scatter`、`matplotlib.pyplot.scatter`などを用いる。

#%%
print('mpg')
display(mpg)

#%%
help(sns.scatterplot)

#%%
sns.scatterplot('horsepower', 'mpg', hue='cylinders', data=mpg)
plt.title('シリンダー数でグループ分けした馬力と燃費の関係')
plt.show()

#%%
help(pd.DataFrame.plot.scatter)

#%%
mpg.plot.scatter('weight', 'mpg', c='cylinders')
plt.title('シリンダー数でグループ分けした重量と燃費の関係')
plt.show()

#%%
help(plt.scatter)

#%%
for label in sorted(mpg['cylinders'].unique()):
    plt.scatter(
        'weight',
        'horsepower',
        data=mpg.query('cylinders==@label'),
        label=label)
plt.legend()
plt.title('シリンダー数でグループ分けした重量と馬力の関係')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# irisデータセットの`species`列でグループ分けし、 x 軸を`petal_length`、 y 軸を`petal_width`にして散布図を表示する。

#%%
print('iris')
display(iris)

#%%

#%% [markdown]
# ### インタラクティブなグラフ表示
# ---
# 層別グラフは表示するカテゴリをインタラクティブに選択できると生産的。
#%% [markdown]
# #### Plotly
# ---
# Pythonの代表的なインタラクティブな表現のできるグラフライブラリ。
# 引数のネストが深すぎてドキュメントが使いにくいので、サンプルにある以上の細かいカスタマイズはやらないほうが無難。どうしてもやる場合はエラーメッセージのほうがわかりやすいので、なさそうな引数名を適当に入れてエラーメッセージをたどっていくのが効率的。

#%%
from plotly.offline import init_notebook_mode
import plotly.offline as py
import plotly.graph_objs as go
init_notebook_mode(connected=True)

data = []
for label in sorted(mpg['cylinders'].unique()):
    subset = mpg.query('cylinders==@label')
    trace = go.Scatter(
        x=subset['weight'],
        y=subset['horsepower'],
        name=str(label),
        mode='markers',
        hovertext=subset['name'])
    data.append(trace)
layout = dict(title='シリンダー数でグループ分けした重量と馬力の関係')
fig = dict(data=data, layout=layout)
py.iplot(fig)

#%% [markdown]
# #### BIツール
# ---
# 有料のものが多いが、その分データの可視化では生産性が上がる。
