import sys
sys.stdin = open('input.txt')
N = int(input())
students = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    students.append([age, name])

t = sorted(students, key=lambda x: x[0])
for i in range(N):
    print(t[i][0], t[i][1])
'''
for i in range(N-1):
    min_idx = i
    for j in range(i, N):
        if int(students[min_idx][0]) > int(students[j][0]):
            min_idx = j
    students[i], students[min_idx] = students[min_idx], students[i]
    print(' '.join(students[i]))
'''
# 선택 정렬시 오류 생김, 오류 복잡도 n의 2승이나, 파이썬 솔트는 nlogn
