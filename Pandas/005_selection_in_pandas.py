import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.indexdf[0:13]
df.drop(0, axis = 0).head() # now it stars from the 1st index.

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis = 0).head(10) 
# value assignment or "inplace = True" operations can be applied to make these deletions permanent.


# ? convert variable to index

df["age"].head()
df.age.head()

df.index = df["age"] # age is added as an index
df.drop("age", axis = 1).head() # axis = 1 means, it is deleted from columns
df.drop("age", axis = 1, inplace = True)


# ? convert index to variable

df.index 

df["age"] # error will occur, because we deleted the age permanently

df["age"] = df.index
df.head()
df.drop("age", axis = 1, inplace = True)
df.reset_index().head()


