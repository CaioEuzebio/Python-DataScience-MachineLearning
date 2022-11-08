import datetime as dt

#Conver Latin date to US Date
df1['Dia'] = df1['Date Created'].str[0:2]
df1['Mes'] = df1['Date Created'].str[3:5]
df1['Ano'] = df1['Date Created'].str[6:10]
df1['Hora'] = df1['Date Created'].str[10:19]

df1['Data_Lost'] = df1['Ano'] + '/' + df1['Mes'] + '/' + df1['Dia'] + ' '+ df1['Hora']
df1['Data_Lost'] = pd.to_datetime(df1['Data_Lost'])


#Get day name
df1['Dia_Semana']= df1['Data_Lost'].dt.day_name()


#Get week nuber 

df1['weeknum'] = df1.Data_Lost.apply(lambda x:x.isocalendar()[1])

#Add days into date

df1['Data_Pago'] = df1['Data_Lost'] + datetime.timedelta(days=31)

#Timedeltas

#Days
df1['time_delta'] = (df1.Data_Pago - df1.Data_Lost)

# create a column with timedelta as total hours, as a float type
df1['tot_hour_diff'] = (df1.Data_Pago - df1.Data_Lost) / pd.Timedelta(hours=1)

# create a colume with timedelta as total minutes, as a float type
df1['tot_mins_diff'] = (df1.Data_Pago - df1.Data_Lost) / pd.Timedelta(minutes=1)


#Dayname

df1['Day_Name'] = df1['Data_Pago'].dt.day_name()


