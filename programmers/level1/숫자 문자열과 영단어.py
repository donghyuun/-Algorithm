def solution(s):
    dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"} 
    for k in dic.keys():
        if k in s:
            s = s.replace(k,dic[k])
    return int(s)
  
# keys() 함수말고 items() 함수 사용했을때
def solution(s):
    dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"} 
    for k, v in dic.items():
        if k in s:
            s = s.replace(k,v)
    return int(s)
