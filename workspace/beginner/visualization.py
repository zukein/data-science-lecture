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
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import seaborn as sns
from IPython.display import display
from ipywidgets import interact
pd.set_option('max_rows', 5)

#%% [markdown]
# ## 考えてみる
# ---
# 1変数のデータを視覚的に表現する手法で知っているものを挙げる。
#%% [markdown]
# ## GUIで実行してみる
#%% [markdown]
# ### 分布の確認
# ---
# RStudio の Console に`library(Rcmdr)`と入力して、 R commander を起動。
#
# - `データ` -> `データのインポート` -> `テキストファイルまたはクリップボード, URLから`
#
# として、`ファイル内に変数名あり`のチェックを外し、`フィールドの区切り記号`を`カンマ`にし、`OK`をクリック。
#
# `workspace/data/islands.csv`を読み込む。
# `データセットを表示`をクリックし、内容を確認。
#
# - `データ` -> `アクティブデータセット` -> `ケース名の設定`
#
# として、`V1`を選択し、`OK`をクリック。
#
# 再度データセットを確認。
#
# - `グラフ` -> `ヒストグラム`
#
# としてヒストグラムを表示。
#%% [markdown]
# ### 外れ値の確認
# ---
# RStudio の Console に`library(Rcmdr)`と入力して、 R commander を起動。
#
# - `データ` -> `データのインポート` -> `テキストファイルまたはクリップボード, URLから`
#
# として、`フィールドの区切り記号`を`カンマ`にし、`OK`をクリック。
#
# `workspace/data/InsectSprays.csv`を読み込む。
# `データセットを表示`をクリックし、内容を確認。
#
# - `グラフ` -> `箱ひげ図`
#
# として、`層別のプロット`から`spray`を選択し、箱ひげ図を表示。
#%% [markdown]
# ## 棒グラフ (bar plot)
# ---
# **カテゴリ別**の数量を把握するのに用いる。

#%%
from helpers.visualization import bar_plot
bar_plot.show()

#%% [markdown]
# ### Pythonでの棒グラフ表示
# ---
# `seaborn.barplot`、`pandas.DataFrame.plot.bar`、`matplotlib.pyplot.bar`などを用いる。
#
# `seaborn`や`pandas`の機能を用いると綺麗なグラフが簡単に描けるが、どちらも`matplotlib`のラッパーなので細かい調整は`matplotlib`の該当部分のドキュメントを参照する。

#%%
tips = pd.read_csv('data/tips.csv')
print('tips')
display(tips)

#%%
help(sns.barplot)

#%%
sns.barplot('day', 'total_bill', data=tips.groupby('day').sum().reset_index())
plt.title('曜日別売り上げ')
plt.show()

#%%
help(pd.DataFrame.plot.bar)

#%%
tips.groupby('sex').mean().reset_index().plot.bar('sex', 'tip')
plt.title('性別ごとチップ平均')
plt.show()

#%%
help(plt.bar)

#%%
plt.bar('time', 'size', data=tips.groupby('time').sum().reset_index())
plt.title('時間帯別入店者数')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# tipsデータセットを`smoker`を基準に`total_bill`の平均を集計した以下の`data`を利用して、棒グラフを表示してみる。

#%%
data = tips.groupby('smoker').mean()['total_bill']
data

#%%

#%% [markdown]
# ## ヒストグラム (histogram)
# ---
# 横軸に階級 (値の範囲) 、縦軸に度数 (頻度) をとったグラフ。
# **データ分布の形や偏り**がないかなどを確認するのに利用する。

#%%
from helpers.visualization import histogram
histogram.show()

#%% [markdown]
# 山が複数ある場合には、性質の異なる複数のグループが混在している可能性がある。
# 外れ値をどこに設定するか、区間の数をいくつに設定するかなどで印象が全く異なるので、複数表示して確認する。
#%% [markdown]
# ###### 練習問題
#
# 以下を実行する関数`histogram`を完成させる。
# 1. `pandas.cut`を使い、`tips`データセットのカラム`tip`を等間隔の`10`階級に分割する。
# 1. 分割した階級別のデータ数を集計し棒グラフを描画して、自分でヒストグラムを作ってみる。

#%%
help(pd.cut)


#%%
def histogram(series):
    # pd.cutを使い、階級を分割

    # 'label'カラムにx軸、'tip'カラムにy軸の値が入ったデータフレームdfを作成する

    df.plot.bar('label', 'tip', width=1.0, color=sns.color_palette()[0])
    plt.xticks(rotation=45)
    plt.show()


#%%
histogram(tips['tip'])

#%% [markdown]
# ### Pythonでのヒストグラム表示
# ---
# `seaborn.distplot`、`pandas.DataFrame.hist`、`matplotlib.pyplot.hist`などを用いる。

#%%
help(sns.distplot)

#%%
sns.distplot(tips['total_bill'])
plt.show()

#%%
help(pd.DataFrame.hist)

#%%
tips.hist('total_bill')
plt.show()

#%%
help(plt.hist)

#%%
plt.hist('total_bill', data=tips)
plt.show()

#%% [markdown]
# ###### 練習問題
#
# `bins`を`10, 20, ... ,100`と変えてみて、ヒストグラムから受ける印象を比べてみる。

#%%

#%% [markdown]
# ## 箱ひげ図 (box plot)
# ---
# 中央値・四分位点・外れ値を一度に可視化できるグラフ。

#%%
from helpers.visualization import boxplot
boxplot.show()

#%% [markdown]
# - 四角 (箱) の上下間 = 四分位範囲 (25%点 ~ 75%点)
# - 四角 (箱) の中の線 = 中央値
# - 上下に伸びた線 (ひげ) = 箱の上 (下) から箱の高さの1.5倍を延長した範囲内で最大 (最小) のデータ点 (データの最小値・最大値は超えない)
# - 上下の点 = 外れ値
#%% [markdown]
# ###### 練習問題
#
# 箱ひげ図を描画する関数`boxplot`を完成させる。

#%%
sepal_width = sns.load_dataset('iris')['sepal_width']
print('sepal_width')
display(sepal_width)


#%%
def boxplot(nparray):
    # 変数medianに中央値を代入

    # 変数box_limに箱の下限・上限を配列で代入

    # 変数boundaryにひげの下限・上限を配列で代入

    show(nparray, median, box_lim, boundary)


#%%
def show(nparray, median, box_lim, boundary):
    color = 'blue'
    box_width = 1
    box_low, box_high = min(box_lim), max(box_lim)
    interquartile_range = box_high - box_low
    boundary_low, boundary_high = min(boundary), max(boundary)
    ax = plt.gca()
    y = nparray[np.logical_or(nparray < boundary_low, boundary_high < nparray)]
    ax.scatter(np.zeros_like(y), y)
    ax.vlines(0, boundary_low, boundary_high, zorder=-1)
    ax.hlines(boundary, -box_width / 4, box_width / 4)
    patch = Rectangle((-box_width / 2, box_low),
                      box_width,
                      interquartile_range,
                      edgecolor=color,
                      facecolor='white')
    ax.add_patch(patch)
    ax.hlines(median, -box_width / 2, box_width / 2, color=color)
    ax.set(xlim=(-box_width, box_width), xticks=())
    plt.show()


#%%
boxplot(sepal_width)

#%% [markdown]
# ### Pythonでの箱ひげ図表示
# ---
# `seaborn.boxplot`、`pandas.DataFrame.boxplot`、`matplotlib.pyplot.boxplot`などを用いる。

#%%
iris = sns.load_dataset('iris').drop(columns='species')
print('iris')
display(iris)

#%%
help(sns.boxplot)

#%%
sns.boxplot(data=iris)
plt.show()

#%%
help(pd.DataFrame.boxplot)

#%%
iris.boxplot()
plt.show()

#%%
help(plt.boxplot)

#%%
plt.boxplot(iris.T)
plt.show()

#%% [markdown]
# ###### 練習問題
#
# :todo
# 箱ひげ図を描画する演習の追加
