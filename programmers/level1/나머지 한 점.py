def solution(v):
    answer = []

    arrX = []
    arrY = []
    
    for sub in v:
        # x좌표에 대해 검사
        if(sub[0] in arrX):
            arrX.remove(sub[0])
        else:
            arrX.append(sub[0])
        
        # y좌표에 대해 검사
        if(sub[1] in arrY):
            arrY.remove(sub[1])
        else:
            arrY.append(sub[1])
        
    answer.append(arrX[0])
    answer.append(arrY[0])

    return answer
