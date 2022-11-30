import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

# 산술평균
print(round(sum(a)/n))

# 중앙값
a.sort()
print(a[n // 2])

# 최빈값
dic = dict()
cnt = 1
dic[a[0]] = a.count(a[0])
for i in range(1, len(a)):
    if a[i-1] == a[i]:
        dic[a[i]] = cnt + 1
        cnt += 1
    else:
        cnt = 1
        dic[a[i]] = cnt

list_value = list(dic.values())

if len(list_value) == len(set(list_value)):
    for i in dic.keys():
        if dic[i] == max(list_value):
            print(i)
            break
else:
    if list_value.count(max(list_value)) != 1:
        ex = []
        for i in dic.keys():
            if dic[i] == max(list_value):
                ex.append(i)
        ex.sort()
        print(ex[1])
    else:
        for i in dic.keys():
            if dic[i] == max(list_value):
                print(i)
                break

# 범위
if n == 1:
    print(0)
else:
    print(abs(a[-1] - a[0]))