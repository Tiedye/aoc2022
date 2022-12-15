from pre import *

lines = open('day8.txt').readlines()

rows = len(lines)
cols = len(lines[1].strip())

grid = tuple(int(c) for line in lines for c in line.strip())

left_visible = list(False for i in grid)
right_visible = list(False for i in grid)
top_visible = list(False for i in grid)
bottom_visible = list(False for i in grid)

for r in range(rows):
    h = -1
    for c in range(cols):
        p = c+cols*r
        if grid[p] > h:
            left_visible[p] = True
            h = grid[p]
    h = -1
    for c in range(cols):
        p = (cols - c - 1)+cols*r
        if grid[p] > h:
            right_visible[p] = True
            h = grid[p]

for c in range(cols):
    h = -1
    for r in range(rows):
        p = c+cols*r
        if grid[p] > h:
            top_visible[p] = True
            h = grid[p]
    h = -1
    for r in range(rows):
        p = c+cols*(rows - r - 1)
        if grid[p] > h:
            bottom_visible[p] = True
            h = grid[p]
    

print(len(list(filter(any, zip(left_visible, right_visible, top_visible, bottom_visible)))))


left_visible = list(0 for i in grid)
right_visible = list(0 for i in grid)
top_visible = list(0 for i in grid)
bottom_visible = list(0 for i in grid)

for r in range(rows):
    d = [0]*10
    for c in range(cols):
        p = c+cols*r
        h = grid[p]
        left_visible[p] = d[h]
        for i in range(10):
            if i <= h:
                d[i] = 1
            else:
                d[i] += 1
    d = [0]*10
    for c in range(cols):
        p = (cols - c - 1)+cols*r
        h = grid[p]
        right_visible[p] = d[h]
        for i in range(10):
            if i <= h:
                d[i] = 1
            else:
                d[i] += 1

for c in range(cols):
    d = [0]*10
    for r in range(rows):
        p = c+cols*r
        h = grid[p]
        top_visible[p] = d[h]
        for i in range(10):
            if i <= h:
                d[i] = 1
            else:
                d[i] += 1
    d = [0]*10
    for r in range(rows):
        p = c+cols*(rows - r - 1)
        h = grid[p]
        bottom_visible[p] = d[h]
        for i in range(10):
            if i <= h:
                d[i] = 1
            else:
                d[i] += 1

print(max(reduce(operator.mul, dirs) for dirs in zip(left_visible, right_visible, top_visible, bottom_visible)))