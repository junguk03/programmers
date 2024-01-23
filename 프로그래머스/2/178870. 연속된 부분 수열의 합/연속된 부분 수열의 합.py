def solution(sequence, k):
    arr = {idx: num for idx, num in enumerate(sequence)}
    start = 0
    sum = 0
    arr1 = []
    
    for idx1, num1 in enumerate(sequence):
        end = idx1
        sum += num1
        while(sum > k):
            sum -= arr[start]
            start += 1
        if(sum == k):
            arr1.append([start,end])
    arr1.sort(key = lambda x: (x[1]-x[0],x[0]))
    return arr1[0]