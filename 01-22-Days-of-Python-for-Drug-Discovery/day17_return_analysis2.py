drugs = {"Aspirin": {"molecular_weight": 180.16,"solubility":3.0}, 
         "Ibuprofen":{"molecular_weight":206.28,"solubility":21.0 }, 
         "Cafeine": {"molecular_weight":194.19,"solubility":16.0}}
def get_molecular_weight():
    return 180.16
weight = get_molecular_weight()
print(weight)

def get_weight_safe(drug_name):
    if drug_name in drugs:
        return drugs[drug_name]["molecular_weight"]
    else:
           return "Drug not found"
   
print(get_weight_safe("Cafeine"))
print(get_weight_safe("paracetamol"))