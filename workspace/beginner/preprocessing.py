#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace/beginner'))
    print(os.getcwd())
except:
    pass

#%%
from seaborn import load_dataset
import numpy as np
import pandas as pd
import sqlite3
import sqlalchemy
from IPython.display import display
pd.set_option('max_rows', 9)
pd.set_option('max_columns', 11)

#%% [markdown]
# ## 型変換

#%%
ozone = pd.read_csv('data/ozone.csv', index_col=0)
print('ozone')
display(ozone)
print('出典 : http://archive.ics.uci.edu/ml/datasets/Ozone+Level+Detection')

#%% [markdown]
# 一般的な型変換には`pandas.Series.astype`を使用する。

#%%
help(pd.Series.astype)

#%%
ozone['OzoneDay'].astype(int)

#%% [markdown]
# ### datetime型への変換
# ---
# よく利用する文字列型から datetime 型への変換と datetime 型からの要素抽出を扱う。
# datetime 型への変換には`pandas.to_datetime`を使用する。

#%%
help(pd.to_datetime)

#%%
dti = pd.to_datetime(ozone.index)
dti

#%% [markdown]
# ### タイムゾーンの変更
# ---
# ローカル時間への変更は`tz_localize`を使用する。

#%%
help(pd.Timestamp.tz_localize)

#%%
dtl = dti.tz_localize('Asia/Tokyo')
dtl

#%% [markdown]
# 設定されたタイムゾーンを別のタイムゾーンに変更するには`tz_convert`を使用する。

#%%
dtl.tz_convert('Etc/GMT')

#%% [markdown]
# ### datetime型からの要素抽出
# ---
# 属性を指定して要素を抽出できる。
# `pandas.Series`オブジェクトからは`dt`属性を経由して使用する。例えば、`df['col'].dt.year`のように指定する。
#
# <table class="border text-center">
#     <tr>
#         <td>年</td>
#         <td>year</td>
#     </tr>
#     <tr>
#         <td>月</td>
#         <td>month</td>
#     </tr>
#     <tr>
#         <td>日</td>
#         <td>day</td>
#     </tr>
#     <tr>
#         <td>時</td>
#         <td>hour</td>
#     </tr>
#     <tr>
#         <td>分</td>
#         <td>minute</td>
#     </tr>
#     <tr>
#         <td>秒</td>
#         <td>second</td>
#     </tr>
#     <tr>
#         <td>四半期</td>
#         <td>quarter</td>
#     </tr>
#     <tr>
#         <td>曜日名</td>
#         <td>weekday_name</td>
#     </tr>
#     <tr>
#         <td>曜日番号</td>
#         <td>weekday</td>
#     </tr>
# </table>
#%% [markdown]
# pandas の datetime 型のメソッド。

#%%
print([p for p in dir(pd.Timestamp) if not p.startswith('_')])

#%%
dti.year

#%% [markdown]
# ## 置換

#%%
usarrests = pd.read_csv('data/USArrests.csv')
usarrests.columns = ['state'] + usarrests.columns.tolist()[1:]
state_code = {v: i + 1 for i, v in usarrests['state'].iteritems()}
print('usarrests')
display(usarrests)
print('state_code')
print(state_code)

#%% [markdown]
# ### 辞書を使用した置換
# ---
# `pandas.Series.replace`または`pandas.Series.map`を使用する。
# 辞書にない値の場合、`replace`では元の値のまま、`map`では欠損値になる。

#%%
usarrests['state'].replace(state_code)

#%%
usarrests['state'].map(state_code)

#%% [markdown]
# ### 自己結合
# ---
# `FROM`に続くテーブル名に別の名前をつけることができるので、これを利用して自身のカラムの値をキーにして結合できる。
#%%
engine = sqlalchemy.create_engine('sqlite:///data/chinook.db')
pd.read_sql('employees', engine)

#%%
print('出典 : http://www.sqlitetutorial.net/sqlite-sample-database/')

#%%
pd.read_sql(
    '''SELECT m.firstname || ' ' || m.lastname AS 'Name',
              e.firstname || ' ' || e.lastname AS 'Direct report'
       FROM employees e
       INNER JOIN employees m ON m.employeeid = e.reportsto
       ORDER BY name
    ''', engine)

#%% [markdown]
# ## 集計
#%% [markdown]
# ### pandas

#%%
iris = load_dataset(
    'iris',
    usecols=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
print('iris')
display(iris)

#%% [markdown]
# #### 基本統計量

#%%
iris.describe()

#%% [markdown]
# #### 合計
# ---
# `pandas.DataFrame.sum`を使用。

#%%
iris.sum()

#%% [markdown]
# #### レコード数
# ---
# 欠損を考慮しない場合はインデックスの長さを取得する。

#%%
iris.index.size

#%% [markdown]
# 欠損を考慮する場合は`pandas.DataFrame.count`を使用する。

#%%
help(pd.DataFrame.count)

#%%
iris.count()

#%% [markdown]
# #### 平均
# ---
# `pandas.DataFrame.mean`を使用する。

#%%
help(pd.DataFrame.mean)

#%%
iris.mean()

#%% [markdown]
# #### 標準偏差
# ---
# `pandas.DataFrame.std`を使用する。既定値は`ddof=1`なので、標本標準偏差。

#%%
help(pd.DataFrame.std)

#%%
iris.std()

#%% [markdown]
# #### 最大値
# ---
# `pandas.DataFrame.max`を使用する。

#%%
help(pd.DataFrame.max)

#%%
iris.max()

#%% [markdown]
# #### 最小値
# ---
# `pandas.DataFrame.min`を使用する。

#%%
help(pd.DataFrame.min)

#%%
iris.min()

#%% [markdown]
# #### 累積和
# ---
# `pandas.DataFrame.cumsum`を使用する。

#%%
help(pd.DataFrame.cumsum)

#%%
usarrests = pd.read_csv('data/USArrests.csv', index_col=0)
print('usarrests')
display(usarrests)

#%%
usarrests.cumsum()

#%% [markdown]
# 値順に並べ替えてから累積和・累積割合を算出したりする。

#%%
usarrests['Murder'].sort_values().cumsum() / usarrests['Murder'].sum()

#%% [markdown]
# ### SQL

#%%
engine = sqlalchemy.create_engine('sqlite:///data/iris.sqlite3')
pd.read_sql('iris', engine)

#%% [markdown]
# #### 合計
# ---
# `SUM`関数を使用する。

#%%
pd.read_sql(
    '''SELECT SUM(sepal_length),
              SUM(sepal_width),
              SUM(petal_length),
              SUM(petal_width)
       FROM iris''', engine)

#%% [markdown]
# このままでは見にくいので、通常は列名を付け直す。

#%%
pd.read_sql(
    '''SELECT SUM(sepal_length) AS sep_len_sum,
              SUM(sepal_width) AS sep_wid_sum,
              SUM(petal_length) AS pet_len_sum,
              SUM(petal_width) AS pet_wid_sum
    FROM iris''', engine)

#%% [markdown]
# #### レコード数
# ---
# `COUNT`関数を使用する。欠損は除外される。

#%%
pd.read_sql('SELECT COUNT(*) AS count FROM iris', engine)

#%% [markdown]
# #### 平均
# ---
# `AVG`関数を使用する。

#%%
pd.read_sql(
    '''SELECT AVG(sepal_length) AS sep_len_avg,
              AVG(sepal_width) AS sep_wid_avg,
              AVG(petal_length) AS pet_len_avg,
              AVG(petal_width) AS pet_wid_avg
       FROM iris''', engine)

#%% [markdown]
# #### 標準偏差
# ---
# データベースごとに異なる標準偏差を求める関数が実装されていることもあるが、 SQLite には標準で実装されていない。
# 分散は以下のようにして求められるので、 Python から得られた結果の平方根を算出すれば標準偏差を求められるが、 [extension-functions.c](https://www.sqlite.org/contrib) をインストールすれば関数が利用可能になるので、通常はそちらを使用する。

#%%
query_varp = '''
SELECT AVG(dev.sepal_length * dev.sepal_length) AS sep_len_var,
       AVG(dev.sepal_width * dev.sepal_width) AS sep_wid_var,
       AVG(dev.petal_length * dev.petal_length) AS pet_len_var,
       AVG(dev.petal_width * dev.petal_width) AS pet_wid_var
FROM (SELECT (iris.sepal_length - avg.sepal_length) AS sepal_length,
             (iris.sepal_width - avg.sepal_width) AS sepal_width,
             (iris.petal_length - avg.petal_length) AS petal_length,
             (iris.petal_width - avg.petal_width) AS petal_width
      FROM iris,
           (SELECT AVG(sepal_length) AS sepal_length,
                   AVG(sepal_width) AS sepal_width,
                   AVG(petal_length) AS petal_length,
                   AVG(petal_width) AS petal_width
            FROM iris
           ) AS avg
     ) AS dev
'''
pd.read_sql(query_varp, engine)

#%% [markdown]
# 標本分散の場合は以下の通り。

#%%
query_var = '''
SELECT SUM(dev.sepal_length * dev.sepal_length) / dof.sepal_length AS sep_len_var,
       SUM(dev.sepal_width * dev.sepal_width) / dof.sepal_width AS sep_wid_var,
       SUM(dev.petal_length * dev.petal_length) / dof.petal_length AS pet_len_var,
       SUM(dev.petal_width * dev.petal_width) / dof.petal_width AS pet_wid_var
FROM (SELECT (iris.sepal_length - avg.sepal_length) AS sepal_length,
             (iris.sepal_width - avg.sepal_width) AS sepal_width,
             (iris.petal_length - avg.petal_length) AS petal_length,
             (iris.petal_width - avg.petal_width) AS petal_width
      FROM iris,
           (SELECT AVG(sepal_length) AS sepal_length,
                   AVG(sepal_width) AS sepal_width,
                   AVG(petal_length) AS petal_length,
                   AVG(petal_width) AS petal_width
                   FROM iris
            ) AS avg
     ) AS dev,
     (SELECT COUNT(sepal_length) - 1 AS sepal_length,
             COUNT(sepal_width) - 1 AS sepal_width,
             COUNT(petal_length) - 1 AS petal_length,
             COUNT(petal_width) - 1 AS petal_width
      FROM iris
     ) AS dof
'''
pd.read_sql(query_var, engine)

#%% [markdown]
# SQLite でのカスタム関数の定義方法は以下の通り。 (集約関数の場合)


#%%
class StandardDeviation(object):
    def __init__(self):
        self.values = []

    def step(self, value):
        self.values.append(value)

    def finalize(self):
        return np.std(self.values)


def sqlite_engine_creator():
    con = sqlite3.connect('data/iris.sqlite3')
    con.create_aggregate("STDEV", 1, StandardDeviation)
    return con


engine_with_stdev = sqlalchemy.create_engine('sqlite://',
                                             creator=sqlite_engine_creator)
pd.read_sql('SELECT STDEV(sepal_length) AS sep_len_std FROM iris',
            engine_with_stdev)

#%% [markdown]
# #### 最大値
# ---
# `MAX`関数を使用する。

#%%
pd.read_sql(
    '''SELECT MAX(sepal_length) AS sep_len_max,
              MAX(sepal_width) AS sep_wid_max,
              MAX(petal_length) AS pet_len_max,
              MAX(petal_width) AS pet_wid_max
       FROM iris''', engine)

#%% [markdown]
# #### 最小値
# ---
# `MIN`関数を使用する。

#%%
pd.read_sql(
    '''SELECT MIN(sepal_length) AS sep_len_min,
              MIN(sepal_width) AS sep_wid_min,
              MIN(petal_length) AS pet_len_min,
              MIN(petal_width) AS pet_wid_min
       FROM iris''', engine)

#%% [markdown]
# #### 累積和
# ---
# ウィンドウ関数を使用する。
# SQLite でウィンドウ関数を使用するには**`SQLite>=3.25`が必要**。
#
# `OVER`句で`ORDER BY`を使用して並び替えると先頭から該当行までの集計になる。

#%%
sqlite3.sqlite_version

#%%
engine = sqlalchemy.create_engine('sqlite:///data/usarrests.sqlite3')
pd.read_sql('usarrests', engine)

#%%
pd.read_sql(
    'SELECT SUM(Murder) OVER (ORDER BY Murder) AS cumsum FROM usarrests',
    engine)

#%% [markdown]
# ## スケーリング
# ---
# 分析にあたって、変数のスケール (大きさ) を揃えることが必要な場合がある。実際に使用するケースは中級編で扱う。
#%% [markdown]
# ### pandas
#%% [markdown]
# #### 正規化 (normalization)
# ---
# 変数内の最大値が $1$ 、最小値が $0$ となるようにスケールを変更する。
# 変数内に外れ値があるとうまく機能しない。

#%%
(iris - iris.min()) / (iris.max() - iris.min())

#%% [markdown]
# #### 標準化 (standardization)
# ---
# 変数の平均が $0$ 、標準偏差が $1$ となるようにスケールを変更する。

#%%
(iris - iris.mean()) / iris.std(ddof=0)

#%% [markdown]
# ### SQL

#%%
engine = sqlalchemy.create_engine('sqlite:///data/iris.sqlite3')
pd.read_sql('iris', engine)

#%% [markdown]
# #### 正規化

#%%
query_norm = '''
SELECT ((iris.sepal_length - min.sepal_length) / (max.sepal_length - min.sepal_length)) AS sep_len_norm,
       ((iris.sepal_width - min.sepal_width) / (max.sepal_width - min.sepal_width)) AS sep_wid_norm,
       ((iris.petal_length - min.petal_length) / (max.petal_length - min.petal_length)) AS pet_len_norm,
       ((iris.petal_width - min.petal_width) / (max.petal_width - min.petal_width)) AS pet_wid_norm
FROM iris,
     (SELECT MIN(sepal_length) AS sepal_length,
             MIN(sepal_width) AS sepal_width,
             MIN(petal_length) AS petal_length,
             MIN(petal_width) AS petal_width
      FROM iris
     ) AS min,
     (SELECT MAX(sepal_length) AS sepal_length,
             MAX(sepal_width) AS sepal_width,
             MAX(petal_length) AS petal_length,
             MAX(petal_width) AS petal_width
      FROM iris
     ) AS max
'''
pd.read_sql(query_norm, engine)

#%% [markdown]
# #### 標準化

#%%
query_dev = '''
SELECT (iris.sepal_length - avg.sepal_length) AS sep_len_dev,
       (iris.sepal_width - avg.sepal_width) AS sep_wid_dev,
       (iris.petal_length - avg.petal_length) AS pet_len_dev,
       (iris.petal_width - avg.petal_width) AS pet_wid_dev
FROM iris,
     (SELECT AVG(sepal_length) AS sepal_length,
             AVG(sepal_width) AS sepal_width,
             AVG(petal_length) AS petal_length,
             AVG(petal_width) AS petal_width
      FROM iris
     ) AS avg
'''
iris_dev = pd.read_sql(query_dev, engine)
iris_stdev = np.sqrt(pd.read_sql(query_varp, engine))
iris_dev.columns = iris_stdev.columns = ('sep_len_std', 'sep_wid_std',
                                         'pet_len_std', 'pet_wid_std')
iris_std = iris_dev / iris_stdev.squeeze()
# iris_std = iris_dev / iris_stdev.iloc[0]
iris_std

#%% [markdown]
# カスタム関数を利用する場合は以下の通り。

#%%
pd.read_sql(
    '''SELECT ((iris.sepal_length - avg.sepal_length) / std.sepal_length) AS sep_len_std,
              ((iris.sepal_width - avg.sepal_width) / std.sepal_width) AS sep_wid_std,
              ((iris.petal_length - avg.petal_length) / std.petal_length) AS pet_len_std,
              ((iris.petal_width - avg.petal_width) / std.petal_width) AS pet_wid_std
       FROM iris,
            (SELECT AVG(sepal_length) AS sepal_length,
                    AVG(sepal_width) AS sepal_width,
                    AVG(petal_length) AS petal_length,
                    AVG(petal_width) AS petal_width
             FROM iris
            ) AS avg,
            (SELECT STDEV(sepal_length) AS sepal_length,
                    STDEV(sepal_width) AS sepal_width,
                    STDEV(petal_length) AS petal_length,
                    STDEV(petal_width) AS petal_width
             FROM iris
            ) AS std
    ''', engine_with_stdev)

#%% [markdown]
# ## カテゴリ別集計

#%%
mpg = load_dataset('mpg')
print('mpg')
display(mpg)

#%% [markdown]
# ### pandas
# ---
# `pandas.DataFrame.groupby`と集約関数 (`sum`や`mean`のように複数の値を 1 つにまとめる関数) を使用する。

#%%
help(pd.DataFrame.groupby)

#%%
#%% [markdown]
# `groupby`のメソッド。

print([
    p for p in dir(pd.core.groupby.groupby.DataFrameGroupBy)
    if not p.startswith('_')
])

#%%
mpg.groupby('origin').sum()

#%%
mpg.groupby('origin').mean()

#%% [markdown]
# 同時に複数の関数を使用したり、 pandas にない関数を使用する場合には、`agg`を利用する。

#%%
mpg.groupby('origin').agg(['mean', 'median'])

#%%
mpg.groupby('origin').agg({'horsepower': ['mean', 'median']})


#%%
def percentile95(series):
    return np.percentile(series.loc[~series.isna()], 95)


mpg.groupby('origin').agg({'horsepower': percentile95})

#%% [markdown]
# ### SQL
# ---
# `GROUP BY`句を使用する。

#%%
engine = sqlalchemy.create_engine('sqlite:///data/mpg.sqlite3')
pd.read_sql('mpg', engine)

#%%
pd.read_sql('SELECT origin, COUNT(*) AS count FROM mpg GROUP BY origin',
            engine)

#%%
pd.read_sql('SELECT origin, AVG(horsepower) AS avg FROM mpg GROUP BY origin',
            engine)

#%% [markdown]
# 集約関数を用いた条件抽出には`HAVING`句を使用する。

#%%
pd.read_sql(
    '''SELECT origin, COUNT(*) AS count
       FROM mpg
       GROUP BY origin
       HAVING count > 75
    ''', engine)

#%%
pd.read_sql(
    '''SELECT origin, AVG(horsepower) AS avg
       FROM mpg
       GROUP BY origin
       HAVING COUNT(*) > 75
    ''', engine)

#%% [markdown]
# ## 集約
#%% [markdown]
# ### pandas

#%%
ozone = pd.read_csv('data/ozone.csv', index_col=0)
print('ozone')
display(ozone)

#%% [markdown]
# #### アンサンブル平均
# ---
# 同じ条件 (同一時点など) で複数の値を集計した平均。

#%%
cols = [
    col for col in ozone.columns if col.startswith('WSR') and '_' not in col
]
ozone[cols].mean(axis=1)

#%% [markdown]
# #### 移動平均
# ---
# 一定期間前までの値の平均。値の変化を滑らかにするために使用する。
# `pandas.DataFrame.rolling`を使用する。

#%%
help(pd.DataFrame.rolling)

#%%
ozone.rolling(3).mean()

#%% [markdown]
# 時間軸でアンサンブル平均のように値をまとめる場合は、移動平均から等間隔で抽出したり、年と月などから`groupby`で集約したりする。

#%%
ozone.rolling(3).mean()[::3]

#%%
ozone_with_date = ozone.reset_index()
ozone_with_date['Date'] = pd.to_datetime(ozone_with_date['Date'])
ozone_with_date['year'] = ozone_with_date['Date'].dt.year
ozone_with_date['month'] = ozone_with_date['Date'].dt.month
ozone_with_date.groupby(['year', 'month']).mean()

#%% [markdown]
# ### SQL

#%%
engine = sqlalchemy.create_engine('sqlite:///data/ozone.sqlite3')
pd.read_sql('ozone', engine, index_col='Date')

#%% [markdown]
# #### アンサンブル平均
# ---
# 欠損値がない場合は、以下のように列名を列挙して列数で割ればよい。

#%%
cols = [
    col for col in ozone.columns if col.startswith('WSR') and '_' not in col
]
query_ensemble = f'''
SELECT Date, (({'+'.join(cols)}) / {len(cols)}) AS ensemble_mean
FROM ozone
'''
pd.read_sql(query_ensemble, engine, index_col='Date')

#%% [markdown]
# 欠損値がある場合には、以下のように欠損でない値の数を数える必要がある。

#%%
wsr = pd.read_sql(
    'SELECT Date, ({sum}) AS sum, ({count}) AS count FROM ozone'.format(
        sum='+'.join(cols),
        count='+'.join(
            [f'(CASE {col} WHEN NULL THEN 0 ELSE 1 END)' for col in cols])),
    engine,
    index_col='Date')
wsr.apply(lambda r: np.nan if r['count'] == 0 else r['sum'] / r['count'],
          axis=1)
#%% [markdown]
# #### 移動平均
# ---
# ウィンドウ関数を使用する。
#
# `OVER`句の中で`BETWEEN`や`ROWS`で該当行からの範囲を指定して平均を算出する。
#
# <table>
#     <tr>
#         <td>$n$ PRECEDING</td>
#         <td>$n$ 行前</td>
#     </tr>
#     <tr>
#         <td>$n$ FOLLOWING</td>
#         <td>$n$ 行後</td>
#     </tr>
# </table>
#
# ただし SQL の集約関数の場合、**`NULL`値は無視される**ので注意が必要。
#%% [markdown]
# 3 件での移動平均は以下の通り。

#%%
pd.read_sql(
    '''SELECT Date,
              AVG(WSR0) OVER (ROWS 2 PRECEDING) AS moving_average0,
              AVG(WSR1) OVER (ROWS 2 PRECEDING) AS moving_average1
       FROM ozone
    ''', engine)

#%% [markdown]
# 前後 1 件ずつの範囲での移動平均は以下の通り。

#%%
pd.read_sql(
    '''SELECT Date,
              AVG(WSR0) OVER (ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS moving_average0,
              AVG(WSR1) OVER (ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS moving_average1
       FROM ozone
    ''', engine)
