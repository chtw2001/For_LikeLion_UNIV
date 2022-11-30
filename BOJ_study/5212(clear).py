r, c = map(int, input().split())
arr = []
res = [[]*c for _ in range(r)]
for i in range(r):
    arr.append(input())
    for j in range(c):
        res[i].append(arr[i][j])
for i in range(r):
    for j in range(c):
        cnt = 0
        if arr[i][j] == 'X':
            try:
                if i-1 < 0:
                    cnt += 1
                elif arr[i-1][j] == '.':
                    cnt += 1
            except:
                cnt += 1
            try:
                if j-1 < 0:
                    cnt += 1
                elif arr[i][j-1] == '.':
                    cnt += 1
            except:
                cnt += 1
            try:
                if arr[i][j+1] == '.':
                    cnt += 1
            except:
                cnt += 1
            try:
                if arr[i+1][j] == '.':
                    cnt += 1
            except:
                cnt += 1
        if cnt >= 3:
            res[i][j] = '.'
x = []
y = []
for i in range(r):
    for j in range(c):
        if res[i][j] == 'X':
            x.append(j)
            y.append(i)
for i in range(min(y),max(y)+1):
    for j in range(min(x),max(x)+1):
        print(res[i][j],end='')
    print()

# try: arr[i-1][j] 이렇게 해서 i-1이 범위에 없으면 except 구문으로 가는게 아니라
# 문자열 바로 맨 뒤로 감
# 상하좌우 이동하는 것으로 수정해야 함