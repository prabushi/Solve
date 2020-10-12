import math

number = 600851475143

def check(n):
    if n == 1:
        return False

    for x in range(2, (int)(math.sqrt(n))):
        if n % x == 0:
            return False
    return True

x = math.floor(math.sqrt(number))

while number % x != 0 or (number % x == 0 and not(check(x))):
    x -= 1

print(x)


