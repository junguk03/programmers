def solution(name, yearning, photo):
    name_yearning = dict()
    arr = list()
    for num in range(len(name)):
        name_yearning[name[num]] = yearning[num]
    for list1 in photo:
        sum = 0
        for list2 in list1:
            if list2 in name:
                sum += name_yearning[list2]
            else:
                sum += 0
        arr.append(sum)
    return arr