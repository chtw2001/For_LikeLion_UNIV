n = int(input())
ox = []
for i in range(n):
    ox.append(input())
for i in range(n):
    score = 0
    cnt = 1
    for k in range(len(ox[i])):
        if ox[i][k] == 'O':
            score += cnt
            cnt += 1
        else: 
            cnt = 1
    print(score)