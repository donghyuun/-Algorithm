#첫번째 시도(실패, 런타임 에러)
def solution(ingredient):
    answer = 0
    qc = 0
    pc = 0
    c = 0
    for v in ingredient:
        c+=1
        # 카운트 시작이면서 v가 1일때
        if pc==0 and v==1: 
            pc=1
            qc=0
            print("카운트 시작&v=1, pc: ", pc, "qc: ", qc, "ans: ", answer);
            continue
        # 카운트 시작이면서 v가 1이 아닐때
        elif pc == 0 and v != 1:
            print("카운트 시작&V!=1, pc: ", pc, "qc: ", qc, "ans: ", answer);
            continue
        # 직전값이 1이었는데 또 1인 경우
        elif pc == 1 and v == 1:
            qc=1
            print("직전값 1, 또 1, pc: ", pc, "qc: ", qc, "ans: ", answer);
            continue
        # 직전값보다 1증가한 값이 온 경우(O)
        elif v == pc+1:
            pc+=1
            print("직전값보다 1증가한 값, pc: ", pc, "qc: ", qc, "ans: ", answer);
        # 123 다음에 1이 온 경우(O)
        elif pc==3 and v == 1:
            answer+=1
            pc = qc 
            qc = 0
            print("1,2,3 다음에 1, pc: ", pc, "qc: ", qc, "ans: ", answer);
        else:
            pc = qc
            qc = 0
            print("가다가 막히는 경우, pc: ", pc, "qc: ", qc, "ans: ", answer);
    return answer

#두번째 시도(실패, 런타임 에러)
def solution(ingredient):
    answer = 0
    cnt = 0
    
    while True:
        del_arr = []
        pc = 0
        cnt = 0
        oor = False
        for idx, v in enumerate(ingredient):
            #뒤에서 3번째인 경우-> 그냥 while문 빠져나오면 됨(끝까지 확인 다 함)
            if idx == len(ingredient) - 3: 
                oor = True
                break;
            # pass 하는 경우
            if pc > 0: 
                pc-=1
                continue
            # idx부터 idx+3까지 재료 순서가 일치하는지 검사
            elif ingredient[idx] == 1 and ingredient[idx] + 1 == ingredient[idx+1] and ingredient[idx+1] + 1 == ingredient[idx+2] and ingredient[idx+3] == 1 :
                # 일치하는 경우, 일치의 시작부분 idx를 저장함
                del_arr.append(idx)
                pc=3 #패스시킬 횟수
                answer+=1 #답 증가시킴
                cnt = 1 #찾았다고 표시(배열안에 존재한다. 한번 더 돌 수 있다)
        if cnt == 0:# 배열내에 올바른 재료 순서가 없는 경우, while문 빠져나옴
            break;
        if oor == False and cnt == 0:
            break;
            
        for i in range(len(del_arr)+1, 0, -1):
            del ingredient[del_arr[i]]
            
    return answer

#세번째 시도(성공)
def solution(ingredient):
    answer = 0
    s = []
    for v in ingredient:
        s.append(v)
        if(s[-4: ] == [1,2,3,1]):
            answer+=1
            del s[-4: ]    
            
    return answer
