import pandas as pd
import csv
from pandas import *
import numpy as np

df1 = pd.read_csv('SALES.csv')
df1 = df1.drop_duplicates()


dfmulti = df1.groupby('ORDER').agg({'SKU': 'nunique'}).reset_index()
dfmulti = dfmulti[dfmulti['SKU']>1]
listamulti = list(dfmulti['ORDER'])
df1 = df1[df1['ORDER'].isin(listamulti)]

df1.index=df1['ORDER']
df3 = df1.assign(col=df1.groupby(level=0).SKU.cumcount()).pivot(columns='col', values='SKU').reset_index()

df4 = df3[df3.columns.difference(['ORDER'])]
df4
df4['List'] = df4.values.tolist()
df3['List'] = df4['List']

def no_nan(listy):
    return list(pd.Series(listy).dropna())

df3['List2'] = df3['List'].apply(no_nan)

df3['List2'] = df3['List2'].apply(lambda x: sorted(set(x)))

df3['List2'] = df3['List2'].apply(lambda x: np.sort(np.unique(x)))
df3 = df3[['ORDER','List2']]


def converter(list):
    return (*list, )

df3['List2'] = df3['List2'].apply(converter)

df5 = df3.groupby('List2').count().sort_values(by='ORDER', ascending=False).reset_index()

df5.head()
