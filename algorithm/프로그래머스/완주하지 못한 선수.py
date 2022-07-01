def solution(participant, completion):
    answer = ''
    dict1 = {}
    for val in participant:
        if val in dict1:
            dict1[val] += 1
        else:
            dict1[val] = 1

    for val1 in completion:
        if dict1[val1] == 1:
            del dict1[val1]
        else:
            dict1[val1] -= 1

    return list(dict1.keys())[0]