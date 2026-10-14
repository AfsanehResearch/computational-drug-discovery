weights = [120.5, 180.2, 250.7, 310.1, 150.3]
between = [weight for weight in weights if 150 <= weight <= 200]
rounded = [round(weight) for weight in between]
minimum = min(rounded)
higher_even = [weight for weight in rounded if weight >  minimum and weight % 2 == 0]
print(minimum, higher_even)
print([minimum] + higher_even)
print(minimum, higher_even[0])
print((minimum, higher_even[0]))
print([minimum], higher_even)
print([[minimum]] + [higher_even])
print([minimum+ higher_even[0]])