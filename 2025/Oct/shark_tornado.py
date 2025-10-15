spread = [(-1, 1, 1), (1,1,1),
          (-1,0,7), (1,0,7),
          (-2,0,2), (2,0,2),
          (-1,-1,10),(1,-1,10),
          (0,-2,5)]
out_sand = 0

dr = [0,1,0,-1]
dc = [-1,0,1,0]

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

#starting pos
r,c = N//2, N//2

#each turn increment step
steps = 1
dir = 0
done = False
while not (r==0 and c==0):
    for _ in range(2):
        if(r==0 and c==0):
            break
        for _ in range(steps):
            if(r==0 and c==0):
                break
            nr,nc = r + dr[dir], c + dc[dir]
            
            sand = board[nr][nc]
            
            if sand == 0:
                r, c = nr,nc
                continue
            moved_total = 0
            for dy, dx, ratio in spread:
                #rotate
                rot_dy, rot_dx = dy, dx
                for _ in range(dir):
                    rot_dy, rot_dx = -rot_dx, rot_dy
                y, x = nr + rot_dy, nc + rot_dx
                sand_moved = (sand*ratio)//100
                moved_total += sand_moved
                if 0 <= y < N and 0 <= x <N:
                    board[y][x] += sand_moved
                else:
                    out_sand += sand_moved
            #a location
            ay, ax = nr + dr[dir], nc + dc[dir]
            remaining = sand - moved_total
            if 0 <= ay < N and 0 <= ax <N:
                board[ay][ax] += remaining
            else:
                out_sand += remaining
            
            
            board[nr][nc] = 0
            r,c = nr,nc
            #print(r,c, board, out_sand)
            if r == 0 and c == 0:
                done = True
                break
            
        dir = (dir+1)%4
        if r == 0 and c == 0:
            done = True
            break
    steps += 1

print(out_sand)


