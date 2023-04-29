import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
from sklearn import metrics
sns.set()
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode


class KMeansOnDigits:
    def __init__(self, n_clusters, random_state):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.digits = None
        self.clusters = None
        self.labels = None
        self.accuracy = None
        self.mat = None

    def load_dataset(self):
        self.digits = datasets.load_digits()

    def predict(self):
        model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        self.clusters = model.fit_predict(self.digits.data)

    def get_labels(self):
        result = np.zeros(len(self.clusters))
        for i in range(10):
            mask = (self.clusters == i)
            subarray = self.digits.target[mask]
            label = mode(subarray)[0][0]
            result[mask] = label
        self.labels = result

    def calc_accuracy(self):
        self.accuracy = round(accuracy_score(self.digits.target, self.labels), 2)

    def confusion_matrix(self):
        self.mat = metrics.confusion_matrix(self.digits.target, self.labels)


# kmeans = KMeansOnDigits(n_clusters=10, random_state=0)
# kmeans.load_dataset()
# kmeans.predict()
# kmeans.get_labels()
# kmeans.calc_accuracy()
# kmeans.confusion_matrix()
#
# print(f'accuracy: {kmeans.accuracy}')
#
# ax = sns.heatmap(kmeans.mat, annot=True, cmap='Blues')
# plt.xlabel('Predicted labels')
# plt.ylabel('True labels')
# plt.show()