from collections import defaultdict
def solution(id_list, report, k):
    answer = [0] * len(id_list) # 결과를 담는 배열
    report = set(report) # 한 사람이 같은 사람을 여러번 신고할 수 있지만 의미가 없음
    stop = [] # 정지 목록자들
    init = defaultdict(set)
    singo = defaultdict(int)
    for i in report:
        start, end = i.split(" ")
        init[start].add(end) # 신고자가 신고한 사람들을 저장
        singo[end] += 1 # 신고 당한 사람을 찾아 카운팅
        if singo[end] == k: # k번 이상 신고 당한 경우
            stop.append(end) # 정지 목록 대상
    for s in stop: # 정자 목록 대상들을 탐색
        for i in range(len(id_list)): # 유저 목록 별로 탐색
            if s in init[id_list[i]]: # 딕셔너리 해당 유저의 value값중에 s가 있는 경우 해당 위치를 찾아서 +1
                answer[i] += 1
    return answer

# 프로그래머스 참고 코드
# 신고 당한 사람의 정보만 저장한 후
# 누적 횟수가 k이상인 경우 신고한 사람인 경우
# 신고한 사람을 찾아 +1
def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
print(solution(id_list, report, k))
