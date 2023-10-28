def solution(l, r):
    arr = list()
    for i in range(1,64):
        if l <= int(format(i,'b'))*5 <= r:
            arr.append(int(format(i,'b'))*5)
    return arr or [-1]