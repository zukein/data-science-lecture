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
pd.set_option('max_rows', 5)

#%%
tips = pd.read_csv('data/tips.csv')
print('tips')
display(tips)

#%% [markdown]
# ###### 練習問題
#
# tipsデータセットを`smoker`を基準に`total_bill`の平均を集計した以下の`data`を利用して、棒グラフを表示してみる。

#%%
data = tips.groupby('smoker').mean()['total_bill']
data

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# 以下を実行する関数`histogram`を完成させる。
# 1. `pandas.cut`を使い、`tips`データセットのカラム`tip`を等間隔の`10`階級に分割する。
# 1. 分割した階級別のデータ数を集計し棒グラフを描画して、自分でヒストグラムを作ってみる。


#%%1
def histogram(series):
    # pd.cutを使い、階級を分割

    # 'label'カラムにx軸、'tip'カラムにy軸の値が入ったデータフレームdfを作成する

    df.plot.bar('label', 'tip', width=1.0, color=sns.color_palette()[0])
    plt.xticks(rotation=45)
    plt.show()


#%%2
def histogram(series):
    # pd.cutを使い、階級を分割

    # 'label'カラムにx軸、'tip'カラムにy軸の値が入ったデータフレームdfを作成する

    df.plot.bar('label', 'tip', width=1.0, color=sns.color_palette()[0])
    plt.xticks(rotation=45)
    plt.show()


#%%3
def histogram(series):
    # pd.cutを使い、階級を分割

    # 'label'カラムにx軸、'tip'カラムにy軸の値が入ったデータフレームdfを作成する

    df.plot.bar('label', 'tip', width=1.0, color=sns.color_palette()[0])
    plt.xticks(rotation=45)
    plt.show()


#%%4
def histogram(series):
    # pd.cutを使い、階級を分割

    # 'label'カラムにx軸、'tip'カラムにy軸の値が入ったデータフレームdfを作成する

    df.plot.bar('label', 'tip', width=1.0, color=sns.color_palette()[0])
    plt.xticks(rotation=45)
    plt.show()


#%%5
def histogram(series):
    # pd.cutを使い、階級を分割

    # 'label'カラムにx軸、'tip'カラムにy軸の値が入ったデータフレームdfを作成する

    df.plot.bar('label', 'tip', width=1.0, color=sns.color_palette()[0])
    plt.xticks(rotation=45)
    plt.show()


#%%
histogram(tips['tip'])

#%% [markdown]
# ###### 練習問題
#
# `bins`を`10, 20, ... ,100`と変えてみて、ヒストグラムから受ける印象を比べてみる。

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# 箱ひげ図を描画する関数`boxplot`を完成させる。

#%%
sepal_width = sns.load_dataset('iris')['sepal_width']
print('sepal_width')
display(sepal_width)


#%%1
def boxplot(nparray):
    # 変数medianに中央値を代入

    # 変数box_limに箱の下限・上限を配列で代入

    # 変数boundaryにひげの下限・上限を配列で代入

    show(nparray, median, box_lim, boundary)


#%%2
def boxplot(nparray):
    # 変数medianに中央値を代入

    # 変数box_limに箱の下限・上限を配列で代入

    # 変数boundaryにひげの下限・上限を配列で代入

    show(nparray, median, box_lim, boundary)


#%%3
def boxplot(nparray):
    # 変数medianに中央値を代入

    # 変数box_limに箱の下限・上限を配列で代入

    # 変数boundaryにひげの下限・上限を配列で代入

    show(nparray, median, box_lim, boundary)


#%%4
def boxplot(nparray):
    # 変数medianに中央値を代入

    # 変数box_limに箱の下限・上限を配列で代入

    # 変数boundaryにひげの下限・上限を配列で代入

    show(nparray, median, box_lim, boundary)


#%%5
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
