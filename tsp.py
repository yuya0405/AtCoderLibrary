INF = float('inf')
edges = [[INF]*V for _ in range(V)]

for s, t, d in STD:
    edges[s][t] = d

#Dpは全体集合の部分集合Sについて最後がvであるという制約の下で順序を最適化したときのSの中での最小コスト
dp = [[INF]*V for _ in range(2**V)]
dp[0][0] = 0

#集合（訪れたか訪れていないかを表す二進数）
for x in range(2**V):
    #最後に訪れたノード
    for y in range(V):
        #最後に訪れた以外のノード
        for z in range(V):
            #1.すでに訪れたかどうか 2.最後に訪れたノードではないか 3. yとzはそもそもつながっているのか
            if ((x >> y) & 1) and y != z and edges[z][y] < 10**6:
                dp[x][y] = min(dp[x][y], dp[x^(1<<y)][z]+edges[z][y])

if dp[-1][0] > 10**6:
    print(-1)
else:
    print(dp[-1][0])
