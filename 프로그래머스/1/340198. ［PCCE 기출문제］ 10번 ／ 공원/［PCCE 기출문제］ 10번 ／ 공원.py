def solution(mats, park):
    answer = 0
    list1 = []
    mats.sort(reverse=True)
    a, b = len(park), len(park[0])
    for i in mats:
        for j in range(a-i+1):
            for k in range(b-i+1):
                if all(park[x][y] == '-1' for x in range(j,j+i) for y in range(k,k+i)):
                    return i
    
    return -1