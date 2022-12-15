from pre import *

dirs = {
    'R': np.array([1,0]),
    'L': np.array([-1,0]),
    'U': np.array([0,1]),
    'D': np.array([0,-1]),
}

instructions = [line.strip().split() for line in open('day9.txt')]

def do(l: int):
    knots = tuple(np.array([0,0]) for _ in range(l))

    visited = set()

    for dir, cnt in instructions:
        for _ in range(int(cnt)):
            h = knots[0]
            h += dirs[dir]
            for h, t in pairwise(knots):
                sd = h - t
                if (abs(sd) > 1).any():
                    t += np.clip(sd, -1, 1)
            visited.add(tuple(knots[-1]))

    return len(visited)

print(do(2))
print(do(10))