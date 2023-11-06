def solution(t, p):
    sum = 0
    for i in range(len(t)-len(p)+1):
        if t[i:i+len(p)] <= p:
            sum += 1
    return sum