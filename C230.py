from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

data= loadtxt('diabetes_dataset.csv' , delimiter=',')
x= data[: , 0:8]
y=data[:,8]
print('Data of X:-',x)
print('Data of Y :-',y)