from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

pd.set_option('display.max_columns' , None)
pd.set_option('display.width' , 600)
df = sns.load_dataset("titanic")
df.head()

df["embarked"].value_counts()
df["sex"].unique()
df["sex"].nunique()

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category " , "object" , "bool"]]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64" , "float64"]]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category " , "object"]]

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]


df[cat_cols].nunique()

[col for col in df.columns if col not in cat_cols]


def cat_summary(dataFrame , col_name):
    print(pd.DataFrame({col_name: dataFrame[col_name].value_counts(), 
                         "Ratio" : 100 * dataFrame[col_name].value_counts() / len(dataFrame)}))
    print("#########################################")

cat_summary(df, "sex")

for col in cat_cols:
         cat_summary(df, col)

# adding visual property
def cat_summary(dataFrame , col_name, plot=False):
    print(pd.DataFrame({col_name: dataFrame[col_name].value_counts(), 
                        "Ratio" : 100 * dataFrame[col_name].value_counts() / len(dataFrame)}))
    print("#########################################")
    if plot:
        sns.countplot(x  = dataFrame[col_name], data = dataFrame)
        plt.show(block = True)



for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int) # True and false becomes 1 and 0.
    cat_summary(df, col,plot=True)
