drugs = {"Aspirin": {"molecular_weight": 180.16,"solubility":3.0}, 
         "Ibuprofen":{"molecular_weight":206.28 ,"solubility":21.0 }, 
         "Cafeine": {"molecular_weight":194.19,"solubility":16.0}}
def get_molecular_weight():
    return 180.16
weight = get_molecular_weight()

print(weight)
print (" === finished === ")

def double_weight(weight):
    return weight*2 
result = double_weight(180.16)

print (result)
print ("=== finished === ")

def get_weight(drug_name):
    return drugs[drug_name]["molecular_weight"]
weight = get_weight("Ibuprofen")

print(weight)
print(drugs["Aspirin"]["molecular_weight"])
print("===finished === ")

try: 
    print(drugs["Paracetamol"]["molecular_weight"])
except KeyError:
    print("Drug not found")
    print(" ===finished=== " )
def get_weight_safe(drug_name):
    if drug_name in drugs:
        return drugs[drug_name]["molecular_weight"]
    else:
        return "Drug not found"
print(get_weight_safe("Aspirin"))
print(get_weight_safe("Paracetamol"))