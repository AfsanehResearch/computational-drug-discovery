molecular_weight = [188.15, 215.19, 262.14, 203.52,277.33,119.36]
selected =[]
for weight in molecular_weight:
    if weight > 250:
        selected.append(weight)
print(selected)
print(len(selected))
