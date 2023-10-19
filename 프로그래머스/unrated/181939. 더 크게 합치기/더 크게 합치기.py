def solution(a, b):
    num1 = str(a) + str(b)
    num2 = str(b) + str(a)
    if num1 > num2:
        answer = num1
    elif num1 < num2:
        answer = num2
    else:
        answer = num1
    return int(answer)