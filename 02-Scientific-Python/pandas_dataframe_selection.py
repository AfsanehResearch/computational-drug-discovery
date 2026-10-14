import pandas as pd
data = {"Drug": ["Aspirin", "Caffeine", "Ibuprofen"], "MW": [180.16, 194.19, 206.28], "logp": [1.2, -0.1, 3.5]}
df = pd.DataFrame(data)
print(df)
print(df["MW"])
print(df["logp"])
print(df[["Drug", "logp"]])
  