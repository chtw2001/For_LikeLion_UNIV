n = int(input())
ex = []
res = []
cnt = 1
for i in range(n):
    num = int(input())
    while cnt <= num:
        ex.append(cnt)
        res.append('+')
        cnt += 1
    if ex[-1] == num:
        ex.pop()
        res.append('-')
    else:
        print('NO')
        quit()
for i in res:
    print(i)