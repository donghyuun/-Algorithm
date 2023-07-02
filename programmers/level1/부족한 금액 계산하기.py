def solution(price, money, count):
    answer=0
    for i in range(1, count+1):
        answer+=i*price
    return max(0, answer-money)
