#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import inspect

#%%
import numpy as np

#%% [markdown]
# ###### 練習問題
#
# 10 から 49 までの整数が並んだベクトル (1 次元配列) を作成 ([100 numpy exercises #7](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb))

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# 0が10個並んだベクトルを作成 ([100 numpy exercises #3](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb))

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# 0 が 10 個並んだベクトルを作成し、 5 番目の要素を 1 にする ([100 numpy exercises #6](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb))

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# ベクトル要素の順番を逆にする ([100 numpy exercises #8](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb))

#%%1

#%%2

#%%3

#%%4

#%%5

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

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# 0 から 8 までの整数が並んだ 3x3 行列を作成 ([100 numpy exercises #9](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb))

#%%1

#%%2

#%%3

#%%4

#%%5
