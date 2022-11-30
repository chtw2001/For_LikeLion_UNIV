n = int(input())
cnt = 0
res = []
a = n
if n % 3 == 0:
    res.append(n//3)
elif n % 5 == 0:
    res.append(n//5)
while a >= 5:
    a -= 3
    cnt += 1
    if a % 5 == 0:
        res.append(cnt + a//5)
cnt = 0
while n >= 3:
    n -= 5
    cnt += 1
    if n % 3 == 0:
        res.append(cnt + n//3)
if res:
    print(min(res))
else:
    print(-1)