n = int(input())
for i in range(n):
    N = int(input())
    cnt ,a = 0, 1
    total = 0
    while total <= N:
        total += a
        cnt += 1
        a += 1
        if ((N-total)//a+1) <= 1:
            print(cnt)
            break
    if total > N:
        print(cnt - 1)