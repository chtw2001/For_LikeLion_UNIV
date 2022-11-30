import sys
input = sys.stdin.readline

a,b,v = map(int, input().split())

c, d = divmod(v-a,a-b)
if d == 0:
    print(c+1)
else:
    print(c+2)