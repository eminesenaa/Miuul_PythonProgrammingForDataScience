import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()


# ? grouping

df.groupby("sex")["age"].mean()
df.groupby("sex").agg({"age": "mean"})

df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean", "sum"], "survived": "mean"})

df.groupby(["sex","embark_town"]).agg({"age": "mean", "survived": "mean"})

df.groupby(["sex","embark_town", "class"]).agg({"age": "mean", "survived": "mean"})

df.groupby(["sex","embark_town", "class"]).agg({"age": "mean", "survived": "mean", "sex" : "count"})





# ? count():
# Counts the number of rows or elements in a dataset.
# Use Case: Useful for determining the total count of items in a dataset.

# ? first():
# Returns the first element or value in a dataset.
# Use Case: Often used to get the first value in a dataset or column when aggregating data.

# ? last():
# Returns the last element or value in a dataset.
# Use Case: Helpful for retrieving the last value in a dataset or column during aggregation.

# ? mean():
# Calculates the average value of a numeric dataset by summing values and dividing by the count.
# Use Case: Provides the mean or average value of a dataset.

# ? median():
# Finds the middle value in a dataset when sorted, or the average of the two middle values in case of an even count.
# Use Case: Useful for finding the central value of a dataset.

# ? min():
# Identifies the minimum (smallest) value in a numeric dataset.
# Use Case: Helpful for determining the minimum value within a dataset.

# ? max():
# Identifies the maximum (largest) value in a numeric dataset.
# Use Case: Useful for determining the maximum value within a dataset.

# ? std() (Standard Deviation):
#  Measures the dispersion of values around the mean. Indicates how spread out the data is.
# Use Case: Useful for understanding the variability or volatility of data.

# ? var() (Variance):
# Measures how much values deviate from the mean. It's the square of the standard deviation.
# Use Case: Provides a quantitative measure of data spread.

# ? sum():
# Adds up all the values in a numeric dataset.
# Use Case: Useful for finding the total or cumulative sum of values.
