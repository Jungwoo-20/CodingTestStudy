from itertools import permutations


def flag(user, banned_id):
    for i in range(len(banned_id)):
        if len(user[i]) != len(banned_id[i]):
            return False
        for j in range(len(user[i])):
            if banned_id[i][j] == '*':
                continue
            if user[i][j] != banned_id[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    users = permutations(user_id, len(banned_id))
    answer = []
    for user in users:
        if flag(user, banned_id):
            user = set(user)
            if user not in answer:
                answer.append(user)
    return len(answer)
