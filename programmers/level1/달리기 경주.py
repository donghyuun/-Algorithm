#방법1: 이중 for문 이용 => 시간 초과 발생
def solution(players, callings):
    answer = []
    for c_index, c_value in enumerate(callings, start = 0):
        for p_index, p_value in enumerate(players, start = 0):
            if(c_value == p_value):
                #swap, 파이썬에서는 temp 변수 필요없음
                players[p_index - 1], players[p_index] = players[p_index], players[p_index - 1]
    
    answer = players
    
    return answer

#방법2: 딕셔너리 이용
def solution(players, callings):
    answer = []
    
    #index: 현재 등수, player: 해당 등수의 선수이름
    index_arr = {index: player for index, player in enumerate(players)}
    #player: 선수이름, index: 해당 선수의 현재 등수
    player_arr = {player: index for index, player in enumerate(players)}
    
    for index, name in enumerate(callings):
        rank = player_arr[name]#불린 선수의 현재 등수
        
        #등수: 선수 딕셔너리에서 
        #rank-1: rank순위의 선수, rank: rank-1순위의 선수로 설정 
        index_arr[rank-1], index_arr[rank] = index_arr[rank], index_arr[rank-1]
        
        #선수: 등수 딕셔너리에서 (index_arr가 변경된 상태)
        #현재 불린선수: rank-1, 추월당한 선수(등수 내려옴, index_arr에 적용되어 있음): rank로 설정
        player_arr[name], player_arr[index_arr[rank]] = rank-1, rank 
        
    #딕셔너리에서 값만 추출해 배열로 만듦
    answer = list(index_arr.values())
    
    
    return answer
