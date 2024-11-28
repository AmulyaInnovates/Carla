import pandas as pd 
from keras.models import Sequential
from keras.layers import Dense

dataset= pd.read_csv(r'book.csv', error_bad_lines=False)
x=dataset.iloc[:,[4,11]].values
y=dataset.iloc[:,3].values

print('Data of X:-',x)
print('Data of Y :-',y)

model= Sequential()
model.add(Dense(112,input_dim=8 ,activation='relu'))
model.add(Dense(127,activation='relu'))
model.add(Dense(52,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.summary()