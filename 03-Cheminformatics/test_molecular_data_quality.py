"""Unit tests for molecular_data_quality.py.

Run from this directory with:
    python -m unittest -v
"""

import unittest

from molecular_data_quality import (
    assign_duplicate_groups,
    process_one_record,
    process_records,
    summarize_records,
)


class MolecularDataQualityTests(unittest.TestCase):
    def test_valid_smiles_is_processed(self):
        record = process_one_record(1, "Ethanol", "CCO")
        self.assertEqual(record.status, "valid")
        self.assertEqual(record.formula, "C2H6O")
        self.assertTrue(record.canonical_smiles)

    def test_invalid_smiles_is_preserved_as_invalid_record(self):
        record = process_one_record(1, "Broken", "C1CC")
        self.assertEqual(record.status, "invalid")
        self.assertIsNone(record.molecular_weight)
        self.assertEqual(record.canonical_smiles, "")

    def test_alternate_smiles_for_ethanol_group_together(self):
        records = process_records(
            [("Ethanol_A", "CCO"), ("Ethanol_B", "OCC")]
        )
        assign_duplicate_groups(records)
        self.assertEqual(records[0].canonical_smiles, records[1].canonical_smiles)
        self.assertEqual(records[0].duplicate_group_id, records[1].duplicate_group_id)
        self.assertEqual(records[0].duplicate_group_size, 2)

    def test_summary_counts_records_and_unique_structures(self):
        records = process_records(
            [
                ("Ethanol_A", "CCO"),
                ("Ethanol_B", "OCC"),
                ("Acetone", "CC(=O)C"),
                ("Broken", "C1CC"),
            ]
        )
        assign_duplicate_groups(records)
        summary = summarize_records(records)

        self.assertEqual(summary["input_records"], 4)
        self.assertEqual(summary["valid_records"], 3)
        self.assertEqual(summary["invalid_records"], 1)
        self.assertEqual(summary["unique_canonical_structures"], 2)
        self.assertEqual(summary["records_in_duplicate_groups"], 2)

    def test_empty_smiles_is_invalid(self):
        record = process_one_record(1, "Empty", "   ")
        self.assertEqual(record.status, "invalid")
        self.assertIn("empty", record.error.lower())


if __name__ == "__main__":
    unittest.main()
