n = input()
na = sorted((map(int, input().split())))
m = input()
ma = map(int, input().split())
def 이분탐색(i,n,start,end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if i == na[mid]:
        return 1
    elif i < na[mid]:
        return 이분탐색(i,n,start,mid-1)
    else:
        return 이분탐색(i,n,mid+1,end)
for i in ma:
    start = 0
    end = len(na) - 1
    print(이분탐색(i,n,start,end))