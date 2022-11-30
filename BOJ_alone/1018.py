세로, 가로 = map(int, input().split())
c = []
result = []
for _ in range(세로):
    c.append(input())
a = [[c[j][i] for i in range(len(c[0]))] for j in range(세로)]
가, 나 = divmod(가로,8)
다, 라 = divmod(세로,8)
for j in range((다-1)*8 + 라 + 1):
    for q in range((가-1)*8 + 나 + 1):
        cnt = 0
        for i in range(j,j+8):
            for k in range(q,q+8):
                if i % 2 == 0:
                    if k % 2 == 0 and a[i][k] != 'B':
                        cnt += 1
                    elif k % 2 == 1 and a[i][k] != 'W':
                        cnt += 1
                else:
                    if k % 2 == 0 and a[i][k] != 'W':
                        cnt += 1
                    elif k % 2 == 1 and a[i][k] != 'B':
                        cnt += 1
        result.append(cnt)
        cnt = 0
        for i in range(j,j+8):
            for k in range(q,q+8):
                if i % 2 == 0:
                    if k % 2 == 0 and a[i][k] != 'W':
                        cnt += 1
                    elif k % 2 == 1 and a[i][k] != 'B':
                        cnt += 1
                else:
                    if k % 2 == 0 and a[i][k] != 'B':
                        cnt += 1
                    elif k % 2 == 1 and a[i][k] != 'W':
                        cnt += 1
        result.append(cnt)
print(min(result))