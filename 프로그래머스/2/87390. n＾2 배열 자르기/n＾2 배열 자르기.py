def solution(n, left, right):
    answer = list(range(1,n+1))
    result = []
    arr1 = []
    num1 = left//n + 1        
    num2 = left%n             
    num3 = right//n + 1        
    num4 = right%n            
    
    for i in range(n):
        if i < num1:
            arr1.append(num1)
        else:
            arr1.append(i+1)
            
    for i in range(num1-1,num3):
        result.extend(arr1)
        arr1[0:i+2] = [i+2]*(i+2)
        
        
    strlen = len(result)
    
    return result[num2:strlen+(num4-n+1)]