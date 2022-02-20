# アルゴ式

# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10 ** 6)

# 頂点 v を根とする部分木を探索
# 頂点 v の子頂点を格納した配列を chs とする
def dfs(v, p):
    if v == 0:
        depth[v] = 0
    else:
        depth[v] = depth[p] + 1

    # 各子頂点を探索
    for ch in chs[v]:
        # 子頂点 ch を根とした部分木を再帰的に探索
        if ch != p:
            dfs(ch, v)

# 各頂点の子頂点リストを作る
chs = [[] for v in range(N)]
for v in range(1, N):
    # 頂点 v の親
    p = P[v - 1]

    # 親 p の子頂点リストに頂点 v を挿入
    chs[p].append(v)

depth = [0] * N

# 根頂点 (0) から再帰的に探索
dfs(0, -1)

for d in depth:
    print (d)
