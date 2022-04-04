#sudoku
import sys
#값 입력받기
graph = []
blank = []
for i in range(9):
    graph.append(list(map(int,sys.stdin.readline().split())))

# 0인 좌표 구하기
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i,j))

#열, 행, 3X3 확인
def checkRow(x,a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkColumn(y,a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkSquare(x,y,a):
    m = x // 3 * 3
    n = y // 3 * 3
    for i in range(m, m+3):
        for j in range(n, n+3):
            if a == graph[i][j]:
                return False
    return True

def dfs(idx):

    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    x = blank[idx][0]
    y = blank[idx][1]
    for i in range(1,10):
        if checkRow(x,i) and checkColumn(y,i) and checkSquare(x,y,i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0

dfs(0)