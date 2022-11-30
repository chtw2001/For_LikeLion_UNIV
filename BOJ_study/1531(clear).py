N, M = map(int, input().split())
count = 0
xy = [[0 for _ in range(100)] for _ in range(100)]
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1,x2+1):
        for k in range(y1,y2+1):
            xy[j-1][k-1] += 1
for i in range(100):
    for k in range(100):
        if xy[i][k] > M:
            count += 1
print(count)