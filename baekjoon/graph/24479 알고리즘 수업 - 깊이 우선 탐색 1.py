import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split()) # 정점 수, 간선 수, 시작 정점
graph = [[] for _ in range(n+1)] # 정점개수 + 1개의 빈 배열 생성, 0번째는 사용 X
visited = [0] * (n+1) # 방문 순서 저장, 0번째는 사용 X
ans = [0] * (n+1)
ans_idx = 1

# 그래프 간선 갯수 이용해 그래프 정점 간 연결정리
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름 차순 정렬
for i in range(1,n+1):
    graph[i].sort()

# dfs 함수
def dfs(graph, i, visited):
    global ans_idx
    visited[i] = 1
    ans[i] = ans_idx
    ans_idx += 1
    for j in graph[i]:
        if visited[j] == 0:
            dfs(graph, j, visited)

dfs(graph, r, visited)

for nn in ans[1:]:
    print(nn)
