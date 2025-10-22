def match(user, banned):
    if (len(user) != len(banned)):
        return False
    for u,b in zip(user,banned):
        if u != b and b!='*':
            return False
    return True
def solution(user_id, banned_id):
    answer = 0
    possible_id = []
    for ban in banned_id:
        matches = [for user in user_id if match(user, banned)]
            
    return answer