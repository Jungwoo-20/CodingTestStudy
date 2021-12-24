def solution(s):
    dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
            'nine': '9'}
    answer = ''
    tmp = ''
    for i in s:
        tmp += i
        if i.isdigit():
            answer += str(i)
            tmp = ''
        elif tmp in dict.keys():
            answer += str(dict[tmp])
            tmp = ''
    return int(answer)