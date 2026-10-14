import numpy as np
data = np.array([[1.2, 180.16],
                    [-0.1, 194.19],
                    [3.5,206.28]])
print(data.shape) 
print(data.ndim)
print(data[0,0])
print(data[1,0])
print(data[2,1])
print(data[:,0])
print(data[1,:])
np.set_printoptions(suppress = True)
print(data[1:,:])