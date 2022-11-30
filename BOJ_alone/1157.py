a = input().upper()
seta = list(set(a))
count = []
for i in seta:
    count.append(a.count(i))
if count.count(max(count)) > 1: 
    print('?')
else:
    print(seta[count.index(max(count))])