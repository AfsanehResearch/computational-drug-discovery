temperature = float(input("Temperature (°C): "))
if temperature <0:
    print("Frozen")
elif temperature <=37:
    print("Normal")
else:
    print("Hot")
