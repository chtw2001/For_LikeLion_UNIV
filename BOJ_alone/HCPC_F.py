from heapq import heappush as push, heappop as pop
import sys
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    a, b, c = input().split()
    push(heap, (int(b), int(c), a))

for _ in range(n):
    a, b, c = pop(heap)
    print(c[b-1].upper(), end='')
