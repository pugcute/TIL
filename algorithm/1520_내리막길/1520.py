import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

def DFS(si, sj):
    global answer
    if si == 0 and sj == 0:
        return 1
    if visited[si][sj] == -1:
        visited[si][sj] = 0
        for i in range(4):
            ni = si + delta[i][0]
            nj = sj + delta[i][1]
            if 0<=ni<row and 0<=nj<col and matrix[ni][nj] > matrix[si][sj]:
                visited[si][sj] += DFS(ni, nj)
    return visited[si][sj]

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
row, col = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]
visited = [[-1]*col for _ in range(row)]
print(DFS(row-1, col-1))

# 단순 dfs로는 런타임에러, dp 반드시 사용해야 하며, 이때는 거꾸로 하는 식으로 해서 올릴 것