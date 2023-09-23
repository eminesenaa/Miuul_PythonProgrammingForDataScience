import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
pd.set_option('display.width' , 600)  
df = sns.load_dataset("titanic")
df.head()

# ? apply
# The apply() method in pandas is used to apply a function along an axis (row or column) of a DataFrame or Series.
# It can be applied to a single Series or to an entire DataFrame.

# ? lambda
# A lambda function is a small, anonymous function defined using the lambda keyword. It can take any number of arguments but can only have one expression. 
# Lambda functions are often used when you need a simple function for a short period and don't want to define a full function using def.

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5
df.head()

for col in df:
    if "age" in col:
        df[col] = df[col] / 10

# via lambda and apply

df[["age" , "age2" , "age3" ]].apply(lambda x: x/10).head() 

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head() 

######

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head() 


def standard_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: standard_scaler(x)).head() 



