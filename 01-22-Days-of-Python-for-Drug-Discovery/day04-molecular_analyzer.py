#اطلاعات جرم اتمی
atomic_mass = {"H": 1.008,"C": 12.011 , "O": 15.999 , "N": 14.007}
#ساختار یک مولکول نمونه
#CO2
molecule = ["C", "O", "O"]
#محاسبه جرم مولکولی
total_mass = 0

for atom in molecule:
    total_mass += atomic_mass [atom]

print("Molecule:" , molecule)
print("Molecular mass:" , total_mass)
#شمارش تعداداتم ها
atom_counter = {}

for atom in molecule:
    if atom in atom_counter:
        atom_counter[atom] += 1
    else:
        atom_counter[atom] = 1

print("Atom composition:")
print(atom_counter)
