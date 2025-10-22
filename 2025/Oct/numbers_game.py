#https://school.programmers.co.kr/learn/courses/30/lessons/12987#

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a_idx = 0
    for b in B:
        if b > A[a_idx]:
            answer += 1
            a_idx += 1
        if a_idx == len(A):
            break
        
    
    return answer