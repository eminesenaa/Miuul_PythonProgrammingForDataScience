import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

# in order: "content" , "row" , "column"
df.pivot_table("survived", "sex" , "embarked")

df.pivot_table("survived", "sex" , "embarked" , aggfunc = "std")

df.pivot_table("survived", "sex" , ["embarked" , "class"])

df.pivot_table("survived", ["sex" , "age"] , ["embarked" , "class"])

df["new_age"] = pd.cut(df["age"] , [0,10,18,25,40,90]) # moved the age content into the column to calculate the survival rate by age range

df.pivot_table("survived" , "sex" , ["new_age" , "class"])
pd.set_option('display.width' , 600) # expanded the output window

