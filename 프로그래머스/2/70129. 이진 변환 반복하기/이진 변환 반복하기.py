def solution(s):
    sum1 = 0
    sum = 0
    arr = []
    while(s != "1"):
        num = s.count("1")
        sum += s.count("0")
        s = format(num,'b')
        sum1 += 1
        
    arr.extend([sum1,sum])
    return arr