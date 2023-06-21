def solution(survey, choices):
    answer = ''
    cn_score = {"1":3,"2":2,"3":1,"4":0,"5":1,"6":2,"7":3}
    pn_score = {"R": 0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for i, cn in enumerate(choices):
        # n = 3 일때 cn_score["3"] 에 접근하기 위해서는 n 을 문자로 바꿔야 접근할 수 있다.
        if 3 >= cn: pn_score[survey[i][0]]+=cn_score[str(cn)]
        elif 5 <= cn: pn_score[survey[i][1]]+=cn_score[str(cn)]
        else: continue 
    
    arr = list(pn_score.items())
    for i in range(0, len(arr), 2):
        if arr[i][1] > arr[i+1][1]: answer+=arr[i][0]
        elif arr[i][1] < arr[i+1][1]: answer+=arr[i+1][0]
        else: answer+=arr[i][0]
        
    return answer
