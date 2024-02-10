def solution(n):
    num = format(n,'b').count('1')
    while(1):
        n += 1
        if num == format(n,'b').count('1'):
            return n
            break