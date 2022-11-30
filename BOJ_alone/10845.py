from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = deque()

def push(x):
    arr.append(x)
def pop():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr.popleft())
def size():
    print(len(arr))
def empty():
    if len(arr) == 0:
        print(1)
    else:
        print(0)
def front():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[0])
def back():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[-1])

for _ in range(n):
    a = input().split()
    try:
        order,x = a[0], int(a[1])
    except:
        order = a[0]
    if order == 'push':
        push(x)
    elif order == 'pop':
        pop()
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    elif order == 'front':
        front()
    elif order == 'back':
        back()