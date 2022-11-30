n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    ex = 0
    for j in range(i,n):
        ex += arr[j]
        if ex == k:
            break
        elif ex < k:
            continue
        else:
            cnt = ex - k
print(cnt)