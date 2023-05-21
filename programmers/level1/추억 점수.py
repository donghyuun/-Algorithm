def solution(name, yearning, photo):
    answer=[]
    
    #딕셔너리 생성
    name_arr = dict(zip(name, yearning))
    
    for arr in photo:
        sum = 0
        for name in arr:
            if(name in name_arr): sum += name_arr[name]
        
        answer.append(sum)
    
    return answer
