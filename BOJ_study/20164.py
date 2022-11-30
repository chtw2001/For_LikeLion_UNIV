import sys
input = sys.stdin.readline

n = input()
n = n[:-1]
global cnt
cnt = 0
for i in n:
    if int(i) % 2 == 1:
        cnt += 1
q = cnt
real = []
def comb(array):   
    global cnt
    for i in range(1,len(array)-1):
        for k in range(1,len(array)-1):
            if i+k == len(array):
                break
            ex = []
            if len(str(n)) >= 3:
                ex.append((int(array[:i]), int(array[i:i+k]), int(array[i+k:])))
                a = 0
                for j in ex[0]:
                    a += j
                for j in str(a):
                    if int(j) % 2 == 1:
                        cnt += 1
                if len(str(a)) >= 3:
                    comb(str(a))
                    continue
            if len(str(a)) == 2:
                just = 0
                for j in str(a):
                    just += int(j)
                if len(str(just)) == 2:
                    zz = 0
                    for j in str(just):
                        zz += int(j)
                        if int(j) % 2 == 1:
                            cnt += 1
                    if zz % 2 == 1:
                        cnt += 1
                else:
                    if just % 2 == 1:
                        cnt += 1
                # 2자리수 일 때 두개로 나누어서 더한 값이한자리수면
                # 끝내고 아니면 한번 더하면 끝 99 -> 18 -> 9
                real.append(cnt)
                cnt = q
            else:
                if int(a) % 2 == 1:
                    cnt += 1
                real.append(cnt)
                cnt = q

comb(n)
print(min(real), max(real))