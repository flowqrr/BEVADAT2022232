from typing import Optional, Tuple

import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix

class KNNClassifier:
    def __init__(self, k: int, test_split_ratio: float):
        self.k = k
        self.test_split_ratio = test_split_ratio
        self.x_train: Optional[pd.DataFrame] = None
        self.y_train: Optional[pd.DataFrame] = None
        self.x_test: Optional[pd.DataFrame] = None
        self.y_test: Optional[pd.DataFrame] = None
        self.y_preds: Optional[pd.DataFrame] = None

    @property
    def k_neighbors(self):
        return self.k

    @staticmethod
    def load_csv(csv_path: str, clean_dataset: bool = False) -> Tuple[pd.DataFrame, pd.DataFrame]:
        dataset = pd.read_csv(csv_path, delimiter=',', header=None)
        dataset = dataset.sample(frac=1, random_state=42).reset_index(drop=True)
        if clean_dataset:
            dataset = dataset.fillna(value=3.5)
            dataset = dataset.replace('""', 3.5)
            dataset = dataset.astype(float)
            mask = (dataset.iloc[:, :4] >= 0) & (dataset.iloc[:, :4] <= 10)
            dataset = dataset[mask.all(axis=1)].reset_index(drop=True)
        x, y = dataset.iloc[:, :4], dataset.iloc[:, -1]
        return x, y

    def train_test_split(self, features: pd.DataFrame, labels: pd.DataFrame):
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert (len(features) == test_size + train_size)
        self.x_train, self.y_train = features.iloc[:train_size, :], labels.iloc[:train_size]
        self.x_test, self.y_test = features.iloc[train_size:train_size + test_size, :], \
            labels.iloc[train_size:train_size + test_size]

    def euclidean(self, element_of_x: pd.Series) -> pd.Series:
        return pd.Series(((self.x_train - element_of_x) ** 2).sum(axis=1) ** 0.5)

    def predict(self, x_test: pd.DataFrame):
        labels_pred = []
        for i in range(len(x_test)):
            distances = self.euclidean(x_test.iloc[i])
            distances = pd.DataFrame({'distance': distances, 'label': self.y_train})
            distances = distances.sort_values(by='distance').reset_index(drop=True)
            label_pred = distances.loc[:self.k-1, 'label'].mode().values[0]
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
        for i in range(1, 21):
            self.k = i
            self.predict(self.x_test)
            accuracies.append((i, self.accuracy()))
        best_k, best_accuracy = max(accuracies, key=lambda x: x[1])
        return best_k, best_accuracy
