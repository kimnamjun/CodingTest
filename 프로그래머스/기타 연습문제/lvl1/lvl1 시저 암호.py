def solution(s, n):
    answer = str()
    A, Z, a, z = ord('A'), ord('Z'), ord('a'), ord('z')
    for ss in s:
        if A <= ord(ss) <= Z:
            answer += chr((ord(ss) - A + n) % 26 + A)
        elif a <= ord(ss) <= z:
            answer += chr((ord(ss) - a + n) % 26 + a)
        else:
            answer += ss
    return answer