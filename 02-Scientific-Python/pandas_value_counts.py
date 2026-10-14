import pandas as pd
data = {"Molecule": ["A", "B", "C", "D", "E"],
         "Class": ["Drug", "Drug", "Lead", "Lead","Drug"],
         "Target":["A", "B", "A", "A", "B"],
         "MW": [180, 250, 210, 310, 275],
         "logP": [1.2, 2.1, 2.8, 3.1, 1.7]}
df = pd.DataFrame(data)
#value_counts() , count() متفاوتند
#count()چند مقدار موجود داریم
#value_count() هر مقدار چندبار تکرار شده
print(df["Class"].count())
print(df["Class"].value_counts())
#normalize=True یک قابلیت جالب که به جای تعداد نسبت می دهد
print(df["Class"].value_counts(normalize = True))
#اگر بخواهیم درصد بگیریم:
print(df["Class"].value_counts(normalize = True)*100)