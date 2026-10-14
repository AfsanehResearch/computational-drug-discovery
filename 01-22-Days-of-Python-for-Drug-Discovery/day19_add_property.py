molecule = {"name": "Aspirin","atoms": 21, "weight": 180.16}
def add_property(mol,key,value):
    mol[key] = value

add_property(molecule, "logP", 1.19)
print(molecule)
