# プリム法

from heapq import heappush, heappop

def prim():
    # プリム法
    # 頂点がマークされているか確認する配列
    marked = [False for _ in range(V)]

    # マークされている頂点数を数える
    marked_cnt = 0

    # はじめに0頂点をマーク
    marked[0] = True
    marked_cnt += 1

    # heap
    q = []

    # 頂点0に隣接する辺を保存
    for j, c in G[0]:
        heappush(q, (c, j))

    total = 0

    # すべての頂点をマークするまでwhileループ
    while marked_cnt < V:
        # 最小の重みの辺をheapで取り出す
        c, i = heappop(q)

        # マークされているならスキップ
        if marked[i]:
            continue

        # 頂点をマーク
        marked[i] = True
        marked_cnt += 1

        total += c

        # 頂点iに隣接する辺を保存
        for j, c in G[i]:
            # マークされていればスキップ
            if marked[j]:
                continue

            heappush(q, (c, j))
    return total

G = [[] for _ in range(V)]
for s, t, w in STW:
    G[s].append((t, w)) 
    G[t].append((s, w))

total = prim()
print (total)
