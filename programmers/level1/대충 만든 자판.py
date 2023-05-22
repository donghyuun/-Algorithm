def solution(keymap, targets):
    answer = []
    hs = {}
    for arr in keymap:
        for index, char in enumerate(arr):
            if(char in hs):
                hs[char] = min(hs[char], index + 1)
            else:
                hs[char] = index + 1

    for string in targets:
        count, flag = 0, False
        for char in string:
            if(not char in hs): 
                answer.append(-1)
                flag = True
                break
            count = count + hs[char]
        if(not flag): answer.append(count)
            
    
    return answer
