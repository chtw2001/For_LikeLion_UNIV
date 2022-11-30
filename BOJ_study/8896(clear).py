round = int(input())

for _ in range(round):
    robot_num = int(input())
    a = [input() for _ in range(robot_num)]
    win = [True]*robot_num
    str_num = len(a[0])
    for i in range(str_num):
        ex = set()
        for j in range(robot_num):
            if win[j]:
                ex.add(a[j][i])
        if len(ex) == 2:
            lose = 'R'
            if 'S' in ex and 'P' in ex:
                lose = 'P'
            elif 'S' in ex and 'R' in ex:
                lose = 'S'
            for j in range(robot_num):
                if a[j][i] == lose:
                    win[j] = False
    if win.count(True) > 1:
        print(0)
    else:
        print(win.index(True) + 1)