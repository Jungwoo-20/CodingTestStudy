def check(u):
    left = []
    for i in range(len(u)):
        if not left:
            if u[i] == '(':
                left.append(u[i])
            else:
                return False
        else:
            if u[i] == '(':
                left.append(u[i])
            else:
                if left[-1] == '(':
                    left.pop()
                else:
                    return False
    return True


def first(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i + 1], p[i + 1:]

def four(u,v):
    answer = '('
    answer += solution(v)
    answer += ')'
    for i in u[1:len(u) - 1]:
        if i == '(':
            answer += ')'
        else:
            answer += '('
    return answer
def solution(p):
    # 1
    if not p:
        return ''
    # 2
    u, v = first(p)
    # 3
    if check(u):
        return u + solution(v)
    else:
        # 4
        return four(u,v)


print(solution('()))((()'))
