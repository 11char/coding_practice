#question: https://www.acmicpc.net/problem/20056
                

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

# def move_fireball(board,N):
#     new_board = [[]for _ in range(N) for _ in range(N)]
#     for r,row in board:
#         for c,cell in row:
#             if len(cell)>0:
#                 for m,s,d in cell:
#                     nr = (r +dr[d]*s) % N
#                     nc = (c + dc[d]*s) % N
#                     new_board[nr][nc].append((m,s,d))
#     board = new_board
def move_fireball(fireballs, N):
    new_map = {}
    for r,c,m,s,d in fireballs:
        nr = (r +dr[d]*s) % N
        nc = (c + dc[d]*s) % N
        if (nr, nc) not in new_map:
            new_map[(nr, nc)] = []
        new_map[(nr,nc)].append((m,s,d))
    return new_map
def split_fireball(new_map):
    nfireballs = []
    for (r,c), balls in new_map.items():
        if len(balls) == 1:
            m,s,d = balls[0]
            nfireballs.append((r,c,m,s,d))
        else:
            total_m = sum(ball[0] for ball in balls)
            total_s = sum(ball[1] for ball in balls)
            count = len(balls)
            new_m = total_m // 5
            if new_m == 0:
                continue
            new_s = total_s // count
            dirs = [b[2] % 2 for b in balls]
            if all(d == dirs[0] for d in dirs):
                new_dirs = [0, 2, 4, 6]
            else:
                new_dirs = [1, 3, 5, 7]
            for nd in new_dirs:
                nfireballs.append((r,c,new_m,new_s,nd))
    
    return nfireballs

N,M,K = map(int, input().split())

fireballs = []
for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    fireball = (r-1,c-1,m,s,d)
    fireballs.append(fireball)

for _ in range(K):
    new_map = move_fireball(fireballs, N)
    fireballs = split_fireball(new_map)



print(sum(m for r,c,m,s,d in fireballs)) 