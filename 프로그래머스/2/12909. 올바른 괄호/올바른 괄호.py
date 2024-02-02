def solution(s):
    arr = list()
    for i in range(len(s)):
        if s[i] == "(":
            arr.append(s[i])
        else:
            try:
                arr.pop()
            except:
                return False
                break
            
    return len(arr) == 0