def solution(a, d, included):
    c = a - d
    sum = 0
    n = len(included)
    for i in range(1,n+1):
        if included[i-1]:
            sum += d*i + c
    return sum