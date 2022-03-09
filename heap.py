import heapq

que = P[0:K]
print(min(que))
heapq.heapify(que)
for k in range(K+1, N+1):
    minima = heapq.heappop(que)
    minima = max(minima, P[k-1])
    heapq.heappush(que, minima)
    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que,ans)
