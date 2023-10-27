def solution(num_list):
    strlen = len(num_list)
    if num_list[strlen-2] < num_list[strlen-1]:
        num_list.append(num_list[strlen-1] - num_list[strlen-2])
    else:
        num_list.append(num_list[strlen-1]*2)
    return num_list