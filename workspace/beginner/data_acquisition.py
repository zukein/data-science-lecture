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
from IPython.display import display
pd.set_option('max_row', 5)

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

#%%1

#%%2

#%%3

#%%4

#%%5

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

#%%1

#%%2

#%%3

#%%4

#%%5

#%% [markdown]
# SQL

#%%1

#%%2

#%%3

#%%4

#%%5

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

#%%1

#%%2

#%%3

#%%4

#%%5
