import math


# '#'이 붙은 음을 소문자로 변환하는 함수
def change(music):
    return music.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')


def solution(m, musicinfos):
    answer = []
    index = 0
    for musicinfo in musicinfos:
        index += 1
        info = musicinfo.split(',')
        start = info[0].split(':')
        end = info[1].split(':')
        # 시간 체크
        start = (int(start[0]) * 60) + int(start[1])
        end = (int(end[0]) * 60) + int(end[1])
        time = end - start
        # # 제거
        melody = change(info[3])
        # 재생 시간
        melody_dist = len(melody)
        # 파라미터 # 제거
        m = change(m)
        melody *= math.ceil(time / melody_dist)
        melody = melody[:time]
        if m in melody:
            answer.append([time, index, info[2]])
    if not answer:
        return '(None)'
    elif len(answer) == 1:
        return answer[0][-1]
    else:
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return answer[0][-1]


m = "ABCDEFG"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))
