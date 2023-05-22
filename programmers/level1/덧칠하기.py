def solution(n, m, section):
    answer = 0
    #첫 페인트 칠 시작할 구역
    cur_idx = section[0]
    
    for idx, empty_idx in enumerate(section):
        #첫 페인트 작업(무조건)
        if(idx == 0):
            cur_idx = cur_idx + (m - 1) #자신도 칠해야 하므로
            answer = answer + 1
            continue
        #그 다음부터의 작업(현재 empty_idx 구역이 이전 작업때 칠해졌었는지 검사)
        if(cur_idx < empty_idx):
            cur_idx = empty_idx  #<- 그다음으로 처음 마주하는 빈구역을 현재 위치한 구역으로 설정(핵심)
            cur_idx = cur_idx + (m - 1) #자신도 칠해야 하므로
            answer = answer + 1
            continue
        
    return answer
