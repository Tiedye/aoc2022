from pre import *

lines = open('day5.txt').readlines()

def parse_move(move: str):
    _, rc, _, rf, _, rt = move.strip().split(' ')
    return int(rc), int(rf) - 1, int(rt) - 1

config = lines[:lines.index('\n')][:-1]
moves = list(map(parse_move, lines[lines.index('\n')+1:]))

init_stacks = [[i for i in reversed(stack) if i != " "] for stack in zip(*(line[1::4] for line in config))]

stacks = deepcopy(init_stacks)

for c, f, t in moves:
    stacks[t] += reversed(stacks[f][-c:])
    del stacks[f][-c:]

print("".join(s[-1] for s in stacks))

stacks = deepcopy(init_stacks)

for c, f, t in moves:
    stacks[t] += stacks[f][-c:]
    del stacks[f][-c:]

print("".join(s[-1] for s in stacks))
