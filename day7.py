from pre import *

lines = open('day7.txt').readlines()

d = ()

files = {}

for line in lines:
    match line.strip().split(' '):
        case ['$', 'cd', '/']:
            d = ()
        case ['$', 'cd', '..']:
            d = d[:-1]
        case ['$', 'cd', dir]:
            d = (*d, dir)
        case ['$', 'ls']:
            pass
        case ['dir', _]:
            pass
        case [size, name]:
            files[(*d, name)] = int(size)


dir_sizes = {}

for name, size in files.items():
    dirs = accumulate(chain([()], name[:-1]), lambda a, c: (*a, c))
    for dir in dirs:
        dir_sizes[dir] = dir_sizes.setdefault(dir, 0) + size

print(sum(v for v in dir_sizes.values() if v <= 100000))

ss = sorted(dir_sizes.values())

avail = 70000000 - dir_sizes[()]
req = 30000000 - avail

print(next(s for s in ss if s >= req))
