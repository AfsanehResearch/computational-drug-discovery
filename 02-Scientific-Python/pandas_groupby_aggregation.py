import pandas as pd
data = {"Molecule": ["A", "B", "C", "D", "E"],
         "Class": ["Drug", "Drug", "Lead", "Lead","Drug"],
         "Target":["A", "B", "A", "A", "B"],
         "MW": [180, 250, 210, 310, 275],
         "logP": [1.2, 2.1, 2.8, 3.1, 1.7]}

df = pd.DataFrame(data)
print(df)
print(df.groupby("Class")["MW"].mean())
print(df.groupby("Class")["MW"].max())
print(df.groupby("Class")["MW"].min())
print(df.groupby("Class")["MW"].sum())
print(df.groupby("Class")["MW"].count())
print(df.groupby("Class")["MW"].median())
print(df["Class"].value_counts())
print(df.groupby(["Class","Target"])["MW"].mean())
print(df.groupby("Class")["MW"].agg(["mean", "min", "max"])) #agg چند عملیات آماری را روی گروه‌ها انجام می دهد
print(df.groupby("Class")[["MW", "logP"]].mean())
print(df.groupby("Class").agg({"MW": ["min" ,"max"], "logP": ["mean", "min", "max"]}))
