import pandas as pd
import csv
from pandas import *
import os
import numpy as np

df1 = pd.read_csv('lines.csv', encoding='latin-1', low_memory=False)

df6 = pd.read_csv('lines.csv', encoding='latin-1', low_memory=False)

df15 = df6.groupby(['Order No']).last()
df16 = df6.groupby(['Order No']).sum()


df1.index=df1['Order No']

df3 = df1.assign(col=df1.groupby(level=0).PartNo.cumcount()).pivot(columns='col', values='PartNo')

df3['ListProds'] = df3.values.tolist()

def no_nan(listy):
    return list(pd.Series(listy).dropna())

df3['ListProds'] = df3['ListProds'].apply(no_nan)

df3['ListProds'] = df3['ListProds'].apply(lambda x: np.sort(np.unique(x)))

df4 = df3[['ListProds']].copy()
df4['QtyPNs'] = df3['QtyProds'] = df3.ListProds.apply(lambda x: len(x))

df4.reset_index(inplace=True)
df15.reset_index(inplace=True)
df16.reset_index(inplace=True)

df67 = pd.merge(df4, df15[['Order No','PGI`d']], on='Order No', how='right')
df67 = pd.merge(df67, df15[['Order No','Order Type']], on='Order No', how='right')
df67 = pd.merge(df67, df15[['Order No','Cut Off Date']], on='Order No', how='right')
df67 = pd.merge(df67, df16[['Order No','Qty']], on='Order No', how='right')
df67 = pd.merge(df67, df15[['Order No','transport mode']], on='Order No', how='right')
df67 = pd.merge(df67, df15[['Order No','Carrier']], on='Order No', how='right')
df67 = pd.merge(df67, df15[['Order No','Carrier Sort']], on='Order No', how='right')
df67 = pd.merge(df67, df15[['Order No','Type Desc']], on='Order No', how='right')

df71 = df6[['Order No','PickNO']]
#df71.reset_index(inplace=True)
df72 = df71.groupby(['Order No']).last()
df72.reset_index(inplace=True)

df67 = pd.merge(df67, df72[['Order No','PickNO']], on='Order No', how='right')

df67.to_csv('Gerar DNs.csv', index=False)
