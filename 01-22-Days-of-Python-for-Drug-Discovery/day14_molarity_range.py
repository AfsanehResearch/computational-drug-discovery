masses = [2.0, 5.0, 10.0]
volumes = [0.5, 1.0, 2.0]
molecular_weight = 100.0
molarities = []
for i in range(3):
    molarity = masses[i] / (molecular_weight * volumes[i])
molarities.append(molarity)

print(molarities)