a = []
for i in range(10):
    a.append(int(input()))
b = []
for i in a:
    b.append(i%42)
print(len(set(b)))