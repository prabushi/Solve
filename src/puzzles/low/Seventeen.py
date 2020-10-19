single = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

double = {
    '00': ' ',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety'
}

other = {
    '100' : 'hundred',
    '1000': 'one thousand'
}

def getCharaterCount(string):
    tot = 0
    stringArray = string.split()
    for i in range(0, len(stringArray)):
        tot += len(stringArray[i])
    return tot

total = 0

for i in range(1, 1001):
    string = str(i)
    currentLength = 0
    length = len(string)
    if length == 4:
        currentLength = getCharaterCount(other[string])
    elif length == 3:
        first = single[string[0]] + 'hundred'
        lastTwoNumbers = string[1] + string[2]
        if lastTwoNumbers != '00':
            first += ' and'
            second = ''
            if double.has_key(lastTwoNumbers):
                second = double[lastTwoNumbers]
            elif string[1] == '0':
                second = single[string[2]]
            else:
                second = double[string[1] + str(0)] + single[string[2]]
            currentLength = getCharaterCount(first + second)
        else:
            currentLength = getCharaterCount(first)
    elif length == 2:
        if double.has_key(string):
            currentLength = getCharaterCount(double[string])
        else:
            number = double[string[0] + str(0)] + single[string[1]]
            currentLength = getCharaterCount(number)
    else:
        currentLength = getCharaterCount(single[string])

    total += currentLength

print(total)




