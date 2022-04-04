
def merge_sort(A):
    if len(A) == 1:
        return A
    N = len(A)
    middle = N // 2
    left = A[:middle]
    right = A[middle:N]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = [0] * (len(left) + len(right))
    idx = 0
    left_idx = right_idx = 0
    left_len = len(left)
    right_len = len(right)

    while left_idx < left_len or right_idx < right_len:
        if left_idx < left_len and right_idx < right_len:
            if left[left_idx] < right[right_idx]:
                result[idx] = left[left_idx]
                left_idx += 1
                idx += 1
            else:
                result[idx] = right[right_idx]
                right_idx += 1
                idx += 1
        elif left_idx < left_len:
            result[idx] = left[left_idx]
            left_idx += 1
            idx += 1
        elif right_idx < right_len:
            result[idx] = right[right_idx]
            right_idx += 1
            idx += 1
    return result

numbers = [7, 5, 4, 1, 2, 10, 3, 6, 9, 8]
print(merge_sort(numbers))