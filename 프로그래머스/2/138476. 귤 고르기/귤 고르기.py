import collections
def solution(k, tangerine):
    answer = 0
    sum1 = 0
    arr = set(tangerine)
    cnt = collections.Counter(tangerine).most_common()
    for i in range(len(cnt)):
        sum1 += cnt[i][1]
        if sum1 >= k:
            return i+1