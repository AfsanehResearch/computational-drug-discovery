def molecule_info(name, formula = "unknown", charge = 0):
    print(name, formula, charge)
molecule_info("Caffeine")
molecule_info("Caffeine", "C8H10N4O2")
molecule_info("Caffeine", charge = 1)
molecule_info("Caffeine", charge = -1, formula = "C8H10N4O2")
