import random

def comparator(c_digit, u_digit):
    d = d2 = 0
    for i in range(len(u_digit)):
        if c_digit.find(u_digit[i]) != -1:
            d += 1
        if c_digit[i] == u_digit[i]:
            d2 += 1
    return d, d2

def generator():
    list = [str(i) for i in range(10)]
    random.shuffle(list)
    return ''.join(list[:4])

stage_number = 0
j = 0
c_digit = generator()
while j != 4:
    u_digit = input("Try to guess four-digit number: ")
    if not u_digit.isdigit() or len(u_digit) != 4:
        print("You should type four-digit number!")
        continue
    i, j = comparator(c_digit, u_digit)
    print("You guessed "+str(i)+" digits")
    print(str(j)+" of them stand on right place!")
    stage_number += 1
print("You won!!!")
print("You needed "+str(stage_number)+" stages to do that")