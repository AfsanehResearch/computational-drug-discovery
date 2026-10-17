
import csv

from rdkit import Chem, DataStructs
from rdkit.Chem import(
    rdFingerprintGenerator,
    Descriptors,
    Crippen,
    Lipinski,
    rdMolDescriptors,)

# 1. Reference molecule
reference_smiles = "CCOc1ccc2nc(S(N)(=O)=O)sc2c1"
reference = Chem.MolFromSmiles(reference_smiles)

if reference is None:
    raise ValueError("Invalid reference SMILES!")

# 2. Morgan fingerprint generator
morgan_gen = rdFingerprintGenerator.GetMorganGenerator(radius=2)
reference_fp = morgan_gen.GetFingerprint(reference)

# 3. Candidate molecules
smiles_list = ["CCOc1ccc2nc(S(N)(=O)=O)sc2c1",
    "CCOc1ccc2nc(S(N)(=O)=O)sc2c1C",
    "CCOc1ccc2nc(N)sc2c1",
    "CCc1ccccc1",
    "CCCCCCCC",]

results = []

# 4. Process each molecule
for smiles in smiles_list:
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        print(f"Skipping invalid SMILES: {smiles}")
        continue

    fingerprint = morgan_gen.GetFingerprint(mol)
    similarity = DataStructs.TanimotoSimilarity(
        reference_fp, fingerprint)

    results.append({
        "SMILES": smiles,
        "Tanimoto_Similarity": round(similarity, 3),
        "Molecular_Weight": round(Descriptors.MolWt(mol), 2),
        "LogP": round(Crippen.MolLogP(mol), 2),
        "H_Bond_Donors": Lipinski.NumHDonors(mol),
        "H_Bond_Acceptors": Lipinski.NumHAcceptors(mol),
        "TPSA": round(rdMolDescriptors.CalcTPSA(mol), 2),})

# 5. Rank by similarity
results.sort(
    key=lambda item: item["Tanimoto_Similarity"],
    reverse=True,)

# 6. Display results
print("\nMolecular Screening Results")
print("=" * 70)

for item in results:
    print(
        f"Similarity: {item['Tanimoto_Similarity']:.3f} | "
        f"MW: {item['Molecular_Weight']:.2f} | "
        f"LogP: {item['LogP']:.2f} | "
        f"SMILES: {item['SMILES']}")

# 7. Export results to CSV
output_file = "03-Cheminformatics/similarity_results.csv"

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"\nResults saved to: {output_file}")
