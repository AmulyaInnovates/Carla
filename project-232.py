from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

dataset= loadtxt('pokemon.csv' , delimiter=',')
x= data[: , 0:8]
y=data[:,8]
print('Data of X:-',x)
print('Data of Y :-',y)

model= Sequential()
model.add(Dense(12,input_dim=8 ,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))


model.compile(loss='binary_crossentropy' , metrics=['accuracy']) 
model.fit(x,y,epoch=250,batch_size=100)
predictions= model.predict_classes(x)

for i in range(785,800):
	print(f'{x[i].tolist()} => {predictions[i]} expected {y[i]}')
model.summary()