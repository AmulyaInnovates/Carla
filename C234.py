import pandas as pd
import pickle
from keras.models import model_from_json
from sklearn.neural_network import MLPClassifier
import tensorflow as tf

data= pd.read_csv('new_radar_data.csv')

x= data.iloc[: , [2,4]].values
y= data.iloc[: , 5].values

model= MLPClassifier(hidden_layer_sizes=20,activation='relu',learning_rate_init=0.03,random_state=5 , batch_size=200)

model.fit(x,y)

prediction =model.predict(x)

file= open('model.pkl' , 'wb')
pickle.dump(model , file)

saved_new_file= open('model.pkl' , 'rb')
saved_file= pickle.load(saved_new_file)

car_data = {
	'throttle': [0.337492082] ,
	'distance': [0.509472993]
}

data= pd.DataFrame(car_data ,columns=['throttle','distance'])
prediction =saved_file.predict(data)
print('The prediction Made By the Computer :- ' , prediction)