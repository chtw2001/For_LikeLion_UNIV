n, m = map(int, input().split())
line = []
for _ in range(m):
    a, b = map(int, input().split())
    line.append((a,b))
ft = {}
for i in range(n):
    
    visited = {}
    for a,b in line:
        if a == i:
            visited[a] = True
            visited[b] = True

    ft[i] = 