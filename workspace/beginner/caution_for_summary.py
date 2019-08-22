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
population.columns = [
    col.replace('Estimate; ', '') for col in population.columns
]
print('population')
display(population)

#%%1

#%%2

#%%3

#%%4

#%%5
