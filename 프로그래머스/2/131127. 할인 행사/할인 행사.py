def solution(want, number, discount):
    num = len(want)
    all_day = len(discount)
    arr = []
    arr1 = []
    for day in range(all_day-9):
        sum1 = 0
        for i in range(num):
            if number[i] == discount[day:day+10].count(want[i]):
                sum1 += 1
            else:
                break
        if sum1 == num:
            arr1.append(day)
            
    return len(arr1)