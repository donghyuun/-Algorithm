def solution(wallpaper):
    start_x, start_y, end_x, end_y = 51,51,-1,-1
    answer = []
    
    for row, arr in enumerate(wallpaper):
        for col, char in enumerate(arr):
            if(char == '#'):
                #시작점 설정
                if row < start_x : start_x = row
                if col < start_y : start_y = col
                
                #끝점 설정
                if row > end_x : end_x = row 
                if col > end_y : end_y = col 
            
    answer.append(start_x)
    answer.append(start_y)
    answer.append(end_x + 1)
    answer.append(end_y + 1)
    return answer
