def solution(n):
    sum = 0
    sum = int(sum)
    if n%2 == 0:
        for i in range(0,n+1,2):
            sum += i * i
    else:
        for i in range(1,n+1,2):
            sum += i
    return sum