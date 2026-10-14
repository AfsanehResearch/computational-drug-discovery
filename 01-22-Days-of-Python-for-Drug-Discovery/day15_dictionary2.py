drugs =  {"Aspirin": 180.16, "Ibuprofen": 206.28, "Caffein": 194.19}
print(drugs)
print("=== finished ====")

for drug in drugs:
    print(drug)
print(" === finished === ")
for weight in drugs.values():
    print(weight)
print ("=== finished ===")
for drug, weight in drugs.items():
    print(drug, weight)
print("=== finished=== ") 