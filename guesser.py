import random

def right_digits()

def generator():
    list = [str(i) for i in range(10)]
    random.shuffle(list)
    return list[:4]