import pandas as pd
import pickle
from keras.models import model_from_json
from sklearn.neural_network import MLPClassifier

dataset = pd.read_csv('new_radar_distance_data.csv')

x = dataset.iloc[:, [2, 4]].values # input
  
y = dataset.iloc[:, 5].values # output

#CNN model
model = MLPClassifier(hidden_layer_sizes= (20), 
						random_state=5, 
						activation='relu', 
						batch_size=200, 
						learning_rate_init=0.03) 
model.fit(x, y)


#prediction
predictions = model.predict(x)

# save the classifier
with open('my_dumpedclassifier2.pkl')
    
# load it again

    
#test model
