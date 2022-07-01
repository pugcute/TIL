def solution(s):
    # 48 57
    # ord
    answer = ''
    tmp = ''
    dict1 = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    for word in s:
        if 48 <= ord(word) <= 57:
            answer += word
        else:
            tmp += word
            if tmp in dict1:
                answer += str(dict1[tmp])
                tmp = ''
    return int(answer)