import sys
sys.setrecursionlimit(10**8)
sys.stdin = open('input.txt')

def binary_search(A):
    if len(A) == 0:
        return
    if len(A) == 1:
        post_numbers.append(A[0])
        return
    root = A[0]
    right_idx = 0
    flag = 0
    for i in range(len(A)):
        if root < A[i]:
            right_idx = i
            flag = 1
            break
    # 라이트가 없다라는 뜻 없을 시에는
    if flag == 0:
        right_idx = 1

    # 이대로면 문제 발생
    binary_search(A[1:right_idx])
    binary_search(A[right_idx:])
    post_numbers.append(root)





numbers = []
for _ in range(10001):
    try:
        x = int(input())
        numbers.append(x)
    except:
        break
post_numbers = []
binary_search(numbers)
for x in post_numbers:
    print(x)

