
def read_compounds(filename):
    """
    Read compound names from a text file.

    Parameters
    ----------
    filename : str
        Path to the input file.

    Returns
    -------
    list[str]
        A list containing the lines read from the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()


def save_results(filename, compounds):
    """
    Save compound names to a text file.

    Parameters
    ----------
    filename : str
        Path to the output file.

    compounds : list[str]
        List of compound names to save.
    """
    with open(filename, "w", encoding="utf-8") as file:
        for compound in compounds:
            file.write(compound + "\n")

