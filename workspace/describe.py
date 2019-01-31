#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import inspect
import numpy as np
from scipy import stats
import pandas as pd

#%% [markdown]
# ## 考えてみる
# ---
# 数値で表現されるデータを少数の指標で表すとしたら、どのようなものがありそうか。
#%% [markdown]
# ## GUIで実行してみる
# ---
# RStudio の Console に`library(Rcmdr)`と入力して、 R commander を起動。
#
# - `データ` -> `データのインポート` -> `テキストファイルまたはクリップボード, URLから`
#
# として、`フィールドの区切り記号`を`カンマ`にし、`OK`をクリック。
#
# `workspace/data/attenu.csv`を読み込む。
# `データセットを表示`をクリックし、内容を確認。
#
# - `統計量` -> `要約` -> `数値による要約`
#
# として`event`以外の変数を選択し、`OK`をクリック。
#
# RStudio の Console に戻って、結果を確認。
#%% [markdown]
# ## 最初に確認すること
# ---
#

#%%
att = pd.read_csv('data/attenu.csv')

#%% [markdown]
# データを読み込んだら、最初に**意図した通りに読み込めているか確認**する。
#%% [markdown]
# ---
#%% [markdown]
# 最初の5件を表示。 (**ヘッダー行やコメント**がデータとして読み込まれていないか確認)

#%%
att.head()

#%% [markdown]
# 表示する件数を指定できる。

#%%
att.head(3)

#%% [markdown]
# 最後の5件を表示。 (データの件数を確認)

#%%
att.tail()

#%% [markdown]
# 最初と最後の件数を指定して表示できる。

#%%
att.iloc[np.r_[0:3, -1]]

#%% [markdown]
# 特にCSVファイルなどの読み込みで、ヘッダー行が含まれていたら`header=0`として最初の行をカラム名に指定たり、不要な行が含まれていたら`skiprows`で指定した行数飛ばしたり、`comment`で`#`など指定した文字で始まるコメント行を飛ばしたりする。

#%%
help('pd.read_csv')

#%%
print('Pandasのデータ読み込み関数')
print([
    f[0] for f in inspect.getmembers(pd, inspect.isfunction)
    if f[0].startswith('read_')
])

#%% [markdown]
# ---
#%% [markdown]
# データ型を確認。 (**数値に見えて文字列**として読み込まれていないか)

#%%
att.dtypes

#%% [markdown]
# ---
#%% [markdown]
# データの件数・欠損・データ型をまとめて確認。

#%%
att.info()

#%% [markdown]
# ## 基本統計量
# ---
# データの性質を表す値のことを統計量という。よく使う基本統計量には以下のものがある。
#
# - 代表値
# - 分散・標準偏差
# - 四分位点
#%% [markdown]
# ### 代表値
# ---
# データ (データフレームのカラム) の**中心的な** (代表的な) 値を表す指標。
# 以下の3種類がある。
#
# - 平均値
# - 中央値
# - 最頻値
#%% [markdown]
# #### 平均値 (mean)
# ---
# データの重心。
#
# $n$ 個のデータをそれぞれ $x_{1} ,\ x_{2} ,\ \dots ,\ x_{n}$ とすると平均 $\bar{x}$ は
#
# $
# \begin{align}
#     \overline{x} & =\frac
#         {1}
#         {n}
#     \sum ^{n}_{i=1} x_{i}\\
#      \\
#      & =\frac
#          {x_{1} +x_{2} +\dots +x_{n}}
#          {n}
# \end{align}
# $
#
# **外れ値に引きずられやすい**ので、データに外れ値が含まれる場合や**データの分布に偏りがある**場合は中央値を用いることもある。 (分布とは、データ中のどれくらいの値にどれくらいのデータ数が集まっているかを表す言葉)
#%% [markdown]
# 例：
#
# $5$ 個のデータ $( 1,3,5,7,9)$ の平均値は $5$

#%%
x = np.arange(1, 10, 2)
print(f'x = {x}')
print(f'平均: {x.mean()}')

#%% [markdown]
# 1つのデータ $( 9)$ を外れ値 $( 20)$ に置き換えただけで、平均値が大きく変わってしまう。

#%%
x[-1] = 20
print(f'x = {x}')
print(f'平均: {x.mean()}')

#%% [markdown]
# ###### 練習問題
#
# 平均を算出する関数`mean`を完成させる。 (NumPyは使わない)

#%%
np.random.seed(1234)
x = np.random.randint(1, 100, 20)
print(f'x = {x}')


def mean(x):
    return


#%%
print(f'結果: {mean(x)}')
print(f'正解: {x.mean()}')

#%% [markdown]
# #### 中央値 (median)
# ---
# データを大きさの順で並べた場合に、真ん中に位置する値。外れ値には強いが、確率論を背景とする分析手法とは相性が悪い。
#%% [markdown]
# 例：
#
# $5$ 個のデータ $( 1,3,5,7,9)$ の中央値は $5$

#%%
x = np.arange(1, 10, 2)
print(f'x = {x}')
print(f'中央値: {np.median(x)}')

#%% [markdown]
# 1つのデータ $( 9)$ を外れ値 $( 20)$ に置き換えても、中央値は変わらない。

#%%
x[-1] = 20
print(f'x = {x}')
print(f'中央値: {np.median(x)}')

#%% [markdown]
# ###### 練習問題
#
# 中央値を算出する関数`median`を完成させる。 (NumPyは使わない)

#%%
np.random.seed(1234)
x = np.random.randint(1, 100, 20)
print(f'x = {x}')


def median(x):
    return


#%%
print(f'結果: {median(x)}')
print(f'正解: {np.median(x)}')

#%% [markdown]
# #### 最頻値 (mode)
# ---
# 最も頻繁に (多く) 現れる値。
#%% [markdown]
# 例：
#
# データ $( 1,2,2,3,3,3,3,4,4,5,5)$ の最頻値は $3$

#%%
x = [1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5]
print(f'x = {x}')
print(f'最頻値: {stats.mode(x).mode}, 出現回数: {stats.mode(x).count}')

#%% [markdown]
# ###### 練習問題
#
# 最頻値を算出する関数`mode`を完成させる。 (SciPyは使わない)

#%%
np.random.seed(1234)
x = np.random.randint(1, 10, 15)


#%%
def mode(x):
    return


#%%
mode(x)

#%% [markdown]
# #### いつ、どの代表値を使うか
#%% [markdown]
# ###### 練習問題
#
# 自分で入手可能なデータを念頭に、そのデータを他人に説明するのにどの代表値を使うのが適切か考えてみる。
#%% [markdown]
# ##### 尺度と代表値
# ---
# データの尺度がわかると、利用可能な代表値が絞り込める。
#
# <table class="text-center border">
#     <tr>
#         <th>尺度</th>
#         <th>一般的な代表値</th>
#         <th>利用可能な代表値</th>
#     </tr>
#     <tr>
#         <td>名義尺度</td>
#         <td>最頻値</td>
#         <td class="text-left">最頻値</td>
#     </tr>
#     <tr>
#         <td>順序尺度</td>
#         <td>中央値</td>
#         <td class="text-left">最頻値・中央値</td>
#     </tr>
#     <tr>
#         <td>間隔尺度</td>
#         <td>平均値</td>
#         <td class="text-left">最頻値・中央値・平均値</td>
#     </tr>
#     <tr>
#         <td>比率尺度</td>
#         <td>平均値</td>
#         <td class="text-left">最頻値・中央値・平均値</td>
#     </tr>
# </table>
#%% [markdown]
# ###### 名義尺度 (nominal scale)
# ---
# 値の**順序に意味がない**種類のデータ。
#
# - 血液型・性別など
#%% [markdown]
# ###### 順序尺度 (ordinal scale)
# ---
# 値の**順序には意味がある**が、値同士の**演算 (加減乗除) には意味がない**種類のデータ。 *(順序で並び替えて積み上げグラフなどにすること = 累積には意味がある)*
#
# - アンケートの5段階評価など
#%% [markdown]
# ###### 間隔尺度 (interval scale)
# ---
# 値の間隔には意味があり、**値同士の加算・減算が可能**だが、値同士の乗算・除算には意味がない種類のデータ。
#
# - 温度 (摂氏・華氏) ・タイムスタンプなど
#
# 摂氏10度と摂氏20度の差や摂氏20度と摂氏30度の差は共に10度だと言えるが、摂氏20度は摂氏10度の2倍の温度 (熱量) だとは言えない。同じように1970年1月1日からの経過時間を表すタイムスタンプ (UNIX時間) は、1990年1月1日が1980年1月1日の2倍の時間とは言えない。原点の取り方に任意性があり、原点自体に特別な意味がない。
#%% [markdown]
# ###### 比率尺度 (ratio scale)
# ---
# 値の比率にも意味があり (原点0に意味がある) 、**値同士の演算 (加減乗除) が可能**な種類のデータ。
#
# - 絶対温度・距離・重量など
#%% [markdown]
# ###### なぜ尺度が代表値と関係あるのか
# ---
# 代表値の算出方法ごとに、データに必要な条件がある。
#
# <table class="border">
#     <tr class="text-center">
#         <td class="border-bottom-bold border-right-bold"></td>
#         <th>算出方法</th>
#         <th>必要条件</th>
#     </tr>
#     <tr>
#         <th class="border-bottom border-right-bold">最頻値</th>
#         <td class="text-left">最も頻繁に出現する要素を割り出す</td>
#         <td class="text-left">要素ごとの出現回数をカウントできればよい</td>
#     </tr>
#     <tr>
#         <th class="border-bottom border-right-bold">中央値</th>
#         <td class="text-left">全要素を大きさの順で並び替え、真ん中の値を割り出す</td>
#         <td class="text-left">要素の大きさで順番に並び替えられないといけない</td>
#     </tr>
#     <tr>
#         <th class="border-bottom border-right-bold">平均値</th>
#         <td class="text-left">全要素を合計して、要素数で割る</td>
#         <td class="text-left">要素同士の足し算ができないといけない</td>
#     </tr>
# </table>
#
# 必要な条件を満たすかどうかは尺度から判断できる。
#
# <table class="text-center border">
#     <tr>
#         <td class="border-bottom-bold border-right-bold"></td>
#         <th>順序</th>
#         <th>加減</th>
#         <th>乗除</th>
#         <th>代表値</th>
#     </tr>
#     <tr>
#         <th class="border-bottom border-right-bold">名義尺度</th>
#         <td>×</td>
#         <td>×</td>
#         <td>×</td>
#         <td>最頻値</td>
#     </tr>
#     <tr>
#         <th class="border-bottom border-right-bold">順序尺度</th>
#         <td>○</td>
#         <td>×</td>
#         <td>×</td>
#         <td>中央値</td>
#     </tr>
#     <tr>
#         <th class="border-bottom border-right-bold">間隔尺度</th>
#         <td>○</td>
#         <td>○</td>
#         <td>×</td>
#         <td>平均値</td>
#     </tr>
#     <tr>
#         <th class="border-bottom border-right-bold">比率尺度</th>
#         <td>○</td>
#         <td>○</td>
#         <td>○</td>
#         <td>平均値</td>
#     </tr>
# </table>
#
# 平均値が算出できるときには中央値も算出でき、中央値が算出できるときには最頻値も算出できるというように、**平均値>中央値>最頻値**の上位互換関係が成り立つ。
# 上位の指標のほうがより多くの情報を使って算出 (平均値は順序だけでなく大きさも利用など) されているため、基本的には上位の指標を使うのが望ましいが、前述のように平均値は**外れ値に引きずられやすい**ので、データに外れ値が含まれる場合や**データの分布に偏りがある**場合は中央値を用いることもある。
#%% [markdown]
# ##### 質的変数 (カテゴリカル変数) と量的変数
# ---
# 名義尺度と順序尺度をまとめて質的変数 (カテゴリカル変数) 、間隔尺度と比率尺度をまとめて量的変数と呼ぶこともある。
#
# <table class="text-center border background-bright">
#     <tr>
#         <th class="border-bottom border-right-bold background-dark" rowspan="2">質的変数<br />カテゴリカル変数</th>
#         <td>名義尺度</td>
#     </tr>
#     <tr>
#         <td>順序尺度</td>
#     </tr>
#     <tr>
#         <th class="border-bottom border-right-bold background-dark" rowspan="2">量的変数</th>
#         <td>間隔尺度</td>
#     </tr>
#     <tr>
#         <td>比率尺度</td>
#     </tr>
# </table>
#%% [markdown]
# ### データの散らばりを表す指標
# ---
# データに含まれる値が代表値の周囲に固まっていると代表値はデータの性質を強く表すが、データが散らばっている場合には代表値だけではデータの性質をうまく把握できない。そのため、**代表値と併せてデータの散らばりを把握**することも重要。

#%%
from helpers.variance import hist
hist.show()

#%% [markdown]
# #### 分散 (variance)
# ---
# $n$ 個のデータをそれぞれ $x_{1} ,x_{2} ,\dots ,x_{n}$ とし、その平均を $\bar{x}$ とすると、分散 $V(x)$ は
#
# $
# \begin{align}
#     V( x) & =\frac
#         {1}
#         {n}
#     \sum ^{n}_{i=1}\left( x_{i} -\overline{x}\right)^{2}\\
#      \\
#      & =\frac
#          {\left( x_{1} -\overline{x}\right)^{2} +\left( x_{2} -\overline{x}\right)^{2} +\dots +\left( x_{n} -\overline{x}\right)^{2}}
#          {n}
# \end{align}
# $
#
# で表される。
#%% [markdown]
# ###### 練習問題
#
# 分散を算出する関数`variance`を完成させる。 (平均の算出以外にNumPyの関数は使わない)

#%%
np.random.seed(1234)
x = np.random.normal(size=100)


#%%
def variance(x):
    return


#%%
print(f'結果: {variance(x):.3f}')
print('正解' if np.isclose(variance(x), x.var()) else '不正解')

#%% [markdown]
# #### 標準偏差 (standard deviation)
# ---
# 分散の平方根。
#
# 元のデータの単位が $m$ だとすると、分散の単位は $m^{2}$ となり、元のデータと比較しにくいので単位を揃えたもの。
#
# $
# \begin{align}
#     S( x) & =\sqrt{V( x)}\\
#      \\
#      & =\sqrt{\frac
#          {1}
#          {n}
#      {\displaystyle \sum ^{n}_{i=1}\left( x_{i} -\overline{x}\right)^{2}} }\\
#      \\
#      & =\sqrt{\frac
#          {\left( x_{1} -\overline{x}\right)^{2} +\left( x_{2} -\overline{x}\right)^{2} +\dots +\left( x_{n} -\overline{x}\right)^{2}}
#          {n}}
# \end{align}
# $
#%% [markdown]
# ###### 練習問題
#
# 標準偏差を算出する関数`standard_deviation`を完成させる。 (NumPyの標準偏差を算出する関数は使わない)

#%%
np.random.seed(1234)
x = np.random.normal(size=100)


#%%
def standard_deviation(x):
    return


#%%
print(f'結果: {standard_deviation(x):.3f}')
print('正解' if np.isclose(standard_deviation(x), x.std()) else '不正解')

#%% [markdown]
# #### 四分位点 (quartile)
# ---
# データを大きさの順で並べた場合に、4分の1ずつの位置にくる値。
#
# 値の演算に基づく積率系の指標 (平均・分散・標準偏差など) は外れ値に影響されやすいが、値の順序に基づく分位系の指標 (中央値・四分位点など) は外れ値に影響されにくい。しかし、利用している情報が少ないため精度が低かったり、確率論を背景とする統計的手法との相性は悪かったりする。
#
# <table class="text-center border">
#     <tr>
#         <td class="border-bottom-bold border-right-bold"></td>
#         <th>外れ値の影響</th>
#         <th>精度</th>
#         <th>確率論との相性</th>
#     </tr>
#     <tr>
#         <th class="border-bottom border-right-bold">積率系<br />(平均・分散・標準偏差など)</th>
#         <td>受けやすい</td>
#         <td>高い</td>
#         <td>よい</td>
#     </tr>
#     <tr>
#         <th class="border-bottom border-right-bold">分位系<br />(中央値・四分位点など)</th>
#         <td>受けにくい</td>
#         <td>低い</td>
#         <td>悪い</td>
#     </tr>
# </table>
#%% [markdown]
# $( 1,2,3,4,5,6,7,8,9)$ の四分位点 $( 25\%,50\%,75\%)$ は $( 3,5,7)$
#%% [markdown]
# ###### 練習問題
#
# 四分位点を算出する関数`quartile`を完成させる。結果は`[25%点, 50%点, 75%点]`の配列で返す。配列`x`の長さは奇数に限定してもよい。 (NumPyの四分位点を算出する関数は使わない)

#%%
np.random.seed(1234)
x = np.random.choice(np.arange(1, 100), size=9, replace=False)


#%%
def quartile(x):
    return


#%%
print(f'結果: {quartile(x)}')
print(f'正解: {np.percentile(x, (25, 50, 75))}')

#%% [markdown]
# ## Pythonでの基本統計量表示
# ---
# `pandas.DataFrame.describe`を用いる。

#%%
help('pd.DataFrame.describe')

#%%
att.describe()
