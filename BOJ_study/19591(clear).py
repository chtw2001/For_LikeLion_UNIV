from collections import deque
import sys, re, time
# input = sys.stdin.readline

ch = 0
a = input()
# start = time.time()
if a[0] == '-':
    ch = 1

a = deque(re.split('([-|+|*|/])', a)) 

if ch == 1:
    a.popleft()
    a.popleft()
    ch = a.popleft()
    a.appendleft(-int(ch))
# 입력 받은 예제 구분자를 통해 분할(덱)
# print('문자열 받기: ',time.time() - start)

# start = time.time()

def calc(left,right,op):
    if op == '-':
        ex = left - right
    elif op == '+':
        ex = left + right
    elif op == '*':
        ex = left * right
    else:
        if left * right < 0 and left % right != 0:
            ex = (left // right) + 1
        else:
            ex = left // right
    return ex

def front(x):
    n = int(x.popleft())
    k = x.popleft()
    m = int(x.popleft())
    x.appendleft(calc(n, m, k))

def back(x):
    n = int(x.pop())
    k = x.pop()
    m = int(x.pop())
    x.append(calc(m, n, k))

def test(x):
    n = int(x[0])
    k = x[1]
    m = int(x[2])
    i = calc(n, m, k)
    k1 = k

    n = int(x[-1])
    k = x[-2]
    m = int(x[-3])
    j = calc(m, n, k)
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
    # print('테스트 할 때마다',time.time() - start)
    # start = time.time()

print(int(a[0]))