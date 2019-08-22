#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace/beginner'))
    print(os.getcwd())
except:
    pass

#%%
import datetime
import numpy as np
import pandas as pd
from pandas_datareader import wb
import pandas_datareader.data as web
from sklearn.datasets import make_blobs
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('max_rows', 5)
pd.set_option('precision', 3)

#%% [markdown]
# ###### 練習問題
#
# economics データセットの`unemploy`列を折れ線グラフで表示し、期間中の最大値とその日付が伝わるように表現してみる。

#%%
economics = pd.read_csv('data/economics.csv')
print('economics')
display(economics)

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# blobsデータセットで、4つのグループがあることがわかるようにし、 $\displaystyle x >0,y >0$ のグループを色によって目立たせる。

#%%
ticks = (-5, 5)
xx, yy = np.meshgrid(ticks, ticks)
centers = np.c_[xx.ravel(), yy.ravel()]
data, _ = make_blobs(centers=centers, random_state=1234)
blobs = pd.DataFrame(data, columns=['x', 'y'])
print('blobs')
display(blobs)
blobs.plot.scatter('x', 'y')
plt.show()

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# sizeデータセットのそれぞれの値を、値に応じたフォントサイズで順に並べて表示する。

#%%
np.random.seed(1234)
size = pd.DataFrame(dict(size=np.random.randint(low=1, high=100, size=4)))
display(size)

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# lowvarデータセットの縦軸を原点から開始した折れ線グラフを表示し、原点から始まっていないグラフから受ける印象と比較してみる。

#%%
np.random.seed(1234)
lowvar = pd.DataFrame(dict(value=np.random.normal(loc=1e2, scale=1, size=10)))
print('lowvar')
display(lowvar)
lowvar.plot()
plt.show()

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# ###### 練習問題
#
# car_crashesデータセットを`pandas.DataFrame.sort_values`関数を用いて`total`列でソートし、値の大きい順に10件のデータだけに絞ったデータフレーム`limited`を作成し、棒グラフを表示する。

#%%
car_crashes = sns.load_dataset('car_crashes')[['total', 'abbrev']]
print('car_crashes')
display(car_crashes)

#%%1

#%%2

#%%3

#%%4

#%%5

#%%
limited.plot.bar('abbrev', 'total', color='gray')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# stocksデータセットの各列を`pandas.DataFrame.apply`を用いて`2018-01-02`時点の値を基準に指数化したデータフレーム`scaled`を作成し、複数系列折れ線グラフで表示する。

#%%
tiingo_access_key = 'YOUR_API_KEY'

#%%
start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2018, 12, 31)
column_map = dict(GOOGL='Google', AAPL='Apple', FB='Facebook', AMZN='Amazon')
stocks = web.DataReader(['GOOGL', 'AAPL', 'FB', 'AMZN'],
                        'tiingo',
                        start,
                        end,
                        access_key=tiingo_access_key)['close'].unstack(level=0)
stocks.columns = [column_map[k] for k in stocks.columns]
print('stocks')
display(stocks)

#%%1

#%%2

#%%3

#%%4

#%%5

#%%
scaled.plot()
plt.show()

#%% [markdown]
# ###### 練習問題
#
# stocksデータセットの各列を`pandas.DataFrame.rolling`関数を用いて、前後2件ずつの移動平均に変換したデータセット`moving_average`を作成し、折れ線グラフを表示する。

#%%
print('stocks')
display(stocks)

#%%1

#%%2

#%%3

#%%4

#%%5

#%%
moving_average.plot()
plt.show()

#%% [markdown]
# ###### 練習問題
#
# gdpデータセットの対数をとったデータセット`log_gdp`を作成し、複数系列折れ線グラフを表示する。

#%%
gdp = wb.download(indicator='NY.GDP.MKTP.CD',
                  country=['JP', 'US', 'CN'],
                  start=1960,
                  end=2017).unstack(level=0).astype(int)
gdp.columns = gdp.columns.levels[1]
print('gdp')
display(gdp)
gdp.plot()
plt.show()

#%%

#%%
log_gdp.plot()
plt.show()

#%% [markdown]
# ###### 練習問題
#
# passengersデータセットを`pandas.DataFrame.shift`関数や`pandas.DataFrame.diff`関数を用いて、前年同期との成長率・対数差分を表す`成長率`列・`対数差分`列を作成し、複数系列折れ線グラフで重ねて表示する。

#%%
flights = sns.load_dataset('flights')
print('flights')
display(flights)
flights.plot(y='passengers')
plt.show()

#%%1

#%%2

#%%3

#%%4

#%%5
