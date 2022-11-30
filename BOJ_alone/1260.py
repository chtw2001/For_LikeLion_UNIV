from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
room = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a ,b = map(int, input().split())
    room[a][b] = room[b][a] = 1

visit_dfs = [0]*(n+1)
visit_bfs = [0]*(n+1)

def DFS(v):
    visit_dfs[v] = 1
    print(v, end=' ')
    for i in range(1,n+1):
        if visit_dfs[i] == 0 and room[v][i] == 1:
            DFS(i)

def BFS(v):
    visit_bfs[v] = 1
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1,n+1):
            if visit_bfs[i] == 0 and room[v][i] == 1:
                q.append(i)
                visit_bfs[i] = 1

DFS(v)
print()
BFS(v)