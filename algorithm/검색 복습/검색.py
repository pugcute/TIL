import sys
sys.stdin = open('input.txt')

def selection_sort(numbers):
    for i in range(len(numbers)-1):
        min_idx = i
        for j in range(i, len(numbers)):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers

def sequence_search(numbers, N):
    N_cnt = numbers.count(N)
    cnt = 0
    idx_list = []
    for i in range(len(numbers)):
        if numbers[i] == N:
            cnt += 1
            idx_list.append(i)
        if N_cnt == cnt and N_cnt > 0:
            break
    if cnt == 0:
        return f'{N}은 존재하지 않습니다.'
    else:
        return f'{N}은 {N_cnt}만큼 존재하며, INDEX는 {idx_list}입니다.'

def sequence_search2(numbers, val):
    N = len(numbers)
    i = 0
    while i < N and numbers[i] != val:
        i += 1
    if i < N:
        return f'{N}은 있습니다. {i}'
    else:
        return f'{N}은 존재하지 않습니다.'

def binary_search(numbers, val):
    start = 0
    end = len(numbers)-1

    while start <= end:
        middle = (start + end) // 2
        if numbers[middle] == val:
            return middle, f'{val}은 존재함'
        elif numbers[middle] > val:
            end = middle - 1
        else:
            start = middle + 1
    return -1

numbers = list(map(int, input().split()))
numbers = selection_sort(numbers)
print(binary_search(numbers, 9))
