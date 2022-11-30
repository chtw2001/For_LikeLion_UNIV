from collections import deque
import sys, re
input = sys.stdin.readline
ch = 0
a = input()  # 예제 입력받기
if a[0] == '-':
    a = a[1:-1]
    ch = 1
else:
    a = a[:-1]   # readline 사용으로 맨 뒤에 \n 포함되어있으니 빼주기
a = deque(re.split('([-|+|*|/])', a)) # re 모듈울 이용하여 다양한 구분자로 나누기
if ch == 1:                           # 소괄호로 감싸주어 해당 구분자 또한 리스트에 넣기
    ch = a.popleft()
    a.appendleft(-int(ch))

def front(x):
    n = int(x.popleft())
    k = x.popleft()
    m = int(x.popleft())
    if k == '-':
        x.appendleft(n - m)
    elif k == '+':
        x.appendleft(n + m)
    elif k == '*':
        x.appendleft(n * m)
    else:
        if n*m < 0 and n%m != 0:
            x.appendleft((n // m) + 1)
        else:
            x.appendleft(n // m)

def back(x):
    n = int(x.pop())
    k = x.pop()
    m = int(x.pop())
    if k == '-':
        x.append(m - n)
    elif k == '+':
        x.append(m + n)
    elif k == '*':
        x.append(m * n)
    else:
        if n*m < 0 and n%m != 0:
            x.append((m // n) + 1)
        else:
            x.append(m // n)

def test(x):
    i, j = 0, 0
    n = int(x[0])
    k = x[1]
    m = int(x[2])
    if k == '-':
        i = n - m
    elif k == '+':
        i = n + m
    elif k == '*':
        i = n * m
    else:
        if n*m < 0 and n%m != 0:
            i = (n // m) + 1
        else:
            i = (n // m)
    k1 = k

    n = int(x[-1])
    k = x[-2]
    m = int(x[-3])
    if k == '-':
        j = m - n
    elif k == '+':
        j = m + n
    elif k == '*':
        j = m * n
    else:
        if n*m < 0 and n%m != 0:
            j = (m // n) + 1
        else:
            j = (m // n)
    k2 = k
    
    if (k1 == '+' or k1 == '-') and (k2 == '*' or k2 == '/'):
        back(x)
    elif (k1 == '*' or k1 == '/') and (k2 == '+' or k2 == '-'):
        front(x)
    else:
        if i >= j:
            front(x)
        else:
            back(x)

while len(a) > 2:
    test(a)

print(int(a[0]))