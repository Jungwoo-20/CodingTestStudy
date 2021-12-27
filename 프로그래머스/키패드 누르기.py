def solution(numbers, hand):
    answer = ''
    matrix = {1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    left = [3, 0]
    right = [3, 2]
    for num in numbers:
        now = matrix[num]
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            left = now
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            right = now
        else:
            # 왼손, 오른손 거리 계산
            left_dist, right_dist = cal_dist(left, right, now)
            if left_dist < right_dist:
                answer += 'L'
                left = now
            elif left_dist > right_dist:
                answer += 'R'
                right = now
            # 왼손 잡이, 오른손 잡이 구분
            else:
                if hand == 'left':
                    answer += 'L'
                    left = now
                else:
                    answer += 'R'
                    right = now
    return answer


def cal_dist(left, right, now):
    left_dist = 0
    right_dist = 0
    for x, y, z in zip(left, right, now):
        left_dist += abs(z-x)
        right_dist += abs(z-y)
    return left_dist, right_dist


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
