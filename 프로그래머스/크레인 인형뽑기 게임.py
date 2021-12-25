def solution(board, moves):
    answer = 0
    stk = []
    for i in range(len(moves)):
        moves[i] = moves[i] - 1
    for i in moves:
        for j in board:
            if j[i] != 0:
                stk.append(j[i])
                j[i] = 0
                break
        if len(stk) >= 2 and stk[-1] == stk[-2]:
            answer += 2
            stk = stk[:-2]
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
