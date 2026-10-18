from rdkit import Chem


SMILES_LIBRARY = [
    ("Ethanol", "CCO"),
    ("Acetic acid", "CC(=O)O"),
    ("Acetoacetic acid", "CC(=O)CC(=O)O"),
    ("Ethylamine", "CCN"),
    ("Benzene", "c1ccccc1"),
]

SMARTS_PATTERNS = {
    "carbonyl": "[CX3]=[OX1]",
    "hydroxyl": "[OX2H]",
    "primary_amine": "[NX3;H2;!$(NC=O)]",
}


def compile_patterns():
    """Compile SMARTS patterns and validate them."""
    patterns = {}

    for name, smarts in SMARTS_PATTERNS.items():
        pattern = Chem.MolFromSmarts(smarts)

        if pattern is None:
            raise ValueError(f"Invalid SMARTS pattern for {name}: {smarts}")

        patterns[name] = pattern

    return patterns


def screen_molecules():
    """Screen molecules using the defined SMARTS patterns."""
    patterns = compile_patterns()
    accepted = []

    for name, smiles in SMILES_LIBRARY:
        mol = Chem.MolFromSmiles(smiles)

        if mol is None:
            print(f"INVALID SMILES: {name} | {smiles}")
            continue

        has_carbonyl = mol.HasSubstructMatch(patterns["carbonyl"])
        has_hydroxyl = mol.HasSubstructMatch(patterns["hydroxyl"])
        has_primary_amine = mol.HasSubstructMatch(
            patterns["primary_amine"])

        passed = (
    has_carbonyl
    and has_hydroxyl
    and not has_primary_amine
)

        status = "ACCEPTED" if passed else "REJECTED"

        print(f"\n{status}: {name} ({smiles})")
        print(f"  Carbonyl: {has_carbonyl}")
        print(f"  Hydroxyl: {has_hydroxyl}")
        print(f"  Primary amine: {has_primary_amine}")

        if passed:
            accepted.append((name, smiles))

    return accepted


def main():
    accepted = screen_molecules()

    print("\n" + "=" * 35)
    print("FINAL ACCEPTED MOLECULES")
    print("=" * 35)

    if accepted:
        for name, smiles in accepted:
            print(f"- {name}: {smiles}")
    else:
        print("No molecules passed the filters.")


if __name__ == "__main__":
    main()