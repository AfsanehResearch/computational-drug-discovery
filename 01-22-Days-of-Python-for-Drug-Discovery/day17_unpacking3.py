drugs = {"Aspirin": {"molecular_weight": 180.16,"solubility":3.0}, 
         "Ibuprofen":{"molecular_weight":206.28,"solubility":21.0 }, 
         "Cafeine": {"molecular_weight":194.19,"solubility":16.0}}
def get_drug_info(drug_name):
    weight = drugs[drug_name]["molecular_weight"]
    solubility = drugs[drug_name]["solubility"]
    name = drug_name
    return name, weight, solubility

name, weight, solubility = get_drug_info("Aspirin")

print(name)
print(weight)
print(solubility)
data = ("Aspirin", 180.16, 3.0, 1.2, 49.3)
name, *properties = data
print(name)
print(properties)

print(" === practice ===")
aspirin_data = ("Aspirin", 180.16,3.0,1.2,63.6)
name,*descriptors = aspirin_data
print(name)
print(descriptors)
molecular_weight = descriptors[0]
solubility = descriptors[1]
print(molecular_weight, solubility)
