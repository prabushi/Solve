globalMax = 0
expected = 0


def divide(num, mod, dividers):
    modulus = mod * 10 % num
    if not (modulus in dividers):
        dividers.add(modulus)
        if modulus == 0:
            return len(dividers)
        else:
            return divide(num, modulus, dividers)
    else:
        return len(dividers)


for i in range(2, 1000):
    result = divide(i, 1, set())
    print(i, ' : ', result)
    if globalMax < result:
        globalMax = result
        expected = i

print(expected)

