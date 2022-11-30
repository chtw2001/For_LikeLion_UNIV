from heapq import heappush, heappop
import sys
input = sys.stdin.readline

t, n = map(int, input().split())
heap = []
for i in range(n):
    id, time, prio = map(int, input().split())
    heappush(heap, (-prio, id ,time))
for i in range(t):
    a = heappop(heap)
    print(a[1])
    if a[2] - 1 > 0:
        heappush(heap, (a[0] + 1, a[1], a[2]-1))