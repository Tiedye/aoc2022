from pre import *

raw_wind = open('day17.txt').readline().strip()
wind_cycle = len(raw_wind)
wind = cycle(raw_wind)

bw = 7

board = np.zeros((3*5000, bw), dtype=int)

tiles = [
    np.array([
        [1,1,1,1],
    ], dtype=int),
    np.array([
        [0,3,0],
        [3,3,3],
        [0,3,0],
    ], dtype=int),
    np.array([
        [5,5,5],
        [0,0,5],
        [0,0,5],
    ], dtype=int),
    np.array([
        [7],
        [7],
        [7],
        [7],
    ], dtype=int),
    np.array([
        [9,9],
        [9,9],
    ], dtype=int),
]

tops = [0]
wind_i = 0
top = 0
cycles = []
for r, tile in zip(count(), cycle(tiles)):
    y = top + 3
    x = 2
    h, w = tile.shape
    while True:
        nx = x - 1 if next(wind) == '<' else x + 1
        if wind_i == 0:
            cycles.append(r)
        wind_i = (wind_i + 1) % wind_cycle
        if 0 <= nx <= bw - w and not (board[y:y+h, nx:nx+w] & tile).any():
            x = nx
        ny = y - 1
        if ny < 0 or (board[ny:ny+h, x:x+w] & tile).any():
            board[y:y+h, x:x+w] += tile
            top = max(top, y+h)
            tops.append(top)
            break
        y = ny
    if len(cycles) == 3:
        break

m = {
    0: '.',
    1: '-',
    3: '+',
    5: 'L',
    7: '|',
    9: '#',
}

print(tops[2022])
print(cycles)

cycle_len = cycles[2] - cycles[1]
cycle_hight = tops[cycles[2]] - tops[cycles[1]]

remaining = 1000000000000 - cycles[1]

cycle_count = remaining // cycle_len
remaining_rocks = remaining % cycle_len

cycles_height = cycle_count * cycle_hight

remaining_height = tops[cycles[1] + remaining_rocks] - tops[cycles[1]]

print(tops[cycles[1]] + cycles_height + remaining_height)
