drug = {"name": "Aspirin", "weight": 180.16}
print(id(drug), "بیرون")

def change_drug(drug):
    print(id(drug), "داخل")
change_drug(drug)