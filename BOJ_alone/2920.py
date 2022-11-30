a = list(map(int, input().split()))
c = 0
cnt = 0
for i in range(len(a)):
    if i+1 == a[i]:
        c += 1
for i in range(len(a),0,-1):
    if i == a[cnt]:
        c += 1
        cnt += 1
if c >= 8 and a[0] == 1:
    print('ascending')
elif c >= 8 and a[0] == 8:
    print('descending')
else:
    print('mixed')