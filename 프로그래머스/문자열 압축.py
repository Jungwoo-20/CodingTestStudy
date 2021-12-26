def solution(s):
    answer = []
    res = ''
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        cnt = 1
        tmpstr = s[:i]
        for j in range(i, len(s), i):
            if s[j:j + i] == tmpstr:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''
                res += str(cnt) + tmpstr
                tmpstr = s[j:j + i]
                cnt = 1
        if cnt == 1:
            cnt = ''
        res += str(cnt) + tmpstr
        answer.append(len(res))
        res = ''
    return min(answer)


matrix = ['aabbaccc', 'ababcdcdababcdcd', 'abcabcdede', 'abcabcabcabcdededededede', 'xababcdcdababcdcd']
for i in matrix:
    print(solution(i))
