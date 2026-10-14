drugs = [{"name": "Aspirin", "MW": 180.16, "targets": ["COX-1", "COX-2"]},
          {"name": "Caffeine", "MW":194.19, "targets": ["Adenosine receptor"]},
          {"name": "Ibuprofen", "MW":206.28, "targets": ["COX-1", "COX-2"]}]
for drug in drugs:
    print(drug["name"])

for index, drug in enumerate(drugs, start = 1):
    print(index,drug["name"])
for drug in drugs:
    print(drug["name"], drug["MW"])
print( "=== finished ===")
names = ["Aspirin", "Caffeine", "Ibuprofen"]
logP = [1.2, -0.1, 3.5]
for names, logP in zip(names,logP):
    print(names, logP)
unique_targets = set()
for drug in drugs:
    for target in drug["targets"]:
        unique_targets.add(target)
print(unique_targets)