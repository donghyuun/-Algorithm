def solution(s):
    ch_dict = {}
    answer = []
    
    for index, ch in enumerate(s):
        if ch in ch_dict:
            answer.append(index - ch_dict[ch])
            ch_dict[ch] = index
        else:
            answer.append(-1)
            ch_dict[ch] = index
    
    return answer
