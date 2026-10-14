import pandas as pd
data = {"compound": ["coo1", "coo2" , "coo3", "coo4", "coo5"],
        "MW": [180.16, 194.19, 250.30, 312.40, 275.35],
        "logP": [1.2, 2.1, 3.4, 4.2, 2.8],
        "HBD": [1, 2, 1, 0, 2],
        "HBA": [4, 5, 3, 6, 4]}
df = pd.DataFrame(data)
print(df)
print(df.loc[2])
#loc میتونه عدد یا لیبل باشه
#ردیف را انتخاب میکنیم
#در فریم کلیدهای دیکشنری تبدیل به نام ستون ها میشن
print(df.loc[2, "logP"])
print(df.loc[df["logP"] < 3 , ["compound" , "MW"]])
#بر اساس جایگاه عددی انتخاب کنiloc فقط عدد باشه
print(df.iloc[2])
print(df.iloc[2, 3])
print(df.loc[2, "logP"])
print(df.iloc[2, 2])
#تغییر دادن
df.loc[2, "logP"] = 3.1
print(df)

df["High_logP"] = df["logP"] > 3
print(df[["compound", "logP", "High_logP"]])
df.loc[2, "HBA"] = 4
print(df)
df["Heavy_Molecule"] = df["MW"] > 250
print(df[["compound", "MW", "Heavy_Molecule"]])
df["Good_logP"] = df["logP"] < 3
print(df[["compound", "logP", "Good_logP"]])