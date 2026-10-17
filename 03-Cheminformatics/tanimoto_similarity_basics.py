from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
mol1 = Chem.MolFromSmiles("CCO")
mol2 = Chem.MolFromSmiles("CCCO")
generator = rdFingerprintGenerator.GetMorganGenerator(radius=2)

fp1 = generator.GetFingerprint(mol1)
fp2 = generator.GetFingerprint(mol2)


bits1 = set(fp1.GetOnBits())
bits2 = set(fp2.GetOnBits())


print("CCO:", bits1)
print("CCCO", bits2)
print("Common bits:", bits1 & bits2)
common = bits1 & bits2
all_bits = bits1 | bits2
a = len(common)
total = len(all_bits)
tanimoto = a /total

print("Common bits:", common)
print("Common count:", a)
print("Union count:", total)
print("Tanimoto:", tanimoto)