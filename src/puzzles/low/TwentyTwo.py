file = open('p022_names.txt', 'r')
strings = file.read().split(',')
length = len(strings)

letters = { 'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14,
           'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26 }

A = [ 0 for i in range( 0, length ) ]
for k in range(0, length):
    A[k] = strings[k][1 : len(strings[k]) - 1]

A.sort()

def value_of_string(string):
    sum = 0
    for x in range(0, len(string)):
        sum += letters[string[x]]
    return sum

total = 0
for i in range(0, length):
    total += value_of_string(A[i]) * (i + 1)

print(total)