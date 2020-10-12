def next(number):
    if number %2 == 0:
        return number/2
    else:
        return number*3 + 1

def chainLength(number):
    count = 1
    currentVal = number
    while currentVal > 1:
        currentVal = next(currentVal)
        count += 1
    return count

maxNumber = 0
maxLength = 0

for x in range(1000000, 1, -1):
    length = chainLength(x)
    if length > maxLength:
        maxLength = length
        maxNumber = x

print(maxNumber, " ", maxLength)