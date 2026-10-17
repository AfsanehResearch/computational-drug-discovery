from rdkit import Chem
from rdkit.Chem import Descriptors

smiles = "CCO"
mol = Chem.MolFromSmiles(smiles)

if mol is None:
    raise ValueError("Invalid SMILES string")

molecular_weight = Descriptors.MolWt(mol)

print("SMILES:", smiles)
print("Molecular weight:", molecular_weight, "g/mol")