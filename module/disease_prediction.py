from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Sample dataset: Replace with actual healthcare data
data = [
    {'symptom1': 1, 'symptom2': 0, 'symptom3': 1, 'disease': 1},
    {'symptom1': 0, 'symptom2': 1, 'symptom3': 0, 'disease': 0},
    # Add more data entries
]

# Convert data to feature matrix X and target vector y
X = [[entry['symptom1'], entry['symptom2'], entry['symptom3']] for entry in data]
y = [entry['disease'] for entry in data]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the model
model = GaussianNB()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Disease Prediction Accuracy: {accuracy * 100:.2f}%')
