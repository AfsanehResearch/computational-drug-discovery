from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
from rdkit import DataStructs
reference = Chem.MolFromSmiles("CCOc1ccc2nc(S(N)(=O)=O)sc2c1")
print("Reference:", reference)
print("Reference is None:", reference is None)
morgan_gen = rdFingerprintGenerator.GetMorganGenerator(radius=2)
reference_fp = morgan_gen.GetFingerprint(reference)
smiles_list = ["CCOc1ccc2nc(S(N)(=O)=O)sc2c1",
               "CCOc1ccc2nc(S(N)(=O)=O)sc2c1C",
               "CCOc1ccc2nc(N)sc2c1",
               "CCc1ccccc1",
               "CCCCCCCC"]
molecules = [Chem.MolFromSmiles(smiles) for smiles in smiles_list]
fps = [morgan_gen.GetFingerprint(mol) for mol in molecules]
similarities = [DataStructs.TanimotoSimilarity(reference_fp, fp) for fp in fps]
results = list(zip(smiles_list, similarities))
results.sort(key = lambda x: x[1], reverse = True)
print("\nSimilarity ranking:")
print("-" * 50)
for smiles, similarity in results:
    print(f"Tanimoto: {similarity:.3f} {smiles}")