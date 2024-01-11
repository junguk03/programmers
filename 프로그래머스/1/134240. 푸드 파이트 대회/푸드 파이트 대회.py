def solution(food):
    arr = "0"
    for i in range(len(food) - 1, 0, -1):
        c = food[i]//2
        while(c > 0):
            arr = str(i) + arr + str(i)
            c -= 1
    return arr