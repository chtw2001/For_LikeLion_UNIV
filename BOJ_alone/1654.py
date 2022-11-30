# 갖고있는 랜선의 수 k, 만들어야 할 
# 랜선의 수 n 입력받기
k ,n = map(int, input().split())

# 갖고있는 각 랜선의 길이 입력받기
line = [int(input()) for _ in range(k)]

# 랜선의 최대 길이를 length에 선언
start, end = 1, max(line)

res = 0
# 가장 긴 길이를 구해야 하기 때문에
# 랜선의 최대 길이에서 1 씩 빼면서  몫 구하기
while start <= end:
    a = 0
    # 갖고있는 각 랜선의 길이를 최대 길이로
    # 나누어 몫 만 리스트 a에 추가
    mid = (start + end) // 2
    for i in line:
        a += i // mid

    # 최대 길이로 최대 개수를 만들어야 한다
    # 5행에서 최대 길이를 넣었으므로
    # 최대 개수를 충족하면 길이 출력
    if a >= n:
        start = mid + 1
        res = mid
    else:
        end = mid -1
print(res)