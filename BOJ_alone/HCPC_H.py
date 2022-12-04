import sys
input = sys.stdin.readline

n = int(input())
up = list(map(int,input().split()))
down = list(map(int,input().split()))

num_b = int(input())
size_b = list(map(int,input().split()))

k = 1
up[0] -= down[0]
for i in down[1:]:
    if up[k] - i <= up[k-1]:
        up[k] -= i
    else:
        up[k]  = up[k-1]
    k += 1

for i in range(num_b):
    left = 0
    right = n-1
    while left <= right:
        mid = (left + right) // 2
        if size_b[i] <= up[mid]:
            left = mid + 1
        elif size_b[i] > up[mid]:
            right = mid - 1
    print(right+1)
    

    # cnt = 0
    # for k in range(n):
    #     if up[k] >= size_b[i]:
    #         cnt += 1
    #     else:
    #         break 
    # print(cnt)