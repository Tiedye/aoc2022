from pre import *

sensors, beacons = zip(*(((sx, sy, abs(sx-bx) + abs(sy-by)), (bx,by)) for sx, sy, bx, by in map(ints, open('day15.txt'))))
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
    return xs[0]-1, zip(chain((1,), (abs(a - b) for a, b in pairwise(xs))), ds)


c = 0
s = 0
for d, t in row_markers(2000000)[1]:
    if c:
        s += d
        if not t:
            s -=1
    c += t
print(s)

p = None
for y in range(4000001):
    if y % 40000 == 0:
        print(y*100//4000000, end='\r')
    x, markers = row_markers(y)
    c = 0
    for d, t in markers:
        if d and not c and 0 <= x <= 4000000:
                p = x*4000000 + y
        x += d
        c += t
print(p)