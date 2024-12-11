def solution(s):
    arr = list(map(int,s.split()))
    str1 = str(min(arr)) + " " + str(max(arr))
    
    return str1