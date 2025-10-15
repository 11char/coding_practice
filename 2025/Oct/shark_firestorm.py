from sys import setrecursionlimit
setrecursionlimit(10**6)

def rotate_grid(grid, n):
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = grid[i][j]
    return rotated

def melt_ice(board):
     # Can't do following due to updating to early also a little hard to read
    # for row,r in board:
    #     for cell,c in row:
    #         #bottom, top, left, right indices of cell
    #         B,T,L,R = r-1,r+1,c-1,c+1
    #         existing_ice = 0
    #         if(0<=B<sz and board[B][c]>0):
    #             existing_ice+=1
    #         if(0<=T<sz and board[T][c]>0):
    #             existing_ice+=1
    #         if(0<=L<sz and board[r][L]>0):
    #             existing_ice+=1
    #         if(0<=R<sz and board[r][R]>0):
    #             existing_ice+=1
    #         if existing_ice <3:
    #             cell-=1
    sz = len(board)
    dec = [] #cells to decrease
    for r in range(sz):
        for c in range(sz):
            if board[r][c]==0:
                continue
            existing_ice = 0
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr,nc = r+dr, c+dc
                if(0<=nr<sz and 0<=nc<sz and board[nr][nc]>0):
                    existing_ice +=1
            
            if(existing_ice < 3):
                dec.append((r, c))
    for r,c in dec:
        board[r][c] -= 1
    return board

def largest_block(board):
    n=len(board)
    visited = [[False]*n for _ in range(n)]
    def dfs(x,y):
        if x < 0 or x>=n or y<0 or y>=n:
            return 0
        if visited[x][y] or board[x][y] <= 0:
            return 0
        visited[x][y] = True
        size = 1 # count current cell
        size += dfs(x+1,y)
        size += dfs(x-1,y)
        size += dfs(x,y+1)
        size += dfs(x,y-1)
        return size
    max_size = 0
    for i in range(n):
        for j in range(n):
            if(board[i][j] > 0 and not visited[i][j]):
                block_size = dfs(i,j)
                max_size = max(max_size, block_size)
    return max_size


N, Q = map(int, input().split())
size = 2**N
board = [list(map(int,input().split())) for _ in range(size)]
Ls = list(map(int,input().split()))

for L in Ls:
    n = 2 ** L
    for i in range(0, size, n):
        for j in range(0, size, n):
            sub = [row[j:j + n] for row in board[i:i + n]]
            # rotate sub-grid
            rot = rotate_grid(sub, n)
            # write back
            for x in range(n):
                for y in range(n):
                    board[i + x][j + y] = rot[x][y]
    board = melt_ice(board)


sum = 0

for row in board:
    for cell in row:
        if cell>0:
            sum+=cell

print(sum)
print(largest_block(board))