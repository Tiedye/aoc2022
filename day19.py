from pre import *

mins = 24

s = 0
for id, oco, cco, bco, bcc, gco, gcb in map(ints, open('day19.txt')):
    def f(ops, turns):
        q = deque(list(ops) + ['g', None])
        oc = np.array([oco,0,0,0])
        cc = np.array([cco,0,0,0])
        bc = np.array([bco,bcc,0,0])
        gc = np.array([gco,0,gcb,0])
        c = np.array([0,0,0,0])
        r = np.array([1,0,0,0])
        for i in range(turns):
            nc = c + r
            match q[0]:
                case 'o':
                    if (c >= oc).all():
                        r[0] += 1
                        nc -= oc
                        q.popleft()
                case 'c':
                    if (c >= cc).all():
                        r[1] += 1
                        nc -= cc
                        q.popleft()
                case 'b':
                    if (c >= bc).all():
                        r[2] += 1
                        nc -= bc
                        q.popleft()
                case 'g':
                    if (c >= gc).all():
                        r[3] += 1
                        nc -= gc
                        q.popleft()
            c = nc
        return tuple(c)

    print(f('cb', 27))
    break


    # states = [{(1,0,0,0,0,0,0): 0}] + [{} for _ in range(mins)]
    # for s1, s2 in pairwise(states):
        
