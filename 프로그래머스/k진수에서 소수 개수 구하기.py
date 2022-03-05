import math


def solution(n, k):
    answer = 0
    # k진수 만들기
    word = ''
    while n:
        word += str(n % k)
        n //= k
    # 숫자 뒤집기
    word = word[::-1]
    matrix = word.split('0')

    res = []
    for ma in matrix:
        # 0을 기준으로 잘랐을 때 공백을 제거
        if len(ma) > 0:
            res.append(ma)
    # 예상되는 숫자만 소수인지 확인
    matrix = list(map(int, res))
    for i in matrix:
        flag = True
        # 소수의 최소 숫자 판별
        if i < 2:
            continue
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            answer += 1
    return answer


n = 437674
k = 3
print(solution(n, k))
