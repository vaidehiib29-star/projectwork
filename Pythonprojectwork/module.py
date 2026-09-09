celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda x: x * 9/5 + 32, celsius))
print(fahrenheit)

#2.filter() + sorted()
numbers = [12, 5, 8, 23, 16, 4, 42, 7]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(sorted(even, reverse = True))

#3. reduce() -max

numbers = [12, 5, 8, 23, 16, 4, 42, 7]
maximum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
print("Maximum numbers:", maximum)

#with using reduce
from functools import reduce
numbers = [12, 5, 8, 23, 16, 4, 42, 7]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)


