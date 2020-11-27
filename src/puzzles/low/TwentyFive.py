limit = 10000
A = [ -1 for i in range( 0, limit) ]

def n_fibonacci(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        n1 = n - 1
        n2 = n - 2
        if n1 < limit:
            fn1 = A[n1]
        else:
            fn1 = -1
        if n2 < limit:
            fn2 = A[n2]
        else:
            fn2 = -1

        if fn1 == -1:
            fn1 = n_fibonacci(n-1)
        if fn2 == -1:
            fn2 = n_fibonacci(n-2)
        return fn1 + fn2

length = 0
count = 3
value = 0
while length < 1000:
    value = n_fibonacci(count)
    if count < limit:
        A[count] = value
    length = len(str(value))
    count += 1

print(count - 1)
