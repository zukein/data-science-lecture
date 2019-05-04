#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import inspect

#%% [markdown]
# ## NumPy とは
# ---
# 多次元配列の演算、特に線形代数などの科学計算の基本的な機能を提供。
#%% [markdown]
# ## NumPy の使い方
#%% [markdown]
# ### インポート
# ---
# 慣習として`np`という名前をつける。

#%%
import numpy as np

#%% [markdown]
# ### 配列の作成
# ---
# `numpy.array`に Python の配列を渡す。

#%%
help(np.array)

#%%
x = np.array([1, 2, 3])
x

#%% [markdown]
# 連続する整数の配列は`numpy.arange`を使用する。

#%%
help(np.arange)

#%%
np.arange(10)

#%% [markdown]
# ###### 練習問題
#
# 10 から 49 までの整数が並んだベクトル (1 次元配列) を作成 ([100 numpy exercises #7](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb))

#%%

#%% [markdown]
# ある区間を等間隔に分割した配列を作成するには`numpy.linspace`を使用する。

#%%
help(np.linspace)

#%%
np.linspace(0, 5, 11)

#%% [markdown]
# 初期値 0 の配列を作成するには`numpy.zeros`を使用する。

#%%
help(np.zeros)

#%%
np.zeros((2, 3))

#%% [markdown]
# ###### 練習問題
#
# 0が10個並んだベクトルを作成 ([100 numpy exercises #3](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb))

#%%

#%% [markdown]
# 初期値 1 の配列を作成するには`numpy.ones`を使用する。

#%%
help(np.ones)

#%%
np.ones((2, 3))

#%% [markdown]
# 任意の初期値で埋められた配列を作成するには`numpy.full`を使用する。

#%%
help(np.full)

#%%
np.full((2, 3), 4)

#%% [markdown]
# `numpy.*_like`で既存の配列と同じサイズの配列を作成可能。

#%%
[
    f[0] for f in inspect.getmembers(np, inspect.isfunction)
    if f[0].endswith('_like')
]

#%%
m = np.array([[1, 2, 3], [4, 5, 6]])
z = np.zeros_like(m)
z

#%% [markdown]
# ### 配列の操作
# ---
# 基本的には Python の配列と同様の方法で値の変更やスライシングが可能。

#%%
a = np.arange(5)
a[2] = 9
a

#%%
a[-2:]

#%% [markdown]
# ###### 練習問題
#
# 0 が 10 個並んだベクトルを作成し、 5 番目の要素を 1 にする ([100 numpy exercises #6](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb))

#%%

#%% [markdown]
# ###### 練習問題
#
# ベクトル要素の順番を逆にする ([100 numpy exercises #8](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb))

#%%

#%% [markdown]
# 2 行 3 列目の値を指定するには以下のように行う。

#%%
m = np.array([[1, 2, 3], [4, 5, 6]])
m[1, 2]

#%% [markdown]
# 行単位や列単位でも指定可能。

#%%
m[1]

#%%
m[:, 2]

#%% [markdown]
# ###### 練習問題
#
# 10x10 の外周の数値が 1 で内側の数値が 0 の行列を作成 ([100 numpy exercises #15](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb))
#
# $$
# \left(\begin{matrix}
#     1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1\\
#     1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1\\
#     1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1\\
#     1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1\\
#     1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1\\
#     1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1\\
#     1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1\\
#     1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1\\
#     1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1\\
#     1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1
# \end{matrix}\right)
# $$

#%%

#%% [markdown]
# 行列 (2 次元配列) の転置 (行と列の入れ替え) は T 属性で取得可能。

#%%
m.T

#%% [markdown]
# 配列のサイズは shape 属性で取得可能。

#%%
m.shape

#%% [markdown]
# 配列のサイズ変更は`numpy.reshape`を使用する。

#%%
help(np.reshape)

#%%
m.reshape((3, 2))

#%% [markdown]
# 配列の要素数は size 属性で取得可能。

#%%
m.size

#%% [markdown]
# ###### 練習問題
#
# 0 から 8 までの整数が並んだ 3x3 行列を作成 ([100 numpy exercises #9](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb))

#%%

#%% [markdown]
# ### 要素同士の演算
# ---
# 同じサイズの配列同士なら、その要素同士の演算は通常の演算子で可能。

#%%
a = np.arange(6).reshape((2, 3))
b = np.arange(4, 10).reshape((2, 3))
print('a=')
print(a)
print('b=')
print(b)

#%%
a + b

#%%
a * b
