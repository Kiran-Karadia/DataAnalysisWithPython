import numpy as np

def calculate(list):

    try:
      input = np.reshape(list, (3,3))
    except ValueError:
      raise ValueError("List must contain nine numbers.")

    calculations = {
    'mean': [np.mean(input, 0).tolist(), np.mean(input, 1).tolist(), np.mean(input).tolist()],
    'variance': [np.var(input, 0).tolist(), np.var(input, 1).tolist(), np.var(input).tolist()],
    'standard deviation': [np.std(input, 0).tolist(), np.std(input, 1).tolist(), np.std(input).tolist()],
    'max': [np.max(input, 0).tolist(), np.max(input, 1).tolist(), np.max(input).tolist()],
    'min': [np.min(input, 0).tolist(), np.min(input, 1).tolist(), np.min(input).tolist()],
    'sum': [np.sum(input, 0).tolist(), np.sum(input, 1).tolist(), np.sum(input).tolist()]
}
    return calculations

