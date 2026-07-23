# Importing numpy for numerical computations
import numpy as np

def mean_squared_error(y_true, y_pred):
    """
    Calculate the mean squared error between true values and predictions.

    Args:
        y_true (numpy.ndarray): Ground truth values.
        y_pred (numpy.ndarray): Predicted values.

    Returns:
        float: Mean squared error.
    """
    # Check if input arrays have the same shape
    if y_true.shape != y_pred.shape:
        raise ValueError("True values and predictions must have the same shape")

    # Calculate squared differences between true and predicted values
    squared_diffs = (y_true - y_pred) ** 2

    # Calculate mean of squared differences
    mse = np.mean(squared_diffs)

    return mse

def coefficients(y, x):
    """
    Calculate coefficients for linear regression using numpy.

    Args:
        y (numpy.ndarray): Target values.
        x (numpy.ndarray): Feature values.

    Returns:
        tuple: Coefficients (slope, intercept).
    """
    # Check if input arrays have the same shape
    if y.shape != x.shape:
        raise ValueError("Target values and feature values must have the same shape")

    # Calculate coefficients using numpy's polyfit function
    # This function returns coefficients of the polynomial that best fits the data
    # For simple linear regression, we expect a polynomial of degree 1
    coeffs = np.polyfit(x, y, 1)

    return coeffs