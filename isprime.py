import math

def is_prime(y):
    if y <= 1:
        return False
    elif y <= 3:
        return True
    elif y % 2 == 0 or y % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(y)) + 1, 6):
        if y % i == 0 or y % (i + 2) == 0:
            return False
    return True