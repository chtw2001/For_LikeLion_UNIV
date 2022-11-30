import sys
input = sys.stdin.readline

n, m = map(int, input().split())
list1 = list(map(int, input().split()))

res = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if list1[i] + list1[j] + list1[k] <= m:
                res.append(list1[i] + list1[j] + list1[k])

print(max(res))            