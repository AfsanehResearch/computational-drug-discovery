drug_name = input("Drug name: ")
mass = float(input("Mass (g): ")) 
molecular_weight = float(input("Molecular Weight (g/mol): "))
volume = float(input("Volume (L): "))
molarity = mass / (molecular_weight * volume)

print("Drug:" , drug_name)
print("Molarity =" , molarity, "M")