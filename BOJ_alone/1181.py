n = int(input())
a = list(set([input() for _ in range(n)]))
a.sort()
a.sort(key = len)
for i in a:
    print(i)