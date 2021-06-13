def dfs(node: int):
    if visited[node]:
        return
    visited[node] = 1
 
    for n_node in graph[node]:
        if not visited[n_node]:
            dfs(n_node)
    return
