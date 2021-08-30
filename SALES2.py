#cell1

import pandas as pd
import csv
from pandas import *
import os
import numpy as np

df1 = pd.read_csv('MOVS.csv')
df1 = df1.drop_duplicates()

df1.index=df1['SHP_SHIPMENT_ID']

dfmulti = df1.groupby('SHP_SHIPMENT_ID').agg({'MELI_SKU': 'nunique'}).reset_index()
dfmulti = dfmulti[dfmulti['MELI_SKU']>1]
listamulti = list(dfmulti['SHP_SHIPMENT_ID'])
df1 = df1[df1['SHP_SHIPMENT_ID'].isin(listamulti)]


#cell2

df3 = df1.assign(col=df1.groupby(level=0).MELI_SKU.cumcount()).pivot(columns='col', values='MELI_SKU').reset_index()


#cell3

df1.index=df1['SHP_SHIPMENT_ID']
df3 = df1.assign(col=df1.groupby(level=0).INVENTORY_ID.cumcount()).pivot(columns='col', values='MELI_SKU').reset_index()

#cell4


df1 = df1[['SHP_SHIPMENT_ID','FBM_QUANTITTY','INVENTORY_ID']]

#cell5

df4 = df3[df3.columns.difference(['SHP_SHIPMENT_ID'])]
df4
df4['List'] = df4.values.tolist()
df3['List'] = df4['List']

#cell6

def no_nan(listy):
    return list(pd.Series(listy).dropna())

df3['List2'] = df3['List'].apply(no_nan)

#cell7

df3['List2'] = df3['List2'].apply(lambda x: sorted(set(x)))

#cell 8

df3['List2'] = df3['List2'].apply(lambda x: sorted(set(x)))

#cell9
df3['List2'] = df3['List2'].apply(lambda x: np.sort(np.unique(x)))
df3 = df3[['SHP_SHIPMENT_ID','List2']]


#cell10

def converter(list):
    return (*list, )
  
#cell11

df3['List2'] = df3['List2'].apply(converter)


#cell12

df4 = df3.groupby('List2').count().sort_values(by='SHP_SHIPMENT_ID', ascending=False).reset_index()
    
