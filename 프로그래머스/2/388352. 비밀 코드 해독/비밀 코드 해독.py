def prepare(list1, list2):
    num1 = 5 - len(set(list1) - set(list2))
    return num1

def cnt(num1):
    list1 = []
    for i in range(1,num1+1):
        list1.append(i)
        
    return list1

def solution(n, q, ans):
    import itertools
    list1 = cnt(n)
    num1 = len(ans)
    list2 = itertools.combinations(list1,5)
    list3 = []
    for j in range(num1):
        for i in list2:
            if prepare(q[j],i) == ans[j]:
                list3.append(i)
        list2 = list3
        list3 = []
    return len(list2)