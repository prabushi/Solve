rows = 100
A = [ [ 0 for y in range( 0, rows ) ]
      for x in range( 0, rows ) ]

file = open('p067_triangle.txt', 'r')
lines = file.readlines()

count = 0
for line in lines:
    stringArray = line.split()
    for i in range(0, len(stringArray)):
        A[count][i] = int(stringArray[i])
    count += 1

for i in range(rows - 2, -1, -1):
    for j in range(0, i + 1):
        one = A[i][j] + A[i + 1][j]
        two = A[i][j] + A[i + 1][j + 1]
        A[i][j] = max(one, two)

print(A[0][0])