def solution(s):
    strlen = len(s)
    sum1 = 0
    for i in range(strlen):
        s2 = s
        while(1):
            if s2.find("()") == -1 and s2.find("{}") == -1 and s2.find("[]") == -1:
                break
            else:
                s2 = s2.replace("()","")
                s2 = s2.replace("{}","")
                s2 = s2.replace("[]","")
                if not s2:
                    sum1 += 1
                    break
        s = s[1:] + s[0]
    return sum1