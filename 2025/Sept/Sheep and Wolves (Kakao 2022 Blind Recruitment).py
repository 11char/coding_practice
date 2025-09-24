def solution(info, edges):
    answer = 0
    #build tree:
    tree = {}
    for p,c in edges:
        if p not in tree:
            tree[p] = []
        tree[p].append(c)
    
    """
    sheeps = num of herded sheep
    wolves = num of wolves met
    cur = current node
    paths = potential nodes
    """
    def dfs(sheep, wolves, cur, paths):
        nonlocal answer
        
        if (wolves >= sheep):
            return
        
        if(sheep > answer):
            answer = sheep
        
        next_nodes = paths[:]
        
        if cur in next_nodes:
            next_nodes.remove(cur) #remove cur
        if cur in tree:
            next_nodes.extend(tree[cur]) #add children
        
        for nxt in next_nodes:
            if info[nxt] == 0:
                dfs(sheep+1, wolves, nxt, next_nodes)
            else:
                dfs(sheep, wolves+1, nxt, next_nodes)
    
    
    dfs(1,0,0,[])
    return answer
