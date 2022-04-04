def quick_sort(A):
    if len(A) <= 1:
        return A
    N = len(A)
    piviot = A[0]
    right = []
    left = []
    for i in range(1, N):
        if piviot > A[i]:
            left.append(A[i])
        else:
            right.append(A[i])
    return quick_sort(left) + [piviot] + quick_sort(right)




numbers = [9, 8, 5, 4, 12, 6]
print(quick_sort(numbers))