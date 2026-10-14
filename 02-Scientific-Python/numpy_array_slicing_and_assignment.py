import numpy as np
numbers = np.array([10,20,30,40,50])
numbers[1:4] = 0
print(numbers)

data = np.array([[1.2, 180.16], [-0.1, 194.19], [3.5, 206.28]])
data[1, 0] = 200
print(data)