from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Sample dataset: Replace with actual transaction data
data = [
    {'amount': 100, 'location': 'NY', 'fraud': 0},
    {'amount': 2000, 'location': 'LA', 'fraud': 1},
    # Add more data entries
]

# Convert data to feature matrix X and target vector y
X = [[entry['amount'], entry['location']] for entry in data]
y = [entry['fraud'] for entry in data]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))
