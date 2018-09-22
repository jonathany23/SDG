import numpy as np
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras import optimizers

def rnn_lstm(layers, params):
	"""Build RNN (LSTM) model on top of Keras and Tensorflow"""

	model = Sequential()
	model.add(LSTM(input_shape=(layers[1], layers[0]), units=64, return_sequences=True))
	model.add(Dropout(params['dropout_keep_prob']))
	model.add(LSTM(layers[2], return_sequences=False))
	model.add(Dropout(params['dropout_keep_prob']))
	model.add(Dense(units=layers[3]))
	model.add(Activation("tanh"))

	rmsOpt = optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0)

	model.compile(loss="mean_squared_error", optimizer=rmsOpt, metrics=['accuracy'])
	
	return model

def predict_next_timestamp(model, history):
	"""Predict the next time stamp given a sequence of history data"""

	prediction = model.predict(history)
	prediction = np.reshape(prediction, (prediction.size,))
	return prediction 

