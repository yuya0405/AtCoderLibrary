from collections import deque

## 入力の受け取り
n, k = map(int, input().split())
a = [int(input()) for i in range(n)]

q = deque()
for c in a:
    q.append(c)  ## dequeの右端に要素を一つ追加する。
    (追加した要素に応じて何らかの処理を行う)

    while q and (満たすべき条件の否定):
        rm = q.popleft() ## 条件を満たさないのでdequeの左端から要素を取り除く
        (取り除いた要素に応じて何らかの処理を行う)

    (何らかの処理を行う。whileがbreakしたので、dequeに入っている連続部分列は条件を満たしている。特に右端の要素から左に延ばせる最大の長さになっている。)
