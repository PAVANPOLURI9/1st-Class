import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample data: replace with your actual data
data = {
    'Temperature': [30, 25, 27, 28, 22, 24, 26, 29, 31, 23],
    'Humidity': [70, 65, 75, 80, 60, 68, 72, 78, 85, 62],
    'Rainfall': [100, 80, 90, 110, 70, 85, 95, 105, 120, 75]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Features and target variable
X = df[['Temperature', 'Humidity']]
y = df['Rainfall']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Example prediction
example_data = np.array([[28, 75]])
predicted_rainfall = model.predict(example_data)
print(f'Predicted Rainfall: {predicted_rainfall[0]}')