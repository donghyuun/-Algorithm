def solution(food):
    answer = ''
    a_list = list(answer)
    od = len(food)-1
    a_list.append('0')
    for i in range(len(food)-1, 0, -1):
        f = food[i]-1 if food[i]%2==1 else food[i]
        for _ in range(1,f//2+1):
            a_list.insert(0,od)
            a_list.append(od)
        od-=1
    answer = ''.join(str(s) for s in a_list)
    return answer
