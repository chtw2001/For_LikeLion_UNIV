sub = int(input())
score = list(map(int, input().split()))

mscore = max(score)
avg = 0
for i in score:
    avg += i/mscore*100
print(avg/sub)