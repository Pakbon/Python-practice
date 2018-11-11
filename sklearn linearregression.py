from sklearn.linear_model import LinearRegression
from sklearn.datasets.samples_generator import make_blobs
import numpy as np

X, y = make_blobs(n_samples=300, centers=2, n_features=5, random_state=2)

X_train = X[:-30]
y_train = y[:-30]
X_test = X[-30:]
y_test = y[-30:]

model = LinearRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
