import math


def cal(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m


def solution(fees, records):
    answer = []
    # 기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
    dt, dw, ut, uw = fees
    # 차량 입출차를 위한 딕셔너리
    dic = dict()
    for re in records:
        time, number, flag = re.split(' ')
        number = int(number)
        time = cal(time)  # 분으로 환산
        # 최초 등록이 아닌 경우
        if number in dic:
            dic[number].append([time, flag])
        else:
            dic[number] = [[time, flag]]
    dic = list(dic.items())
    dic.sort(key=lambda x: x[0])  # 차량 번호별로 정렬
    for di in dic:
        t = 0  # 주차장에 있었던 시간을 체크
        for d in di[1]:
            if d[1] == 'IN':
                t -= d[0]
            else:
                t += d[0]
        if di[1][-1][1] == 'IN':
            t += cal('23:59')
        # 기본요금 시간인 경우 기본 요금
        if t<=dt:
            answer.append(dw)
        else:
            answer.append(dw + math.ceil((t-dt)/ut)*uw)
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
