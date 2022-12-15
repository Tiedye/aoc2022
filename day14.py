from pre import *

np.set_printoptions(threshold=1000000)

rocks = [[tuple(int(c) for c in pair.split(',')) for pair in line.strip().split(' -> ')] for line in open('day14.txt')]

start = (500,0)

minx, miny = np.array(list(map(np.array, flatten(rocks)))).min(axis=0)
maxx, maxy = np.array(list(map(np.array, flatten(rocks)))).max(axis=0)

grid = np.full((maxx + maxy + 2, maxy + 3), False)

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

def do(grid):
    total = 0
    while True:
        loc = start
        while True:
            try:
                loc = next(c for c in (tuple(loc + d) for d in dirs) if not grid[c])
            except StopIteration:
                if loc == start:
                    total += 1
                    return total
                break
            except IndexError:
                return total
        total += 1
        grid[loc] = True

print(do(grid.copy()))
# grid2 = grid.copy()
# grid2[:, maxy+2] = True
# print(do(grid2))
