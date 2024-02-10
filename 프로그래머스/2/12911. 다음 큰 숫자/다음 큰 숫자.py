def solution(n):
    num = format(n,'b').count('1')
    for i in range(n+1,1000001):
        if num == format(i,'b').count('1'):
            return i
            break