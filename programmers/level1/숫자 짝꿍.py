def solution(X, Y):
    dic = {}
    answer=''
    listX = list(X)
    listY = list(Y)
    for x in listX:
        if x not in dic:
            n = min(listX.count(x), listY.count(x))
            if n != 0: dic[x] = n
    
    arr = sorted(dic.items(), reverse=True)
    if len(arr) == 0: return "-1"
    elif arr[0][0] == '0': return "0" 
   
    for tup in arr:
        for i in range(0, tup[1]):
            answer+=tup[0]

    return answer
