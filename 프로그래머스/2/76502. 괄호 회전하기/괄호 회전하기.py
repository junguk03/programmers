def solution(s):
    count = 0
    for i in range(len(s)):
        stack = []
        for j in s:
            if not stack:
                stack.append(j)
                continue
            if stack[-1] + j == "()" or stack[-1] + j == "[]" or stack[-1] + j == "{}":
                stack.pop()
            else:
                stack.append(j)
        if not stack:
            count += 1
        s = s[1:] + s[0]
            
    return count