import math
import sys
input = sys.stdin.readline

a,b = map(int, input().split())
for i in range(a,b+1):
    ch = 0
    if i == 1:
        continue
    if i == 2:
        print(2)
        continue
    x = round(math.sqrt(i))+1
    for k in range(2,x):
        if i % k == 0:
            ch = 1
            break
    if ch == 0:
        print(i)