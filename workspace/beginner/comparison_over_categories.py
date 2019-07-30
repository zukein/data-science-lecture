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
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
pd.set_option('max_rows', 5)

#%% [markdown]
# ## 層別グラフ
# ---
# ある特徴 (通常はカテゴリカル変数の値) によって、いくつかのグループに分けられたグラフ。
# グループごとに傾向の差があるのか比較するのに用いる。
#%% [markdown]
# ### 層別棒グラフ

#%%
va = pd.read_csv('data/VADeaths.csv', index_col=0)
print('va')
display(va)

va.plot.bar()
plt.show()

#%% [markdown]
# #### Pythonでの層別棒グラフ表示
# ---
# `seaborn.countplot`、`pandas.DataFrame.plot.bar`などを用いる。

#%%
tips = sns.load_dataset('tips')
print('tips')
display(tips)

#%%
help(sns.countplot)

#%%
sns.countplot('day', hue='sex', data=tips)
plt.title('性別でグループ分けした曜日ごとのデータ数')
plt.show()

#%%
help(pd.DataFrame.plot.bar)

#%%
pd.crosstab(tips['day'],
            tips['smoker'],
            values=tips['total_bill'],
            aggfunc=sum).plot.bar()
plt.title('喫煙者かどうかでグループ分けした曜日ごとの売り上げ')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# tipsデータセットの`time`列でグループ分けし、`day`ごとのデータ数を層別棒グラフで表示する。

#%%
print('tips')
display(tips)

#%%

#%% [markdown]
# ### 積み上げ棒グラフ
# ---
# カテゴリ別の値を縦に積み上げた棒グラフ。全体の変化や割合の変化を見るために用いる。

#%%
print('va')
display(va)
va.plot.bar(stacked=True)
plt.show()

#%% [markdown]
# #### Pythonでの積み上げ棒グラフ表示
# ---
# `pandas.DataFrame.plot.bar`を用いる。

#%%
help(pd.DataFrame.plot.bar)

#%%
pd.crosstab(tips['day'],
            tips['smoker'],
            values=tips['total_bill'],
            aggfunc=sum).plot.bar(stacked=True)
plt.title('喫煙者かどうかでグループ分けした曜日ごとの売り上げ')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# tipsデータセットの`sex`列でグループ分けし、`day`ごとのデータ数を積み上げ棒グラフで表示する。

#%%
print('tips')
display(tips)

#%%

#%% [markdown]
# ### 100%積み上げ棒グラフ
# ---
# 積み上げ棒グラフの高さを揃えたグラフ。割合の変化を見るのに用いる。

#%%
print('va')
display(va)
va.apply(lambda x: x / va.sum(axis=1), axis=0).plot.bar(stacked=True)
plt.show()

#%% [markdown]
# #### Pythonでの100%積み上げ棒グラフ表示
# ---
# データセットの数値を割合に計算し直してから、`pandas.DataFrame.plot.bar`を用いる。

#%%
pd.crosstab(tips['day'],
            tips['smoker'],
            values=tips['total_bill'],
            aggfunc=sum,
            normalize='index').plot.bar(stacked=True)
plt.title('喫煙者かどうかでグループ分けした曜日ごとの売り上げ')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# tipsデータセットの`smoker`列でグループ分けし、`day`ごとのデータ数を100%積み上げ棒グラフで表示する。

#%%
print('tips')
display(tips)

#%%

#%% [markdown]
# ### 層別箱ひげ図

#%%
iris = sns.load_dataset('iris')
print('iris')
display(iris)

iris.boxplot('sepal_length', by='species')
plt.show()

#%% [markdown]
# #### Pythonでの層別箱ひげ図表示
# ---
# `seaborn.boxplot`、`pandas.DataFrame.boxplot`などを用いる。

#%%
print('tips')
display(tips)

#%%
help(sns.boxplot)

#%%
sns.boxplot('day', 'total_bill', hue='smoker', data=tips)
plt.title('喫煙家どうかでグループ分けされた、曜日別支払額の箱ひげ図')
plt.show()

#%%
help(pd.DataFrame.boxplot)

#%%
tips.boxplot('tip', by='day')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# irisデータセットの`species`列でグループ分けし、`petal_length`列の箱ひげ図を表示する。

#%%
print('iris')
display(iris)

#%%

#%% [markdown]
# ### 層別散布図

#%%
whiteside = pd.read_csv('data/whiteside.csv')
print('whiteside')
display(whiteside)

whiteside.plot.scatter(
    x='Temp',
    y='Gas',
    c=whiteside['Insul'].astype('category').cat.rename_categories(
        ['blue', 'red']))
plt.show()

#%% [markdown]
# #### Pythonでの層別散布図表示
# ---
# `seaborn.scatterplot`、`pandas.DataFrame.plot.scatter`、`matplotlib.pyplot.scatter`などを用いる。

#%%
mpg = sns.load_dataset('mpg')
print('mpg')
display(mpg)

#%%
help(sns.scatterplot)

#%%
sns.scatterplot('horsepower', 'mpg', hue='cylinders', data=mpg)
plt.title('シリンダー数でグループ分けした馬力と燃費の関係')
plt.show()

#%%
help(pd.DataFrame.plot.scatter)

#%%
mpg.plot.scatter('weight', 'mpg', c='cylinders')
plt.title('シリンダー数でグループ分けした重量と燃費の関係')
plt.show()

#%%
help(plt.scatter)

#%%
for label in sorted(mpg['cylinders'].unique()):
    plt.scatter('weight',
                'horsepower',
                data=mpg.query('cylinders==@label'),
                label=label)
plt.legend()
plt.title('シリンダー数でグループ分けした重量と馬力の関係')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# irisデータセットの`species`列でグループ分けし、 x 軸を`petal_length`、 y 軸を`petal_width`にして散布図を表示する。

#%%
print('iris')
display(iris)

#%%

#%% [markdown]
# ### インタラクティブなグラフ表示
# ---
# 層別グラフは表示するカテゴリをインタラクティブに選択できると生産的。
#%% [markdown]
# #### Plotly
# ---
# Pythonの代表的なインタラクティブな表現のできるグラフライブラリ。
# 引数のネストが深すぎてドキュメントが使いにくいので、サンプルにある以上の細かいカスタマイズはやらないほうが無難。どうしてもやる場合はエラーメッセージのほうがわかりやすいので、なさそうな引数名を適当に入れてエラーメッセージをたどっていくのが効率的。

#%%
from plotly.offline import init_notebook_mode
import plotly.offline as py
import plotly.graph_objs as go
init_notebook_mode(connected=True)

data = []
for label in sorted(mpg['cylinders'].unique()):
    subset = mpg.query('cylinders==@label')
    trace = go.Scatter(x=subset['weight'],
                       y=subset['horsepower'],
                       name=str(label),
                       mode='markers',
                       hovertext=subset['name'])
    data.append(trace)
layout = dict(title='シリンダー数でグループ分けした重量と馬力の関係')
fig = dict(data=data, layout=layout)
py.iplot(fig)

#%% [markdown]
# #### BIツール
# ---
# 有料のものが多いが、その分データの可視化では生産性が上がる。
#%% [markdown]
# ## 複数系列グラフ
# ---
# 同じ時間軸上に表示された複数の変数のグラフ。

#%%
start = datetime.datetime(2008, 1, 1)
end = datetime.datetime(2017, 12, 31)
inflation = web.DataReader(['CPIAUCSL', 'CPILFESL'], 'fred', start, end)
print('inflation')
display(inflation)
inflation.plot()
plt.show()

#%% [markdown]
# ### Pythonでの複数系列グラフ表示
# ---
# `seaborn.lineplot`、`pandas.DataFrame.plot`、`matplotlib.pyplot.plot`などを用いる。

#%%
tiingo_access_key = 'YOUR_API_KEY'
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

#%%
help(sns.lineplot)

#%%
sns.lineplot(data=stocks[['Google', 'Apple']])
monthly = pd.date_range(stocks.index[0], stocks.index[-1], freq='M')
idx = [i for i, d in enumerate(stocks.index) if d in monthly]
xticks = stocks.index[idx]
xticklabels = stocks.index.date[idx]
plt.xticks(xticks, xticklabels, rotation='vertical')
plt.show()

#%%
help(pd.DataFrame.plot)

#%%
stocks[['Facebook', 'Amazon']].plot()
plt.xticks(xticks, xticklabels, rotation='vertical')
plt.show()

#%%
help(plt.plot)

#%%
plt.plot(stocks.index, stocks[['Apple', 'Amazon']])
plt.xticks(xticks, xticklabels, rotation='vertical')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# economicsデータセットの`psavert`列と`uempmed`列を折れ線グラフで表示する。

#%%
economics = pd.read_csv('data/economics.csv', parse_dates=[0])
print('economics')
display(economics)

#%%
