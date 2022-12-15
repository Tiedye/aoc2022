from pre import *

# using Ilia's idea

X = 1
snaps = []
for line in open("day10.txt"):
    snaps.append(X)
    match line.strip().split():
        case "addx", n:
            snaps.append(X)
            X += int(n)

print(sum(snaps[c - 1] * c for c in range(20, 221, 40)))

for line in batched(snaps, 40):
    print(*("#" if abs(X - c) <= 1 else " " for c, X in zip(count(), line)), sep="")
