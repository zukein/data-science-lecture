#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
from IPython.display import display
import numpy as np
import pandas as pd
pd.set_option('max_rows', 6)

#%% [markdown]
# ###### 練習問題
#
# データフレームの任意のカラムを行・列に持つクロス集計表を作成する関数`cross_tabulation`を完成させる。

#%%
titanic = pd.read_csv('data/Titanic.csv')
titanic


#%%1
def cross_tabulation(index=None, columns=None, data=None):
    '''
    index: str
    columns: str
    data: Pandas DataFrame
    '''
    return


#%%2
def cross_tabulation(index=None, columns=None, data=None):
    '''
    index: str
    columns: str
    data: Pandas DataFrame
    '''
    return


#%%3
def cross_tabulation(index=None, columns=None, data=None):
    '''
    index: str
    columns: str
    data: Pandas DataFrame
    '''
    return


#%%4
def cross_tabulation(index=None, columns=None, data=None):
    '''
    index: str
    columns: str
    data: Pandas DataFrame
    '''
    return


#%%5
def cross_tabulation(index=None, columns=None, data=None):
    '''
    index: str
    columns: str
    data: Pandas DataFrame
    '''
    return


#%%
print('結果')
display(cross_tabulation(index='Class', columns='Age', data=titanic))
print('正解')
display(pd.crosstab(index=titanic['Class'], columns=titanic['Age']))

#%% [markdown]
# ###### 練習問題
#
# 2変数の相関係数を算出する`correlation_coefficient`を完成させる。

#%%
np.random.seed(1234)
r = 0.7
mat = np.array([[1.0, r], [r, 1.0]])
data = pd.DataFrame(np.random.multivariate_normal(np.zeros(2), mat, size=100),
                    columns=['x', 'y'])
data


#%%1
def correlation_coefficient(x, y):
    return


#%%2
def correlation_coefficient(x, y):
    return


#%%3
def correlation_coefficient(x, y):
    return


#%%4
def correlation_coefficient(x, y):
    return


#%%5
def correlation_coefficient(x, y):
    return


#%%
x, y = data['x'], data['y']
print(f'結果: {correlation_coefficient(x, y):.2f}')
print('正解' if np.isclose(
    np.corrcoef(x, y)[0, 1], correlation_coefficient(x, y)) else '不正解')
