from pre import *

lines = open('day1.txt').readlines()

sums = list(sum(map(int, group)) for group in split('\n', lines))

print(max(sums))
print(sum(sorted(sums)[-3:]))