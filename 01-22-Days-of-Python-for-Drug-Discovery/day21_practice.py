def describe_drug(name, weight, * , unit = "mg", form = "tablet"):
    return name, weight,unit, form
print(describe_drug("Aspirin", 180.16))
print(describe_drug("Aspirin", 180.16, unit = "mL"))
print(describe_drug("Aspirin", 180.16, form = "capsule", unit = "mg"))
