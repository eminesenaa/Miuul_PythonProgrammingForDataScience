from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# Numeric variable: hist, boxplot

pd.set_option('display.max_columns' , None)
pd.set_option('display.width' , 600)
df = sns.load_dataset("titanic")
df.head()


plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()
