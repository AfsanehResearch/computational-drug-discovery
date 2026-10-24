"""
Day 32 — Molecular Data Quality with RDKit
==========================================

An educational, reproducible mini-workflow for:
- parsing and validating SMILES input;
- generating canonical isomeric SMILES;
- calculating basic molecular descriptors;
- detecting exact representation duplicates under this workflow;
- reporting data-quality statistics;
- exporting a record-level CSV report.

IMPORTANT SCIENTIFIC SCOPE
--------------------------
"Valid" in this script means that RDKit successfully parsed the SMILES and
created a molecule object. It does NOT mean the record is experimentally
confirmed, chemically stable, biologically active, or ready for docking.

Duplicate detection uses RDKit canonical isomeric SMILES as the grouping key.
This is a useful first-pass check, not full chemical standardization. In
particular, salts, mixtures, protonation states, tautomers, isotopes, and
stereochemistry require project-specific policies.

Requirements
------------
Python 3.9+ and RDKit.

Run
---
python molecular_data_quality.py
python molecular_data_quality.py --input molecules.csv --output report.csv

Input CSV format
----------------
The input CSV must contain columns named: name, smiles

Example:
name,smiles
Ethanol,CCO
Ethanol_alternate,OCC

Educational convention
----------------------
This file intentionally contains detailed comments and small functions so
that each step can be studied, tested, and reused.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors


# ============================================================================
# 1. Example dataset
# ============================================================================
# A dict is convenient for a tiny demonstration because each record has a
# label. Real datasets can contain repeated names, so the CSV loader below
# stores records in a list instead of relying on names being unique.
#
# Compound_A, Compound_B, and Compound_D are ethanol representations.
# Compound_C is acetone. Compound_E is intentionally invalid.
SAMPLE_MOLECULES: List[Tuple[str, str]] = [
    ("Compound_A", "CCO"),
    ("Compound_B", "OCC"),
    ("Compound_C", "CC(=O)C"),
    ("Compound_D", "CCO"),
    ("Compound_E_Invalid", "C1CC"),
    ("Compound_F_Benzene", "c1ccccc1"),
    ("Compound_G_Toluene", "Cc1ccccc1"),
    ("Compound_H_Ethanol_Stereo_Not_Applicable", "CCO"),
]


# ============================================================================
# 2. Data model
# ============================================================================
@dataclass
class MoleculeRecord:
    """
    Store input, validation, canonicalization, and descriptor results.

    Optional fields are None when the SMILES cannot be parsed. Keeping the
    invalid record is useful: dropping it silently would hide data-quality
    problems and make the report harder to audit.
    """

    record_id: int
    name: str
    original_smiles: str
    status: str
    error: str = ""
    canonical_smiles: str = ""
    formula: str = ""
    molecular_weight: Optional[float] = None
    exact_mass: Optional[float] = None
    heavy_atom_count: Optional[int] = None
    duplicate_group_size: Optional[int] = None
    duplicate_group_id: str = ""


# ============================================================================
# 3. Parsing and molecular-data validation
# ============================================================================
def process_one_record(record_id: int, name: str, smiles: str) -> MoleculeRecord:
    """
    Parse one SMILES and calculate descriptors if parsing succeeds.

    Why check `mol is None`?
    ------------------------
    Chem.MolFromSmiles() normally returns an RDKit Mol object on success and
    None when RDKit cannot parse the input. We must not pass None into
    descriptor or MolToSmiles functions.

    Scientific boundary:
    --------------------
    This is syntax/representation-level validation. It is not a full
    chemical curation protocol.
    """
    clean_name = name.strip()
    clean_smiles = smiles.strip()

    if not clean_name:
        clean_name = f"Unnamed_record_{record_id}"

    if not clean_smiles:
        return MoleculeRecord(
            record_id=record_id,
            name=clean_name,
            original_smiles=smiles,
            status="invalid",
            error="SMILES field is empty.",
        )

    mol = Chem.MolFromSmiles(clean_smiles)

    if mol is None:
        return MoleculeRecord(
            record_id=record_id,
            name=clean_name,
            original_smiles=clean_smiles,
            status="invalid",
            error="RDKit could not parse this SMILES string.",
        )

    # canonical=True asks RDKit for its canonical ordering.
    # isomericSmiles=True retains stereochemical/isotopic information encoded
    # in the molecule when writing SMILES; it does not invent missing stereo.
    canonical_smiles = Chem.MolToSmiles(
        mol,
        canonical=True,
        isomericSmiles=True,
    )

    # Molecular formula and descriptors are computed from the parsed Mol.
    # Average molecular weight and exact mass are different quantities.
    formula = rdMolDescriptors.CalcMolFormula(mol)
    molecular_weight = Descriptors.MolWt(mol)
    exact_mass = rdMolDescriptors.CalcExactMolWt(mol)
    heavy_atom_count = mol.GetNumHeavyAtoms()

    return MoleculeRecord(
        record_id=record_id,
        name=clean_name,
        original_smiles=clean_smiles,
        status="valid",
        canonical_smiles=canonical_smiles,
        formula=formula,
        molecular_weight=round(molecular_weight, 4),
        exact_mass=round(exact_mass, 4),
        heavy_atom_count=heavy_atom_count,
    )


def process_records(
    input_records: Iterable[Tuple[str, str]],
) -> List[MoleculeRecord]:
    """
    Process all (name, SMILES) pairs while preserving input order.

    enumerate(..., start=1) gives each row a stable ID within this run.
    A list is used because input data may contain repeated names.
    """
    processed: List[MoleculeRecord] = []

    for record_id, (name, smiles) in enumerate(input_records, start=1):
        processed.append(process_one_record(record_id, name, smiles))

    return processed


# ============================================================================
# 4. Duplicate grouping
# ============================================================================
def assign_duplicate_groups(records: Sequence[MoleculeRecord]) -> None:
    """
    Add duplicate group IDs and group sizes to valid records in-place.

    The grouping key is canonical isomeric SMILES. Invalid records are not
    grouped because no canonical representation was produced.

    In-place means this function updates the existing MoleculeRecord objects
    rather than creating and returning a second list.
    """
    groups: Dict[str, List[MoleculeRecord]] = defaultdict(list)

    for record in records:
        if record.status == "valid" and record.canonical_smiles:
            groups[record.canonical_smiles].append(record)

    # Sorting makes the group IDs deterministic for the same set of
    # canonical SMILES, regardless of the order in which groups were found.
    for group_number, canonical_smiles in enumerate(sorted(groups), start=1):
        group_id = f"STRUCT_{group_number:04d}"
        group_records = groups[canonical_smiles]

        for record in group_records:
            record.duplicate_group_id = group_id
            record.duplicate_group_size = len(group_records)


def summarize_records(records: Sequence[MoleculeRecord]) -> Dict[str, int]:
    """Return transparent counts for records and unique canonical structures."""
    valid = [record for record in records if record.status == "valid"]
    invalid = [record for record in records if record.status != "valid"]
    unique_structures = {
        record.canonical_smiles for record in valid if record.canonical_smiles
    }
    duplicate_records = sum(
        1
        for record in valid
        if record.duplicate_group_size is not None
        and record.duplicate_group_size > 1
    )

    return {
        "input_records": len(records),
        "valid_records": len(valid),
        "invalid_records": len(invalid),
        "unique_canonical_structures": len(unique_structures),
        "records_in_duplicate_groups": duplicate_records,
    }


# ============================================================================
# 5. Reporting
# ============================================================================
def print_report(records: Sequence[MoleculeRecord]) -> None:
    """Print a human-readable summary and record-level findings."""
    summary = summarize_records(records)

    print("\nMOLECULAR DATA QUALITY REPORT")
    print("=" * 72)
    print(f"Input records:                    {summary['input_records']}")
    print(f"Valid SMILES records:             {summary['valid_records']}")
    print(f"Invalid SMILES records:           {summary['invalid_records']}")
    print(
        "Unique canonical structures:     "
        f"{summary['unique_canonical_structures']}"
    )
    print(
        "Records in duplicate groups:     "
        f"{summary['records_in_duplicate_groups']}"
    )

    print("\nRECORD-LEVEL RESULTS")
    print("-" * 72)
    for record in records:
        print(f"[{record.status.upper():7}] #{record.record_id}: {record.name}")
        print(f"         Original SMILES:  {record.original_smiles}")

        if record.status == "invalid":
            print(f"         Issue:            {record.error}")
            continue

        print(f"         Canonical SMILES: {record.canonical_smiles}")
        print(f"         Formula:          {record.formula}")
        print(f"         Average MW:       {record.molecular_weight}")
        print(f"         Exact mass:       {record.exact_mass}")
        print(f"         Heavy atoms:      {record.heavy_atom_count}")
        print(
            f"         Duplicate group:  {record.duplicate_group_id} "
            f"(size={record.duplicate_group_size})"
        )

    print("\nINTERPRETATION NOTES")
    print("-" * 72)
    print("* Invalid means RDKit could not parse the input SMILES.")
    print("* A shared group means identical canonical isomeric SMILES here.")
    print("* It does not establish biological equivalence or activity.")
    print("* No salt stripping, tautomer normalization, or neutralization is done.")


def export_csv(records: Sequence[MoleculeRecord], output_path: Path) -> None:
    """
    Export one row per input record.

    DictWriter writes named columns, making the output easier to inspect in
    spreadsheet software or load later with pandas.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(MoleculeRecord.__dataclass_fields__.keys())

    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for record in records:
            writer.writerow(asdict(record))


# ============================================================================
# 6. Optional CSV input
# ============================================================================
def load_csv(input_path: Path) -> List[Tuple[str, str]]:
    """
    Load a CSV containing `name` and `smiles` columns.

    `newline=""` is the recommended CSV-file opening pattern. utf-8 supports
    common text labels. Required columns are checked explicitly to produce a
    useful error message before processing begins.
    """
    with input_path.open("r", newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)

        required_columns = {"name", "smiles"}
        actual_columns = set(reader.fieldnames or [])
        missing_columns = required_columns - actual_columns

        if missing_columns:
            missing_text = ", ".join(sorted(missing_columns))
            raise ValueError(
                f"Input CSV is missing required column(s): {missing_text}"
            )

        records: List[Tuple[str, str]] = []
        for row_number, row in enumerate(reader, start=2):
            name = row.get("name") or f"Row_{row_number}"
            smiles = row.get("smiles") or ""
            records.append((name, smiles))

    return records


# ============================================================================
# 7. Command-line interface
# ============================================================================
def parse_arguments() -> argparse.Namespace:
    """Define optional command-line arguments for real CSV files."""
    parser = argparse.ArgumentParser(
        description="Validate SMILES, calculate basic descriptors, and group duplicates."
    )
    parser.add_argument(
        "--input",
        type=Path,
        help="Optional CSV input with required columns: name, smiles",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("molecular_validation_results.csv"),
        help="Path for the output report CSV (default: molecular_validation_results.csv)",
    )
    return parser.parse_args()


def main() -> None:
    """Coordinate input, processing, duplicate grouping, reporting, and export."""
    args = parse_arguments()

    if args.input:
        input_records = load_csv(args.input)
    else:
        input_records = SAMPLE_MOLECULES

    records = process_records(input_records)
    assign_duplicate_groups(records)
    print_report(records)
    export_csv(records, args.output)

    print(f"\nCSV report written to: {args.output.resolve()}")


if __name__ == "__main__":
    main()
