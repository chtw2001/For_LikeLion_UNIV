a = ''
while True:
    a = input()
    if a == '0':
        break
    k = len(a) // 2
    if len(a) % 2 != 0:
        if a[:k] == a[-1:k:-1]:
            print('yes')
        else:
            print('no')
    else:
        if a[:k] == a[-1:k-1:-1]:
            print('yes')
        else:
            print('no')