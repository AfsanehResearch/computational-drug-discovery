weights = [180.16, 206.28, 151.16,342.30,194.19]
high_weights = []
for weight in weights:
    if weight >200:
        high_weights.append(weight)
print(high_weights)