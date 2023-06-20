# 첫번째 풀이
def solution(number):
    answer=0
    for i1 in range(len(number)):
        for i2 in range(i1+1, len(number)):
            for i3 in range(i2+1, len(number)):
                if number[i1]+number[i2]+number[i3] == 0:
                    answer+=1
    return answer

# 두번째 풀이
def solution (number) :
    from itertools import combinations
    answer = 0
    
    # 예) 1,3,-4  3,1,-4 가 동일하게 취급되기 때문에 조합을 사용한다.
    # 중복 없는 조합 사용(3명이 각각 다른 학생이어야 하기 때문)
    arr = list(combinations(number, 3))
    for tup in arr:
        if(sum(tup) == 0):
            answer+=1
    return answer
