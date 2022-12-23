from pre import *

valves = {}
for line in open('day16.txt'):
    _, raw_id, _, _, raw_flow, _, _, _, _, *tunnels = line.strip().split(' ')
    flow, = ints(raw_flow)
    tunnels = [t.strip(',') for t in tunnels]
    valves[raw_id] = (flow, tunnels)

state = {'AA':{frozenset(): 0}}

@cache
def rate(vs):
    return sum(f for id, (f, _) in valves.items() if id in vs)

for i in range(30):
    print(i, sum(len(i) for i in state.values()))
    next_state: dict[str, dict[frozenset[str], int]] = {}
    for v in state.keys():
        for vs in state[v].keys():
            r = state[v][vs] + rate(vs)
            if v not in vs and valves[v][0]:
                nvs = vs | {v}
                next_state[v][nvs] = max(r, next_state.setdefault(v, {}).setdefault(nvs, 0))
            for t in valves[v][1]:
                # if t in next_state:
                #     if any(vs & svs == vs and c >= r for svs, c in next_state[t].items()):
                #         continue
                #     tod = []
                #     for suvs, c in next_state[t].items():
                #         if suvs & vs != suvs:
                #             continue
                #         if c <= r:
                #             tod.append(suvs)
                #     for suvs in tod:
                #         del next_state[t][suvs]
                next_state[t][vs] = max(r, next_state.setdefault(t, {}).setdefault(vs, 0))
    state = next_state

print(max(max(v.values()) for v in state.values()))