#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'workspace'))
	print(os.getcwd())
except:
	pass

#%%
import pandas as pd
from IPython.display import display
pd.set_option('max_rows', 5)
pd.set_option('max_columns', 13)
pd.set_option('precision', 3)

#%% [markdown]
# ## 解釈にあたっての注意点
# ---
# - 要約された数値の背景を考える
#  - 主張を補強するために一部のみを切り出したりしていないか
#  - 外れ値のありそうなデータなのに平均などの外れ値に弱いものを使っていないか
# - 値が自分の感覚とかけ離れていないか注意する
#  - 元データに不適切なもの (集計行など) が混入している可能性もある
#%% [markdown]
# ### シンプソンのパラドックス
# ---
# 以下のような工場・製品ごとの品質データがある。

#%%
simpson1 = pd.read_csv('data/simpson1.csv')
cross = pd.crosstab(
    simpson1['品質'], [simpson1['製品'], simpson1['工場']],
    values=simpson1['数量'],
    aggfunc=sum)
cross.index.name = None
cross.columns.names = [None, None]
cross

#%% [markdown]
# 列方向に割合を集計すると製品 A でも製品 B でも工場 1 のほうが不良品率は低い。

#%%
cross_ratio = pd.crosstab(
    simpson1['品質'], [simpson1['製品'], simpson1['工場']],
    values=simpson1['数量'],
    aggfunc=sum,
    normalize='columns')
cross_ratio.index.name = None
cross_ratio.columns.names = [None, None]
cross_ratio

#%% [markdown]
# しかし、製品を区別せずに集計すると、工場 2 のほうが不良品率は低くなる。

#%%
cross_all = pd.crosstab(
    simpson1['品質'],
    simpson1['工場'],
    values=simpson1['数量'],
    aggfunc=sum,
    normalize='columns')
cross_all.index.name = None
cross_all.columns.name = None
cross_all

#%% [markdown]
# このような状態をシンプソンのパラドックスという。
#%% [markdown]
# 同様に、以下のようなデータがあるときに

#%%
simpson2 = pd.read_csv('data/simpson2.csv')
cross2 = pd.crosstab(
    simpson2['属性1'], [simpson2['属性2'], simpson2['属性3']],
    values=simpson2['数量'],
    aggfunc=sum)
cross2.index.name = None
cross2.columns.names = [None, None]
display(cross2)
cross2_ratio = pd.crosstab(
    simpson2['属性1'], [simpson2['属性2'], simpson2['属性3']],
    values=simpson2['数量'],
    aggfunc=sum,
    normalize='columns')
cross2_ratio.index.name = None
cross2_ratio.columns.names = [None, None]
display(cross2_ratio)
cross2_all = pd.crosstab(
    simpson2['属性1'],
    simpson2['属性2'],
    values=simpson2['数量'],
    aggfunc=sum,
    normalize='columns')
cross2_all.index.name = None
cross2_all.columns.name = None
display(cross2_all)

#%% [markdown]
# 以下のように子供が遊んでいて汚れてしまったトランプのデータだとすると、汚れの有無によって絵柄カードの割合が異なるのは単なる偶然であり、絵柄によってカードの色の割合が異なるように製造されているとは考えない。

#%%
trump = cross2.copy()
trump.index = ['赤', '黒']
trump.columns = pd.MultiIndex(
    levels=[['汚れあり', '汚れなし'], ['絵柄', '数字']],
    labels=[[0, 0, 1, 1], [0, 1, 0, 1]],
    names=[None, None])
trump

#%% [markdown]
# 一方、以下のように従前の治療法と新しい治療法を男女別に比較したデータだとすると、男女別で集計した場合と全体で集計した場合に結論が異なるのはおかしいと感じられる。
# そのため、男女の治療法に対する選好の違いを考えたり、男女のサンプル数の違いによる影響をコントロールしたりして、詳しく検討する必要がある。

#%%
treat = cross2.copy()
treat.index = ['生存', '死亡']
treat.columns = pd.MultiIndex(
    levels=[['男性', '女性'], ['旧治療法', '新治療法']],
    labels=[[0, 0, 1, 1], [0, 1, 0, 1]],
    names=[None, None])
treat

#%% [markdown]
# 以上のように、データから得られる知見はデータそのものから自動的に得られるわけではなく、ドメイン知識と呼ばれるデータの背景にある事情と併せて初めて意味を持つ。
#%% [markdown]
# ## 作成にあたっての注意点
# ---
# - 集計の目的・何が知りたいのかを意識する
#  - 全体の傾向を知りたい・グループ間で比較したいなど
#%% [markdown]
# ###### 練習問題
#
# アメリカの州・人種・性・年齢階級・退役軍人別の人口統計データから関心のある軸を設定して、集計してみる。 (U.S. Census Bureau, 2011-2015 American Community Survey 5-Year Estimates より抜粋)
# 入手元 : [American Fact Finder](https://factfinder.census.gov/faces/nav/jsf/pages/guided_search.xhtml)

#%%
population = pd.read_csv(
    'data/ACS_15_SPT_B21001_with_ann.csv',
    header=1,
    usecols=[
        'Id', 'Id2', 'Geography', 'Id.1', 'Population Group',
        'Estimate; Total:', 'Estimate; Total: - Veteran',
        'Estimate; Total: - Nonveteran', 'Estimate; Total: - Male:',
        'Estimate; Total: - Male: - Veteran',
        'Estimate; Total: - Male: - Nonveteran',
        'Estimate; Total: - Male: - 18 to 34 years:',
        'Estimate; Total: - Male: - 18 to 34 years: - Veteran',
        'Estimate; Total: - Male: - 18 to 34 years: - Nonveteran',
        'Estimate; Total: - Male: - 35 to 54 years:',
        'Estimate; Total: - Male: - 35 to 54 years: - Veteran',
        'Estimate; Total: - Male: - 35 to 54 years: - Nonveteran',
        'Estimate; Total: - Male: - 55 to 64 years:',
        'Estimate; Total: - Male: - 55 to 64 years: - Veteran',
        'Estimate; Total: - Male: - 55 to 64 years: - Nonveteran',
        'Estimate; Total: - Male: - 65 to 74 years:',
        'Estimate; Total: - Male: - 65 to 74 years: - Veteran',
        'Estimate; Total: - Male: - 65 to 74 years: - Nonveteran',
        'Estimate; Total: - Male: - 75 years and over:',
        'Estimate; Total: - Male: - 75 years and over: - Veteran',
        'Estimate; Total: - Male: - 75 years and over: - Nonveteran',
        'Estimate; Total: - Female:', 'Estimate; Total: - Female: - Veteran',
        'Estimate; Total: - Female: - Nonveteran',
        'Estimate; Total: - Female: - 18 to 34 years:',
        'Estimate; Total: - Female: - 18 to 34 years: - Veteran',
        'Estimate; Total: - Female: - 18 to 34 years: - Nonveteran',
        'Estimate; Total: - Female: - 35 to 54 years:',
        'Estimate; Total: - Female: - 35 to 54 years: - Veteran',
        'Estimate; Total: - Female: - 35 to 54 years: - Nonveteran',
        'Estimate; Total: - Female: - 55 to 64 years:',
        'Estimate; Total: - Female: - 55 to 64 years: - Veteran',
        'Estimate; Total: - Female: - 55 to 64 years: - Nonveteran',
        'Estimate; Total: - Female: - 65 to 74 years:',
        'Estimate; Total: - Female: - 65 to 74 years: - Veteran',
        'Estimate; Total: - Female: - 65 to 74 years: - Nonveteran',
        'Estimate; Total: - Female: - 75 years and over:',
        'Estimate; Total: - Female: - 75 years and over: - Veteran',
        'Estimate; Total: - Female: - 75 years and over: - Nonveteran'
    ])
population.columns = [col.replace('Estimate; ', '') for col in population.columns]
print('population')
display(population)


#%%



