import numpy as np
from sklearn.svm import LinearSVC


class LinearClassifier:

    def __init__(self):
        self.model = LinearSVC(
            C=1000,
            max_iter=10000,
        )

    def fit(self, point_cloud):

        X = []
        y = []

        for dp in point_cloud.data_points:
            X.append(dp.get_center())
            y.append(dp.label)

        X = np.array(X)
        y = np.array(y)

        self.model.fit(X, y)

        return self

    @property
    def normal(self):
        return self.model.coef_[0]

    @property
    def bias(self):
        return self.model.intercept_[0]