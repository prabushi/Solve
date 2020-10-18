# https://researchideas.ca/wmt/c6b3.html#:~:text=In%20fact%2C%20the%20order%20of,five%20right%2C%20five%20down).&text=There%20are%20252%20unique%20paths.

number = 21

A = [ [ 0 for y in range( 0, number ) ]
        for x in range( 0, number ) ]

for i in range(0, number):
    for j in range(0, number):
        if (i == 0 or j == 0):
            A[i][j] = 1
        else:
            A[i][j] = A[i][j - 1] + A[i - 1][j]

print(A[20][20])