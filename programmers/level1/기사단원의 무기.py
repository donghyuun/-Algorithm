def solution(number, limit, power):
    answer = 0
    def count(n):
        cnt = 0
        for i in range(1, int(n**(1/2))+1):
            if n%i==0: 
                if n == 1 or i**2 == n: cnt+=1
                else: cnt+=2 
        return cnt
    
    for i in range(1, number+1):
        res = count(i)
        if res > limit:
            answer+=power
        else:
            answer+=res
    
    return answer
