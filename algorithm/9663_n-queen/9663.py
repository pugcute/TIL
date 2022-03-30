import sys
sys.stdin = open('input.txt')

def check(row):
    for prev_row in range(row):
        if queens[row] == queens[prev_row] or abs(queens[row]-queens[prev_row]) == abs(row-prev_row):
            # 이 식 때문에 꽤 걸림, 대각선 판정 조건이 귀찮았음
            return False
    return True

def dfs(row):
    global answer
    if row == N:
        answer += 1
        return
    else:
        for i in range(N):
            queens[row] = i
            flag = check(row)
            if flag is False:
                continue
            else:
                dfs(row+1)
    # 백준에선 continue를 써도 python3에서는 시간초과이나, pypy에서는 통과


N = int(input())
queens = [0]*N
answer = 0
dfs(0)
print(answer)


