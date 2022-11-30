import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

res = dict()

for i in range(m):
    try:
        ex = a.index(b[i])
        cnt = 2
        if a.count(b[i]) == 1:
            res[i] = cnt - 1

        for j in range(ex,n-2):
            if a[j] == a[j+1]:
                res[i] = cnt
                cnt += 1
            else:
                break
    except:
        res[i] = 0
answ = list(res.values())
for i in answ:
    print(i,end = ' ')