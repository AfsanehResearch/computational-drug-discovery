import pandas as pd
data = {"compound": ["coo1", "coo2" , "coo3", "coo4", "coo5"],
        "MW": [180.16, 194.19, 250.30, 312.40, 275.35],
        "logP": [1.2, 2.1, 3.4, 4.2, 2.8],
        "HBD": [1, 2, 1, 0, 2],
        "HBA": [4, 5, 3, 6, 4]}
df = pd.DataFrame(data)
df["TPSA"] = [63.6, 75.2, 42.1, 81.4, 68.3]
print(df)
df["Lipophilic"] =  df["logP"] > 3
print(df)
df = df.drop(columns = ["Lipophilic"])
print(df)
df = df.drop(columns = ["HBD", "HBA"])
print(df)
df = df.rename(columns = {"MW": "Molecular_Weight", "logP": "Logarithm P"})
print(df)