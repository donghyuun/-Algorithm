def solution(a, b, n):
    answer = 0
    while n >= a:
        cock=(n//a)*b # 빈병 n개로부터 콜라 cock 개 얻음
        answer+=cock # 콜라 얻은 개수 누적합에 추가
        emt=n%a # 사용되지 못한 빈병 개수
        n = cock+emt # 콜라 마시고 다시 빈병 만들어진것 기존 빈병에 추가
    return answer
