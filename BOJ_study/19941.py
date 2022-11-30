n, k = map(int, input().split())
a = input()
arr = []
for i in a:
    arr.append(i)
cnt = 0
for i in range(len(arr)):
    if arr[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if arr[j] == 'H':
                arr[j] = i
                cnt += 1
                break
print(cnt)