import sys
sys.setrecursionlimit(10**8)
sys.stdin = open('input.txt')

def DFS(si, sj):
    if visited[si][sj] < 0:
        visited[si][sj] = 0
        for i in range(4):
            ni, nj = si+delta[i][0], sj+delta[i][1]
            if 0<=ni<N and 0<=nj<N and matrix[si][sj] < matrix[ni][nj]:
                visited[si][sj] = max(DFS(ni, nj), visited[si][sj])
        visited[si][sj] += 1
    return visited[si][sj]


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*N for _ in range(N)]
cnt_matrix = [[1] * N for _ in range(N)]
answer = 0

for row in range(N):
    for col in range(N):
        answer = max(answer, DFS(row, col))
print(answer)

