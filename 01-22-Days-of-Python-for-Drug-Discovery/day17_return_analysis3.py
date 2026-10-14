drugs = {"Aspirin": {"molecular_weight": 180.16,"solubility":3.0}, 
         "Ibuprofen":{"molecular_weight":206.28 ,"solubility":21.0 }, 
         "Cafeine": {"molecular_weight":194.19,"solubility":16.0}}
def calculate_total(weight,amount):
    return weight * amount
result = calculate_total(180.16,3)
print(result)
def get_total_weight(drug_name, amount):
    return drugs[drug_name]["molecular_weight"] * amount
result = get_total_weight("Ibuprofen", 3)
print(result)
