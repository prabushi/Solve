def reverse(string):
    string = string[::-1]
    return string

max = 0
for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        val = x * y
        if str(val) == reverse(str(val)) and max < val:
            max = val
            break

print(max)