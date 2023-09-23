# Seaborn is a high-level data visualization library for data analysis, data visualization, and graphing in Python.

import seaborn as sns

df = sns.load_dataset("titanic") # The load_dataset function in the Seaborn library takes the name of the dataset and loads this dataset.
df.head()
df.tail(3)

df.columns
df.index

df.info() # The f.info() function is a useful way to show general information of a Pandas DataFrame:
# Total number of rows (number of input data points).
# The name and data type of each column.
# The number of non-null values in each column.
#  Memory usage in each column.

df.describe().T # It is used to display basic statistical information of numeric columns in DataFrame.

df.isnull().values.any()
df.isnull().sum() # calculated how many missing in each value


df["sex"].head()
df["sex"].value_counts()