n = int(input())
a = []
for i in range(n):
    a.append(input().split())
for i in a:
    str = i[1]
    for k in str:
        print(k*int(i[0]),end="")
    print()