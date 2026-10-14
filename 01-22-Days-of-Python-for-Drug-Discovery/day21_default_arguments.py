def calculate_dose(weight,dose_per_kg = 5):
    dose = weight * dose_per_kg
    return dose
print(calculate_dose(60))
print(calculate_dose(60,8))