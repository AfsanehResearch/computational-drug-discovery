choice =2
if choice == 1:
    molecule = {"name": "Aspirin",
             "atoms": 21, 
             "weight": 180.16}
    def add_property(a):
        molecule.update(a)
    log_p = {"log P": 1.19}
    add_property(log_p)
    print(molecule)
elif choice ==2:
    molecule = {"name": "Aspirin",
                 "atoms": 21, 
                 "weight": 180.16}
    def add_property(mol,prop):
        molecule.update(prop)
        return mol
    log_p = {"log P": 1.19}

    molecule = add_property(molecule, log_p)
    print("Code 2:")
    print(molecule)
else:
    print("Please enter 1 or 2.")
