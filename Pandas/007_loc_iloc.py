import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# ? iloc: integer based selection

df.iloc[0:3] # ! select the first three elements 0 1 2 indexes
df.iloc[0,0] # select element in row zero column zero


#? loc: label based selection

df.loc[0:3] # ! selects 0 1 2 3 indexes
df.iloc[0:3] 


df.iloc[0:3, 0:3] # this only works for integers, cannot take age or other str
df.loc[0:3, "age"]

col_names = ["age" , "embarked" , "alive"]
df.loc[0:3, col_names]