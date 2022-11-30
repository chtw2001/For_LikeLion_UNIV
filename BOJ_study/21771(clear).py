n,m = map(int, input().split())
dn ,dm ,pn ,pm= map(int, input().split())
cntp = 0
room = [input() for _ in range(n)]
for i in room:
    cntp += i.count('P')
p = pn*pm
if cntp != p:
    print(1)
else:
    print(0)