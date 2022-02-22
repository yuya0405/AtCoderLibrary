lim = 10**3+5
space = [[0] * lim for _ in range(lim)]

for lx, ly, rx, ry in LR:
    space[lx][ly] += 1
    space[rx][ry] += 1
    space[rx][ly] -= 1
    space[lx][ry] -= 1

for h in range(lim):
    for w in range(lim-1):
        space[h][w+1] += space[h][w]

for w in range(lim):
    for h in range(lim-1):
        space[h+1][w] += space[h][w]

ans = [0 for _ in range(N+1)]

for h in range(lim):
    for w in range(lim):
        ans[space[h][w]] += 1

for k in range(1, N+1):
    print (ans[k])
