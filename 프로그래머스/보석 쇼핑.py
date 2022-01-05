import sys
def solution(gems):
    answer = []
    short = sys.maxsize
    start, end = 0, 0
    dist = len(set(gems))
    dic = dict()
    while end < len(gems):
        if gems[end] not in dic:
            dic[gems[end]] = 1
        else:
            dic[gems[end]] += 1
        end += 1
        if len(dic) == dist:
            while start < end:
                if dic[gems[start]] > 1:
                    dic[gems[start]] -= 1
                    start += 1
                elif short > end - start:
                    short = end - start
                    answer = [start + 1, end]
                    break
                else:
                    break
    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
