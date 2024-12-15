def solution(n):
    arr = [1,2]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(1,n-1):
            arr.append(arr[i-1]+arr[i])
        return arr[n-1] % 1234567