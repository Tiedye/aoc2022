from pre import *

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    if isinstance(left, int):
        return compare([left], right)
    if isinstance(right, int):
        return compare(left, [right])
    for l, r in zip_longest(left, right):
        if l is None:
            return -1
        if r is None:
            return 1
        if v := compare(l, r):
            return v


packets = [eval(line) for line in open("day13.txt") if line.strip()]

print(sum(i for i, (left, right) in zip(count(1), batched(packets, 2)) if compare(left, right) < 0))

m1 = [[2]]
m2 = [[6]]
sorted_packets = sorted(chain(packets, [m1, m2]), key=cmp_to_key(compare))
print((sorted_packets.index(m1) + 1) * (sorted_packets.index(m2) + 1))
