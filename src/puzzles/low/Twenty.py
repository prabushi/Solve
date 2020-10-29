multipliedSum = 1
for num in range(2, 101):
    multipliedSum *= num

sum = 0
string = str(multipliedSum)
for i in range(0, len(string)):
    sum += int(string[i])

print(sum)