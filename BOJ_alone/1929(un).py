def square(n):
	return int(n ** 0.5) ** 2 == n
n = sorted(map(int, input().split()))
for i in range(n[0],n[-1]+1):
    cnt = 0
    if i == 1:
        continue
    if square(i):
        continue
    for k in range(2,i):
        if i % k == 0:
            cnt = 1
            break
    if cnt == 0:
        print(i)