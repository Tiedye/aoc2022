from pre import *

lines = open('day8.txt').readlines()

rows = len(lines)
cols = len(lines[1].strip())

grid = tuple(int(c) for line in lines for c in line.strip())

print(len(list(filter(any, ((reduce(max, ts, -1) < grid[p] for ts in (grid[r*cols:p], grid[p+1:(r+1)*cols], grid[c:p:cols], grid[p+cols::cols])) for r, c, p in ((r, c, r*cols+c) for r in range(rows) for c in range(cols)))))))

print(max(reduce(operator.mul, (min(len(list(takewhile(lambda t: t < grid[p], ts))) + 1, len(ts)) for ts in (grid[p-1:r*cols-1:-1], grid[p+1:(r+1)*cols], grid[p-cols::-cols], grid[p+cols::cols]))) for r,c,p in ((r, c, r*cols+c) for r in range(rows) for c in range(cols))))

