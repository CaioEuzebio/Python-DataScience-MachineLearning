for k, v in df1.groupby('Status WMS'):
    v.to_excel(f'{k}.xlsx')