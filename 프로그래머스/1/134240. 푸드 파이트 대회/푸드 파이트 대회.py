def solution(food):
    num = len(food) - 1
    str1 = list()
    arr = list()
    for i in range(num):
        for j in range(food[i+1] // 2):
            str1.append(i+1)
    arr = str1 + str1[::-1]
    arr.insert(len(arr)//2,0)
    return "".join(map(str,arr))