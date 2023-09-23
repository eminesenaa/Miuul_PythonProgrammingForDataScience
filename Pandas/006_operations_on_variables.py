import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)  # It deletes the ellipsis where the items are not shown.
df = sns.load_dataset("titanic")
print(df)


"age" in df


df["age"].head()
df.age.head()

type(df["age"].head()) # this is now the panda series, if you want it to remain as a dataframe, you need to enclose it in double square brackets:
type(df[["age"]].head())

df[["age" , "alive"]] # choosing mutliple elements

col_names = [ "age" ,"adult_male" ,"alive"]
df[col_names]


df["age2"] = df["age"]**2  # adding a new variable, here we add the expression "age2" containing the squares of the "age" variables.,
df["age3"] = df["age"] / df["age2"]


df.drop("age3", axis = 1, inplace = True) # deleting age3 column


df.loc[:, df.columns.str.contains("age")].head() # select only age variables
df.loc[:, ~df.columns.str.contains("age")].head() # select all but age variables


