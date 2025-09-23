def solution(n, info):
    best_diff = -1
    answer = [-1]
    def calc_diff(lion):
        peach_score,lion_score = 0,0
        for i in range(11):
            if(lion[i]==0 and info[i]==0):
                continue
            elif(info[i]>lion[i]):
                peach_score+=10-i
            else:
                lion_score+=10-i
        return lion_score-peach_score
    
    #left == right, if left better-> true
    def better(left, right):
        for i in range(10, -1, -1):
            if left[i] != right[i]:
                return left[i]>right[i]
        return False
            
    def dfs(i, arrows_left, cur):
        nonlocal best_diff, answer
        if(i == 11 or arrows_left == 0):
            if(arrows_left>0):
                cur[10] +=arrows_left
            diff = calc_diff(cur)
            if diff > 0:
                if diff > best_diff:
                    best_diff = diff
                    answer = cur[:]
                elif diff == best_diff:
                    if better(cur,answer):
                        answer = cur[:]
            if (arrows_left>0):
                cur[10] -= arrows_left
            return
            
        need = info[i] + 1    
        if (need<=arrows_left):
            cur[i] = need
            dfs(i+1, arrows_left - need, cur)
            cur[i] = 0 #reset/backtrack
            
        dfs(i+1, arrows_left, cur)
        
    dfs(0,n,[0]*11)
    
    return answer
