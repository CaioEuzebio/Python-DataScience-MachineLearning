df['diff_days'] = df['End_date'] - df['Start_date']
df['diff_days']=df['diff_days']/np.timedelta64(1,'D')
 
print(df)
