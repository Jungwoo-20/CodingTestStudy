def solution(dartResult):
    answer = []
    tmp = ''
    point = {'S': 1, 'D': 2, 'T': 3}
    for i in dartResult:
        if i in point:
            answer.append(int(tmp) ** point[i])
            tmp = ''
        elif i == '*':
            answer[-1] *= 2
            if len(answer) >= 2:
                answer[-2] *= 2
        elif i == '#':
            answer[-1] *= -1
        else:
            tmp += i
    return sum(answer)
