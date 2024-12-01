def solution(n):
    sum = 0
    while(1):
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            sum += 1
        if n == 0:
            break

    return sum