drug = {"name": "Aspirin", "weight": 180.16}
def change_drug(drug):
    drug["name"] = "Ibuprofen"
    print(drug, "Inside the function")
change_drug(drug)
print(drug, "Outside the function")