import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)
print(sum(stack))