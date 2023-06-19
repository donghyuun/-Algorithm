def solution(babbling):
    answer = 0
    
    for bab in babbling:
        for word in ["aya", "ye", "woo", "ma"]:
            if word in bab:
                # 같은 문자열 연달아 존재O
                if word*2 in bab: 
                    break
                # 같은 문자열 연달아 존재X => 해당 문자열을 공백으로 대체한 후 재검
                else: 
                    bab=bab.replace(word, " ")
        if len(bab.strip()) == 0:
            answer+=1
    
    return answer
