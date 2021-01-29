def solution(A, B):
    A.sort()
    B.sort()

    answer = 0
    a, b = 0, 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            a += 1
            b += 1
            answer += 1
        else:
            b += 1
    
    return answer