def solution(t, p):
    arr = list()
    sum = 0
    for i in range(len(t)-len(p)+1):
        arr1 = ""
        for j in range(len(p)):
            arr1 += t[i+j]
        arr.append(arr1)
    for i in range(len(arr)):
        if arr[i] <= p:
            sum += 1
    return sum