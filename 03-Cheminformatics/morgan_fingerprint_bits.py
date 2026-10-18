from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator

smiles = "CCO"
mol = Chem.MolFromSmiles(smiles)

if mol is None:
    raise ValueError(f"Invalid SMILES: {smiles}")

generator = rdFingerprintGenerator.GetMorganGenerator(
    radius=2,
    fpSize=2048,
)
fingerprint = generator.GetFingerprint(mol)

bit_string = fingerprint.ToBitString()
active_bits = list(fingerprint.GetOnBits())

print(f"SMILES: {smiles}")
print(f"Fingerprint size: {len(bit_string)} bits")
print(f"Bit string preview: {bit_string[:64]}...")
print(f"Active bit indices: {active_bits}")
print(f"Number of active bits: {len(active_bits)}")