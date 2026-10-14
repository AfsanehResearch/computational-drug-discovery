import numpy as np
data = np.array([[1.2,180],
                 [-0.1, 194],
                 [3.5,206]])
print(data.shape)
print(data.sum())
print(data.sum(axis = 0))
print(data.sum(axis = 1))
print(data.mean(axis = 0))
print(data.mean(axis = 1))
print(data.max(axis = 0))
print(data.min(axis = 1))