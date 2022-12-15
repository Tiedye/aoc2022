from pre import *

file = open('day6.txt')

line = file.readlines()[0].strip()

def do(n):
    groups = zip(*(islice(iter(line), i, None) for i in range(n)))

    for i, g in enumerate(groups):
        if len(set(g)) == n:
            print(i+n)
            break

do(4)
do(14)
