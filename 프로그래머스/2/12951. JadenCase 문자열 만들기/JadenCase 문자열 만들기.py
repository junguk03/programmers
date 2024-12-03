def solution(s):
    str1 = s.split(" ")
    result = []
    for str2 in str1:
        if(str2):
            result.append(str2[0].upper() + str2[1:].lower())
        else:
            result.append(str2)
    return " ".join(result)