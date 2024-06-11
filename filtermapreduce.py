from functools import reduce

def add_ab(a, b):
    return a + b

nums = [2, 4, 8, 6, 8, 4, 5, 9, 7]

evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

doubles = list(map(lambda n: n + 2, evens))
print(doubles)

sum1 = reduce(lambda a, b: a + b, doubles)
print(sum1)
