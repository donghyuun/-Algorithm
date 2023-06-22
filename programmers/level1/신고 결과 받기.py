def solution(id_list, report, k):
    call_dic={}# 신고한 유저와 신고당한 유저 매핑
    called_dic={} # 신고당한 유저와 신고한 유저 매핑
    ans_dic={}
    for usr_name in id_list: ans_dic[usr_name]=0
    for s in report:
        sp = s.split(' ')
        if sp[0] in call_dic: # 신고한 전적이 있는 유저인 경우
            if sp[1] not in call_dic[sp[0]]: # 해당 유저를 처음 신고하는 경우
                call_dic[sp[0]].append(sp[1])
        else: call_dic[sp[0]] = [sp[1]] # 신고한 전적이 없는 경우
        
        if sp[1] in called_dic: # 신고당한 전적이 있는 유저인 경우
            if sp[0] not in called_dic[sp[1]]:
                called_dic[sp[1]].append(sp[0])
        else: called_dic[sp[1]] = [sp[0]] # 신고당한 전적이 없는 경우

    for key in list(called_dic.keys()):
        if len(called_dic[key]) >= k: #신고 당한 횟수가 k번 이상인 경우
            for call_name in called_dic[key]: #해당 유저를 신고한 유저들을 모은 배열
                ans_dic[call_name]+=1
    
        
    return list(ans_dic.values())

# 다른 풀이(참고)
def solution(id_list, report, k):
    called_dic={name:0 for name in id_list} 
    answer=[0]*len(id_list) # 결과 배열 
    for r in set(report): # 중복된 신고 제외
        called_dic[r.split()[1]]+=1 # 신고당한유저/신고당한횟수 딕셔너리
    
    for r in set(report):
        if called_dic[r.split()[1]] >= k: # 신고당한횟수 >= k 이면
            answer[id_list.index(r.split()[0])]+=1 # 신고한유저에게 알림+1
            
        
    return answer
