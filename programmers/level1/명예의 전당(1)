#첫번째 풀이
def solution(k, score):
    answer = [] #결과 배열(최하위 점수 매번 기록)
    arr = [] #명예의 전당
    for sc in score:
        inserted = 0
        if(len(arr) == 0): 
            arr.append(sc)
            answer.append(sc)
            continue

        for idx, num in enumerate(arr):
            if sc >= num:
                arr.insert(idx, sc)
                inserted = 1
                break
        # arr의 길이가 k보다 작으면서 arr을 탐색했을때 오늘의 점수보다 같거나 작은 경우가 없을때
        if(len(arr) < k and not inserted):
            arr.append(sc)
            
        answer.append(arr[k-1]) if len(arr) >= k else answer.append(arr[len(arr)-1]) 
        
    return answer

#두번째 풀이
def solution(k, score):
    answer = [] #결과 배열(최하위 점수 매번 기록)
    arr = [] #명예의 전당
    for sc in score:
        inserted = 0
        for idx, num in enumerate(arr):
            if sc >= num:
                arr.insert(idx, sc)
                inserted = 1
                break
        # arr의 길이가 k보다 작으면서 arr을 탐색했을때 오늘의 점수보다 같거나 작은 경우가 없을때
        if(len(arr) < k and not inserted):
            arr.append(sc)
            
        answer.append(arr[k-1]) if len(arr) >= k else answer.append(arr[len(arr)-1]) 
        
    return answer

#세번째 풀이
def solution(k, score):
    answer = [] 
    arr = [] 
    
    for s in score:
        arr.append(s)
        
        if len(arr) > k:
            arr.remove(min(arr))
            
        answer.append(min(arr))
                   
    return answer
