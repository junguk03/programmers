def solution(n):
    sum = 0
    for i in range(1,n//2+1,2):
        if n%i == 0:
            sum += 1
    if n%2 == 1:
        sum += 1
    return sum