
def validate_compound_name(name):
    """
    Check whether a compound name is a non-empty string.

    Parameters
    ----------
    name : str
        Compound name to validate.

    Returns
    -------
    bool
        True if the name is a non-empty string.
    """
    return isinstance(name, str) and bool(name.strip())


def process_compounds(compounds):
    """
    Remove empty entries and duplicate compound names.

    The order of first appearance is preserved.

    Parameters
    ----------
    compounds : list[str]
        List of compound names.

    Returns
    -------
    list[str]
        Processed compound names.
    """
    unique_compounds = []
    seen = set()

    for compound in compounds:
        if not validate_compound_name(compound):
            continue

        compound = compound.strip()

        if compound not in seen:
            unique_compounds.append(compound)
            seen.add(compound)

    return unique_compounds

