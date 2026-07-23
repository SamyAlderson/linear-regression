import numpy as np

def load_data(file_path):
    try:
        data = np.loadtxt(file_path)
        return data
    except FileNotFoundError:
        print(f'File {file_path} not found')
        return None

def save_data(data, file_path):
    np.savetxt(file_path, data)