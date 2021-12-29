def solution(files):
    answer = []
    for file in files:
        head, num, tail = '', '', ''
        num_flag = False
        for i in range(len(file)):
            if file[i].isdigit():
                num += file[i]
                num_flag = True
            elif not num_flag:
                head += file[i]
            else:
                tail += file[i:]
                break
        answer.append([head, num, tail])
    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(res) for res in answer]


inp = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

print(solution(inp))
