#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
from IPython.display import display
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

pd.set_option('max_rows', 10)
pd.set_option('max_columns', 10)

#%%
Groceries = pd.read_csv('data/Groceries.csv')
print('変数Groceriesの中身')
display(Groceries)

#%% [markdown]
# ###### 練習問題
#
# `apriori`の`min_support`を変更して、扱いやすい (実行時間が長くなりすぎない) サイズのルールを抽出したり、`association_rules`の引数を変更して重要そうなルールの候補を選んでみる。

#%%1

#%%2

#%%3

#%%4

#%%5
