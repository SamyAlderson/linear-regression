# Linear Regression
## Simple linear regression model in Python

Linear Regression is a simple tool for implementing and testing linear regression models in Python. It includes a basic model, coefficient calculation, and mean squared error calculation.

## Install

To use Linear Regression, simply clone this repository and install the required dependencies with pip:
```bash
git clone https://github.com/your-username/linear-regression.git
cd linear-regression
pip install numpy
```

## Usage

You can use the linear regression model like this:
```python
from linear_regression import LinearRegression

# create a sample dataset
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# create a linear regression model
model = LinearRegression(x, y)

# calculate the coefficients
coefficients = model.coefficients()
print(coefficients)

# calculate the mean squared error
mse = model.mean_squared_error()
print(mse)
```

## Build from Source

To build from source, simply clone this repository and run:
```bash
git clone https://github.com/your-username/linear-regression.git
cd linear-regression
python setup.py build_ext --inplace
```

## Project Structure

* `linear_regression.py`: the main module containing the linear regression model
* `test_linear_regression.py`: the test suite for the linear regression model
* `setup.py`: setup script for building from source

## License

Copyright (c) 2026 SamyAlderson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.