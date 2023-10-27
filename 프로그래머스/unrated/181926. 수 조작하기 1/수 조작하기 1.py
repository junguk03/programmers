def solution(n, control):
    
    return n + 10*(control.count('d')-control.count('a')) + (control.count('w')-control.count('s'))