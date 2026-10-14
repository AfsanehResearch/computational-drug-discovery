print("You are in a freeway")

speed = float(input("Speed: "))

if speed < 300 and speed > 150:
    print("You are a good driver")
elif speed <150 and speed >= 100:
    print("Hey turtle")
else:
    print("are you Crazy?")
is_freeway = speed >300
print(is_freeway)
