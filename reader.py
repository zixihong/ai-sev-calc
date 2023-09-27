import numpy as np
import pandas as pd
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load data from CSV files
X_data = pd.read_csv('x_data.csv')  # Assuming X_data.csv contains 'Weight,' 'Age,' 'Virion Count,' and 'Gender'
Y_data_variance = pd.read_csv('y_data_variance.csv')  # Assuming Y_data_variance.csv contains 'Severity' with variance
Y_data_precise = pd.read_csv('y_data_precise.csv')  # Assuming Y_data_precise.csv contains 'Severity' without variance

# Convert Y_data_variance to a 1D array
Y_data_variance = Y_data_variance.values.ravel()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_data, Y_data_variance, test_size=0.2, random_state=42)

# Create and train the Bayesian Ridge Regression model
model = BayesianRidge()
"""
    alpha_1=2.0,       # Alpha 1 is bigger than 1
    alpha_2=0.01,      # Alpha 2 is a small scale
    lambda_1=0.001,    # Lambda 1 is smaller
    lambda_2=0.01,     # Lambda 2 is a small scale
    alpha_init=None,   # Alpha init is set to None
    lambda_init=None   # Lambda init is set to None
    """
model.fit(X_train, y_train)


# Define parameter values for prediction
virioncount = 5185092289  # Replace with the actual virioncount value
weight = 15.511799661471816         # Replace with the actual weight value
age = 18            # Replace with the actual age value
gender = 0       # Replace with the actual gender value

# Create a new data point for prediction with the same order of features as during training
new_data_point = pd.DataFrame({'Age': [age], 'Weight': [weight], 'Virion Count': [virioncount], 'Gender': [gender]})

# Make predictions for the new data point
predicted_severity = model.predict(new_data_point)

# Print the predicted severity
print("Predicted Severity:", predicted_severity[0])

# Test the model on the test dataset
y_pred = model.predict(X_test)

# Print evaluation metrics for the model's performance on the test data with variance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE) on Test Data with Variance:", mse)
print("R-squared (R2) on Test Data with Variance:", r2)

# Compare the model's predictions (with variance) to the precise data (without variance)
precise_target = Y_data_precise['Severity'].values
precise_predictions = model.predict(X_data)

# Calculate evaluation metrics for the model's performance on the precise data
precise_mse = mean_squared_error(precise_target, precise_predictions)
precise_r2 = r2_score(precise_target, precise_predictions)

print("Mean Squared Error (MSE) on Precise Data without Variance:", precise_mse)
print("R-squared (R2) on Precise Data without Variance:", precise_r2)


