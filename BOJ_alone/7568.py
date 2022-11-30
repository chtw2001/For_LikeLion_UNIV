n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([x,y])
    print(x,y)
res = []
for i in range(n):
    rank = 1
    for k in range(n):
        if a[i][0] < a[k][0] and a[i][1] < a[k][1]:
            rank += 1
    res.append(rank)
for i in res:
    print(i,end=' ')