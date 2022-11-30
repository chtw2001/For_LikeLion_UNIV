import sys, math
input = sys.stdin.readline
up = 1
n, k = map(int, input().split())
for i in range(1,k+1):
    up *= (n-i+1)
down = math.factorial(k)
print(int(up/down))