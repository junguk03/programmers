def solution(numLog):
    str = ""
    for i in range(len(numLog)-1):
        if numLog[i+1] - numLog[i] == 1:
            str += "w"    
        elif numLog[i+1] - numLog[i] == -1:
            str += "s"    
        elif numLog[i+1] - numLog[i] == 10:
            str += "d"    
        elif numLog[i+1] - numLog[i] == -10:
            str += "a"    
    return str