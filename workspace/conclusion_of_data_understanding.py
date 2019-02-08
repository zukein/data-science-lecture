#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import pandas as pd
import seaborn as sns
from IPython.display import display
pd.set_option('max_rows', 11)
pd.set_option('precision', 2)

#%% [markdown]
# ## データ可視化の重要性・粒度
# ---
# データを日常的に可視化しておくと、異常が発生した場合などに把握しやすい。
# データに基づいて意思決定する場合には、データに捏造や改ざんがあったり、分析に誤りがあると間違った意思決定を行ってしまう。分析者は通常意思決定に対する責任は負わないが、データの真正性・分析の正しさについては責任を持つことを意識する。
#%% [markdown]
# ###### 練習問題
#
# 普段、業務などで扱っているデータがどのようなタイミングで発生し、その基本統計量 (代表値や分散・四分位点など) を把握できているか話し合う。
#%% [markdown]
# ### Anscombe の例
# ---
# 平均や分散などの統計量はあくまでデータの要約であり、失われている情報がある。常に必要に応じて生データやデータ収集方法まで遡って確認する姿勢が重要なことの一例として、全く異なる分布のデータが同じ統計量を持つ [Anscombe の例](https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%B3%E3%82%B9%E3%82%B3%E3%83%A0%E3%81%AE%E4%BE%8B)を示す。

#%%
from helpers.conclusion_of_data_understanding.anscombe import Anscombe
ans = Anscombe()
anscombe = ans.data
print('anscombe')
display(anscombe)

#%% [markdown]
# 平均・分散などの統計量はデータセット I~IV でほぼ同じ。 (相関係数もほぼ同じ)

#%%
anscombe.describe()

#%% [markdown]
# 実際には、それぞれの分布は全く異なる。

#%%
ans.show()
