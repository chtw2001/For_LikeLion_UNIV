n = int(input())
a = []
for i in range(n):
    a.append(input().split())
for i in range(n):
    print(int(a[i][0])+int(a[i][1]))