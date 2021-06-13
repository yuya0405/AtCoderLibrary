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
