import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
room = list(list(input()) for _ in range(r))

x, y = 0,0
for i in range(r):
    for j in range(c):
        if room[i][j] == 'G':
            y, x = i, j
            break
    if room[i][j] == 'G':
        room[y][x] = '.'
        break

dx = [0,0,-1,1]
dy = [-1,1,0,0]
s = 0
maxs = 0
def DFS(x,y,t,s):
    if t == 0:
        global maxs
        maxs = max(maxs, s)
        return
    for mx, my in zip(dx,dy):
        nx, ny = x+mx, y+my
        if 0 <= nx < c and 0 <= ny < r and room[ny][nx] != '#':
            if room[ny][nx] == '.':
                DFS(nx,ny,t-1,s)
            elif room[ny][nx] == 'S':
                room[ny][nx] = '.'
                DFS(nx,ny,t-1,s+1)
                room[ny][nx] = 'S'

DFS(x,y,t,s)
print(maxs)