import pandas as pd 
data= pd.read_csv('radar_data.csv')

data.loc[data['distance']<=17 , 'Action'] ='1'
data.loc[data['distance']>17 , 'Action'] ='2'
data.loc[data['steer']<0 , 'Action'] ='0'

data.to_csv('new_radar_data.csv' , index=False)

print(data)