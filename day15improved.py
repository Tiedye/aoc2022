from pre import *

sensors, beacons = zip(*(((sx, sy, abs(sx-bx) + abs(sy-by)), (bx,by)) for sx, sy, bx, by in map(ints, open('day15s.txt'))))
beacons = set(beacons)

def row_markers(y):
    xs, ds = zip(*sorted(chain(
        flatten(
            ((x - (r - d), 1), (x + (r - d) + 1, -1))
            for x, d, r
            in ((sx, abs(y-sy), r) for sx, sy, r in sensors)
            if d <= r
        ),
        ((bx, 0) for bx, by in beacons if by == y)
    )))
    return zip(chain((0,), (abs(a - b) for a, b in pairwise(xs))), ds)


# c = 0
# s = 0
# for d, t in row_markers(2000000):
#     if c:
#         s += d
#         if not t:
#             s -=1
#     c += t
# print(s)

diag_markers = sorted(flatten(product(((sx+sy-r, 1), (sx+sy+r, -1)), ((sx-sy-r, sx-sy+r),)) for sx, sy, r in sensors))

print(list(row_markers(10)))
print(len(sensors), len(diag_markers))
print(*diag_markers, sep='\n')

def find_index(l, value, key=None):
    a, b = 0, len(l)
    key = key if key else lambda x: x
    value = key(value)
    while a < b:
        c = (a + b) // 2
        cmp = key(l[c])
        if cmp == value:
            return c
        elif cmp < value:
            a = c + 1
        else:
            b = c - 1

s = []
for (d, op), (ol, ou) in diag_markers:
    
    insort(s, (ol, op))
