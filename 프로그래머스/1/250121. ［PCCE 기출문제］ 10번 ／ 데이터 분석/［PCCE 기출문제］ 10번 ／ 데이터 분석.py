def solution(data, ext, val_ext, sort_by):
    result = []
    by = ["code", "date", "maximum", "remain"]
        
    for i in range(len(data)):
        if data[i][by.index(ext)] < val_ext:
            result.append(data[i])
    
    result.sort(key = lambda x:x[by.index(sort_by)])
    return result