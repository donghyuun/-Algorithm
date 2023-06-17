#첫번째 풀이(시간 초과)
def solution(k, m, score):
    s_len = len(score)
    answer = 0
    cnt = 0
    for i in range(s_len):
        maxS = max(score)
        score.remove(max(score))
        cnt+=1
        if cnt%m == 0:
            answer+=m*maxS

    return answer


#두번째 풀이
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(m-1, len(score), m):
        answer+=m*score[i]

    return answer
