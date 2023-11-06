def solution(number):
    sum = 0
    for a in range(len(number)-2):
        for b in range(a+1,len(number)-1):
            for c in range(b+1,len(number)):
                if number[a] + number[b] + number[c] == 0:
                    sum += 1
    return sum