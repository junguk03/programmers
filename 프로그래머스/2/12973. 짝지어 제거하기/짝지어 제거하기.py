from collections import deque

def solution(s):
    arr = deque()
    arr_index = 0
    s_index = 0
    while s_index < len(s):
        arr.append(s[s_index])
        s_index += 1
        if arr_index > 0:
            if arr[arr_index] == arr[arr_index-1]:
                arr.pop()
                arr.pop()
                arr_index -= 1
            else:
                arr_index += 1
        else:
            arr_index += 1
    if len(arr) == 0:
        return 1
    else:
        return 0