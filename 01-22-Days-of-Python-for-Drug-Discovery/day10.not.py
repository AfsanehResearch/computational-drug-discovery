is_basic = True
print(not is_basic)


pH = float(input("Enter pH: "))
is_acidic = pH < 7
if not is_acidic:
    print("Basic or Neutral")
