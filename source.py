"""
Favor não alterar as estruturas e de controle e estruturas de dados sem ter absoluta certeza do que está fazendo. Sempre faça um backup do core original.

"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import numpy as np

df1 = pd.read_csv('lines.csv', encoding='latin-1', low_memory=False)
df1.rename(columns={"Order Type": "OrderType"}, inplace=True)

df1.loc[(df1.Processed != '?'), 'OrderTypeProcessed'] = df1['Qty']
df1.loc[(df1.Processed == '?'), 'OrderTypeProcessed'] = 0

df2 = df1.groupby('OrderType').sum()
df3 = df1.groupby(' Packout station Number').sum()
df4 = df1.groupby('Packout station Operator').sum()
df5 = df1.groupby('Product Category').sum()
df1.rename(columns={df1.columns[12]:'Received Time'}, inplace=True)
df6 = df1.groupby('Received Time').sum()
df7 = df1.groupby('Cut Off Time').sum()




df2.reset_index(inplace=True)
df3.reset_index(inplace=True)
df4.reset_index(inplace=True)
df5.reset_index(inplace=True)
df6.reset_index(inplace=True)
df7.reset_index(inplace=True)

df5['Product Category'] = df5['Product Category'].str.upper()

app = dash.Dash()
app.layout = html.Div([
    html.H1(children = "Dashboard Para Gestão De Produção - Caio",
    style = {'textAlign' : 'center',}),
        html.Div(children = "_______________________________",
                 style = {'textAlign' : 'center',}),
        
    dcc.Graph(
        id = 'lines-chart',
        figure = {
            'data' : [
        {'x': df2['OrderType'], 'y': df2['Qty'],                'type': 'bar', 'name': 'Dropado'},
        {'x': df2['OrderType'], 'y': df2['OrderTypeProcessed'], 'type': 'bar', 'name': 'Realizado'}
        
            
            ],
            'layout' : {
                'title': 'Grafico'
            }
        }
    ),
    
    dcc.Graph(
        id = 'linehart',
        figure = {
            'data' : [
        {'x': df3[' Packout station Number'], 'y': df3['OrderTypeProcessed'], 'type': 'bar', 'name': 'Unidades / Hora'},
        #{'x': ['DCO13','DCO14','DCO15'], 'y': [37,78,43], 'type': 'line', 'name': 'DNs / Hora'}
        
            ],
            'layout' : {
                'title': 'Qty Processada Por Estação'
            }
        }
    ),
    
        dcc.Graph(
        id = 'linehaaaaart',
        figure = {
            'data' : [
        {'x': df4['Packout station Operator'], 'y': df4['OrderTypeProcessed'], 'type': 'bar', 'name': 'Unidades / Hora'},
        #{'x': ['DCO13','DCO14','DCO15'], 'y': [37,78,43], 'type': 'line', 'name': 'DNs / Hora'}
        
            ],
            'layout' : {
                'title': 'Qty Processada Por Operador'
            }
        }
    ),
    
    dcc.Graph(
        id = 'linehaaaaartz',
        figure = {
            'data' : [
        {'x': df5['Product Category'], 'y': df5['Qty'], 'type': 'bar', 'name': 'Dropado'},
        {'x': df5['Product Category'], 'y': df5['OrderTypeProcessed'],'type': 'bar', 'name': 'Realizado'}
        
            ],
            'layout' : {
                'title': 'Unidades Por Categoria'
            }
        }
    ),
    
    dcc.Graph(
        id = 'dropchart',
        figure = {
            'data' : [
        {'x': df6['Received Time'], 'y': df6['Qty'], 'type': 'line', 'name': 'Dropado'},
        {'x': df6['Received Time'], 'y': df6['OrderTypeProcessed'],'type': 'line', 'name': 'Realizado'}
        
            ],
            'layout' : {
                'title': 'Drops'
            }
        }
    ),
    
    dcc.Graph(
        id = 'cutofpogress',
        figure = {
            'data' : [
        {'x': df7['Cut Off Time'], 'y': df7['Qty'], 'type': 'bar', 'name': 'Dropado'},
        {'x': df7['Cut Off Time'], 'y': df7['OrderTypeProcessed'],'type': 'bar', 'name': 'Realizado'}
        
            ],
            'layout' : {
                'title': 'CutOff Progress'
            }
        }
    )
    
])


if __name__ == '__main__':
    app.run_server(port =4050)
