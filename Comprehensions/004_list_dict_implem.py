import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns


newDf = []
for col in df.columns:
    newDf.append(col.upper())

df.columns = [col.upper() for col in df.columns]
df.columns


# ? if variable includes "INS" add FLAG else add NO_FLAG

[col for col in df.columns if "INS" in col]
["FLAG_" + col  if "INS" in col else "NO_FLAG_" + col for col in df.columns]


# ? key will be string, value will be its functions for numeric variables
df = sns.load_dataset("car_crashes")
df.columns

num_columns = [col for col in df.columns if df[col].dtype != "O"] #  this catches the non categoric variables
dict = {}
agg_list = ["mean" , "min" , "max" , "sum"]


#for col in num_columns:
#    dict[col] = agg_list

{col : agg_list for col in df.columns if df[col].dtype != "O"}
dict.items()



#! super easy. this provides to implement all values functions in dictioanry to the common keys
new_dict = {col: agg_list for col in num_columns }
df[num_columns].head()
df[num_columns].agg(new_dict)





