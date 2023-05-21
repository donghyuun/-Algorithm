def solution(park, routes):
    #정사각형 배열이 아니라 직사각형 배열이 될 수도 있음 <- 놓치면 안됨
    length_x = len(park)#행의 크기
    length_y = len(park[0])#열의 크기
    
    answer = []
    x, y = (0, 0) 
    
    #시작 위치 설정
    for index_x, arr in enumerate(park):
        for index_y, char in enumerate(arr):
            if(isinstance(char, str) and char == 'S'):
                #x = index_x, y = index_y <- 이거 안됨!
                x, y = (index_x, index_y)
            
    def check(dir, n):
        if dir == 'E': #동쪽, 열을 움직여야 함
            for index in range(y, y+n+1):
                if park[x][index] == 'X':
                    return False
            return True
        elif dir == 'S': #남쪽, 행을 움직여야 함
            for index in range(x, x+n+1):
                if park[index][y] == 'X':
                    return False
            return True
        elif dir == 'W': #서쪽, 열을 움직여야 함
            for index in range(y, y-n-1, -1):
                if park[x][index] == 'X':
                    return False
            return True
        elif dir == 'N': #북쪽, 행을 움직여야 함
            for index in range(x, x-n-1, -1):
                if park[index][y] == 'X':
                    return False
            return True
    
    for route in routes:#2차원 배열 routes를 돌면서
        arr = route.split(' ')
        dir = arr[0]#방향
        num = int(arr[1])#갈 칸수
        
        #공원 벗어나거나 중간에 장애물 있을때
        #동쪽일때
        if(dir == 'E'):
            if(y + num  > length_y - 1 or not check(dir, num)):
                continue
            else: 
                y = y + num
        #남쪽일때
        elif(dir == 'S'):
            if(x + num > length_x - 1 or not check(dir, num)): 
                continue
            else:
                x = x + num
        #서쪽일때
        elif(dir == 'W'):
            if(y - num < 0 or not check(dir,num)):
                continue
            else:
                y = y - num
        #북쪽일때
        elif(dir == 'N'):
            if(x - num < 0 or not check(dir, num)):
                continue
            else:
                x = x - num
    
    answer.append(x)
    answer.append(y)

    return answer
