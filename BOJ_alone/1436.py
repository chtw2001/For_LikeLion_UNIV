a = int(input())
count = 666
check = 0
while True:
    if '666' in str(count):
        check += 1
    if a == check:
        print(count)
        break
    count += 1