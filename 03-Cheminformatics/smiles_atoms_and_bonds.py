from rdkit import Chem
smiles = "CCO" #ایتجا رشته داریم استرینگ
mol = Chem.MolFromSmiles(smiles) # اینجا رشته رو با ابزار rdkit تفسیر کن و مولکولار آبجکت را داخل متغیر مل قرار بده
print(mol)
print(Chem.MolToSmiles(mol))
print(mol.GetNumAtoms())
print(mol.GetNumBonds())
#rdkit به صورت پیش فرض اتمهای صریح موجود در ساختار مولکولی را می شمارد implicit Hzdrogen

print(mol.GetAtomWithIdx(0).GetSymbol())
print(mol.GetAtomWithIdx(1).GetSymbol())
print(mol.GetAtomWithIdx(2).GetSymbol())
print("Number of atoms:" , mol.GetNumAtoms())
print("Atoms:")
for atom in mol.GetAtoms():
    print(atom.GetIdx(), atom.GetSymbol())
print("/nBond:")
for bond in mol.GetBonds():
    print(bond.GetBeginAtomIdx(), bond.GetEndAtomIdx())
print("========= Let's go ============")
for bond in mol.GetBonds():
        print(bond.GetBeginAtomIdx(),
              bond.GetEndAtomIdx(),
              bond.GetBondType())
#نوع پیوند برای همه و نه فقط برای شروع و انتها
for bond in mol.GetBonds():
     print(bond.GetBondType())
#اگر شماره خود باند را داشته باشیم
for i, bond in enumerate(mol.GetBonds()):
     print(i, bond.GetBondType())
arom = Chem.MolFromSmiles("c1ccccc1")
for bond in arom.GetBonds():
     print(bond.GetBondType())