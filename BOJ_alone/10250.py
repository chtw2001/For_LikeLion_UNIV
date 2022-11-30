import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    y, x, nth = map(int, input().split())
    a, b = divmod(nth, y)
    if nth % y == 0:
        print(y * 100 + a)
    else:
        print(b * 100 + a+1)