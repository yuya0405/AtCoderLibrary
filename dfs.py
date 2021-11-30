def dfs(node):
    if visited[node]:
        return
    visited[node] = 1
 
    for n_node in graph[node]:
        if not visited[n_node]:
            dfs(n_node)
    return

# アルゴ式
# 頂点 v を根とする部分木を探索
# 頂点 v の子頂点を格納した配列を chs とする
def rec(v):
    # 頂点 v を出力
    print(v)

    # 各子頂点を探索
    for ch in chs:
        # 子頂点 ch を根とした部分木を再帰的に探索
        rec(ch)
