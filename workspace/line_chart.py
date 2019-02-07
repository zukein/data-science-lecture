#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
pd.set_option('max_rows', 5)

#%% [markdown]
# ## 考えてみる
# ---
# 時系列のデータを視覚的に表現するにはどのような手法が適しているか考えてみる。
#%% [markdown]
# ## GUIで実行してみる
# ---
# RStudio の Console に`library(Rcmdr)`と入力して、 R commander を起動。
#
# - `データ` -> `データのインポート` -> `テキストファイルまたはクリップボード, URLから`
#
# として、`フィールドの区切り記号`を`カンマ`にし、`OK`をクリック。
#
# `workspace/data/economics.csv`を読み込む。
# `データセットを表示`をクリックし、内容を確認。
#
# - `データ` -> `アクティブデータセット内の変数の管理` -> `データセットに観測値番号を追加`
#
# として、再度データセットを確認。
#
# - `データ` -> `アクティブデータセット` -> `アクティブデータセットの部分集合を抽出`
#
# として、`部分集合の表現`を`ObsNumber < 11`にし、`OK`をクリックし、再度データセットを確認。
#
# - `グラフ` -> `折れ線グラフ`
#
# として、`x変数`に`ObsNumber`、`y変数`に`psavert`を選択し、`OK`をクリックし、折れ線グラフを表示。
#%% [markdown]
# ## 折れ線グラフ
# ---
# 横軸に時間、縦軸に数量をとって、隣り合う時間の数量同士を結んだグラフ。
# 時間の経過などによる連続的な変化を確認するのに利用する。

#%%
economics = pd.read_csv('data/economics.csv', parse_dates=[0])
print('economics')
display(economics[['date', 'uempmed']])
economics.plot('date', 'uempmed', legend=False)
plt.show()

#%% [markdown]
# ### Pythonでの折れ線グラフ表示
# ---
# `seaborn.lineplot`、`pandas.DataFrame.plot`、`matplotlib.pyplot.plot`などを用いる。

#%%
print('economics')
display(economics)

#%%
help(sns.lineplot)

#%%
sns.lineplot('date', 'unemploy', data=economics)
plt.show()

#%%
help(pd.DataFrame.plot)

#%%
economics.plot('date', 'pop')
plt.show()

#%%
help(plt.plot)

#%%
plt.plot('date', 'pce', data=economics)
plt.show()

#%% [markdown]
# ###### 練習問題
#
# economicsデータセットの`psavert`列を折れ線グラフで表示する。

#%%
print('economics')
display(economics)

#%%

#%%
economics['psavert'].plot()
plt.show()
