import numpy as np
from sklearn import datasets
from sklearn import linear_model

def diabetes(): #regression
    diabetes = datasets.load_diabetes()
    np.random.seed(2)
    indices = np.random.permutation(len(diabetes.data))
    diabetes_X_train = diabetes.data[:-20]
    diabetes_X_test  = diabetes.data[-20:]
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test  = diabetes.target[-20:]
    print(type(diabetes.data))
    regression = linear_model.LinearRegression()
    regression.fit(diabetes_X_train, diabetes_y_train)
    print(regression.score(diabetes_X_test, diabetes_y_test))
    print(regression.predict(diabetes_X_test))

diabetes()

