n = input()
list1 = []
def odd(x):
    cnt = 0
    for z in str(x):
        if int(z) % 2 == 1:
            cnt += 1
    return cnt

def comb(array, cnt):
    if len(array) >= 3:
        for i in range(len(array) - 2):
            for k in range(i + 1, len(array) - 1):
                ex = int(array[:i+1]) + int(array[i+1:k+1]) + int(array[k+1:])
                comb(str(ex), odd(ex) + cnt)
    elif len(array) == 2:
        ex = int(array[0]) + int(array[1])
        comb(str(ex) , odd(ex) + cnt)   
    else:
        list1.append(cnt)
comb(n,odd(n))
print(min(list1), max(list1))