import random

def generator():
    list = [str(i) for i in range(10)]
    random.shuffle(list)
    return ''.join(list[:4])
print(generator())
