import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample dataset: Replace with actual student data
data = {
    'study_time': [10, 15, 20, 25, 30],
    'attendance': [80, 85, 90, 95, 100],
    'marks': [60, 65, 70, 75, 80]
}

df = pd.DataFrame(data)

# Define features and target
X = df[['study_time', 'attendance']]
y = df['marks']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
