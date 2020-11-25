df1a = df1.groupby('Warehouse_Id').agg({'Stock': 'sum', 'SKU': 'nunique'})
