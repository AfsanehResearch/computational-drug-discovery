import numpy as np
data = np.array([[1.2,180.16],
                  [-0.1,194.19],
                  [3.5,206.28]])
data[0,1] = 2.0
print(data)
np.set_printoptions(suppress = True)
print(data)
