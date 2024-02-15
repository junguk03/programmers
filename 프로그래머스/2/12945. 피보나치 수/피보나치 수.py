def solution(n):
    dic = {0:0,1:1}
    for i in range(1,n):
        sum = dic[i]+dic[i-1]
        dic[i+1] = sum
    answer = dic[n]%1234567
    return answer