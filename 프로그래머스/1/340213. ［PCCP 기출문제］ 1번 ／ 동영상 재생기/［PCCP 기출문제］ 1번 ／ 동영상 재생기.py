def minute(time):
    time = time.split(":")
    num1 = int(time[1])
    num1 += int(time[0]) * 60
    
    return num1

def original(num):
    result1 = num // 60
    result2 = num % 60
    if result1 < 10:
        result1 = "0" + str(result1)
    if result2 < 10:
        result2 = "0" + str(result2)
        
    result = str(result1) + ":" + str(result2)
    
    return result

def solution(video_len, pos, op_start, op_end, commands):
    num1 = minute(video_len)
    num2 = minute(pos)
    num3 = minute(op_start)
    num4 = minute(op_end)
    for i in commands:
        if num2 >= num3 and num2 <= num4:
            num2 = num4
        if i == "prev":
            if num2 < 10:
                num2 = 0
            else:
                num2 -= 10
        elif i == "next":
            if num2 > num1-10:
                num2 = num1
            else:
                num2 += 10
    
    if num2 > num3 and num2 < num4:
        num2 = num4
    return original(num2)