from sklearn.datasets import fetch_openml
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import SGDClassifier 
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle

mnist = fetch_openml('mnist_784', version=1, as_frame=False)
mnist.keys()

X, y = mnist["data"], mnist["target"]
y = y.astype(np.uint8)

X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]
#by scaling the inputs, it increases overall accuracy
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train.astype(np.float64))
#Train SGD classifier
sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train) 

forest_clf = RandomForestClassifier(random_state=42)
forest_clf.fit(X_train, y_train) 
#forest_clf.predict([some_digit])

with open('sgd_model.pkl', 'wb') as f:
    pickle.dump(sgd_clf, f)

with open('forest_model.pkl', 'wb') as f:
    pickle.dump(forest_clf, f)
   