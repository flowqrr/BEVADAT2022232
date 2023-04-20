import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas.core.frame
import sklearn.utils
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error

'''
1.
Készíts egy függvényt, betölti majd vissza adja az iris adathalmazt.


Egy példa a kimenetre: iris
return type: sklearn.utils.Bunch
függvény neve: load_iris_data
'''


def load_iris_data() -> sklearn.utils.Bunch:
    iris_data = load_iris()
    return iris_data


# print(load_iris_data())


'''
2.
Készíts egy függvényt, ami a betölti az virágokhoz tartozó levél méretket egy dataframebe, majd az első 5 sort visszaadja.
Minden oszlop tartalmazza, hogy az milyen mérethez tartozik.

Egy példa a bemenetre: iris
Egy példa a kimenetre: iris_df
return type: pandas.core.frame.DataFrame
függvény neve: check_data
'''


def check_data(iris: sklearn.utils.Bunch) -> pandas.core.frame.DataFrame:
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    return iris_df.head()


# print(check_data(load_iris_data()))

'''
3.
Készíts egy függvényt ami előkészíti az adatokat egy lineaáris regressziós model feltanításához.
Featurejeink legyenek a levél méretek kivéve a "sepal length (cm)", ez legyen a targetünk.

Egy példa a bemenetre: iris
Egy példa a kimenetre: X, y
return type: (numpy.ndarray, numpy.ndarray)
függvény neve: linear_train_data
'''


def linear_train_data(iris: sklearn.utils.Bunch) -> (np.ndarray, np.ndarray):
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    X = iris_df.drop(['sepal length (cm)'], axis=1).values
    y = iris_df['sepal length (cm)'].values
    return X, y


# print(linear_train_data(load_iris_data()))


'''
4.
Készíts egy függvényt ami előkészíti az adatokat egy logisztikus regressziós model feltanításához.
Featurejeink legyenek a levél méretek, targetünk pedig a 0, 1-es virág osztályok.
Fontos csak azokkal az adatokkal tanítsunk amihez tartozik adott target. 

Egy példa a bemenetre: iris
Egy példa a kimenetre: X, y
return type: (numpy.ndarray, numpy.ndarray)
függvény neve: logistic_train_data
'''


def logistic_train_data(iris: sklearn.utils.Bunch) -> (np.ndarray, np.ndarray):
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['target'] = iris.target

    X = iris_df.drop(['target'], axis=1).values
    y = iris_df['target'].values

    X = X[y != 2]
    y = y[y != 2]

    return X, y


# print(logistic_train_data(load_iris_data()))


'''
5.
Készíts egy függvényt ami feldarabolja az adatainkat train és test részre. Az adatok 20%-át használjuk fel a teszteléshez.
Tegyük determenisztikussá a darabolást, ennek értéke legyen 42.

Egy példa a bemenetre: X, y
Egy példa a kimenetre: X_train, X_test, y_train, y_test
return type: (numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray)
függvény neve: split_data
'''


def split_data(X, y) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


# X, y = logistic_train_data(load_iris_data())
# X_train, X_test, y_train, y_test = split_data(X, y)
# print(f"X_train: {X_train}\nX_test: {X_test}\ny_train: {y_train}\ny_test: {y_test}\n")

'''
6.
Készíts egy függvényt ami feltanít egy lineaáris regressziós modelt, majd visszatér vele.

Egy példa a bemenetre: X_train, y_train
Egy példa a kimenetre: model
return type: sklearn.linear_model._base.LinearRegression
függvény neve: train_linear_regression
'''


def train_linear_regression(X_train, y_train):  # -> sklearn.linear_model._base.LinearRegression:
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


# linear_regression = train_linear_regression(X_train, y_train)

'''
7.
Készíts egy függvényt ami feltanít egy logisztikus regressziós modelt, majd visszatér vele.

Egy példa a bemenetre: X_train, y_train
Egy példa a kimenetre: model
return type: sklearn.linear_model._base.LogisticRegression
függvény neve: train_logistic_regression
'''


def train_logistic_regression(X_train, y_train):  # -> sklearn.linear_model._base.LogisticRegression:
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model


# logistic_regression = train_logistic_regression(X_train, y_train)

'''
8.
Készíts egy függvényt, ami a feltanított modellel predikciót tud végre hajtani.

Egy példa a bemenetre: model, X_test
Egy példa a kimenetre: y_pred
return type: numpy.ndarray
függvény neve: predict
'''


def predict(model, X_test) -> np.ndarray:
    y_pred = model.predict(X_test)
    return y_pred


# linear_y_pred = predict(linear_regression, X_test)
# logistic_y_pred = predict(logistic_regression, X_test)
#
# print(f"linear regression prediction: {linear_y_pred}")
# print(f"logistic regression prediction: {logistic_y_pred}")

'''
9.
Készíts egy függvényt, ami vizualizálni tudja a label és a predikciók közötti eltérést.
Használj scatter plotot a diagram elkészítéséhez.

Diagram címe legyen: 'Actual vs Predicted Target Values'
Az x tengely címe legyen: 'Actual'
Az y tengely címe legyen: 'Predicted'

Egy példa a bemenetre: y_test, y_pred
Egy példa a kimenetre: scatter plot
return type: matplotlib.figure.Figure
függvény neve: plot_actual_vs_predicted
'''


def plot_actual_vs_predicted(y_test, y_pred):  # -> plt.figure.Figure:
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.set_xlabel('Actual')
    ax.set_ylabel('Predicted')
    ax.set_title('Actual vs Predicted Target Values')
    return fig


# linear_pred_plot = plot_actual_vs_predicted(y_test, linear_y_pred)
# logistic_pred_plot = plot_actual_vs_predicted(y_test, logistic_y_pred)
# plt.show()

'''
10.
Készíts egy függvényt, ami a Négyzetes hiba (MSE) értékét számolja ki a predikciók és a valós értékek között.

Egy példa a bemenetre: y_test, y_pred
Egy példa a kimenetre: mse
return type: float
függvény neve: evaluate_model
'''


def evaluate_model(y_test, y_pred):  # -> float:
    return np.mean((y_pred - y_test) ** 2)


# print(evaluate_model(y_test, linear_y_pred))
# print(evaluate_model(y_test, logistic_y_pred))
