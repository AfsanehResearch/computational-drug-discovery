import pandas as pd
import numpy as np
data = {"compound": ["coo1", "coo2" , "coo3", "coo4", "coo5"],
        "MW": [180.16, 194.19, np.nan, 312.40, 275.35],
        "logP": [1.2, np.nan, 3.4, 4.2, 2.8],
        "HBD": [1, 2, 1, np.nan, 2],
        "HBA": [4, 5, 3, 6, np.nan]}
df = pd.DataFrame(data)

 # تغییر نمیدهد فقط نتیجه رو نمایش می دهدdf.dropna() 
print(df.dropna())
print(df.dropna(subset = ["MW"]))
print(df.fillna(0))