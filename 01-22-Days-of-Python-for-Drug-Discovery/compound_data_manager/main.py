
from file_handler import read_compounds, save_results
from compound_utils import process_compounds


def main():
    input_file = "compounds.txt"
    output_file = "processed_compounds.txt"

    # Read the input file
    try:
        compounds = read_compounds(input_file)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' was not found.")
        return

    # Process the compound names
    processed_compounds = process_compounds(compounds)

    # Save the processed results
    try:
        save_results(output_file, processed_compounds)
    except OSError as error:
        print(f"Error while saving results: {error}")
        return

    # Display a summary
    print("Processing completed successfully.")
    print(f"Input lines: {len(compounds)}")
    print(f"Unique compounds: {len(processed_compounds)}")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()

