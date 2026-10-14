numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
print("=== finished ===")
weights= [45, 120, 180, 250, 310]
small = filter(lambda x: x < 200, weights)
print(list(small))
print(" === finished ===")

numbers = [3, 8, 11, 14, 17, 20]
result = filter(lambda x: x > 10, numbers)
print(list(result))