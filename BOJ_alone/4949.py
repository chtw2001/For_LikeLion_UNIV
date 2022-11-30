a = []
while True:
    a.append(input())
    if len(a[-1]) == 1 and a[-1] == '.':
        del a[-1]
        break
for i in a:
    stack = [0]
    for k in i:
        if k == '(':
            stack.append('(')
        elif k == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append('no')
                break
        elif k == '[':
            stack.append('[')
        elif k == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append('no')
                break
    if 'no' in stack:
        print('no')
    elif len(stack) == 1:
        print('yes')
    else:
        print('no')