import sys
input = sys.stdin.readline

n = int(input())
origin = sorted(list(map(int, input().split())))

m = int(input())
find = list(map(int, input().split()))

dic_a = {}

for i in origin:
    try:
        if dic_a[i]:
            dic_a[i] += 1
        else:
            dic_a[i] = 0
    except:
        dic_a[i] = 1

for i in find:
    try:
        dic_a[i]
        print(dic_a[i], end=' ')
    except:
        print(0, end=' ')