def solution(new_id):
    result = ''
    new_id = new_id.lower()
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            result += i
    while '..' in result:
        result = result.replace('..', '.')
    if result[0] == '.':
        result = result[1:] if len(result) > 1 else '.'
    if result[-1] == '.':
        result = result[:-1]
    if result == '':
        result = 'a'
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == '.':
            result = result[:-1]
    while len(result) < 3:
        result += result[-1]
    return result