def solution(s):
    sum = 0
    for i in range(len(s)):
        if s[i] == "(":
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            break
    return sum == 0