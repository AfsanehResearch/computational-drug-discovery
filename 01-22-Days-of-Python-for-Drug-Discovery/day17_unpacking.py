drugs = {"Aspirin": {"molecular_weight": 180.16,"solubility":3.0}, 
         "Ibuprofen":{"molecular_weight":206.28,"solubility":21.0 }, 
         "Cafeine": {"molecular_weight":194.19,"solubility":16.0}}
def get_properties(drug_name):
    weight = drugs[drug_name]["molecular_weight"]
    solubility = drugs[drug_name]["solubility"]
    return weight, solubility
    
properties = get_properties("Ibuprofen")
print(properties)   
print("=== next step ===")
weight, solubility = get_properties("Ibuprofen")
print(weight)
print(solubility)
print("=== step three ===")
properties = get_properties("Aspirin")
print(properties)
print ("=== step four ===")
weight, solubility = properties
print(weight)
print(solubility)