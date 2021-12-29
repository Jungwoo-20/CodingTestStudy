def solution(msg):
    answer = []
    dic = {}
    index = 27
    word = ''
    for i in range(26):
        dic[chr(65 + i)] = i + 1
    c = 0
    while c < len(msg):
        word += msg[c]
        if word in dic.keys():
            c += 1
        else:
            dic[word] = index
            index += 1
            word = word[:-1]
            answer.append(dic[word])
            word = ''
    else:
        answer.append(dic[word])
    return answer


msg = 'KAKAO'
print(solution(msg))
