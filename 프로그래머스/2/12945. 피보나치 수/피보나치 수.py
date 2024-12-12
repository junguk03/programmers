def solution(num):
    answer=[0,1]
    for i in range(2,num+1):
        answer.append(answer[i-1]+answer[i-2])
    return answer[-1]%1234567