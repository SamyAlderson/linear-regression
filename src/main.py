# Import necessary libraries
import numpy as np

# Define a class for the linear regression model
class LinearRegression:
    def __init__(self, learning_rate=0.001, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = 0
        self.bias = 0
        self.cost = []

    def fit(self, X, y):
        # Initialize parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        # Gradient Descent
        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias
            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)
            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            # Store cost
            cost = self.__compute_cost(y, y_predicted)
            self.cost.append(cost)

    def predict(self, X):
        y_approximated = np.dot(X, self.weights) + self.bias
        return y_approximated

    def __compute_cost(self, y, y_predicted):
        # Mean Squared Error
        return np.mean((y - y_predicted) ** 2)

# Load data from utils.py
from utils import load_data

def main():
    # Load dataset
    X, y = load_data()
    # Create and train the model
    model = LinearRegression()
    model.fit(X, y)
    # Make predictions
    predictions = model.predict(X)
    print(predictions)

if __name__ == "__main__":
    main()