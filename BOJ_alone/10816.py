import sys
input = sys.stdin.readline

n = int(input())
origin = sorted(list(map(int, input().split())))

m = int(input())
find = list(map(int, input().split()))

dic_a = {}

for i in origin:
    try:
        if dic_a[i]:
            dic_a[i] += 1
        else:
            dic_a[i] = 0
    except:
        dic_a[i] = 1

for i in find:
    try:
        dic_a[i]
        print(dic_a[i], end=' ')
    except:
        print(0, end=' ')






# for i in range(m):
#     cnt = 0
#     left = 0
#     right = n-1
#     num = find[i]
#     while left <= right:
#         mid = (left + right) // 2
#         if num < origin[mid]:
#             right = mid - 1
#         elif num > origin[mid]:
#             left = mid + 1
#         else:
#             cnt = origin[left:right + 1].count(num)
#             res[num] = cnt
#             break
#     if cnt == 0:
#         res[num] = cnt
# for i in find:
#     print(res[i],end=' ')