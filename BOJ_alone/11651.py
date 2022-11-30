from heapq import heappush as push, heappop as pop
import sys
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    push(heap, (b,a))
for _ in range(n):
    y, x = pop(heap)
    print(x,y)