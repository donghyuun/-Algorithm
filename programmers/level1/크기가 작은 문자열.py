def solution(t, p):
    answer = 0
    for index, num in enumerate(t):
        temp = t[index : index + len(p)]
        if temp <= p: answer += 1
        
        if index + len(p) - 1 == len(t) - 1:
            break;
    return answer
