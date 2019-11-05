import pandas as pd
import csv
from pandas import *
import os
import numpy as np

df1 = pd.read_csv('lines.csv', encoding='latin-1', low_memory=False)

df1.index=df1['Order No']
df3 = df1.assign(col=df1.groupby(level=0).PartNo.cumcount()).pivot(columns='col', values='PartNo')

df3['ListProds'] = df3.values.tolist()

def no_nan(listy):
    return list(pd.Series(listy).dropna())

df3['ListProds'] = df3['ListProds'].apply(no_nan)

df3['ListProds'] = df3['ListProds'].apply(lambda x: np.sort(np.unique(x)))

df4 = df3[['ListProds']].copy()
df4['QtyPNs'] = df3['QtyProds'] = df3.ListProds.apply(lambda x: len(x))

df4.to_csv('Gerar.csv')
