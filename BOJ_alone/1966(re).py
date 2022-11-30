from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    st = input().split()
    a = dict()
    for i in range(n):
        a[i] = int(st[i])
    i = 1
    k = a[m]
    pior = deque(a.values())
    name = deque(a.keys())
    if n == 1:
        print(1)
    else:
        while True:
            if pior[0] == k and pior[0] == max(pior) and name[0] == m:
                print(i)
                break
            elif pior[0] == max(pior):
                pior.popleft()
                name.popleft()
                i += 1        
            else:
                pior.append(pior[0])
                pior.popleft()
                name.append(name[0])
                name.popleft()