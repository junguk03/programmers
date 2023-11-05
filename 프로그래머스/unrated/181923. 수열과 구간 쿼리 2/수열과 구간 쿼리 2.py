def solution(arr, queries):
    arr1 = list()
    for a,b,c in queries:
        arr2 = []
        for i in range(a,b+1):
            if arr[i] > c:
                arr2.append(arr[i])
        if len(arr2) == 0:
            arr1.append(-1)
        else:
            arr1.append(min(arr2))
    return arr1