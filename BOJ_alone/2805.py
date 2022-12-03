import sys
input = sys.stdin.readline

n, m = map(int, input().split())

height = sorted(list(map(int, input().split())))

left = 0
right = height[-1]
while left <= right:
    mid = (left + right) // 2
    summ = 0
    for j in range(n):
        if height[j] - mid > 0:
            summ += height[j] - mid
    if summ < m:
        right = mid -1
    elif summ > m:
        left = mid + 1
    else:
        print(mid)
        quit()
print(right)