numbers = [1,2,3,4,5]
squares = map(lambda x: x**2, numbers)
print(squares)
print(list(squares))

print(" === finished ===")

weights = [180.16,194.19, 46.07]
rounded = map(lambda x: round(x), weights)
print(list(rounded))

print(" === finished ===")

numbers = [2, 4, 6, 8]
result = map(lambda x: x*2, numbers)

print(list(result))