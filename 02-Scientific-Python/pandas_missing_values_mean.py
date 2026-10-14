import pandas as pd
import numpy as np
data = {"Molecule": ["A", "B", "C", "D", "E"], 
        "MW": [180.2, 250.5, None, 310.7, 275.1], 
        "LogP": [1.2, None, 2.8, 3.1, None]}
df = pd.DataFrame(data)
print(df)
print(df.dropna())
df["MW"] = df["MW"]. fillna(df["MW"].mean())
df["LogP"] = df["LogP"].fillna(df["LogP"].mean())
print(df["MW"])
print(df["LogP"])
