def solution(arr1, arr2):
    str1 = len(arr1)
    str2 = len(arr1[0])
    str3 = len(arr2[0])
    sum1 = -1
    sum2 = 0
    answer = []
    answer1 = []
    for i in range(str1): 
        answer.append([])
        sum1 += 1
        for j in range(str3):
            for k in range(str2):
                sum2 += (arr1[i][k] * arr2[k][j])
            answer[sum1].append(sum2)
            sum2 = 0
    return answer