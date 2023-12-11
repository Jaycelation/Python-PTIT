import random
from os import system
from time import sleep

def christmas_tree(height):
    colors = ['\033[1;31m', '\033[33m', '\033[1;32m']
    print('\n')
    for i in range(height):
        print(' ' * (height - i - 1), end='')
        for _ in range((2 * i) + 1):
            if random.random() < 0.1:
                color = random.choice(colors)
                print(color + '*', end='')
            else:
                print('\033[32m' + '*', end='')
        print()
    
    print(' ' * (height - 1) + 'mWm')
    print(' ' * (height - 1) + 'mWm')

    color = random.choice(colors)
    print(color + (' ' * 8) + 'Merry Christmas!')
    print(color + (' ' * 14) + '2023')
    print(color + (' ' * 7) + 'Ối dồi ôi')
while True:
    christmas_tree(16)
    sleep(0.5)
    system('clear')