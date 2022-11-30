import sys
input = sys.stdin.readline

t = int(input())

def calc(list1):
    global count
    global res
    b = []
    count += 1
    for i in range(len(list1)):
        b.append(sum(list1[:i+1]))
    if count == k:
        res = b[n-1]
    else:
        calc(b)

for _ in range(t):
    k = int(input())
    n = int(input())
    a = []
    res = 0
    count = 0
    for i in range(n):
        a.append(i+1)
    calc(a)
    print(res)