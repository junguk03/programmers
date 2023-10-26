def solution(num_list):
    str1 = ""
    str2 = ""
    for i in range(len(num_list)):
        if(num_list[i]%2 == 1):
            str1 += str(num_list[i])
        else:
            str2 += str(num_list[i])
    result = int(str1) + int(str2)
    return result