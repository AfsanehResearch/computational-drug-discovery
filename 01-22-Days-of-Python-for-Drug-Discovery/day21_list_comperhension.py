numbers = [1, 2, 3, 4, 5]

#with for
squares = []
for number in numbers:
    squares.append(number**2)
print(squares)
print(" === finished ===")
#List Comperhension
squares = [number ** 2 for number in numbers]
print(squares)
