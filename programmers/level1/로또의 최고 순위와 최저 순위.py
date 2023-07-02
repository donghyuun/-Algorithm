def solution(lottos, win_nums):
    answer = []
    c = 0
    for n in win_nums:
        if n in lottos:
            c+=1
    if c > 0 : # 일치하는 숫자가 한개 이상
        answer=[7-(c+lottos.count(0)), 7-c]
    elif lottos.count(0) > 0 : # 일치하는 숫자 한개도 없음 & 0 한개 이상 
        answer = [7-lottos.count(0), 6]
    else: # 일치하는 숫자 한개도 없음 & 0 한개도 없음
        answer = [6,6]
                
    return answer
  
# 다른 풀이(참고)
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1] # 순위 배열

    cnt_0 = lottos.count(0) # 0의 개수
    ans = 0 # 일치하는 숫자의 개수
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans] # 가장 높은 & 낮은 순위를 index로 접근
