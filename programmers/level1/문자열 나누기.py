#첫번째 풀이
def solution(s):
    answer = 0
    arr = list(s)

    while(1):
        s_cnt = 1
        d_cnt = 0
        first = arr[0]
        # 배열 길이 1
        if(len(arr) == 1):
            answer = answer + 1  
            break

        # 배열 길이 2이상
        for idx in range(1, len(arr)):
            # 첫 문자와 다른 경우 
            if(arr[idx] != first):
                d_cnt = d_cnt + 1
            # 첫 문자와 동일한 경우
            else:
                s_cnt = s_cnt + 1
            # 카운트가 같은 경우
            if(d_cnt == s_cnt):
                answer = answer + 1     
                # idx가 배열의 끝 인덱스인 경우 => answer 리턴
                if(idx+1 == len(arr)):
                    return answer
                # 그렇지 않은 경우 => arr 인덱스 idx + 1 부터로 변경
                else:
                    arr = arr[idx+1: ]
                    break;
            # 카운트가 같지 않으면서 배열의 끝에 도달한 경우
            if(idx+1 == len(arr)):
                answer = answer + 1
                return answer

    return answer

#두번째 풀이
def solution(s):
    answer = 0
    s_cnt = 0
    d_cnt = 0
    pivot = ''
    
    # 이렇게 풀려면 첫 문자인 경우에도 s_cnt == d_cnt 적용해서 answer+=1 적용시켜줄 수 밖에 없음
    # => 맨 마지막에 남은 문자열에 대해 answer+=1 해줄 필요 없게 됨
    for ch in s: 
        # 직전 for문에서 이미 문자 카운트가 동일해진 경우임 
        if(s_cnt == d_cnt):
            answer+=1
            a = ch #다시 시작하기 위해 pivot을 설정
        
        if(ch == a):#현재 문자가 pivot인 경우(pivot과 동일한 경우 포함)
            s_cnt+=1
        else:
            d_cnt+=1
        
    return answer
