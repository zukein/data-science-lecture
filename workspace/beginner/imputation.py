#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import string
import numpy as np
from scipy.stats import norm
from statsmodels import robust
import pandas as pd
from IPython.display import display
pd.set_option('max_rows', 5)

#%% [markdown]
# ## 外れ値・異常値・欠損値とは
# ---
# <table class="text-left border">
#     <tr>
#         <th class="border-bottom border-right-bold">外れ値 (outlier)</th>
#         <td>他の値から大きく外れた値</td>
#         <td><li>特異なイベントの発生</li></td>
#     </tr>
#     <tr>
#         <th class="border-bottom border-right-bold">異常値 (anomaly)</th>
#         <td>データの生成プロセスに照らして、起こるべきでない異常によって生じた値<br />異常値である外れ値と異常値でない外れ値は<strong>データのみでは区別できない</strong></td>
#         <td><li>センサーの故障</li><li>データの入力ミス</li><li>表計算ソフトの集計行混入</li></td>
#     </tr>
#     <tr>
#         <th class="border-bottom border-right-bold">欠損値 (missing value)</th>
#         <td>値の抜けているデータ</td>
#         <td><li>NULL 値</li><li>空欄</li><li>プレースホルダー文字列</li></td>
#     </tr>
# </table>
#
# 外れ値・異常値の検出は中級編以降で扱い、ここでは欠損値の確認、検出した外れ値・欠損値の除去・補完を扱う。
#%% [markdown]
# ## 欠損値の確認
# ---
# `pandas.DataFrame.isnull`を使用する。

#%%
n_sample = 1000
n_features = 5
np.random.seed(1234)
sample = pd.DataFrame(
    np.random.normal(size=(n_sample, n_features)),
    columns=[string.ascii_uppercase[i] for i in range(n_features)])
for i, rate in enumerate(np.linspace(0, 0.5, n_features)):
    missing = np.random.choice(
        n_sample, size=int(n_sample * rate), replace=False)
    sample.iloc[missing, i] = np.nan

print('sample')
display(sample)

#%%
help(pd.DataFrame.isna)

#%%
sample.isna()

#%% [markdown]
# 列ごとに欠損値の有無を確かめるには`any`、欠損値の数を確かめるには`sum`を使用する。
# `pandas.DataFrame.info`を使用してもよい。

#%%
sample.isna().any()

#%%
sample.isna().sum()

#%%
sample.info()

#%% [markdown]
# ## 除去
# ---
# 最も単純な対処法だが、やりすぎるとデータが不足したり、必要な情報まで失われる可能性がある。
# 欠損がランダムに発生するわけではない場合 (年齢の高い人や収入の高い人ほど収入を尋ねる欄に回答しないなど) は、**取り除いてしまうとデータに偏りが生じる**。
#%% [markdown]
# ### 欠損値
# ---
# `pandas.DataFrame.dropna`を使用する。

#%%
help(pd.DataFrame.dropna)

#%% [markdown]
# #### 欠損を含む行

#%%
sample.dropna()

#%% [markdown]
# #### 欠損を含む列

#%%
sample.dropna(axis=1)

#%% [markdown]
# #### 全ての値が欠損している行

#%%
sample.loc[:, 'B':'E'].dropna(how='all')

#%% [markdown]
# #### 欠損でない値が任意の数以上ある行を残す

#%%
sample.dropna(thresh=3)

#%% [markdown]
# #### 特定の列に欠損がある行

#%%
sample.dropna(subset=['B'])

#%% [markdown]
# ### 外れ値
# ---
# 条件式などを使って絞り込む。
#%% [markdown]
# #### 3$\sigma$法
# ---
# 平均から$\pm 3\sigma $ (標準偏差) を超える値を外れ値とする方法。正規分布では約 $0.03\%$ が外れ値になる。

#%%
mean = sample['A'].mean()
sigma = sample['A'].std(ddof=0)
sample.loc[(mean - 3 * sigma <= sample['A'])
           & (sample['A'] <= mean + 3 * sigma)]

#%% [markdown]
# ###### 練習問題
#
# 正規分布で$\pm 3\sigma$範囲に含まれる値の割合を求める。

#%%

#%% [markdown]
# #### Hampel判別法 (Hampel identifier)
# ---
# $3\sigma$法の平均を中央値に、標準偏差を中央絶対偏差 (Median Absolute Deviation) に置き換えた方法。$3\sigma$法よりサンプルに含まれる外れ値の影響を受けにくい。
#
# $\displaystyle median( x) \pm 3\times ( MAD\times 1.4826)$
#
# $\displaystyle MAD=median( |x_{i} -median( x) |)$
#
# $1.4826$ は正規分布を仮定した場合に、中央絶対偏差 ($75\%$ 点に相当) を標準偏差に補正するための定数。
#%% [markdown]
# ###### 練習問題
#
# 中央絶対偏差を求める以下の関数 mad を完成させる。


#%%
def mad(x):
    return


#%%
mad(sample['A'])

#%% [markdown]
# 中央絶対偏差は`statsmodels.robust.mad`で求められる。
# 既定値では、正規化定数 $c=0.6744897501960817$ で割って補正してあるので、そのままの値を求めるには $c=1$ とする。 (正規化定数で割った値を中央絶対偏差と呼ぶこともある)

#%%
help(robust.mad)

#%%
robust.mad(sample['A'], c=1)

#%% [markdown]
# ###### 練習問題
#
# 標準正規分布の $75\%$ 点を求め、 $0.6744897501960817$ と比較する。
# $1$ を標準正規分布の $75\%$ 点で割り、 $1.4826$ と比較する。

#%%

#%% [markdown]
# ###### 練習問題
#
# Hampel 判別法に基づいて外れ値かどうかを判定する (外れ値でない場合に True 、外れ値の場合に False を返す) 以下の関数 Hampel を完成させる。


#%%
def hampel(ndarray):
    return


#%%
sample.loc[hampel(sample['A'])]

#%% [markdown]
# #### 箱ひげ図
# ---
# 箱ひげ図では第 1 四分位点 ($Q_{1/4}$, lower quartile) 、第 3 四分位点 ($Q_{3/4}$, upper quartile) 、四分位範囲 (IQR, interquartile range) を用いて、以下のように外れ値を決めることが多い。
#
# $Q_{1/4} -1.5*IQR,Q_{3/4} +1.5*IQR$
#
# $IQR=Q_{3/4}-Q_{1/4}$
#%% [markdown]
# ###### 練習問題
#
# 箱ひげ図における外れ値かどうかを判定する (外れ値でない場合に True 、外れ値の場合に False を返す) 以下の関数 isin_box を完成させる。


#%%
def isin_box(ndarray):
    return


#%%
sample.loc[isin_box(sample['A'])]

#%% [markdown]
# ## 補完
# ---
# 欠損値を別の値で埋めること。
# ここでは代表値による補完を扱い、より高度な補完手法は中級編以降で扱う。
#
# 欠損値の補完には、`pandas.DataFrame.fillna`を使用する。

#%%
help(pd.DataFrame.fillna)

#%% [markdown]
# 平均値での補完。

#%%
sample.fillna(sample.mean())

#%% [markdown]
# 中央値での補完。

#%%
sample.fillna(sample.median())
