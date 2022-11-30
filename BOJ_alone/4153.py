import sys
input = sys.stdin.readline

a = [0,0,0]

while True:
    a[0], a[1], a[2] = map(int, input().split())
    if sum(a) == 0:
        break
    a.sort()
    if a[2]**2 == a[0]**2 + a[1]**2:
        print('right')
    else:
        print('wrong')