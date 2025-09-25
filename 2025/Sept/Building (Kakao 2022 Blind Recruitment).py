def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    diff = [[0]*(m+2) for _ in range(n+2)]
    
    for t,r1,c1,r2,c2,degree in skill:
        if (t==1):
            degree = -degree
        diff[r1][c1] += degree
        diff[r1][c2+1] -= degree
        diff[r2+1][c1] -= degree
        diff[r2+1][c2+1] += degree
    
    for i in range(n+2):
        for j in range(1,m+2):
            diff[i][j] += diff[i][j-1]
            
    for j in range(m+2):
        for i in range(1,n+2):
            diff[i][j] += diff[i-1][j]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] + diff[i][j]>0:
                answer+=1
    
    return answer
