import numpy as np
data = np.array([[ 10, 20, 30],
                 [ 40, 50, 60]])
result = data +10
print(result)
print(" ===finished ===")
# جمع بندی
MW = np.array([180.16, 194.19, 206.28, 150.12, 250.30])
print("shape:" , MW.shape)
print("Mean:" , MW.mean())
print("Maximum:" , MW.max())
heavy = MW[MW > 200]
print("Heavy molecules", heavy)
light = MW[MW <= 200]
print(light)
new = MW[(MW < 210) & (MW > 180)]
print(new)