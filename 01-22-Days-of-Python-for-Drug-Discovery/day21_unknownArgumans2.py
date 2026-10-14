def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(add(10,20))
print(add(10,20,30,40))
print(add(1,2,3,4,5,6,7))
