def triangleNumber(num):
    sum = 1
    for x in range(2, num + 1):
        sum += x
    return sum

def countDivisors(num):
    count = 1
    for y in range(2, num):
        if num % y == 0:
            count += 1
    return count

divisors = 5
number = 7
while divisors < 500 :
    number += 1
    divisors = countDivisors(triangleNumber(number))
    print('number: ', number, ' divisors: ', divisors)

print(triangleNumber(number))
