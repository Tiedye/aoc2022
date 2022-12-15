from pre import *

instructions = [line.strip().split() for line in open('day10.txt')]

checks = tuple(range(20,221,40))

c = 0
X = 1
s = 0
for i in instructions:
    c += 1
    if c in checks:
        s += c*X
    match i:
        case "addx", n:
            c+=1
            if c in checks:
                s += c*X
            X += int(n)

print(s)

X = 1
r = []
for i in instructions:
    r += '#' if abs(X - len(r) % 40) <= 1 else ' '
    match i:
        case "addx", n:
            r += '#' if abs(X - len(r) % 40) <= 1 else ' '
            X += int(n)

print(*(''.join(l) for l in batched(r, 40)), sep='\n')
