from pre import *

@dataclass
class Item:
    worry: int

@dataclass
class Monkey:
    items: List[Item]
    op: Any
    a: int | None
    t: int
    dt: int
    df: int
    count: int = 0


input_monkeys: List[Monkey] = []

mod = 1

for m in batched((line.strip().split() for line in open('day11.txt')), 7):
    items = [Item(int(i.strip(','))) for i in m[1][2:]]
    t = int(m[3][3])
    mod *= t
    dt = int(m[4][5])
    df = int(m[5][5])

    op = operator.mul if m[2][4] == '*' else operator.add
    a = int(m[2][5]) if m[2][5] != 'old' else None

    input_monkeys.append(Monkey(items, op, a, t, dt, df))

ms = deepcopy(input_monkeys)

for _ in range(20):
    for m in ms:
        for i in m.items:
            if m.a:
                i.worry = m.op(m.a, i.worry)
            else:
                i.worry = m.op(i.worry, i.worry)
            i.worry //= 3
            if i.worry % m.t == 0:
                ms[m.dt].items.append(i)
            else:
                ms[m.df].items.append(i)
        m.count += len(m.items)
        m.items = []

print(reduce(operator.mul, sorted(m.count for m in ms)[-2:]))
    
ms = deepcopy(input_monkeys)

for _ in range(10000):
    for m in ms:
        for i in m.items:
            if m.a:
                i.worry = m.op(m.a, i.worry)
            else:
                i.worry = m.op(i.worry, i.worry)
            i.worry %= mod
            if i.worry % m.t == 0:
                ms[m.dt].items.append(i)
            else:
                ms[m.df].items.append(i)
        m.count += len(m.items)
        m.items = []

print(reduce(operator.mul, sorted(m.count for m in ms)[-2:]))
    