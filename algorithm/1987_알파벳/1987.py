import sys
sys.stdin = open('input.txt')

def DFS(start_row, start_col):
    result = 1
    to_visits = set([(start_row, start_col, matrix[start_row][start_col])])
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    while to_visits:
        current = to_visits.pop()
        current_row = current[0]
        current_col = current[1]
        visited = current[2]
        for i in range(4):
            next_row = current_row+dxs[i]
            next_col = current_col+dys[i]
            if 0<=next_row<row and 0<=next_col<col and matrix[next_row][next_col] not in visited:
                next_visited = visited + matrix[next_row][next_col]
                to_visits.add((next_row, next_col, next_visited))
                result = max(result, len(next_visited))
                # result 값을 하나 설정해서 비교해야 하는데 안해서 중간에 끊겨서 시간이 걸렸다
    return result


row, col = map(int, input().split())
matrix = [list(input()) for _ in range(row)]
print(DFS(0, 0))


