numbers = [10, 20, 30, 40, 50]
result = []
for number in numbers: 
    result.append(number*2)
print(result)
print("===new way by numpy ===")

import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
print(numbers +10)
print(numbers*2)
print(number / 10)
print(numbers /10)
result = numbers *2 
print(result)