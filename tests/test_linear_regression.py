# tests/test_linear_regression.py

import unittest
from src.main import LinearRegression
from src.utils import load_dataset
import numpy as np

class TestLinearRegression(unittest.TestCase):

    def test_linear_regression(self):
        # Load the dataset
        X, y = load_dataset()

        # Create a linear regression model
        model = LinearRegression()

        # Train the model
        model.fit(X, y)

        # Make predictions
        y_pred = model.predict(X)

        # Calculate mean squared error
        mse = model.mse(y, y_pred)

        # Check that the mean squared error is reasonable
        self.assertLess(mse, 10)

    def test_coefficient_calculation(self):
        # Create a linear regression model
        model = LinearRegression()

        # Check that the coefficients are correctly calculated
        coefficients = model.coefficients
        self.assertIsInstance(coefficients, np.ndarray)
        self.assertEqual(coefficients.shape, (2,))

    def test_mean_squared_error_calculation(self):
        # Create a linear regression model
        model = LinearRegression()

        # Check that the mean squared error is correctly calculated
        y_pred = np.array([1, 2, 3])
        y = np.array([2, 3, 5])
        mse = model.mse(y, y_pred)
        self.assertEqual(mse, 2.6666666666666665)

if __name__ == "__main__":
    unittest.main()