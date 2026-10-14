import pandas as pd
data = {"compound": ["c001", "c002", "c003", "c004", "coo5"],
         "MW": [180.16, 194.19, 250.30, 312.40, 275.35],
         "logP": [1.2, 2.1, 3.4, 4.2, 2.8],
         "HBD" : [1, 2, 1, 0, 2],
         "HBA" :[4, 5, 3, 6, 4]}
df = pd.DataFrame(data)
print(df)
print(df["logP"])
print(df[["MW" , "logP"]])
print(df["logP"] < 3)
print(df["MW"] < 300) & (df["logP"] < 3)
print(df[(df["logP"] <2 ) | (df["HBD"] == 0)])