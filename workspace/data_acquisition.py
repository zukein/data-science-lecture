#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace'))
    print(os.getcwd())
except:
    pass

#%%
import sqlite3
import sqlalchemy
import pandas as pd
from seaborn import load_dataset
from IPython.display import display
pd.set_option('max_row', 5)

#%% [markdown]
# ## データ取得で主に使用するライブラリ
# ---
# Python でデータ分析を行う場合には主に SQL と pandas を使用する。
#
# <table class="border text-center">
#     <tr>
#         <th class="border-top-none border-left-none border-right-bold border-bottom-bold background-default"></th>
#         <th>メリット</th>
#         <th>デメリット</th>
#     </tr>
#     <tr>
#         <th class="border-right-bold border-bottom">表計算ソフト</th>
#         <td>習得が簡単</td>
#         <td>小さいデータしか扱えない</td>
#     </tr>
#     <tr>
#         <th class="border-right-bold border-bottom">pandas</th>
#         <td>Python だけで完結する</td>
#         <td><strong>メモリに収まるデータしか扱えない</strong></td>
#     </tr>
#     <tr>
#         <th class="border-right-bold border-bottom">SQL</th>
#         <td><strong>大規模データも扱える</strong></td>
#         <td>習得するものが増える</td>
#     </tr>
# </table>
#
# SQL を使ったデータベースには複数の種類があるが、以下では Python の標準モジュールに採用されている SQLite3 を使用する。他のデータベースでも基本的な部分は同じ。
# Python の代表的な ORM である SQLAlchemy を使うと、 Python でプログラムを書くようにデータベースを扱うこともできる。また、 pandas からデータベースに接続する場合には SQLAlchemy のエンジンが必要。
#%% [markdown]
# ## データベースへの接続
# ---
# `sqlite3.connect`を使用する。

#%%
help(sqlite3.connect)

#%%
con = sqlite3.connect('data/iris.sqlite3')

#%% [markdown]
# SQL 文を実行するためには`cursor`を取得する。

#%%
cur = con.cursor()
cur.execute('SELECT * FROM iris LIMIT 5').fetchall()

#%% [markdown]
# 使用し終えたら必ず接続を閉じる。閉じ忘れるとファイルがロックされたままになる。

#%%
con.close()

#%% [markdown]
# SQLite 以外で実行するときのため、 SQLAlchemy を使って同様の操作を行う例を示す。

#%%
engine = sqlalchemy.create_engine('sqlite:///data/iris.sqlite3')
con = engine.raw_connection()
cur = con.cursor()
cur.execute('SELECT * FROM iris LIMIT 5').fetchall()

#%%
con.close()

#%% [markdown]
# ただし、 SQL文を実行するだけなら`engine.execute`で可能。

#%%
engine.execute('SELECT * FROM iris LIMIT 5').fetchall()

#%% [markdown]
# ## データ読み込み
#%% [markdown]
# ### pandas
# ---
# `pandas.read_csv`( CSV ファイル ) や`pandas.read_sql_table`( データベース ) を使用する。
# CSV や SQL 以外にも様々な形式を読み込める。

#%%
[att for att in dir(pd) if att.startswith('read_')]

#%%
help(pd.read_csv)

#%%
pd.read_csv('data/Titanic.csv')

#%% [markdown]
# #### CSVファイル読み込みでよく利用するオプション
# ---
# 詳細は[ドキュメント](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)を参照。
#
# <table class="text-left background-default border">
#     <tr>
#         <td><code>header</code></td>
#         <td>列名をどうするか<br />デフォルトは自動で推論<br />列名として使用する行の番号を与える</td>
#     </tr>
#     <tr>
#         <td><code>names</code></td>
#         <td>列名の指定<br />列名の入ったリストを与える</td>
#     </tr>
#     <tr>
#         <td><code>index_col</code></td>
#         <td>行名として使用する列<br />列の番号を与える</td>
#     </tr>
#     <tr>
#         <td><code>usecols</code></td>
#         <td>読み込む列の指定<br />列番号や列名のリストを与える</td>
#     </tr>
#     <tr>
#         <td><code>skipinitialspace</code></td>
#         <td>コンマなどの区切り文字の後のスペースを削除するか<br />真偽値を与える</td>
#     </tr>
#     <tr>
#         <td><code>skiprows</code></td>
#         <td>スキップする行の指定<br />スキップする行番号のリストや先頭からスキップする行数を与える</td>
#     </tr>
#     <tr>
#         <td><code>na_values</code></td>
#         <td>欠損値の指定<br />読み込み時に欠損値として扱いたい文字列などを与える</td>
#     </tr>
#     <tr>
#         <td><code>parse_dates</code></td>
#         <td>日付型データへの変換の指定<br />行名を変換する場合は真偽値を与える<br />特定の列を変換する場合は行番号や行名のリストなどを与える</td>
#     </tr>
#     <tr>
#         <td><code>iterator</code></td>
#         <td>ファイルサイズが大きい場合などにイテレータとして一部ずつ読み込むかどうか<br />真偽値を与える</td>
#     </tr>
#     <tr>
#         <td><code>chunksize</code></td>
#         <td>イテレータで一度に読み込む行数の指定<br />数値を与える</td>
#     </tr>
#     <tr>
#         <td><code>comment</code></td>
#         <td>コメントとしてスキップする行の指定<br /># などコメント行を表す文字列を与える</td>
#     </tr>
#     <tr>
#         <td><code>encoding</code></td>
#         <td>文字列エンコードの指定</td>
#     </tr>
# </table>
#%% [markdown]
# ### SQL
# ---
# `pandas.read_sql_table`か`pandas.read_sql`から`SELECT`文を使用する。
# `SELECT`に続けて列名を列挙し、その後`FROM`に続けてテーブル名 (表計算ソフトのシートに相当) を指定する。列名に * (アスタリスク) を使うと全ての列を指定できる。

#%%
help(pd.read_sql_table)

#%%
engine = sqlalchemy.create_engine('sqlite:///data/iris.sqlite3')

#%%
pd.read_sql_table('iris', engine)

#%%
help(pd.read_sql)

#%%
pd.read_sql('SELECT * FROM iris', engine)

#%% [markdown]
# ## 特定のカラムを取得
#%% [markdown]
# ### pandas
# ---

#%%
iris = load_dataset('iris')
print('iris')
display(iris)

#%% [markdown]
# 1 列のみ取得

#%%
iris['species']

#%%
iris.loc[:, 'species']

#%%
iris.iloc[:, -1]

#%% [markdown]
# 複数列取得

#%%
iris[['sepal_length', 'sepal_width']]

#%%
iris.loc[:, ['sepal_length', 'sepal_width']]

#%%
iris.loc[:, 'sepal_length':'sepal_width']

#%%
iris.iloc[:, [0, 1]]

#%%
iris.iloc[:, :2]

#%% [markdown]
# ### SQL
# ---

#%%
engine = sqlalchemy.create_engine('sqlite:///data/iris.sqlite3')

#%% [markdown]
# 1 列のみ取得

#%%
pd.read_sql_table('iris', engine, columns=['species'])

#%%
pd.read_sql('SELECT species FROM iris', engine)

#%% [markdown]
# 複数列取得

#%%
pd.read_sql_table('iris', engine, columns=['sepal_length', 'sepal_width'])

#%%
pd.read_sql('SELECT sepal_length, sepal_width FROM iris', engine)

#%% [markdown]
# ## 不要なカラムの削除
# ---
# データ分析者がデータベースに変更を加えることはほとんどないため、ここでは pandas で一旦データを読み込んだ後に不要なものを取り除く方法のみ扱う。
#
# `pandas.DataFrame.drop`を使用するが、 inplace 引数を True にするとそのデータフレームの値を削除し、 False にすると列 (行) を削除したコピーを返す。 True の場合、メモリを節約できるが、途中でやり直したい場合にはまたデータ読み込みから始めなければならない。 False の場合はその逆。

#%%
help(pd.DataFrame.drop)

#%%
iris.drop('species', axis=1)

#%%
iris.drop(columns='species')

#%%
iris_copy = iris.copy()
iris_copy.drop('species', axis=1, inplace=True)
iris_copy

#%% [markdown]
# ## データ保存
# ---
# `pandas.DataFrame.to_csv`や`pandas.DataFrame.to_sql`などを使用する。
# ただし、分析者が保存元のデータを変更することはまずないので、 SQL で保存する場合でも別の手元のデータベースを使う。

#%%
help(pd.DataFrame.to_csv)

#%%
iris.to_csv('data/iris_copy.csv')

#%%
help(pd.DataFrame.to_sql)

#%%
engine = sqlalchemy.create_engine('sqlite:///data/iris_copy.sqlite3')
iris.to_sql('iris_copy', engine, if_exists='replace')

#%% [markdown]
# ###### 練習問題
#
# [アメリカの統計情報](https://factfinder.census.gov/faces/nav/jsf/pages/guided_search.xhtml)から以下の条件で人口統計のデータを探し、「SEX BY AGE BY VETERAN STATUS FOR THE CIVILIAN POPULATION 18 YEARS AND OVER」の最新のものをダウンロードする。
# - People:Basic Count/Estimate: Civilian Population
# - All available races
# - All States within United States, Puerto Rico, and the Island Areas
#
# ダウンロードしたCSVファイルからデータを 100 件ずつ読み込み、随時`data/census.db`というデータベースに保存する。データベースへの保存には`pandas.DataFrame.to_sql`を使用する。
# (サイズの大きいCSVファイルや複数に分かれているデータをまとめる練習)

#%%
help(pd.DataFrame.to_sql)

#%%
reader = pd.read_csv(
    'data/ACS_15_SPT_B21001_with_ann.csv', skiprows=1, chunksize=100)
engine = sqlalchemy.create_engine('sqlite:///data/census-example.db')
for i, chunk in enumerate(reader):
    chunk.to_sql(
        'census',
        engine,
        if_exists='replace' if i is 0 else 'append',
        index=False)

#%% [markdown]
# ## データ絞り込み
#%% [markdown]
# ### 件数指定

#%%
titanic = pd.read_csv('data/Titanic.csv')
print('titanic')
display(titanic)

#%% [markdown]
# #### pandas
# ---
# `head`や`iloc`を使用する。

#%%
titanic.head(3)

#%%
titanic.iloc[:3]

#%% [markdown]
# #### SQL
# ---
# `LIMIT`句を使用する。

#%%
engine = sqlalchemy.create_engine('sqlite:///data/iris.sqlite3')
pd.read_sql('SELECT * FROM iris LIMIT 3', engine)

#%% [markdown]
# ### ソート

#%%
mpg = load_dataset('mpg')
print('mpg')
display(mpg)

#%% [markdown]
# #### pandas
# ---
# `pd.DataFrame.sort_values`を使用する。

#%%
help(pd.DataFrame.sort_values)

#%% [markdown]
# 昇順

#%%
mpg.sort_values('acceleration')

#%% [markdown]
# 降順

#%%
mpg.sort_values('acceleration', ascending=False)

#%% [markdown]
# 上位 5 件の取得は以下のように行う。

#%%
mpg.sort_values('acceleration', ascending=False).head(5)

#%% [markdown]
# #### SQL
# ---
# `ORDER BY`を使用する。

#%%
mpg_db = sqlalchemy.create_engine('sqlite:///data/mpg.sqlite3')

#%% [markdown]
# 昇順

#%%
pd.read_sql('SELECT * FROM mpg ORDER BY acceleration', mpg_db)

#%%
pd.read_sql('SELECT * FROM mpg ORDER BY acceleration ASC', mpg_db)

#%% [markdown]
# 降順

#%%
pd.read_sql('SELECT * FROM mpg ORDER BY acceleration DESC', mpg_db)

#%% [markdown]
# 上位 5 件の取得は以下のように行う。

#%%
pd.read_sql('SELECT * FROM mpg ORDER BY acceleration DESC LIMIT 5', mpg_db)

#%% [markdown]
# ### 条件指定
#%% [markdown]
# #### pandas
# ---
# `loc`や`query`を使用する。
#%% [markdown]
# ##### 特定の値のデータ
# ---
# `loc`

#%%
titanic.loc[titanic['Class'] == '1st']

#%% [markdown]
# 条件文の評価結果は真偽値の配列。

#%%
titanic['Class'] == '1st'

#%% [markdown]
# `query`

#%%
titanic.query('Class == "1st"')

#%% [markdown]
# `@`をつけると Python の変数も使用可能。

#%%
c = '1st'
titanic.query('Class == @c')

#%% [markdown]
# ##### 特定の値以外のデータ

#%%
titanic.loc[titanic['Class'] != 'Crew', ['Class', 'Survived']]

#%%
titanic.query('Class != "Crew"')[['Class', 'Survived']]

#%% [markdown]
# ##### 一定の範囲内のデータ

#%%
iris.loc[(2 < iris['petal_length']) & (iris['petal_length'] < 4)]

#%%
iris.query('2 < petal_length < 4')

#%% [markdown]
# ##### 先頭文字列
# ---
# `pandas.Series.str.startswith`を使用する。
# `pandas.Series.str`や`pandas.Index.str`には他にも文字列操作のためのメソッドが用意されている。

#%%
print([att for att in dir(pd.Series.str) if not att.startswith('_')])

#%%
help(pd.Series.str.startswith)

#%%
mpg.loc[mpg['name'].str.startswith('toyota')]

#%%
mpg.query('name.str.startswith("toyota")')

#%% [markdown]
# ##### 部分文字列
# ---
# `pandas.Series.str.contains`を使用する。

#%%
help(pd.Series.str.contains)

#%%
mpg.loc[mpg['name'].str.contains('corolla')]

#%%
mpg.query('name.str.contains("corolla")')

#%% [markdown]
# #### SQL
# ---
# `WHERE`句を使用する。

#%%
titanic_db = sqlalchemy.create_engine('sqlite:///data/titanic.sqlite3')
iris_db = sqlalchemy.create_engine('sqlite:///data/iris.sqlite3')
mpg_db = sqlalchemy.create_engine('sqlite:///data/mpg.sqlite3')
iris_duplicated_db = sqlalchemy.create_engine(
    'sqlite:///data/iris_duplicated.sqlite3')

#%% [markdown]
# ##### 特定の値のデータ

#%%
pd.read_sql('SELECT * FROM titanic WHERE Class = "1st"', titanic_db)

#%% [markdown]
# ##### 特定の値以外のデータ

#%%
pd.read_sql('SELECT Class, Survived FROM titanic WHERE Class != "Crew"',
            titanic_db)

#%%
pd.read_sql('SELECT Class, Survived FROM titanic WHERE Class <> "Crew"',
            titanic_db)

#%% [markdown]
# ##### 一定の範囲内のデータ
# ---
# `BETWEEN`を使用する。 (両端が含まれる)

#%%
pd.read_sql('SELECT * FROM iris WHERE petal_length BETWEEN 2 AND 4', iris_db)

#%% [markdown]
# 両端を含まないようにするには、以下のようにする。

#%%
pd.read_sql('SELECT * FROM iris WHERE 2 < petal_length < 4', iris_db)

#%% [markdown]
# ##### 先頭文字列
# ---
# `LIKE`とワイルドカード`%`を使用する。

#%%
pd.read_sql('SELECT * FROM mpg WHERE name LIKE "toyota%"', mpg_db)

#%% [markdown]
# ##### 部分文字列
# ---
# 先頭文字列と同様に`LIKE`とワイルドカード`%`を使用する。

#%%
pd.read_sql('SELECT * FROM mpg WHERE name LIKE "%corolla%"', mpg_db)

#%% [markdown]
# ### 重複の除去

#%%
iris_duplicated = iris.sample(
    iris.index.size + 10, replace=True,
    random_state=1234).reset_index(drop=True)
iris_duplicated.to_sql(
    'duplicated', iris_duplicated_db, if_exists='replace', index=False)
print('iris_duplicated')
display(iris_duplicated)

#%% [markdown]
# #### pandas
# ---
# `pandas.DataFrame.drop_duplicates`を使用する。

#%%
help(pd.DataFrame.drop_duplicates)

#%%
iris_duplicated.drop_duplicates()

#%% [markdown]
# #### SQL
# ---
# `DISTINCT`を使用する。

#%%
pd.read_sql('SELECT DISTINCT * FROM duplicated', iris_duplicated_db)

#%% [markdown]
# ###### 練習問題
#
# 上で保存したアメリカの人口統計データから、以下の条件に合致するデータを pandas と SQL でそれぞれ抽出する。
#
# - Geography カラムの値が New York
# - Population Group カラムの値が Total population のものは除外
# - Estimate; Total: カラムの値が大きいものから上位 5 件
# - 取り出すカラムは Population Group と Estimate; Total:
#%% [markdown]
# pandas

#%%

#%% [markdown]
# SQL

#%%

#%% [markdown]
# ### ランダムサンプリング
# ---
# - 数十万レコードのデータに対して、ランダムまたは一定間隔にデータを抽出できる
# - サンプリングやアンサンブル平均によって適量にデータ量を減らすことができる
#
#%% [markdown]
# #### pandas
# ---
# `pandas.DataFrame.sample`を使用する。

#%%
help(pd.DataFrame.sample)

#%%
titanic.sample(10, random_state=1234)

#%% [markdown]
# #### SQL
# ---
# 乱数を生成する関数を使用して全レコードを並び替え、`LIMIT`で件数を指定して取得する手法もあるが、ランダムサンプリングを行うのは通常レコード数が膨大なときなので、全レコードを並び変えるのは非効率。
# ID などレコードごとに固有の値を持つカラムのみを並び替え、それに基づいてデータを取得する。

#%%
titanic_with_id = sqlalchemy.create_engine(
    'sqlite:///data/titanic_with_id.sqlite3')
pd.read_sql('SELECT * FROM titanic LIMIT 5', titanic_with_id)

#%%
ids = pd.read_sql('SELECT id FROM titanic', titanic_with_id).sample(
    10, random_state=1234)['id']
query = f'SELECT * FROM titanic WHERE id IN ({",".join([str(i) for i in ids])})'
print(query)
pd.read_sql(query, titanic_with_id)

#%% [markdown]
# ## データ統合
# ---
# データベースでは以下のように必要な情報が複数のテーブルにまたがっていることがある。
#
# - 共通する情報が別のテーブルにまとめられてる
#
# <table class="text-center border">
#     <tr>
#         <th class="border-none background-default" colspan="4">customer テーブル (顧客情報)</th>
#     </tr>
#     <tr>
#         <th>id</th>
#         <th>氏名</th>
#         <th>メールアドレス</th>
#         <th>ユーザーランク</th>
#     </tr>
#     <tr>
#         <td>1</td>
#         <td>AAA BBB</td>
#         <td>aa@bb.com</td>
#         <td>S</td>
#     </tr>
#     <tr>
#         <td>2</td>
#         <td>XXX YYY</td>
#         <td>cc@dd.org</td>
#         <td>A</td>
#     </tr>
# </table>
#
# <table class="text-center border">
#     <tr>
#         <th class="border-none background-default" colspan="3">item テーブル (商品情報)</th>
#     </tr>
#     <tr>
#         <th>id</th>
#         <th>名称</th>
#         <th>単価</th>
#     </tr>
#     <tr>
#         <td>1</td>
#         <td>M</td>
#         <td>1000</td>
#     </tr>
#     <tr>
#         <td>2</td>
#         <td>N</td>
#         <td>1500</td>
#     </tr>
# </table>
#
# <table class="text-center border">
#     <tr>
#         <th class="border-none background-default" colspan="5">sales テーブル (売上情報)</th>
#     </tr>
#     <tr>
#         <th>id</th>
#         <th>customer_id</th>
#         <th>item_id</th>
#         <th>数量</th>
#         <th>金額</th>
#     </tr>
#     <tr>
#         <td>1</td>
#         <td>1</td>
#         <td>2</td>
#         <td>2</td>
#         <td>3000</td>
#     </tr>
#     <tr>
#         <td>2</td>
#         <td>2</td>
#         <td>1</td>
#         <td>1</td>
#         <td>1000</td>
#     </tr>
#     <tr>
#         <td>3</td>
#         <td>2</td>
#         <td>2</td>
#         <td>3</td>
#         <td>4500</td>
#     </tr>
# </table>
#
# - 同種の情報が別のテーブルにまたがっている
#
# <table class="text-center border">
#     <tr>
#         <th class="border-none background-default" colspan="2">国内売上</th>
#     </tr>
#     <tr>
#         <th>id</th>
#         <th>金額</th>
#     </tr>
#     <tr>
#         <td>1</td>
#         <td>2500</td>
#     </tr>
#     <tr>
#         <td>2</td>
#         <td>1250</td>
#     </tr>
#     <tr>
#         <td>3</td>
#         <td>3000</td>
#     </tr>
# </table>
#
# <table class="text-center border">
#     <tr>
#         <th class="border-none background-default" colspan="2">海外売上</th>
#     </tr>
#     <tr>
#         <th>id</th>
#         <th>金額</th>
#     </tr>
#     <tr>
#         <td>1</td>
#         <td>20</td>
#     </tr>
#     <tr>
#         <td>2</td>
#         <td>50</td>
#     </tr>
# </table>
#
# データを分析するにあたっては、これらの中から必要な情報をまとめなければならない。
# テーブル間の関係は ER 図などにまとめられていることがあるので、適宜参照する。
#%% [markdown]
# ### 結合
# ---
# テーブルを横方向に統合。
#%% [markdown]
# #### pandas
# ---
# `pandas.merge`や`pandas.concat`を使用する。
# `pandas.concat`は比較する値が 2 つのテーブルのインデックス同士になる。 (日付をインデックスにしている場合など)

#%%
help(pd.merge)

#%%
help(pd.concat)

#%% [markdown]
# ##### 内部結合
# ---
# 2 つのテーブルのある列同士の値で、両方に同じ値がある行を結合する方法。
#%% [markdown]
# `pandas.merge`

#%%
left = pd.read_csv('data/sample.csv', usecols=['A', 'B', 'Key']).iloc[:4]
print('left')
display(left)
right = pd.read_csv(
    'data/sample.csv', usecols=['C', 'D',
                                'Key']).iloc[1:5].reset_index(drop=True)
print('right')
display(right)

#%%
pd.merge(left, right, on='Key')

#%% [markdown]
# 比較対象のカラムには重複する値があっても良い。

#%%
left2 = left.append(left.sample(2, random_state=1234)).reset_index(drop=True)
print('left2')
display(left2)
right2 = right.append(right.sample(2,
                                   random_state=2345)).reset_index(drop=True)
print('right2')
display(right2)

#%%
pd.merge(left2, right2, on='Key')

#%% [markdown]
# `pandas.concat`

#%%
left = pd.read_csv('data/sample.csv', usecols=['A', 'B', 'C', 'D']).iloc[:4]
print('left')
display(left)
right = pd.read_csv(
    'data/sample.csv', usecols=['B', 'D', 'F']).iloc[[2, 3, 6, 7]]
print('right')
display(right)

#%%
pd.concat([left, right], axis=1, join='inner')

#%% [markdown]
# 1 列 (Series オブジェクト) 追加するときにも使用可能。

#%%
df = pd.read_csv('data/sample.csv', usecols=['A', 'B', 'C', 'D']).iloc[:4]
print('df')
display(df)
series = pd.Series([f'X{i}' for i in range(df.index.size)])
print('series')
display(series)

#%%
series.name = 'X'
pd.concat([df, series], axis=1)

#%% [markdown]
# 同様のことは以下でも可能。

#%%
df['X'] = series
df

#%% [markdown]
# ##### 外部結合
# ---
# 2 つのテーブルのある列同士の値で、全ての値を用いて結合する方法。
# どちらかにある値を基準に結合する左外部結合・右外部結合もある。 (`pandas.merge`のみ)
# 逆のテーブルに値がないところは欠損値になる。
#%% [markdown]
# `pandas.merge`

#%%
left = pd.read_csv('data/sample.csv', usecols=['A', 'B', 'Key']).iloc[:4]
print('left')
display(left)
right = pd.read_csv(
    'data/sample.csv', usecols=['C', 'D',
                                'Key']).iloc[1:5].reset_index(drop=True)
print('right')
display(right)

#%%
pd.merge(left, right, how='outer', on='Key')

#%% [markdown]
# 左外部結合

#%%
pd.merge(left, right, how='left', on='Key')

#%% [markdown]
# 右外部結合

#%%
pd.merge(left, right, how='right', on='Key')

#%% [markdown]
# `pandas.concat`

#%%
left = pd.read_csv('data/sample.csv', usecols=['A', 'B', 'C', 'D']).iloc[:4]
print('left')
display(left)
right = pd.read_csv(
    'data/sample.csv', usecols=['B', 'D', 'F']).iloc[[2, 3, 6, 7]]
print('right')
display(right)

#%%
pd.concat([left, right], axis=1)

#%% [markdown]
# #### SQL

#%%
engine = sqlalchemy.create_engine('sqlite:///data/sample.sqlite3')

#%% [markdown]
# ##### 内部結合
# ---
# `INNER JOIN`と`ON`を使用。

#%%
for table in ['left', 'right']:
    print(table)
    display(pd.read_sql(f'SELECT * FROM {table}', engine))

#%%
pd.read_sql('SELECT * FROM left INNER JOIN right ON left.Key = right.Key',
            engine)

#%% [markdown]
# ##### 外部結合
# ---
# `OUTER JOIN`と`ON`を使用。
# SQLite では`FULL OUTER JOIN`と`RIGHT OUTER JOIN`はサポートされていないので、左外部結合のみ。

#%%
print('left')
display(pd.read_sql('SELECT * FROM left', engine))
print('right')
display(pd.read_sql('SELECT * FROM right', engine))

#%%
pd.read_sql('SELECT * FROM left LEFT OUTER JOIN right ON left.Key = right.Key',
            engine)

#%% [markdown]
# ### Union処理
# ---
# テーブルを縦方向に統合。
#%% [markdown]
# #### pandas
# ---
# `pandas.concat`と`pandas.DataFrame.append`が使用可能。

#%%
sample = pd.read_csv('data/sample.csv', usecols=['A', 'B', 'C', 'D'])
first = sample.iloc[:4]
second = sample.iloc[4:8].reset_index(drop=True)
third = sample.iloc[8:].reset_index(drop=True)
for name, df in zip(['first', 'second', 'third'], [first, second, third]):
    print(name)
    display(df)

#%% [markdown]
# `pandas.concat`

#%%
pd.concat([first, second, third])

#%% [markdown]
# `pandas.DataFrame.append`
# Python のリストと異なり、**元のオブジェクトを変更せず**新しいオブジェクトを返す。

#%%
help(pd.DataFrame.append)

#%%
union = first.append([second, third])

#%%
print('first')
first

#%%
print('union')
union

#%% [markdown]
# インデックスを振り直す場合は、`ignore_index`を True にする。

#%%
pd.concat([first, second, third], ignore_index=True)

#%%
first.append([second, third], ignore_index=True)

#%% [markdown]
# #### SQL
# ---
# `UNION ALL`を使用する。 (`UNION`は重複をチェックするがその分コストがかかるので、できる限り避ける)

#%%
engine = sqlalchemy.create_engine('sqlite:///data/sample.sqlite3')

#%%
for table in ['first', 'second', 'third']:
    print(table)
    display(pd.read_sql(f'SELECT * FROM {table}', engine))

#%%
pd.read_sql(
    '''
    SELECT * FROM first
    UNION ALL
    SELECT * FROM second
    UNION ALL
    SELECT * FROM third
    ''', engine)

#%% [markdown]
# ###### 練習問題
#
# [アメリカの統計情報](https://factfinder.census.gov/faces/nav/jsf/pages/guided_search.xhtml)から以下の条件で 2 種類のデータを探し、共通してデータがある年度のもののうち、それぞれ最新のものから 2 期分をダウンロードする。
#
# 産業統計 (Wholesale Trade: Geographic Area Series: Summary Statistics for the U.S., States, Metro Areas, Counties, and Places)
# - Business and Industry:Expenses & Purchased Services: All Expenses
# - All States within United States, Puerto Rico, and the Island Areas
# - ALL: All available codes
#
# 人口統計 (Industry by Sex and Median Earnings in the Past 12 Months for the Civilian Employed Population 16 Years and Over)
# - People:Basic Count/Estimate: Civilian Population
# - All States within United States, Puerto Rico, and the Island Areas
#
# ダウンロードした CSV ファイルを年度が同じもの同士で州をキーにして内部結合し、異なる年度のものも 1 つのデータフレームにまとめる。それを`data/merge.db`というデータベースに保存する。

#%%

#%% [markdown]
# ## インターネットからのデータ収集
# ---
# 手元にあるデータだけでは不十分な場合に、インターネットから情報を集めることはよくある。その際に Python で使用する主なパッケージを以下に示す。
#%% [markdown]
# ### [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
# ---
# HTML から情報を取り出すためのライブラリ。
# CSS セレクタを使って要素を選択できる。
#%% [markdown]
# ### [Scrapy](https://scrapy.org/)
# ---
# ウェブサイトを巡回してデータを取得するスクレイピングのためのフレームワーク。
#%% [markdown]
# ### [Selenium](https://www.seleniumhq.org/docs/)
# ---
# Web ブラウザを操作するためのライブラリ。
# 主に JavaScript を使用した動的なサイトから情報を取得する場合に使用。
#%% [markdown]
# ### [Splash](https://splash.readthedocs.io/en/stable/)
# ---
# Selenium と同じく Web ブラウザを操作するためのものだが、 HTTP API を備えた Docker のサービスとして提供。
# 画像の読み込みを無効化したりできる。
