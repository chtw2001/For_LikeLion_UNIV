테스트케이스 = int(input())
요금소 = []
for _ in range(테스트케이스):
    요금 = 0
    시간입력 = input()
    시분, 게임시간 = 시간입력.split()[0] ,int(시간입력.split()[1])
    시, 분= int(시분.split(':')[0]), int(시분.split(':')[1])
    while 게임시간 > 0:
        if (시 >= 22 or 시 < 3) and 게임시간 > 300:
            while 시 != 8 and 게임시간 > 0:
                게임시간 -= 60                 
                시 = (시+1) % 24
            요금 += 5000
            게임시간 += 분
            분 = 0
        else:       
            시 = (시+1) % 24  
            요금 += 1000  
            게임시간 -= 60
    요금소.append(요금)
for i in  요금소:
    print(i)