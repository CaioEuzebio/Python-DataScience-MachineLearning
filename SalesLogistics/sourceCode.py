import pandas as pd
import csv
from pandas import *
import os
import numpy as np

df1 = pd.read_csv('Sales.csv')

df1.index=df1['Ordem']
df3 = df1.assign(col=df1.groupby(level=0).Produto.cumcount()).pivot(columns='col', values='Produto')
