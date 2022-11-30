n = int(input())
order = []
stack = []
for _ in range(n):
    order.append(input())
def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        a = stack.pop()
        print(a)

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

for i in order:
    if i == 'pop':
        pop()
    elif i == 'empty':
        empty()
    elif i == 'size':
        size()
    elif i == 'top':
        top()
    else:
        push(i[5:])