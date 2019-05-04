#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import numpy as np

#%% [markdown]
# ## pandasとは
# ---
# データフレームという表計算ソフトのような構造とデータ分析のための機能を提供。
#%% [markdown]
# ## pandasの使い方
#%% [markdown]
# ### インポート
# ---
# 慣習として`pd`という名前をつける。

#%%
import pandas as pd

#%% [markdown]
# ### データフレームの作成
# ---
# `pandas.DataFrame`に配列や辞書型のオブジェクトを渡す。

#%%
np.random.seed(1234)
length = 4
a = np.arange(length)
b = np.arange(length) * 2
c = np.arange(length) + length
data = np.random.randint(0, 9, (length, 3))
print(f'a={a}')
print(f'b={b}')
print(f'c={c}')
print('data=')
print(data)

#%%
help(pd.DataFrame)

#%%
pd.DataFrame(data)

#%%
pd.DataFrame(dict(A=a, B=b))

#%% [markdown]
# ### 行・列の名前変更
# ---
# データフレームの`columns`属性や`index`属性に配列で指定可能。

#%%
df = pd.DataFrame(data)
df.columns = ['列A', '列B', '列C']
df.index = ['行1', '行2', '行3', '行4']
df

#%% [markdown]
# データフレームを作成する際にも指定可能。

#%%
pd.DataFrame(data, index=['行1', '行2', '行3', '行4'], columns=['列A', '列B', '列C'])

#%% [markdown]
# ### 要素の取得
# ---
# 列名を指定して、各列を取得可能。

#%%
df['列A']

#%%
df[['列A', '列C']]

#%% [markdown]
# データフレームの各列は`pandas.Series`オブジェクト。
# `pandas.DataFrame`で利用可能な関数の多くは`pandas.Series`でも利用可能。

#%%
type(df['列A'])

#%% [markdown]
# `loc`を使用すると行名や列名でデータを取得可能。
# スライシングも利用可能。

#%%
df.loc['行1']

#%%
df.loc['行2', '列A']

#%%
df.loc[:, ['列A', '列C']]

#%%
df.loc['行2':, '列B']

#%% [markdown]
# `iloc`を使用すると行番号や列番号でデータを取得可能。
# `loc`と同様にスライシングも利用可能。

#%%
df.iloc[0]

#%%
df.iloc[1, 0]

#%%
df.iloc[:, [0, 2]]

#%%
df.iloc[1:, 1]
