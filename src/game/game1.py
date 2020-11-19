for a in range(1, 10000):
    for b in range(1, 10000):
        for c in range(1, 10000):
            aa = int(str(a) + str(a))
            bbcc = int(str(b) + str(b) + str(c) + str(c))
            if aa * aa == bbcc:
                print(a, '-', b, '-', c)
                break

print("end")
