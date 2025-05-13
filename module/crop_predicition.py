from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

# Sample dataset: Replace with actual crop data
data = [
    {'temperature': 25, 'rainfall': 100, 'yield': 200},
    {'temperature': 30, 'rainfall': 150, 'yield': 250},
    # Add more data entries
]

# Convert data to feature matrix X and target vector y
X = [[entry['temperature'], entry['rainfall']] for entry in data]
y = [entry['yield'] for entry in data]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the model
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae:.2f}')
