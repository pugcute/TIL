def solution(array, commands):
    answers = []
    for command in commands:
        i = command[0]-1
        k = command[1]
        j = command[2]-1
        tmp_array = array[i:k]
        tmp_array.sort()
        answer = tmp_array[j]
        answers.append(answer)

    return answers