from pre import *

id_count = 0
@cache
def get_id(id):
    global id_count
    id_count += 1
    return id_count - 1

valves = {}
for line in open('day16.txt'):
    _, raw_id, _, _, raw_flow, _, _, _, _, *tunnels = line.strip().split(' ')
    flow, = ints(raw_flow)
    tunnels = [get_id(t.strip(',')) for t in tunnels]
    valves[get_id(raw_id)] = (flow, tunnels)

INF = 1000
ids = list(valves.keys())
_dm = {id: INF for id in valves}
ds = {id: _dm.copy() for id in valves}
for id, (flow, tunnels) in valves.items():
    for t in tunnels:
        ds[id][t] = 1

while True:
    updated = False
    for a, b, c in product(ids, repeat=3):
        if ds[a][b] + ds[b][c] < ds[a][c]:
            ds[a][c] = ds[a][b] + ds[b][c]
            updated = True
    if not updated:
        break

ds = {a: {b: d for b, d in dm.items() if valves[b][0]} for a, dm in ds.items() if valves[a][0] or a == get_id('AA')}

@cache
def rate(vs):
    return sum(f for id, (f, _) in valves.items() if 1 << id & vs)

mins = 30

states = [{(get_id('AA'), 0): 0}] + [{} for _ in range(mins)]

for i in range(mins):
    print(i, len(states[i]))
    for (v, vs), acc in states[i].items():
        r = rate(vs)
        has_next = False
        if not 1 << v & vs:
            has_next = True
            nvs = vs | 1 << v
            states[i+1][(v, nvs)] = max(acc+r, states[i+1].setdefault((v, nvs), 0))
        for t, d in ds[v].items():
            if not 1 << t & vs and i + d <= mins:
                has_next = True
                states[i+d][(t, vs)] = max(acc+r*d, states[i+d].setdefault((t, vs), 0))
        
        if not has_next:
            states[mins][(v, vs)] = max(acc+r*(mins-i), states[mins].setdefault((v, vs), 0))

print(max(states[mins].values()))

state = {(get_id('AA'), 0, get_id('AA'), 0, 0): 0}

def key(a, b):
    if a < b:
        return *a, *b
    return *b, *a

for i in range(26):
    print(i, len(state))
    next_state: dict[tuple[int, str, int, str, int], int] = {}
    for (a, ad, b, bd, vs), acc in state.items():
        r = rate(vs) + acc
        aos = []
        if not ad:
            if not 1 << a & vs and i:
                aos.append(a)
            else:
                for t, d in ds[a].items():
                    if not 1 << t & vs and t != b:
                        aos.append((t, d-1))
        if not aos:
            aos.append((a, ad-1))
        bos = []
        if not bd:
            if not 1 << b & vs and i:
                bos.append(b)
            else:
                for t, d in ds[b].items():
                    if not 1 << t & vs and t != a:
                        bos.append((t, d-1))
        if not bos:
            bos.append((b ,bd-1))
        
        for ao, bo in product(aos, bos):
            nvs = vs
            match ao:
                case int(c):
                    nvs = nvs | 1 << c
                    an = (a, ad)
                case p:
                    an = p
            match bo:
                case int(c):
                    nvs = nvs | 1 << c
                    bn = (b, bd)
                case p:
                    bn = p
            if bn[0] == an[0]:
                continue
            k = (*key(an, bn), nvs)
            next_state[k] = max(r, next_state.setdefault(k, 0))
    state = next_state

print(max(state.values()))