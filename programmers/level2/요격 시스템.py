def solution(targets):
    answer=0
    pivot=0
    targets.sort(key=lambda x: (x[0],x[1]))
    
    for t in targets:
        if pivot <= t[0]:
            answer+=1
            pivot=t[1]
        else:
            pivot=min(t[1], pivot)
    return answer
