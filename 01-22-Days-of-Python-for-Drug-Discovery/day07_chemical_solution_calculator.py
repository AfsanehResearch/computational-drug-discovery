print("=== Chemical Solution Calculator ===")

drug_name = input("Drug name: ")

mass = float(input("Mass (g): "))

molecular_weight = float(input("Molecular Weight (g/mol): "))

volume = float(input("Volume (L): "))
moles = mass / molecular_weight

molarity = moles / volume

print()
print("==== Results ====")
print("Drug:", drug_name)
print("Mass:", mass, "g")
print("Molecular Weight: ", molecular_weight, "g/mol")
print("Volume: ", volume, "L")
print("Moles:", moles)
print("Molarity: ", molarity,"M")
