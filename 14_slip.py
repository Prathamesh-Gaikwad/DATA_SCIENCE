import numpy as np

arr = np.array([1, 2, 3, 4])
weight = np.array([0.1, 0.2, 0.2, 0.3])

print("Weighted Average : ", np.average(arr, weights = weight))
