import pandas as pd 
data= pd.read_csv('student_promoted.csv')

data.loc[data['Attendence']>75 , 'Student_Promoted'] = 'Promoted'
data.loc[data['Attendence']<75 , 'Student_Promoted'] = 'Not Promoted'

print(data)