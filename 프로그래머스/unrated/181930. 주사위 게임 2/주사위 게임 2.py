def solution(a, b, c):
    arr1 = [a, b, c]
    arr2 = [1, 2, 3, 4, 5, 6]
    sum = set(arr1) & set(arr2)
    if len(sum) == 3:
        answer = a + b + c
    elif len(sum) == 2:
        answer = (a + b + c) * (a*a + b*b + c*c )
    else:
        answer = (a + b + c) * (a*a + b*b + c*c ) * (a*a*a + b*b*b + c*c*c)
    return answer