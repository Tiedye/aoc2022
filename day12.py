from pre import *

grid = np.array([[ord(c) for c in line.strip()] for line in open('day12.txt')])
shape = np.array(grid.shape)

start = next(zip(*np.where(grid == ord('S'))))
end = next(zip(*np.where(grid == ord('E'))))

grid[start] = ord('a')
grid[end] = ord('z')

grid -= ord('a')

dirs = [
    np.array([1,0]),
    np.array([-1,0]),
    np.array([0,1]),
    np.array([0,-1]),
]

queue = deque([(0, end)])

visited = {end}

ground_found = False

while True:
    dist, l = queue.popleft()
    h = grid[l]
    if not ground_found and h == 0:
        print('p2:', dist)
        ground_found = True
    if l == start:
        print('p1:', dist)
        break
    for dl in (tuple(l + d) for d in dirs):
        if dl in visited:
            continue
        if (dl < np.zeros(2)).any() or (dl >= shape).any():
            continue
        dh = grid[dl]
        if h - 1 > dh:
            continue
        visited.add(dl)
        queue.append((dist+1, dl))
