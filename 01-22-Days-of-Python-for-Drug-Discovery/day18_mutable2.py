drug = "Aspirin"
def change_drug(drug):
    drug += "plus"
    print(drug, "Inside the function")
change_drug(drug)
print(drug, "Outside the function")