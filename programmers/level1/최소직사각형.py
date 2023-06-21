def solution(sizes):
    l_max=0
    r_max=0
    for s in sizes:
        if s[0] > l_max: l_max=s[0]
        if s[1] > l_max: l_max=s[1]
    for s in sizes:
        if min(s[0],s[1])> r_max: r_max = min(s[0],s[1])
            
    return l_max*r_max
