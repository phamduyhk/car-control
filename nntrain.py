
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier
from keras.layers import Dense
from keras.models import Sequential
import pandas
import glob
from scipy import stats
# multi-class classification with Keras
# load dataset
from keras.datasets.mnist import load_data
# load the data - it returns 2 tuples of digits & labels - one for
# the train set & the other for the test set
(train_digits, train_labels), (test_digits, test_labels) = load_data()

train_digits = train_digits.reshape(train_digits.shape[0],train_digits.shape[1]*train_digits.shape[2])
test_digits = test_digits.reshape(test_digits.shape[0],test_digits.shape[1]*test_digits.shape[2])
print(train_digits.shape)
print(test_digits.shape)
print(stats.describe(train_labels))
# define baseline model
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(128, input_dim=train_digits.shape[1], activation='relu'))
	model.add(Dense(10, activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy',
	              optimizer='adam', metrics=['accuracy'])
	return model

estimator = KerasClassifier(
	build_fn=baseline_model, epochs=10, batch_size=5, verbose=1)
kfold = KFold(n_splits=3, shuffle=True)
results = cross_val_score(estimator, train_digits,train_labels, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
