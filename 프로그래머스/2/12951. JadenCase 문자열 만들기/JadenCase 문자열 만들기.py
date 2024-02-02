def solution(s):
    words = s.split(" ")
    result = []
    for word in words:
        if word:  # 빈 문자열이 아닌 경우에만 처리
            result.append(word[0].upper() + word[1:].lower())
        else:  # 빈 문자열인 경우에도 그대로 유지
            result.append(word)
    return " ".join(result)