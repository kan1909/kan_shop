import random


def random_String(length=7):
    generator = [str(i) for i in range(1, 10)]
    return ''.join(random.choice(generator) for i in range(length))
