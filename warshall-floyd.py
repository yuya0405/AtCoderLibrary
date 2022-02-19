INF = float('inf')
cost = [[INF]*V for _ in range(V)]
for v in range(V):
    cost[v][v] = 0
for s, t, d in STD:
    cost[s][t] = d

for i in range(V): # 中継点
    for j in range(V): # 始点
        for k in range(V): # 終点
            cost[j][k] = min(cost[j][i]+cost[i][k], cost[j][k])
