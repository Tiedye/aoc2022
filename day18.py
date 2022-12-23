from pre import *

coords = np.array([list(i + 1 for i in ints(line)) for line in open('day18.txt')])

size = np.max(coords, axis=0) + 2

cells = np.full(size, False)

for c in coords:
    cells[tuple(c)] = True

dirs = [
    np.array([0,1,0]),
    np.array([0,-1,0]),
    np.array([1,0,0]),
    np.array([-1,0,0]),
    np.array([0,0,1]),
    np.array([0,0,-1]),
]

def calc_sa():
    sa = 0
    for c in coords:
        sides = 6
        for a in (tuple(c+d) for d in dirs):
            if cells[a]:
                sides -= 1
        sa += sides
    return sa

print(calc_sa())

acells = np.full(size, False)

z = np.zeros((3))

stack = [(0,0,0)]

while stack:
    p = stack.pop()
    if (p < z).any() or (p >= size).any():
        continue
    if acells[p] or cells[p]:
        continue
    acells[p] = True
    for a in (tuple(p+d) for d in dirs):
        stack.append(a)

cells = np.bitwise_not(acells)

print(calc_sa())
