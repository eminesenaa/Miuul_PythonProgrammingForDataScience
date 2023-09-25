import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


df = sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x  = df["sex"], data = df)
df["sex"].value_counts().plot(kind = 'bar')
plt.show()


sns.boxplot(x = df["total_bill"])
plt.show()


df = sns.load_dataset("tips")
sns.scatterplot(x=df["tip"], y=df["total_bill"], hue=df["smoker"], data=df)
plt.show()