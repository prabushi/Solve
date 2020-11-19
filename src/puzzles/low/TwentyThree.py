limit = 28124

abundantList = []
finalSum = 0

def sum_of_proper_divisors(number):
    sum = 1
    for x in range(2, (int)(number/2 + 1)):
        if number%x == 0:
            sum += x
    return sum

def can_addup(value, total):
    for a in range(0, len(abundantList)):
        valueToAdd = abundantList[a]
        if total <= valueToAdd:
            return False
        if total == valueToAdd + value:
            return True
    return False

def can_write_with_abundants(num):
    for z in range(0, len(abundantList)):
        val = abundantList[z]
        if num <= val:
            return False
        if can_addup(val, num):
            return True
    return False


for y in range(12, limit):
    if (y < sum_of_proper_divisors(y)):
        abundantList.append(y)

for b in range(1, limit):
    if not(can_write_with_abundants(b)):
        finalSum = finalSum + b

print(finalSum)
