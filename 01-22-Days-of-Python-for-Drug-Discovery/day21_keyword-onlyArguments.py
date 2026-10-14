def describe_drug(name, weight, * ,unit = "mg"):
    return name, weight, unit
print(describe_drug("Aspirin", 180.16, unit = "mg"))