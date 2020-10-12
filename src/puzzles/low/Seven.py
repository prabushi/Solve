import math

def check(n):
    if n == 1:
        return False

    for x in range(2, (int)(math.sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True

count = 0
value = 2
while count != 10001:
    if check(value):
        count += 1
    value += 1

print(value - 1)
