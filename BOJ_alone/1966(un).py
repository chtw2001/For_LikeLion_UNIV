from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = deque(map(int, input().split()))
    k = a[m]
    i = 1
    print(a)
    if n == 1:
        print(1)
    else:
        while True:
            if a[0] == k and a[0] == max(a):
                print(i)
                break
            elif a[0] == max(a):
                a.popleft()
                i += 1        
            else:
                a.append(a[0])
                a.popleft()
            
