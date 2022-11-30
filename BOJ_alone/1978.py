n = int(input())
a = sorted(map(int, input().split()))
cnt = 0
over = 0
for i in a:
    if i == 1:
        continue
    elif i == 2:
        cnt += 1
        continue
    else:
        for k in range(2,i):
            if i % k == 0:
                over = 1
                break
    if over == 0:
        cnt += 1
    over = 0
print(cnt)