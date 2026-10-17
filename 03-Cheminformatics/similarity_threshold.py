from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
from rdkit import DataStructs
reference = Chem.MolFromSmiles("CCO")
generator = rdFingerprintGenerator.GetMorganGenerator(radius=2)
reference_fp = generator.GetFingerprint(reference)
library = {"Ethanol": "CCO",
           "Propanol": "CCCO",
           "Butanol": "CCCCO",
           "Acetic acid":"CC(=O)O",
           "Benzene": "c1ccccc1"}
results = []
for name, smiles in library.items():
    mol = Chem.MolFromSmiles(smiles)
    fp = generator.GetFingerprint(mol)
    similarity = DataStructs.TanimotoSimilarity(reference_fp, fp)
    results.append({"Name": name, "Similarity": similarity})
results_sorted = sorted(results, key = lambda x : x["Similarity"], reverse = True)
for result in results_sorted:
        print(result["Name"], "→", result["Similarity"])
print("====== AND THEN =====")
threshold = 0.5
top_hits = []
for result in results_sorted:
      if result["Similarity"] >= threshold: 
           top_hits.append(result)
for hit in top_hits:
     print(hit["Name"],"→", hit["Similarity"])