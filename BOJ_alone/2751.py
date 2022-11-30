import sys
input = sys.stdin.readline
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a = sorted(list(set(a)))
for i in a:
    print(i)