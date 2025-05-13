from sklearn.linear_model import LogisticRegression
import numpy as np

class DiseasePredictorModel:
    def __init__(self):
        self.model = LogisticRegression()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)
