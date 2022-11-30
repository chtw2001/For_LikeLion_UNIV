# BFS 사용시 처음 방문했을 때 만 고구마를 먹어야하지만
# 그렇게 구현하기가 어려웠다.
# 고구마를 먹고 '.' 으로 바꾸어주고 그 길이 아니면
# 고구마를 다시 'S' 로 바꿔주려면 재귀함수를 쓰는 것이 더 낫겠다.

from collections import deque
import sys
input = sys.stdin.readline

x, y = 0,0
r, c, t = map(int, input().split())

room = list(list(input()) for _ in range(r))

for i in range(r):
    for j in range(c):
        if room[i][j] == 'G':
            y, x = i, j
            room[y][x] = '.'
s = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def BFS(x,y,t,s):
    q = deque()
    q.append((x,y,t,s))
    maxs = s
    while q:
        x, y, t, s= q.popleft()
        if t == -1:
            return maxs
        maxs = max(maxs,s)
        for dx1, dy1 in zip(dx, dy):
            if x + dx1 >= 0 and x + dx1 < c and y + dy1 >= 0 and y + dy1 < r:
                if room[y + dy1][x + dx1] == '.':
                    q.append((x + dx1,y + dy1,t-1,s))
                elif room[y + dy1][x + dx1] == '#':
                    continue
                elif room[y + dy1][x + dx1] == 'S':
                    room[y + dy1][x + dx1] = '.'
                    q.append((x + dx1,y + dy1,t-1,s+1))

print(BFS(x,y,t,s))