def solution(str1, str2):
    strlen = len(str1)
    answer = list()
    for i in range(strlen):
        answer.append(str1[i] + str2[i]) 
    answer = ''.join(answer)
    return answer