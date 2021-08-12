import random

def comparator(c_digit, u_digit):
    d = 0
    for i in range(len(u_digit)):
        if u_digit[i] in c_digit:
            d += 1
    return d

def right_digits(digit):
    i = 0
    digits = [str(i) for i in range(10)]
    right_number = None
    while i != 4:
        random.shuffle(digits)
        right_number = digits[:4]
        i = comparator(digit, right_number)
    return right_number

def generator():
    list = [str(i) for i in range(10)]
    random.shuffle(list)
    return list[:4]

def guesser():
    digit = generator()
    print(right_digits(digit))
    print(digit)