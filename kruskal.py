def kruskal():
    uf = UnionFind(V)
    
    edges = []
    for s, t, w in STW:
        edges.append((w, s, t))

    edges.sort()
    
    cost = 0
    
    for edge in edges:
        w, s, t = edge
        if not uf.same(s, t):
            cost += w # 重みを足し
            uf.union(s, t) # 頂点同士をつなげる
    
    return cost

ans = kruskal()
print (ans)
