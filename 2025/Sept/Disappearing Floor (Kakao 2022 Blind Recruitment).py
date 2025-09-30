def solution(board, aloc, bloc):
    X, Y = len(board), len(board[0])
    
    #mask for better & easier access to board
    mask = 0
    for x in range(X):
        for y in range(Y):
            if board[x][y]:
                mask |= 1<<x*Y+y
    
    answer = -1
    
    def in_board(x, y):
        return 0 <= x < X and 0 <= y < Y
    
    def has_tile(msk, x, y):
        return (msk>>x*Y+y) & 1
    
    def clear_tile(msk, x, y):
        return msk & ~(1<<x*Y+y)
    
    
    DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
    
    def dfs(ax, ay, bx, by, msk):
        if not has_tile(msk,ax, ay):
            return (False, 0)
        can_move = False
        win_turns = float('inf')
        lose_turns = 0
        
        for dx, dy in DIRS:
            nx, ny = ax + dx, ay + dy
            if not in_board(nx,ny) or not has_tile(msk,nx,ny):
                continue
            
            can_move = True
            
            new_mask = clear_tile(msk,ax,ay)
            #next turn: flip turn, new mask new loc
            opp_win, turns = dfs(bx, by, nx, ny, new_mask)
            
            if not opp_win:
                win_turns = min(win_turns, turns + 1)
            else:
                lose_turns = max(lose_turns, turns + 1)
        
        if (not can_move):
            return (False, 0)
        if (win_turns != float('inf')):
            return (True, win_turns)
        else:
            return (False,lose_turns)
        
    _, answer = dfs(aloc[0], aloc[1], bloc[0], bloc[1], mask)
        
    return answer
