import sqlite3
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np

class TreatmentPredictor:
    def __init__(self):
        self.model = LogisticRegression()
        self.label_encoder = LabelEncoder()

    def train_model(self, data):
        X = [item[0] for item in data]  # Symptoms
        y = [item[2] for item in data]  # Effectiveness

        # Encode categorical data
        X = self.label_encoder.fit_transform(X).reshape(-1, 1)
        y = np.array(y)

        # Train the model
        self.model.fit(X, y)

    def predict_treatment(self, symptom):
        encoded_symptom = self.label_encoder.transform([symptom])
        prediction = self.model.predict([encoded_symptom])
        return prediction[0]
