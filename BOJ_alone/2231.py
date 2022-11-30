a = int(input())
answ = 0
for i in range(1,a+1):
    for k in str(i):
        answ += int(k)
    if i>=answ and i + answ == a:
        print(i)
        quit()
    else:
        answ = 0
if answ == 0:
        print(0)