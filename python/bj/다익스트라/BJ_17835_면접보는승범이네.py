import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

INF = sys.maxsize
def dijkstra(start):
    q = [(0, start)]
    dist = [INF] * (N + 1)
    dist[start] = 0
    
    while q:
        cur_cost, cur = heappop(q)
        
        if dist[cur] < cur_cost:    
            continue
        
        for next, next_cost in graph[cur]:
            cost = cur_cost + next_cost
            if cost < dist[next]:
                dist[next] = cost
                heappush(q, (cost, next))
    return sorted(dist[meeting] for meeting in meetings)[0]

N, M, K = map(int, input().split())
# 그래프 초기화
graph = {i: [] for i in range(1, N+1)}

# 간선 초기화
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
meetings = list(map(int, input().split()))
result = sorted([(dijkstra(i), i) for i in range(1, N+1)], key=lambda x: (-x[0], x[1]))[0]

print(result[1], result[0], sep="\n")