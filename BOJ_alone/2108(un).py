import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

# 산술평균
print(round(sum(a)/n))

# 중앙값
a = sorted(a)
print(a[n // 2])

# 최빈값
if n == 1:
    print(a[0])
else:
    cnt = 1
    max = 1
    counter = {}
    for i in range(1,n+1):
        counter[i] = []
    for i in range(1,n):
        if a[i-1] == a[i]:
            cnt += 1
        else:
            counter[cnt].append(a[i-1])
            if max < cnt:
                max = cnt
                cnt = 1
        if i == n - 1:
            counter[cnt].append(a[i])
            if max < cnt:
                max = cnt
    counter[max].sort()
    if len(counter[max]) == 1:
        print(counter[max][0])
    else:
        print(counter[max][1])

# 범위
if n == 1:
    print(0)
else:
    print(a[-1] - a[0])