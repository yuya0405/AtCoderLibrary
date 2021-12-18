#自作関数
def bfs(node):
    queue = deque([node])
    d = [None] * n # uからの距離の初期化
    d[node] = 0 # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d

#アルゴ式
# 最初の頂点集合 (スタートは頂点 0 のみ)
nodes = [0]

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * N

# todo リストを表すキュー
que = Queue()

# 頂点 0 を始点とする
dist[0] = 0
que.put(0)

# キューが空になるまで探索する
while not que.empty():
    # キューから頂点を取り出す
    v = que.get()

    # 頂点 v から 1 手で行ける頂点 next_v を探索
    for next_v in G[v]:
        # 頂点 next_v が探索済みであれば何もしない
        if dist[next_v] != -1:
            continue

        # 頂点 next_v を探索する
        dist[next_v] = dist[v] + 1
        que.put(next_v)
