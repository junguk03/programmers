def solution(number, n, m):
    max_num = max(n,m)
    min_num = min(n,m)
    if max_num%min_num == 0:
        result = int(not(number%max_num))
    else:
        result = int(not(number%(n*m)))
        
    return result