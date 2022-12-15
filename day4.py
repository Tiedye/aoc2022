lines = [[int(v) for pair in line.strip().split(',') for v in pair.split('-')] for line in open('day4.txt')]

print(sum(1 for al, ah, bl, bh in lines if al <= bl and bh <= ah or bl <= al and ah <= bh))

print(sum(1 for al, ah, bl, bh in lines if bl <= ah and al <= bh))
