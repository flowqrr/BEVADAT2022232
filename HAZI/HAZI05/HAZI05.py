import pandas as pd
from typing import Tuple
import seaborn as sns
from sklearn.metrics import confusion_matrix

class KNNClassifier:
    def __init__(self, k: int, test_split_ratio: float):
        self.k = k
        self.test_split_ratio = test_split_ratio
        self.x_train: pd.DataFrame = None
        self.y_train: pd.DataFrame = None
        self.x_test: pd.DataFrame = None
        self.y_test: pd.DataFrame = None
        self.y_preds: pd.DataFrame = None

    @property
    def k_neighbors(self):
        return self.k

    @staticmethod
    def load_csv(csv_path: str) -> Tuple[pd.DataFrame, pd.Series]:
        pd.random.seed(42)
        dataset = pd.read_csv(csv_path, delimiter=',', header=None)
        dataset = dataset.sample(frac=1).reset_index(drop=True)
        x, y = dataset.iloc[:, :4], dataset.iloc[:, -1]
        return x, y

    def train_set_split(self, features: pd.DataFrame, labels: pd.Series):
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        self.x_train, self.y_train = features.iloc[:train_size, :], labels.iloc[:train_size]
        self.x_test, self.y_test = features.iloc[train_size:train_size + test_size, :],\
            labels.iloc[train_size:train_size + test_size]

    def euclidean(self, element_of_x: pd.Series) -> pd.Series:
        return pd.Series(((self.x_train - element_of_x) ** 2).sum(axis=1) ** 0.5)

    def predict(self, x_test: pd.DataFrame):
        labels_pred = []
        for i in range(len(x_test)):
            distances = self.euclidean(x_test.iloc[i])
            distances = pd.DataFrame({'distance': distances, 'label': self.y_train})
            distances = distances.sort_values(by='distance').reset_index(drop=True)
            label_pred = distances.loc[:self.k - 1, 'label'].mode().values[0]
            labels_pred.append(label_pred)
        self.y_preds = pd.Series(labels_pred, dtype='int32').values

    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100

    def confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test, self.y_preds)
        sns.heatmap(conf_matrix, annot=True)

    def best_k(self) -> Tuple[int, float]:
        accuracies = []
        for i in range(20):
            KNNClassifier(i, self.test_split_ratio)
            accuracies.append((i, round(KNNClassifier.accuracy(self), 2)))
        return max(accuracies)



