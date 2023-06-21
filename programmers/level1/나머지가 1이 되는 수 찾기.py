def solution(n):
    x=1
    r=0
    while r!=1:
        r=n%x
        x+=1
    return x-1
