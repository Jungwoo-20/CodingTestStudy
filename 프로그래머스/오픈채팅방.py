def solution(record):
    answer = []
    dic = dict()
    res = []
    for i in record:
        tmp = i.split(' ')
        # leave
        if len(tmp) == 2:
            answer.append(['Leave', tmp[1]])
        # enter, change
        else:
            if tmp[0] == 'Enter':
                dic[tmp[1]] = tmp[2]
                answer.append(['Enter', tmp[1]])
            else:
                dic[tmp[1]] = tmp[2]
    for i in answer:
        if i[0] == 'Enter':
            res.append(dic[i[1]] + "님이 들어왔습니다.")
        else:
            res.append(dic[i[1]] + "님이 나갔습니다.")
    return res


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))