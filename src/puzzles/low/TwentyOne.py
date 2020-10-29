def sum_of_proper_divisors(number):
    sum = 1
    for x in range(2, (int)(number/2 + 1)):
        if number%x == 0:
            sum += x
    return sum

A = [ 0 for i in range( 0, 10000 ) ]

for num in range(1, 10001):
    A[num - 1] = sum_of_proper_divisors(num)

finalTotal = 0
for y in range(0, 10000):
    if 10000 > A[y] - 1 != y and y + 1 == A[A[y] - 1]:
        finalTotal += A[y]

print(finalTotal)


