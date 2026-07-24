# Linear Regression
A minimal linear regression implementation in Python.

## What it does
This is a simple single-purpose tool that performs ordinary least squares linear regression on a given dataset. It's designed to be easy to use and understand.

## Install
To install, run:
```bash
pip install linear-regression
```
Or, to use it without installing:
```bash
python -m linear_regression
```

## Usage
```bash
linear_regression -h
```
To run the example usage:
```bash
linear_regression example.csv
```
Replace `example.csv` with the path to your dataset.

## Build from Source
Clone the repository:
```bash
git clone https://github.com/SamyAlderson/linear-regression.git
```
Navigate to the project directory:
```bash
cd linear-regression
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the tool using Python:
```bash
python -m linear_regression
```

## Project Structure
- `linear_regression.py`: The main tool implementation.
- `test_linear_regression.py`: A test suite for the tool.
- `requirements.txt`: A list of dependencies required to build and run the tool.

## License
Copyright (c) 2026 SamyAlderson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.