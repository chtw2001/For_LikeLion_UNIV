from heapq import heappush as push , heappop as pop
import sys
input = sys.stdin.readline

arr = []
n = int(input())
for i in range(n):
    info = input()
    a , b = int(info.split()[0]), info.split()[1]
    push(arr, (a, i, b))

for _ in range(n):
    ex = pop(arr)
    print(ex[0], ex[2])