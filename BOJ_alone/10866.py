from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
deq = deque()


def push_front(x):
    deq.appendleft(x)

def push_back(x):
    deq.append(x)

def pop_front():
    try:
        print(deq.popleft())
    except:
        print(-1)

def pop_back():
    try:
        print(deq.pop())
    except:
        print(-1)

def size():
    print(len(deq))

def empty():
    if len(deq) == 0:
        print(1)
    else:
        print(0)

def front():
    try:
        print(deq[0])
    except:
        print(-1)

def back():
    try:
        print(deq[-1])
    except:
        print(-1)

for _ in range(n):
    a = input()
    a = a[:-1]
    if a.split()[0] == 'push_back':
        a = a.split()[1]
        push_back(a)
    elif a.split()[0] == 'push_front':
        a = a.split()[1]
        push_front(a)
    elif a == 'pop_front':
        pop_front()
    elif a == 'pop_back':
        pop_back()
    elif a == 'size':
        size()
    elif a =='empty':
        empty()
    elif a == 'front':
        front()
    elif a == 'back':
        back()