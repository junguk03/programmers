def sum2(num1):
    num2 = num1 % 100
    num3 = num1 // 100
    
    if num2 > 59:
        num2 %= 60
        num3 += 1
    num1 = num3*100 + num2
    return num1

def solution(schedules, timelogs, startday):
    people = len(schedules)
    result = 0
    for i in range(people):
        sum1 = startday
        num1 = 0
        while num1 != 7:
            if sum1 % 7 == 0 or sum1 % 7 == 6:
                sum1 += 1
            else:
                if timelogs[i][num1] <= sum2(schedules[i] + 10):
                    sum1 += 1
                else:
                    num1 == 6
            num1 += 1
        if sum1 == startday + 7:
            result += 1
                    
    return result