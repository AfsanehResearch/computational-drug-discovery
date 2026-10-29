# Compound Data Manager

## Overview

Compound Data Manager is a beginner-level Python project developed as part of my learning journey in computational chemistry and drug discovery.

The program reads compound names from a text file, removes empty entries and duplicate names, and saves the processed results to an output file.

## Learning Objectives

- File handling and text file processing
- Exception handling and error management
- Functions and input validation
- Python modules and imports
- Code organization and separation of responsibilities
- Working with lists and sets
- Basic command-line execution

## Project Structure

```text
compound_data_manager/
├── main.py
├── file_handler.py
├── compound_utils.py
├── compounds.txt
├── processed_compounds.txt
└── README.md
```

## How to Run

Run the following command from the project directory:

```bash
python main.py
```

The program reads `compounds.txt` and saves the processed compound names to `processed_compounds.txt`.

## Example Output

```text
Processing completed successfully.
Input lines: 8
Unique compounds: 5
Results saved to: processed_compounds.txt
```

The output depends on the contents of the input file.

## Scope and Limitations

This project processes compound names as text. It does not validate chemical structures, parse SMILES, or calculate molecular properties.

It provides a foundation for future projects involving scientific Python and cheminformatics with RDKit.

## Project Status

Implemented and tested locally.