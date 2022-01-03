def solution(n, t, m, timetable):
    answer = 0
    bustime = [9 * 60 + t * i for i in range(n)]
    crewtime = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    crewtime.sort()
    idx = 0
    for bus in bustime:
        cnt = 0
        while cnt < m and idx < len(crewtime) and crewtime[idx] <= bus:
            cnt += 1
            idx += 1
        if cnt < m:
            answer = bus
        else:
            answer = crewtime[idx - 1] - 1
    return str(answer//60).zfill(2) + ':' + str(answer%60).zfill(2)


n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable))
