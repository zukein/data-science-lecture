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
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
pd.set_option('max_rows', 5)

#%% [markdown]
# ## ロジスティック回帰
# ---
# 2 値変数 ( 2 種類の値をとる) を目的変数として、対応するカテゴリにそのデータが属する確率を推定する手法の 1 つ。
#
# <table class="border text-center background-bright">
#     <tr class="background-dark">
#         <th></th>
#         <th>$x$</th>
#         <th>正解</th>
#         <th class="border-right-double">$y$</th>
#         <th>$\hat{y}$</th>
#         <th>Aである確率</th>
#         <th>Bである確率</th>
#         <th>予測</th>
#     </tr>
#     <tr>
#         <td>1</td>
#         <td class="text-right">1.1</td>
#         <td>A</td>
#         <td class="border-right-double">1</td>
#         <td>0.98</td>
#         <td class="text-right">98%</td>
#         <td class="text-right">2%</td>
#         <td>A</td>
#     </tr>
#     <tr>
#         <td>2</td>
#         <td class="text-right">0.5</td>
#         <td>B</td>
#         <td class="border-right-double">0</td>
#         <td>0.55</td>
#         <td class="text-right">55%</td>
#         <td class="text-right">45%</td>
#         <td>A</td>
#     </tr>
#     <tr>
#         <td colspan="8">$\vdots$</td>
#     </tr>
#     <tr>
#         <td>n</td>
#         <td class="text-right">-2.5</td>
#         <td>B</td>
#         <td class="border-right-double">0</td>
#         <td>0.04</td>
#         <td class="text-right">4%</td>
#         <td class="text-right">96%</td>
#         <td>B</td>
#     </tr>
# </table>
#
#
#%% [markdown]
# ### ダミー変数
# ---
# カテゴリ変数 (主に名義尺度) を 0 または 1 の値をとる 2 値変数に変換して数値計算可能にする手法。
# One-hot エンコーディングとも呼ぶ。
#
# <table class="background-bright border text-center">
#     <tr>
#         <th class="background-default border-top-none border-left-none border-bottom" rowspan="2"></th>
#         <th class="background-dark">カテゴリ変数</th>
#         <td class="background-default border-top-none border-bottom-none" rowspan="2"></td>
#         <th class="background-dark" colspan="3">ダミー変数</th>
#     </tr>
#     <tr class="background-dark border-bottom">
#         <th>色</th>
#         <th>赤</th>
#         <th>緑</th>
#         <th>青</th>
#     </tr>
#     <tr>
#         <td>1</td>
#         <td>赤</td>
#         <td class="background-default border-top-none border-bottom-none" rowspan="3">→</td>
#         <td>1</td>
#         <td>0</td>
#         <td>0</td>
#     </tr>
#     <tr>
#         <td>2</td>
#         <td>緑</td>
#         <td>0</td>
#         <td>1</td>
#         <td>0</td>
#     </tr>
#     <tr>
#         <td>3</td>
#         <td>青</td>
#         <td>0</td>
#         <td>0</td>
#         <td>1</td>
#     </tr>
# </table>
#
# ダミー変数は 1 列削っても情報は失われない (その他の変数から削除された列の値がわかる) ので、特にカテゴリの水準 (カテゴリ数) が 2 つしかない場合には 1 列だけで表現することが多い。
#
# <table class="background-bright border text-center">
#     <tr>
#         <th class="background-default border-top-none border-left-none border-bottom" rowspan="2"></th>
#         <th class="background-dark">カテゴリ変数</th>
#         <th class="background-default border-top-none border-bottom-none" rowspan="2"></th>
#         <th class="background-dark" colspan="2">ダミー変数</th>
#     </tr>
#     <tr class="background-dark border-bottom">
#         <th>性別</th>
#         <th>男</th>
#     </tr>
#     <tr>
#         <td>1</td>
#         <td>男</td>
#         <td class="background-default border-top-none border-bottom-none" rowspan="2">→</td>
#         <td>1</td>
#     </tr>
#     <tr>
#         <td>2</td>
#         <td>女</td>
#         <td>0</td>
#     </tr>
# </table>
#
# ダミー変数を用いずに各カテゴリに $1,\ 2,\ 3,\ \cdots $ のような数値を割り振ると、カテゴリ間に順序が生じてしまうので行ってはいけない。
# 例えば、名義尺度の変数に赤 = 1 ・緑 = 2 ・青 = 3 のように割り振ると、赤 < 緑 < 青という順序尺度の変数になってしまう。
#%% [markdown]
# ### 確率の推定方法
# ---
# 回帰分析を利用すると、データから実数値 $(-\infty \sim \infty)$ を推定できるので、実数値→確率 $(0\sim 1)$ に変換できると便利。そこで、累積分布関数を使って実数を確率に変換することが考えられる。
# その分布 (累積分布関数) にロジスティック分布 (ロジスティック関数) を使うのがロジスティック回帰。
#
# $\displaystyle ロジスティック関数\ f( x) =\frac{e^{x}}{1+e^{x}} =\frac{1}{1+e^{-x}}$
#%% [markdown]
# ###### 練習問題
#
# ロジスティック分布の累積分布関数のグラフを表示する。

#%%

#%% [markdown]
# ロジスティック分布は正規分布に似ているが、正規分布より計算しやすいのが特徴。
#%% [markdown]
# ###### 練習問題
#
# ロジスティック分布の確率密度関数のグラフを表示する。確率密度関数 $f'( x)$ は累積分布関数を $f( x)$ とすると、以下で表される。
#
# $\displaystyle f'( x) =f( x) \times ( 1-f( x))$

#%%

#%% [markdown]
# ### Pythonでのロジスティック回帰の実行
# ---
# `sklearn.linear_model.LogisticRegression`を用いる。 scikit-learn の実装は厳密には上の説明と異なるが、引数 $C\rightarrow \infty $ で両者は一致する。

#%%
x, y = make_classification(
    n_features=1,
    n_informative=1,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=1234)
clf = pd.DataFrame(dict(x=x.ravel(), y=y))
print('clf')
display(clf)

#%%
help(LogisticRegression)

#%%
# 最初にインスタンスを作成
model = LogisticRegression()
# fitメソッドで分布関数を求める
# xはサイズが(サンプル数 × 変数の数)の行列でなければならない
x = clf['x'].values.reshape((-1, 1))
y = clf['y']
model.fit(x, y)
# 予測した確率はpredict_probaで得られる
# 予測結果は[クラス0の確率, クラス1の確率]の配列
print('予測結果')
print(model.predict_proba(x))
# クラス1の確率のみ得るには列を取り出す
print('クラス1の確率')
print(model.predict_proba(x)[:, 1])

#%% [markdown]
# ###### 練習問題
#
# clfデータセットの散布図とclfデータセットから学習したロジスティック回帰の予測曲線 (累積分布関数) を表示する。

#%%
