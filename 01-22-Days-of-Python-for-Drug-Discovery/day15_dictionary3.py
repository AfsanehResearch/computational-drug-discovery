drugs = {"Aspirin": {"molecular_weight": 180.16, "solubility": 3.0}, 
         "Ibuprofen":{"molecular_weight": 206.28, "solubility" :21.0}, 
         "Caffeine":{"molecular_weight":194.19, "solubility": 16.0}}
for drug, data in drugs.items():
    if data["molecular_weight"] > 190:
        print(drug)
        print(drug, data["molecular_weight"])
