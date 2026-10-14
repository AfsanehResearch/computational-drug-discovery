atoms = ["C", "C","O", "H", "H"]
def add_atom(atom_list, new_atom):
  atom_list.append(new_atom)  
molecule_atoms = ["C", "C", "O"] 
add_atom(molecule_atoms, "N")
print(molecule_atoms)