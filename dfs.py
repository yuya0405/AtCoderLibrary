# 自作関数
def dfs(node):
    if visited[node]:
        return
    visited[node] = 1
 
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
    return

# アルゴ式

# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10 ** 6)

# 頂点 v を根とする部分木を探索
# 頂点 v の子頂点を格納した配列を chs とする
def rec(v, p):
    if v == 0:
        depth[v] = 0
    else:
        depth[v] = depth[p] + 1

    # 各子頂点を探索
    for ch in chs[v]:
        # 子頂点 ch を根とした部分木を再帰的に探索
        rec(ch, v)

# 各頂点の子頂点リストを作る
chs = [[] for v in range(N)]
for v in range(1, N):
    # 頂点 v の親
    p = P[v - 1]

    # 親 p の子頂点リストに頂点 v を挿入
    chs[p].append(v)

depth = [0] * N

# 根頂点 (0) から再帰的に探索
rec(0, -1)

for d in depth:
    print (d)
