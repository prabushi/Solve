for a in range(0, 1000):
    for b in range(a, 1000):
        for c in range(max(a,b), 1000):
            if (a + b + c == 1000 and a*a + b*b == c*c):
                print(a*b*c)