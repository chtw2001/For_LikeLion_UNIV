import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a = input()
    arr = []
    res = []
    ch = 0
    for i in a:
        arr.append(i)
    del arr[-1]
    for i in range(len(arr)):
        try:
            if arr[i] == '(':
                res.append('(')
            else:
                res.pop()
        except:
            print('NO')
            ch = 1
            break
    if len(res) == 0 and ch == 0:
        print('YES')
    elif len(res) != 0 and ch == 0:
        print('NO')
    else:
        pass