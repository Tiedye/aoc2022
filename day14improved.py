from pre import *

np.set_printoptions(threshold=1000000)

rocks = [[tuple(int(c) for c in pair.split(',')) for pair in line.strip().split(' -> ')] for line in open('day14.txt')]

start = (500,0)

minx, miny = np.array(list(map(np.array, flatten(rocks)))).min(axis=0)
maxx, maxy = np.array(list(map(np.array, flatten(rocks)))).max(axis=0)

grid = np.full((maxx + maxy + 2, maxy + 2), False)

for rock in rocks:
    for current, end in pairwise(rock):
        current = np.array(current)
        grid[tuple(current)] = True
        while (current != end).any():
            current += np.clip(end - current, -1, 1)
            grid[tuple(current)] = True

dirs = [
    np.array([0, 1]),
    np.array([-1, 1]),
    np.array([1, 1]),
]

def p1():
    filled = grid.copy()
    sum = 0
    def check(loc):
        nonlocal sum
        try:
            if all(check(c) for c in (tuple(loc + d) for d in dirs) if not filled[c]):
                sum += 1
                filled[loc] = True
                return True
            return False
        except IndexError:
            return False
    check(start)
    return sum

def p2():
    sand = np.full((maxx + maxy + 2, maxy + 2), False)

    sand[start] = True
    for y in range(1, sand.shape[1]):
        sand[:, y] = np.logical_and(np.convolve(sand[:, y - 1], [1,1,1], mode='same'), np.logical_not(grid[:,y]))

    return sum(sum(sand))

print(p1())
print(p2())