
"""
SMARTS Query Patterns with RDKit
=================================

Learn how to define, validate, and apply SMARTS queries to molecules.

Topics:
- SMARTS atom and bond patterns
- Carbonyls, carboxylic acids, alcohols, and primary amines
- Logical operators: OR, AND, and NOT
- Explicit hydrogen counts and formal charges
- Substructure matching and atom indices
- Counting multiple matches in one molecule

Run:
    python 03-Cheminformatics/smarts_query_patterns.py
"""

from rdkit import Chem


# ------------------------------------------------------------
# 1. Example molecule library
# ------------------------------------------------------------

MOLECULES = {
    "Ethanol": "CCO",
    "Acetic acid": "CC(=O)O",
    "Acetone": "CC(=O)C",
    "Acetoacetic acid": "CC(=O)CC(=O)O",
    "Ethylamine": "CCN",
    "Acetamide": "CC(=O)N",
    "Benzene": "c1ccccc1",
    "Acetate ion": "CC(=O)[O-]",
    "Ammonium ion": "[NH4+]",
    "Water": "O",
}


# ------------------------------------------------------------
# 2. SMARTS query library
# ------------------------------------------------------------

SMARTS_PATTERNS = {
    "Carbonyl": {
        "smarts": "[CX3]=[OX1]",
        "description": "Carbon-oxygen double bond in a carbonyl group",
    },
    "Carboxylic acid": {
        "smarts": "[CX3](=O)[OX2H1]",
        "description": "Carboxylic acid group",
    },
    "Alcohol": {
        "smarts": "[CX4][OX2H]",
        "description": "Hydroxyl oxygen attached to a saturated carbon",
    },
    "Primary amine": {
        "smarts": "[NX3;H2;!$(NC=O)]",
        "description": "Primary amine nitrogen, excluding amide nitrogen",
    },
    "Benzene ring": {
        "smarts": "c1ccccc1",
        "description": "A six-membered aromatic carbon ring",
    },
    "Negative oxygen": {
        "smarts": "[O-]",
        "description": "Negatively charged oxygen atom",
    },
    "Positive nitrogen": {
        "smarts": "[N+]",
        "description": "Positively charged nitrogen atom",
    },
}


# ------------------------------------------------------------
# 3. Parse and validate molecules and SMARTS patterns
# ------------------------------------------------------------

def build_molecule_library(smiles_library):
    """Convert SMILES strings into RDKit molecule objects."""
    molecules = {}

    for name, smiles in smiles_library.items():
        mol = Chem.MolFromSmiles(smiles)

        if mol is None:
            raise ValueError(
                f"Invalid SMILES for {name}: {smiles}"
            )

        molecules[name] = mol

    return molecules


def compile_smarts_patterns(pattern_library):
    """Compile SMARTS strings and reject invalid patterns."""
    patterns = {}

    for name, details in pattern_library.items():
        smarts = details["smarts"]
        query = Chem.MolFromSmarts(smarts)

        if query is None:
            raise ValueError(
                f"Invalid SMARTS pattern for {name}: {smarts}"
            )

        patterns[name] = query

    return patterns


# ------------------------------------------------------------
# 4. Match a pattern and report the matching atoms
# ------------------------------------------------------------

def get_matches(mol, query):
    """Return unique substructure matches as atom-index tuples."""
    return mol.GetSubstructMatches(query, uniquify=True)


def format_match_atoms(mol, match):
    """Describe the atoms involved in one match."""
    atoms = []

    for idx in match:
        atom = mol.GetAtomWithIdx(idx)
        atoms.append(f"{idx}:{atom.GetSymbol()}")

    return ", ".join(atoms)


# ------------------------------------------------------------
# 5. Build a molecule-versus-pattern comparison table
# ------------------------------------------------------------

def print_match_matrix(molecules, patterns):
    """Print the number of matches for each molecule and query."""
    pattern_names = list(patterns)

    name_width = max(
        len("Molecule"),
        max(len(name) for name in molecules),
    )

    pattern_width = 13

    print("\nSUBSTRUCTURE MATCHING SUMMARY")
    print("=" * (name_width + 3 + pattern_width * len(pattern_names)))

    header = f"{'Molecule':<{name_width}}"
    for pattern_name in pattern_names:
        header += f" | {pattern_name[:pattern_width]:>{pattern_width}}"

    print(header)
    print("-" * len(header))

    for molecule_name, mol in molecules.items():
        row = f"{molecule_name:<{name_width}}"

        for pattern_name in pattern_names:
            count = len(get_matches(mol, patterns[pattern_name]))
            row += f" | {count:>{pattern_width}}"

        print(row)

    print("\nEach number is the count of unique substructure matches.")


# ------------------------------------------------------------
# 6. Demonstrate SMARTS logical operators
# ------------------------------------------------------------

def demonstrate_logical_operators(molecules):
    """Compare OR and AND atom queries on the same molecule."""
    mol = molecules["Acetic acid"]

    logical_patterns = {
        "OR: oxygen or nitrogen": "[O,N]",
        "AND: oxygen with one H": "[O;H1]",
    }

    print("\nLOGICAL OPERATORS")
    print("=" * 60)
    print("Test molecule: Acetic acid (CC(=O)O)")

    for name, smarts in logical_patterns.items():
        query = Chem.MolFromSmarts(smarts)

        if query is None:
            raise ValueError(f"Invalid SMARTS pattern: {smarts}")

        matches = get_matches(mol, query)

        print(f"\n{name}")
        print(f"SMARTS: {smarts}")
        print(f"Number of matches: {len(matches)}")

        for match in matches:
            print(f"  Matched atoms: {format_match_atoms(mol, match)}")


# ------------------------------------------------------------
# 7. Demonstrate multiple matches and atom indices
# ------------------------------------------------------------

def demonstrate_multiple_matches(molecules, patterns):
    """Show each carbonyl match in a molecule with two carbonyls."""
    molecule_name = "Acetoacetic acid"
    pattern_name = "Carbonyl"

    mol = molecules[molecule_name]
    query = patterns[pattern_name]
    matches = get_matches(mol, query)

    print("\nMULTIPLE SUBSTRUCTURE MATCHES")
    print("=" * 60)
    print(f"Molecule: {molecule_name}")
    print(f"SMILES: {MOLECULES[molecule_name]}")
    print(f"SMARTS: {SMARTS_PATTERNS[pattern_name]['smarts']}")
    print(f"Number of carbonyl matches: {len(matches)}")

    for number, match in enumerate(matches, start=1):
        print(
            f"  Match {number}: "
            f"{format_match_atoms(mol, match)}"
        )


# ------------------------------------------------------------
# 8. Demonstrate formal charges and hydrogen counts
# ------------------------------------------------------------

def demonstrate_atom_properties(molecules):
    """Query charged atoms and atoms with specified H counts."""
    examples = [
        ("Water", "[OH2]", "Oxygen with two hydrogens"),
        ("Ammonium ion", "[NH4+]", "Nitrogen with four hydrogens and a positive charge"),
        ("Acetate ion", "[O-]", "Negatively charged oxygen"),
        ("Ammonium ion", "[N+]", "Positively charged nitrogen"),
    ]

    print("\nATOM PROPERTIES")
    print("=" * 60)

    for molecule_name, smarts, description in examples:
        mol = molecules[molecule_name]
        query = Chem.MolFromSmarts(smarts)

        if query is None:
            raise ValueError(f"Invalid SMARTS pattern: {smarts}")

        matches = get_matches(mol, query)

        print(f"\nMolecule: {molecule_name}")
        print(f"Purpose: {description}")
        print(f"SMARTS: {smarts}")
        print(f"Matches: {len(matches)}")

        for match in matches:
            print(f"  Matched atoms: {format_match_atoms(mol, match)}")


# ------------------------------------------------------------
# 9. Run the educational examples
# ------------------------------------------------------------

def main():
    molecules = build_molecule_library(MOLECULES)
    patterns = compile_smarts_patterns(SMARTS_PATTERNS)

    print("SMARTS QUERY PATTERNS WITH RDKIT")
    print("=" * 60)
    print(f"Molecules loaded: {len(molecules)}")
    print(f"SMARTS patterns compiled: {len(patterns)}")

    print_match_matrix(molecules, patterns)
    demonstrate_logical_operators(molecules)
    demonstrate_multiple_matches(molecules, patterns)
    demonstrate_atom_properties(molecules)


if __name__ == "__main__":
    main()