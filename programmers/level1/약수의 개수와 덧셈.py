def solution(left, right):
    answer=0
    for i in range(left, right+1):
        c = 0
        for j in range(1, int(i**(1/2))+1):
            if i%j == 0:
                c = c+1 if j == i**(1/2) else c+2
        answer = answer+i if c%2==0 else answer-i
    return answer

# 개선한 풀이
def solution(left, right):
    answer=0
    for i in range(left, right+1):
        if i**(0.5)==int(i**(0.5)): # 제곱수인지 판단
            answer-=i
        else:
            answer+=i
    return answer
