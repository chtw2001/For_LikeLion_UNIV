from collections import deque
import sys
sys.setrecursionlimit(1050) # RecursionError가 발생하여
input = sys.stdin.readline  # 파이썬의 최대 재귀 깊이를 임의로 설정

n, k = map(int, input().split())
a = deque([i for i in range(1,n+1)])
res = []
def delete(x):
    if len(x) == 0:
        return 
    x.rotate(-k+1)
    res.append(x.popleft())
    delete(x)
delete(a)
print('<',end='')
for i in res:
    if i == res[-1]:
        print(i,end='>')
    else:
        print(i,end=', ')