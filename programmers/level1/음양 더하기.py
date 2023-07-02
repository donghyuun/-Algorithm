def solution(absolutes, signs):
    ans = 0
    for n, b in zip(absolutes, signs):
        if b == True:
            ans += n
        else:
            ans -= n
    return ans
