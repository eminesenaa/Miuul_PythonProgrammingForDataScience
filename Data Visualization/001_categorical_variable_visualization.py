from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# categorical variable: column chart: count, plot 'bar'

pd.set_option('display.max_columns' , None)
pd.set_option('display.width' , 600)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind = 'bar') # barh, pie, line, area, hist, box etc
plt.show()

df[["sex" , "age" ]].plot(kind = 'bar')
plt.show()

df[df["age"] >= 60]["sex"].value_counts().plot(kind ='bar')
plt.show()