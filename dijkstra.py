from heapq import heappush, heappop
INF = 10 ** 9
def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist

# ノード数, エッジ数, 始点ノード
v, e, r = N+1, 2*N, 0

# ノード番号、ノード番号、辺重み
TMP = []
for i in range(1, N+1):
    TMP.append([0, i, T[i-1]])
for i in range(1, N):
    TMP.append([i, i+1, S[i-1]])
TMP.append([N, 1, S[N-1]])

# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
adj = [[] for _ in range(v)]
for tmp in TMP:
    s, t, d = tmp
    adj[s].append((t, d))

D = dijkstra(r, v)
for d in D[1:]:
    print (d)
