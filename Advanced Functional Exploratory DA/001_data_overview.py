from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

pd.set_option('display.max_columns' , None)
pd.set_option('display.width' , 600)
df = sns.load_dataset("titanic")
df.head()

def check_df(dataFrame, head = 5):
    print('\n#################### SHAPE ####################')
    print(dataFrame.shape)
    print('\n#################### TYPES ####################')
    print(dataFrame.dtypes)
    print('\n#################### HEAD ####################')
    print(dataFrame.head(head))
    print('\n#################### TAIL ####################')
    print(dataFrame.tail(head))
    print('\n#################### NA ####################')
    print(dataFrame.isnull().sum())
    print('\n#################### QUANTILES ####################')
    print(dataFrame.describe([0 , 0.05, 0.50, 0.95, 0.99]).T)

check_df(df)