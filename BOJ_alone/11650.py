from heapq import heappush as push, heappop as pop
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    a = input()
    push(heap, (int(a.split()[0]), int(a.split()[1])))

for _ in range(n):
    a, b = pop(heap)
    print(a, b)